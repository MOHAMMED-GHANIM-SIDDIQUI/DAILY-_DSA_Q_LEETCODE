# 1306. Jump Game III

## 🔗 Problem Link
https://leetcode.com/problems/jump-game-iii/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, DFS, BFS

---

## 🧩 Problem Summary
Given an array `arr` of **non-negative** integers and a starting index `start`, from any index `i` you can jump to either `i + arr[i]` or `i - arr[i]` (as long as the target is in-bounds). Return `True` if there is any reachable index whose value is `0`.

### 📌 Constraints
- `1 <= arr.length <= 5 * 10^4`
- `0 <= arr[i] < arr.length`
- `0 <= start < arr.length`

---

## 💭 Intuition
Each index is a graph node with **at most two outgoing edges**: `i → i + arr[i]` and `i → i - arr[i]`. The question collapses to a simple reachability check from `start` to any node tagged with value `0`.

So this is a plain DFS/BFS on an implicit graph. The only twist is the **visited set** — without it, two indices can ping-pong forever (e.g. `arr[i] = arr[j]` and `i ± arr[i] = j`). And because `arr[i]` is guaranteed non-negative, we can encode "visited" *in the array itself* by negating the value. A negative entry can be both detected as visited and never revisited — no extra `set` needed.

---

## ⚡ Approach — DFS with in-place visited marking

### 🧠 Idea
1. Recursive function `solve(idx)`:
   - If `idx` is out of bounds → return `False`.
   - If `arr[idx] < 0` → already visited along this DFS → return `False` (no cycle help here).
   - If `arr[idx] == 0` → reached a zero → return `True`.
   - Snapshot the jump distance, **negate** `arr[idx]` to mark it visited, then return `solve(idx + jump) or solve(idx - jump)`.
2. Call `solve(start)` and return its result.

### 🔑 Why negation works as a visited marker
- Inputs are guaranteed `arr[i] >= 0`, so a negative value can *only* come from us.
- We must snapshot `jump = arr[idx]` **before** flipping the sign, otherwise the recursive call uses the wrong distance.
- We never need to restore the value: once we've explored both edges from `idx`, every reachable zero downstream has been searched, so re-entering `idx` later would only redo that same work.

### 🔑 Why we don't need a separate `visited` set
The array itself doubles as the visited tracker. This drops auxiliary space from `O(n)` to `O(1)` (excluding the recursion stack).

---

## 💻 Code

```python
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)

        def solve(idx):
            if idx < 0 or idx >= n or arr[idx] < 0:
                return False

            if arr[idx] == 0:
                return True

            jump = arr[idx]
            arr[idx] = -arr[idx]   # mark visited

            return solve(idx + jump) or solve(idx - jump)

        return solve(start)
```

---

## 🧠 Dry Run
### Input
```
arr   = [4, 2, 3, 0, 3, 1, 2]
start = 5
```

### Trace
```
solve(5): arr[5]=1, jump=1, mark arr[5]=-1
  solve(6): arr[6]=2, jump=2, mark arr[6]=-2
    solve(8): out of bounds → False
    solve(4): arr[4]=3, jump=3, mark arr[4]=-3
      solve(7): out of bounds → False
      solve(1): arr[1]=2, jump=2, mark arr[1]=-2
        solve(3): arr[3]=0 → True ✅
```
Returns `True`.

### Visited-block case
```
arr   = [3, 0, 2, 1, 2]
start = 2
solve(2): jump=2, mark -2
  solve(4): jump=2, mark -2
    solve(6): OOB → False
    solve(2): arr[2]=-2 < 0 → False
  → False
solve(0): jump=3 (oops, but start=2, branch was solve(0))
  ...
```
The negation marker breaks the cycle that would otherwise loop `2 ↔ 4`.

---

## ⏱️ Time Complexity
```
O(n)   — each index is visited at most once because the first visit flips it
         negative and every later entry short-circuits on `arr[idx] < 0`.
```

## 💾 Space Complexity
```
O(n)   — recursion stack in the worst case (chain of unique jumps).
O(1)   — auxiliary, since we encode "visited" inside the input array itself.
```

---

## ⚠️ Edge Cases
- **`arr[start] == 0`** → first call returns `True` immediately.
- **No zero in the array** → every DFS path exhausts and returns `False`. The constraint `0 <= arr[i] < arr.length` does NOT guarantee a zero exists.
- **Single-element array `[0]`, start=0** → returns `True`.
- **Single-element array `[1]`, start=0** → both jumps go OOB, returns `False`.
- **Stuck at a self-zero loop position** → `arr[i] = 0` triggers the success branch before any jump, so a zero adjacent to start is found on the first probe.
- **Trapped sub-region** (e.g. `[1, 1, 2]` starting at 0 → bounces 0↔1 forever without visited) → negation marker prevents the cycle.
- **Input mutation caveat** → this solution mutates `arr` in place. If the caller reuses `arr` afterwards, restore it (`arr[idx] = -arr[idx]` after the two recursive calls) or use a separate `visited` set.

---

## 🎯 Interview Takeaways
- Recognise the shape: "from each index, fan out to a small constant number of next indices" → graph reachability, not a DP/greedy "minimum jumps" problem.
- The "negate the value to mark visited" trick is a recurring pattern any time inputs are constrained non-negative and you don't want an auxiliary set (LC 41, LC 442, LC 448 are siblings).
- BFS works equally well here and avoids recursion depth concerns for long chains — flag the choice in interviews. DFS is shorter; BFS is safer for `n` near the 5·10⁴ upper bound on some runtimes.
- The `or` short-circuit means we stop as soon as one branch succeeds — important for performance.

---

## 📌 Key Pattern
👉 **"Reachability on an implicit graph where each node has ≤ k neighbours → DFS/BFS with a visited set. If inputs are non-negative, mark visited in place by negating."**

---

## 🔁 Related Problems
- 55. Jump Game
- 45. Jump Game II
- 1340. Jump Game V
- 1345. Jump Game IV
- 1654. Minimum Jumps to Reach Home
- 2059. Minimum Operations to Convert Number

---

## 🚀 Final Thoughts
This problem looks like "Jump Game" but is fundamentally different — there's no optimisation (min jumps / max reach), just a yes/no reachability question. Once that reframe lands, the answer is the textbook DFS template plus a non-negativity trick to skip the visited set. The whole solution is six lines of logic, and the only thing that earns Medium difficulty is recognising that the recursion would loop without the marker.

---

✨ **Rule to remember:**
> When a problem reads "can you reach X from Y under move rules," the first instinct should be graph search, not DP. And when inputs are non-negative, you almost never need a separate `visited` set — negate the value in place.
