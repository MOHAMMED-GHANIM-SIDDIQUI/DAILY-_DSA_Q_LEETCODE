# 3161. Block Placement Queries

## 🔗 Problem Link
https://leetcode.com/problems/block-placement-queries/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Binary Indexed Tree, Segment Tree, Binary Search

---

## 🧩 Problem Summary
Imagine an infinite number line. You process `queries`:
- `[1, x]` — place an **obstacle** at position `x`.
- `[2, x, sz]` — ask whether a block of width `sz` can be placed in `[0, x]` such that it fits **between two consecutive obstacles** (or between `0` and the first obstacle), i.e. there is a gap of length `>= sz` entirely within `[0, x]`.

Return a boolean array, one answer per type-2 query, in order.

### 📌 Constraints
- `1 <= queries.length <= 1.5 * 10^4`
- `2 <= x <= 5 * 10^4`, and for type-2, `1 <= sz <= x`.
- All type-1 positions are distinct.

---

## 💭 Intuition
A type-2 query at `(x, sz)` succeeds if **either**:
1. There's a gap of size `>= sz` strictly to the **left** of the last obstacle `<= x` (a fully-enclosed gap between two obstacles, both within `[0, x]`), **or**
2. The space from that last obstacle up to `x` itself is `>= sz` (`x - prev_obs >= sz`) — a gap whose right edge is `x`.

The hard part is (1): "the **maximum gap** between consecutive obstacles among all obstacles up to position `p`." Gaps **change** as obstacles are inserted (an insertion splits one gap into two). Handling that online with a moving `x` is messy — so we process **offline, in reverse**.

**Reverse trick:** First, place **all** obstacles that ever get added (plus sentinels `0` and a max bound). Then walk the queries **backwards**:
- A reversed type-1 (`[1, x]`) means we are *removing* `x` going back in time → its two neighbouring gaps **merge** into one bigger gap `right - left`.
- A reversed type-2 reads the current obstacle configuration (which reflects exactly the obstacles present at that point in forward time).

To answer "max gap among obstacles `<= p`," we keep a **Binary Indexed Tree (Fenwick) for prefix maximum**, indexed by obstacle position: `bit.update(pos, gapEndingAtPos)` and `bit.query(p)` returns the largest gap whose **right endpoint** is `<= p`. A `SortedList` of current obstacles lets us find neighbours and the predecessor of `x` via binary search (`index`, `bisect_right`).

---

## ⚡ Approach — Offline reverse + Fenwick prefix-max + SortedList

