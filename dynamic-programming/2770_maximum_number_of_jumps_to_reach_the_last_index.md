# 2770. Maximum Number of Jumps to Reach the Last Index

## 🔗 Problem Link
https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Dynamic Programming

---

## 🧩 Problem Summary
You are given a 0-indexed integer array `nums` of length `n` and an integer `target`. Starting at index `0`, you may jump from index `i` to any index `j` (`i < j < n`) **iff** `-target <= nums[j] - nums[i] <= target` — i.e. the absolute value difference of the elements is at most `target`.

Return the **maximum** number of jumps needed to reach index `n - 1`. If `n - 1` is unreachable, return `-1`.

### 📌 Constraints
- `2 <= n <= 1000`
- `-10^9 <= nums[i] <= 10^9`
- `0 <= target <= 2 * 10^9`

---

## 💭 Intuition
We want **the longest path** from index `0` to index `n - 1` in a DAG where the edges go strictly left-to-right and an edge `(j, i)` exists iff `|nums[i] - nums[j]| <= target`.

Because edges always go forward (`j < i`), the graph is acyclic and we can fill a DP left-to-right:

> `dp[i]` = the maximum number of jumps to reach `i` starting from `0`. (`-1` if unreachable.)

Transition is the obvious one: to land at `i`, we must have come from some valid `j < i`, so
```
dp[i] = max(dp[j] + 1)  over all j < i where dp[j] != -1 and |nums[i] - nums[j]| <= target
```
`dp[0] = 0` (we start there, zero jumps so far). The answer is `dp[n-1]`.

Why **max** and not **min**? Because the problem asks for the *most* jumps. Counter-intuitive, but mechanically the same DP shape — only the comparator flips. Mixing them up is the classic trap on this problem.

---

## ⚡ Approach — O(n²) DAG Longest Path DP

### 🧠 Idea
1. Initialize `dp = [-1] * n`, then set `dp[0] = 0`.
2. For each `i` from `1` to `n - 1`:
   - For each `j` from `0` to `i - 1`:
     - If `dp[j] != -1` **and** `|nums[i] - nums[j]| <= target`:
       - `dp[i] = max(dp[i], dp[j] + 1)`
3. Return `dp[n - 1]` (already `-1` if unreachable — no special-casing needed).

The `dp[j] != -1` guard is crucial: an unreachable `j` cannot extend a path to `i`, no matter how compatible the jump is.

---

## 💻 Code

```python
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)

        dp = [-1] * n
        dp[0] = 0

        for i in range(1, n):
            for j in range(i):
                if dp[j] != -1 and abs(nums[i] - nums[j]) <= target:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[-1]
```

---

## 🧠 Dry Run
### Input
```
nums = [1, 3, 6, 4, 1, 2],  target = 2
```

### DP fill
```
i=0: dp = [0, -1, -1, -1, -1, -1]
i=1: j=0  |3-1|=2 ≤ 2 ✓  dp[0]=0  → dp[1] = 0+1 = 1
     dp = [0, 1, -1, -1, -1, -1]
i=2: j=0  |6-1|=5 ✗
     j=1  |6-3|=3 ✗
     dp = [0, 1, -1, -1, -1, -1]   (index 2 unreachable)
i=3: j=0  |4-1|=3 ✗
     j=1  |4-3|=1 ≤ 2 ✓  dp[1]=1  → dp[3] = 2
     j=2  dp[2] = -1 → skip
     dp = [0, 1, -1, 2, -1, -1]
i=4: j=0  |1-1|=0 ≤ 2 ✓  dp[0]=0  → dp[4] = 1
     j=1  |1-3|=2 ≤ 2 ✓  dp[1]=1  → dp[4] = max(1, 2) = 2
     j=2  skip
     j=3  |1-4|=3 ✗
     dp = [0, 1, -1, 2, 2, -1]
i=5: j=0  |2-1|=1 ≤ 2 ✓  → dp[5] = 0+1 = 1
     j=1  |2-3|=1 ≤ 2 ✓  → dp[5] = max(1, 2) = 2
     j=2  skip
     j=3  |2-4|=2 ≤ 2 ✓  → dp[5] = max(2, 3) = 3
     j=4  |2-1|=1 ≤ 2 ✓  → dp[5] = max(3, 3) = 3
     dp = [0, 1, -1, 2, 2, 3]
```

Return `dp[5] = 3`. Path: `0 → 1 → 3 → 5` (or `0 → 1 → 4 → 5`), three jumps. ✅

---

## ⏱️ Time Complexity
```
O(n²) — pair-wise scan over indices. n ≤ 1000 so ≈ 10^6 ops, comfortably fast.
```

## 💾 Space Complexity
```
O(n) for the dp array.
```

---

## ⚠️ Edge Cases
- **`n == 2`**: only one possible jump (`0 → 1`). It's valid iff `|nums[1] - nums[0]| <= target`. The DP returns `1` or `-1` accordingly — no special case needed.
- **Unreachable last index**: `dp[-1]` stays `-1`, which is exactly what we return.
- **`target == 0`**: only equal-valued elements can be jumped between. Still a valid DP run; just heavier filtering.
- **Large `nums[i]` values (up to `10^9`)**: `abs(nums[i] - nums[j])` fits in Python's arbitrary-precision int with no overflow. In C++/Java use `long long` or cast to 64-bit before subtracting.
- **All elements equal**: every jump is valid → `dp[i] = i` → answer is `n - 1` (you take every step one by one to maximize the count).
- **Strictly increasing/decreasing with small `target`**: short hops are valid, long hops aren't — DP still works, but reachability may dead-end early. The `dp[j] != -1` guard prevents poisoned chains.

---

## 🎯 Interview Takeaways
- **Longest-path on a DAG** can be done with a simple forward DP — no Bellman-Ford, no topological sort, because the indices themselves are a valid topo order.
- **Maximize vs. minimize** uses the same recurrence shape; only the operator changes. Read the problem twice — "max jumps" is uncommon and easy to misread as "min jumps."
- The **unreachable sentinel** (`-1`) must propagate correctly. Don't write `dp[i] = max(dp[i], dp[j] + 1)` without first checking `dp[j] != -1`, or you'll happily extend non-existent paths.
- For `n ≤ 1000` the O(n²) loop is the right call; don't over-engineer with segment trees or sliding-window-min/max unless the constraints push you there.

---

## 📌 Key Pattern
👉 **"Forward DP on a DAG where indices give the topo order — `dp[i] = op_{j<i, valid} (dp[j] + 1)`, with a sentinel guarding unreachable states."**

---

## 🔁 Related Problems
- 55. Jump Game
- 45. Jump Game II (min jumps — same shape, flipped operator + BFS-greedy trick)
- 1306. Jump Game III
- 1340. Jump Game V (max chain length on a DAG)
- 2369. Check if There is a Valid Partition For The Array
- 300. Longest Increasing Subsequence (classic O(n²) DAG longest-path DP)

---

## 🚀 Final Thoughts
The problem's structure is the same as Longest Increasing Subsequence — pairwise scan, compatibility test, take the max-plus-one. The only special detail is the unreachable sentinel; once you're careful about that, the rest writes itself.

---

✨ **Rule to remember:**
> Forward DAG DP only works if you propagate "unreachable" honestly — guard the transition, don't silently extend phantom paths.
