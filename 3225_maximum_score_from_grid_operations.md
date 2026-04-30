# 3225. Maximum Score From Grid Operations

## 🔗 Problem Link
https://leetcode.com/problems/maximum-score-from-grid-operations/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Dynamic Programming, Matrix, Prefix Sum

---

## 🧩 Problem Summary
Given an `n × n` grid of non-negative integers, paint some cells black such that in every column the black cells form a contiguous prefix from the top. After painting, a white cell scores its value if at least one of its horizontal neighbors (left or right) is black. Return the maximum total score.

### 📌 Constraints
- 1 <= n <= 100
- grid is n × n
- 0 <= grid[i][j] <= 10^9

---

## 💭 Intuition
👉 Each column's "shape" collapses to a single number — its black-prefix height. The points earned at the boundary between column `i-1` and column `i` depend only on those two heights, so this is naturally a DP keyed on `(prev_height, curr_height)`. The tricky part is that a white cell sandwiched between two black neighbors must score only once — we handle that by splitting transitions based on which side is taller.

---

## ⚡ Approach — DP on Adjacent Heights with Prefix/Suffix-Max Acceleration

### 🧠 Idea
- Let `h[c]` be the black height in column `c` (0 means the column stays fully white).
- For consecutive columns with heights `prev_h` and `curr_h`:
  - **Case `curr_h <= prev_h`**: column `i`'s white cells in rows `[curr_h, prev_h)` get points from their black left neighbor. Score gained = `col_sum[i][prev_h] - col_sum[i][curr_h]`.
  - **Case `curr_h > prev_h`**: column `i-1`'s white cells in rows `[prev_h, curr_h)` get points from their black right neighbor. Score gained = `col_sum[i-1][curr_h] - col_sum[i-1][prev_h]`. But to avoid double-counting (those cells may already have earned points from a black left neighbor at column `i-2`), we restrict to states where `h[i-2] <= prev_h`.
- `dp[i][curr_h][prev_h]` = best score after processing column `i`, given the heights of columns `i` and `i-1`.
- Two running tables — `prev_max[prev_h][k]` (prefix-max over the second-to-last height up to `k`) and `prev_suffix_max[prev_h][k]` (suffix-max from `k`) — let each transition fetch the right "best previous state" in O(1).

---

## 💻 Code

```python
class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        if n == 1: return 0

        dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n)]
        prev_max = [[0] * (n + 1) for _ in range(n + 1)]
        prev_suffix_max = [[0] * (n + 1) for _ in range(n + 1)]
        col_sum = [[0] * (n + 1) for _ in range(n)]

        for c in range(n):
            for r in range(1, n + 1):
                col_sum[c][r] = col_sum[c][r - 1] + grid[r - 1][c]

        for i in range(1, n):
            for curr_h in range(n + 1):
                for prev_h in range(n + 1):
                    if curr_h <= prev_h:
                        extra_score = col_sum[i][prev_h] - col_sum[i][curr_h]
                        dp[i][curr_h][prev_h] = max(
                            dp[i][curr_h][prev_h],
                            prev_suffix_max[prev_h][0] + extra_score,
                        )
                    else:
                        extra_score = col_sum[i - 1][curr_h] - col_sum[i - 1][prev_h]
                        dp[i][curr_h][prev_h] = max(
                            dp[i][curr_h][prev_h],
                            prev_max[prev_h][curr_h] + extra_score,
                            prev_suffix_max[prev_h][curr_h]
                        )

            for curr_h in range(n + 1):
                cur_max = 0
                for next_h in range(n + 1):
                    cur_max = max(cur_max, dp[i][next_h][curr_h])
                    prev_max[curr_h][next_h] = cur_max

                cur_suffix_max = 0
                for next_h in range(n, -1, -1):
                    cur_suffix_max = max(cur_suffix_max, dp[i][next_h][curr_h])
                    prev_suffix_max[curr_h][next_h] = cur_suffix_max

        ans = 0
        for prev_h in range(n + 1):
            ans = max(ans, prev_suffix_max[prev_h][0])

        return ans
```

---

## 🧠 Dry Run
### Input
```
grid = [[0,0,0,0,0],
        [0,0,3,0,0],
        [0,1,0,0,0],
        [5,0,0,3,0],
        [0,0,0,0,2]]
```
### Steps
```
n = 5. Build column prefix sums col_sum[c][r] = sum of grid[0..r-1][c].

Iterate columns i = 1..4. For each (curr_h, prev_h):
  curr_h <= prev_h  -> col i contributes white cells under col i-1's black shadow
                       (white-on-the-right pattern)
  curr_h >  prev_h  -> col i-1 contributes white cells under col i's black shadow,
                       but only when h[i-2] <= prev_h (using prev_max) so those
                       cells aren't already counted from the left side.

After each column, refresh prev_max / prev_suffix_max so the next column can
look up the best previous state in O(1).

Final answer = max over (prev_h) of prev_suffix_max[prev_h][0].

Result: 11
```

---

## ⏱️ Time Complexity
```
O(n^3) — for each of n columns we iterate over (curr_h, prev_h) pairs and refresh the running max tables. The amortization is what saves us from a naive O(n^4).
```

## 💾 Space Complexity
```
O(n^3) — the dp array is n × (n+1) × (n+1). The prefix/suffix-max tables and column prefix sums are O(n^2).
```

---

## ⚠️ Edge Cases
- **n == 1** — only one column, no horizontal neighbor ever exists, so the answer is 0 (handled by the early return).
- **All zeros** — every transition still works; the answer is trivially 0.
- **A single tall column next to short ones** — the asymmetric `curr_h > prev_h` branch is what captures the right-neighbor contribution without double-counting against the left.
- **Increasing then decreasing heights** — exercises both branches and is the case where the `prev_max` (height-bounded) lookup matters most.

---

## 🎯 Interview Takeaways
- "Per-column choice with adjacency interaction" is a strong signal for a DP keyed on `(prev_state, curr_state)`.
- Double-counting trap: a cell with two black neighbors should still score only once. Splitting transitions by which side is taller — and pulling the right max via `prev_max` vs `prev_suffix_max` — is how to avoid it cleanly.
- Running prefix-max / suffix-max tables collapse naive O(n^4) transitions into O(n^3) by amortizing the "best previous state" lookup.

---

## 📌 Key Pattern
👉 **"DP on adjacent column heights + prefix/suffix-max acceleration to avoid double counting"**

---

## 🔁 Related Problems
- 1411. Number of Ways to Paint N × 3 Grid
- 1931. Painting a Grid With Three Different Colors
- 3197. Find the Minimum Area to Cover All Ones II
- 1444. Number of Ways of Cutting a Pizza

---

## 🚀 Final Thoughts
The key insight is that each column's commitment is just a single integer (its black height), shrinking the state space dramatically. The remaining cleverness is splitting the transition by which side is taller so the same cell never scores twice, and using running maxima so the inner lookup is O(1). It's a textbook example of "compress the state, then amortize the transition."

---

✨ **Rule to remember:**
> When adjacent columns interact and points can come from either side, split the DP by which side is taller and pre-compute running maxima to avoid an O(n^4) blowup.