### 🧠 Idea
**Setup**
1. `MX = min(50000, len(queries) * 3)` — an upper bound covering all positions.
2. `obstacles = SortedList([0, MX])` — sentinels. Add **every** type-1 position (final state).
3. Build a Fenwick **max** tree: for consecutive obstacles `arr[i-1], arr[i]`, record the gap `arr[i] - arr[i-1]` at index `arr[i]` (the gap's right endpoint).

**Process queries in reverse**
- **`[1, x]` (undo an insertion):** find `x`'s neighbours `left`, `right` in the SortedList. Removing `x` merges its two gaps → record `bit.update(right, right - left)`. Then `obstacles.remove(x)`.
- **`[2, x, sz]`:** let `prev_obs` = largest obstacle `<= x` (`bisect_right(x) - 1`). Answer is:
  - `bit.query(prev_obs) >= sz` (a fully enclosed gap ending at or before `prev_obs` fits), **OR**
  - `x - prev_obs >= sz` (the tail gap from `prev_obs` to `x` fits).

Finally **reverse** the collected answers back to forward order.

### 🔑 Why reverse + Fenwick-max
- Forward insertions **split** gaps (hard: one value becomes two, max can go down). Reverse insertions **merge** gaps (easy: two become one, only need to *raise* a max). A Fenwick tree supports point-update / prefix-max efficiently, and merging only ever **increases** a stored gap — perfectly matched to a max-BIT (`bit[i] = max(bit[i], val)`).
- Indexing gaps by their **right endpoint** makes "max gap fully within `[0, p]`" a clean **prefix-max query** up to `p`.

---

## 💻 Code

```python
from sortedcontainers import SortedList

class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i, val):
        while i <= self.n:
            self.bit[i] = max(self.bit[i], val)
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            res = max(res, self.bit[i])
            i -= i & -i
        return res


class Solution:
    def getResults(self, queries):
        MX = min(50000, len(queries) * 3)

        obstacles = SortedList([0, MX])
        for q in queries:
            if q[0] == 1:
                obstacles.add(q[1])

        bit = BIT(MX + 2)

        arr = list(obstacles)
        for i in range(1, len(arr)):
            bit.update(arr[i], arr[i] - arr[i - 1])

        ans = []

        for q in reversed(queries):
            if q[0] == 1:
                x = q[1]

                idx = obstacles.index(x)
                left = obstacles[idx - 1]
                right = obstacles[idx + 1]

                bit.update(right, right - left)
                obstacles.remove(x)

            else:
                _, x, sz = q

                idx = obstacles.bisect_right(x)
                prev_obs = obstacles[idx - 1]

                ans.append(
                    bit.query(prev_obs) >= sz or
                    x - prev_obs >= sz
                )

        return ans[::-1]
```

---

## 🧠 Dry Run
### Input
```
queries = [[1,2], [2,3,3], [2,3,1], [2,2,2]]
```

### Final obstacle set
```
obstacles = [0, 2, MX]   (MX large)
bit: gap ending at 2 → 2-0 = 2 ; gap ending at MX → MX-2
```

### Reverse pass
```
q=[2,2,2]: prev_obs = largest ≤ 2 = 2
   bit.query(2) = 2  ≥ 2 ? yes → True
q=[2,3,1]: prev_obs = largest ≤ 3 = 2
   bit.query(2)=2 ≥1 → True
q=[2,3,3]: prev_obs = 2
   bit.query(2)=2 ≥3? no ; x-prev = 3-2 =1 ≥3? no → False
q=[1,2]: undo insert of 2 → neighbours 0 and MX → merge gap MX-0
   bit.update(MX, MX) ; remove 2
ans (reverse order) = [True, True, False]
→ reversed back: [False, True, True]
```
Answer (forward, one per type-2 query): `[False, True, True]`.

---

## ⏱️ Time Complexity
```
O(Q log Q)   — each query does O(log) SortedList ops and O(log MX) Fenwick ops.
```

## 💾 Space Complexity
```
O(Q + MX)   — Fenwick array sized to the coordinate bound, plus the SortedList.
```

---

## ⚠️ Edge Cases
- **Type-2 before any obstacle** → `prev_obs = 0` sentinel; answer driven by `x - 0 >= sz`.
- **Block fitting exactly** (`gap == sz`) → `>=` makes it succeed.
- **The tail gap (right edge = x)** is the case the enclosed-gap Fenwick query misses — that's why the `x - prev_obs >= sz` second condition exists.
- **Sentinels `0` and `MX`** keep neighbour lookups total (no missing left/right when removing the first/last real obstacle).
- **Removing yields neighbours across the whole span** → merged gap can become the new global max.

---

## 🎯 Interview Takeaways
- When **forward** updates make a tracked maximum **decrease** (gap splits), flip to **offline reverse** so updates only **increase** it (gap merges) — a max-Fenwick loves monotonic-up updates.
- Index interval/gap data by an **endpoint** so "best within `[0, p]`" becomes a **prefix query**.
- Decompose the answer into "fully enclosed gap" (data-structure query) **plus** a boundary case ("gap touching `x`") — missing the boundary term is the most common wrong answer here.
- `SortedList` (order-statistics + `bisect`) is the right tool for dynamic neighbour/predecessor lookups; the binary searches (`index`, `bisect_right`) are why this sits in the **binary-search** family.

---

## 📌 Key Pattern
👉 **"Offline-reverse so splits become merges; Fenwick prefix-max over gaps indexed by right endpoint; SortedList for neighbour/predecessor binary search."**

---

## 🔁 Related Problems
- 715. Range Module
- 2276. Count Integers in Intervals
- 307. Range Sum Query - Mutable
- 2940. Find Building Where Alice and Bob Can Meet
- 218. The Skyline Problem

---

## 🚀 Final Thoughts
This problem stacks three ideas — offline reverse processing, a Fenwick tree repurposed for prefix **maximum**, and a SortedList for predecessor/neighbour queries. The single most important reframe is reversing time: forward, an insertion *splits* a gap (max can drop, which a BIT can't easily do); backward, it *merges* gaps (max only rises), which the max-BIT handles in `O(log)`. Everything else is bookkeeping plus the boundary `x - prev_obs` term.

---

✨ **Rule to remember:**
> If online updates would force a tracked maximum to *decrease*, process queries offline in reverse so the operation becomes a *merge* that only ever increases it — then a Fenwick prefix-max nails each query in O(log n).
