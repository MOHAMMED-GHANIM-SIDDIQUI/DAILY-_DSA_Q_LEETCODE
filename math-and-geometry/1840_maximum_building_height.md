# 1840. Maximum Building Height

## 🔗 Problem Link
https://leetcode.com/problems/maximum-building-height/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Math, Sorting

---

## 🧩 Problem Summary

There are `n` buildings in a row, labeled `1..n`. Rules:
- Building `1` must have height `0`.
- The height of every building is a non-negative integer.
- The absolute height difference between two **adjacent** buildings cannot exceed `1`.

Some buildings carry a restriction `[id, maxHeight]` capping their height. Return the **maximum possible height** of the tallest building under all these rules.

### 📌 Constraints
- `2 <= n <= 10^9`
- `0 <= restrictions.length <= min(n - 1, 10^5)`
- `2 <= id_i <= n`
- `id_i` is unique
- `0 <= maxHeight_i <= 10^9`

---

## 💭 Intuition

👉 Only the restricted buildings (plus the implied anchors) actually matter — between any two fixed heights the terrain rises and falls like a triangle. The trick is to make every restriction **mutually consistent**: a restriction can be lowered not just by its own cap but also by what its neighbors force on it (since adjacent buildings differ by at most 1, building at distance `d` can be at most `neighborHeight + d`). After two relaxation passes (left→right, right→left) every restriction holds its true achievable height, and the peak between any adjacent pair is a simple formula.

---

## ⚡ Approach — Sentinels + Two-Pass Relaxation

### 🧠 Idea
- Add two sentinel restrictions: `[1, 0]` (building 1 is forced to height 0) and `[n, n - 1]` (building `n` can be at most `n-1` since it's `n-1` steps from building 1).
- **Sort** restrictions by building id.
- **Forward pass:** for each restriction, cap it by `prev.height + distance` — the most it can be given the building to its left.
- **Backward pass:** symmetrically cap it by `next.height + distance` — the most it can be given the building to its right.
- Now between each adjacent pair `(x1, h1)` and `(x2, h2)` with gap `d = x2 - x1`, heights can rise from both ends and meet in the middle. The maximum peak is `(h1 + h2 + d) // 2` (integer division, since heights are integers). Track the global max.

---

## 💻 Code

```python
class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.append([n, n - 1])

        restrictions.sort()

        # Forward pass
        for i in range(1, len(restrictions)):
            d = restrictions[i][0] - restrictions[i - 1][0]
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i - 1][1] + d
            )

        # Backward pass
        for i in range(len(restrictions) - 2, -1, -1):
            d = restrictions[i + 1][0] - restrictions[i][0]
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i + 1][1] + d
            )

        ans = 0

        # Maximum possible peak between adjacent restrictions
        for i in range(1, len(restrictions)):
            x1, h1 = restrictions[i - 1]
            x2, h2 = restrictions[i]

            d = x2 - x1
            peak = (h1 + h2 + d) // 2
            ans = max(ans, peak)

        return ans
```

---

## 🧠 Dry Run

### Input
```
n = 5, restrictions = [[2, 1], [4, 1]]
```

### Steps
```
After appending sentinels: [[2,1],[4,1],[1,0],[5,4]]
After sort by id:           [[1,0],[2,1],[4,1],[5,4]]

Forward pass:
  i=1: d=2-1=1 -> h = min(1, 0+1=1) = 1   -> [2,1]
  i=2: d=4-2=2 -> h = min(1, 1+2=3) = 1   -> [4,1]
  i=3: d=5-4=1 -> h = min(4, 1+1=2) = 2   -> [5,2]
  state: [[1,0],[2,1],[4,1],[5,2]]

Backward pass:
  i=2: d=5-4=1 -> h = min(1, 2+1=3) = 1   -> [4,1]
  i=1: d=4-2=2 -> h = min(1, 1+2=3) = 1   -> [2,1]
  i=0: d=2-1=1 -> h = min(0, 1+1=2) = 0   -> [1,0]
  state: [[1,0],[2,1],[4,1],[5,2]]

Peaks:
  pair (1,0)-(2,1): d=1, peak=(0+1+1)//2 = 1
  pair (2,1)-(4,1): d=2, peak=(1+1+2)//2 = 2   <- max
  pair (4,1)-(5,2): d=1, peak=(1+2+1)//2 = 2
  ans = 2
```

Answer: **2** (between buildings 2 and 4, building 3 can reach height 2).

---

## ⏱️ Time Complexity
```
O(m log m)
```
Where `m = restrictions.length`. Sorting dominates; the two relaxation passes and the peak scan are each `O(m)`.

---

## 💾 Space Complexity
```
O(m)
```
We mutate the restrictions list in place (plus two appended sentinels); sorting may use `O(m)` auxiliary space. Independent of `n`.

---

## ⚠️ Edge Cases
- `restrictions = []`: only the two sentinels remain; the single pair `(1,0)-(n,n-1)` gives peak `(0 + (n-1) + (n-1)) // 2 = n - 1`, the unrestricted maximum.
- A restriction of `0` somewhere in the middle pins the terrain down, forcing neighbors lower through the relaxation passes.
- `n` is up to `10^9`, so any solution scanning all buildings would TLE — this is exactly why we only process restriction points.

---

## 🎯 Interview Takeaways
- The two implicit anchors (building 1 = 0, building n <= n-1) are easy to forget; encoding them as sentinels unifies the logic.
- Bidirectional relaxation is the key insight: a cap propagates outward from each fixed point at slope 1.
- The triangular peak formula `(h1 + h2 + d) // 2` comes from solving `h1 + a = h2 + b`, `a + b = d` and maximizing the meeting height.

---

## 📌 Key Pattern
👉 **"Anchor the endpoints, relax constraints left-then-right, then compute the triangular peak between adjacent fixed points."**

---

## 🔁 Related Problems
- 845. Longest Mountain in Array
- 2008. Maximum Earnings From Taxi
- 1648. Sell Diminishing-Valued Colored Balls

---

## 🚀 Final Thoughts
This problem looks geometric but reduces to constraint propagation over a sparse set of key points. The slope-1 adjacency rule means every cap influences its neighbors linearly, so two sweeps make all restrictions globally consistent. After that, the answer is just the highest triangle peak between consecutive anchors — an elegant collapse of a `10^9`-scale problem into `O(m log m)`.

---

✨ **Rule to remember:**
> "When adjacent values differ by at most 1, constraints propagate at slope 1 — relax both directions, then the max between two fixed points is (h1 + h2 + gap) // 2."
