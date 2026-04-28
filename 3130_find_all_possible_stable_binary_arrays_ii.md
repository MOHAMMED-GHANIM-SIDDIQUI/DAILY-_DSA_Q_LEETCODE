# 3130. Find All Possible Stable Binary Arrays II

## 🔗 Problem Link
https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Dynamic Programming, Combinatorics, Prefix Sum

---

## 🧩 Problem Summary
Same as Problem 3129 but with larger constraints. A stable binary array has no subarray of length > `limit` consisting of only 0s or only 1s. Given `zero`, `one`, and `limit`, return the count of stable binary arrays modulo 10^9 + 7.

### 📌 Constraints
- `1 <= zero, one <= 1000`
- `1 <= limit <= 1000`

---

## 💭 Intuition
👉 The top-down approach from 3129 is too slow for larger constraints. Use bottom-up DP with inclusion-exclusion: `dp[i][j][k]` counts stable arrays using `i` zeros and `j` ones where the last element is `k`. Subtract the overcounted states where a run exceeds the limit.

---

## ⚡ Approach — Bottom-Up DP with Inclusion-Exclusion

### 🧠 Idea
- `dp[i][j][0]` = number of stable arrays with `i` zeros, `j` ones, ending in 0.
- `dp[i][j][1]` = number of stable arrays with `i` zeros, `j` ones, ending in 1.
- Transition: adding a 0 to the end can come from either ending (last was 0 or 1), but we must subtract cases where a consecutive run of 0s exceeds `limit`.
- The subtracted term uses inclusion-exclusion: `dp[i - limit - 1][j][1]` represents arrays where removing `limit + 1` trailing zeros still ends in 1 (meaning we had an illegal run).

---

## 💻 Code

```python
class Solution:
  # Same as 3129. Find All Possible Stable Binary Arrays I
  def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
    MOD = 1_000_000_007
    # dp[i][j][k] := the number of stable arrays, where the number of
    # occurrences of 0 is i and the number of occurrences of 1 is j and the last
    # number is k (0/1)
    dp = [[[0] * 2
          for _ in range(one + 1)]
          for _ in range(zero + 1)]

    for i in range(min(zero, limit) + 1):
      dp[i][0][0] = 1

    for j in range(min(one, limit) + 1):
      dp[0][j][1] = 1

    for i in range(1, zero + 1):
      for j in range(1, one + 1):
        dp[i][j][0] = (
            dp[i - 1][j][0] + dp[i - 1][j][1] -
            (dp[i - limit - 1][j][1] if i - limit >= 1 else 0) + MOD) % MOD
        dp[i][j][1] = (
            dp[i][j - 1][0] + dp[i][j - 1][1] -
            (dp[i][j - limit - 1][0] if j - limit >= 1 else 0) + MOD) % MOD

    return (dp[zero][one][0] + dp[zero][one][1]) % MOD
```

---

## 🧠 Dry Run
### Input
```
zero = 2, one = 2, limit = 1
```
### Steps
```
1. Base cases: dp[0][0][0]=1, dp[1][0][0]=1; dp[0][0][1]=1, dp[0][1][1]=1
2. dp[1][1][0] = dp[0][1][0] + dp[0][1][1] = 0 + 1 = 1
   dp[1][1][1] = dp[1][0][0] + dp[1][0][1] = 1 + 0 = 1
3. dp[1][2][0] = dp[0][2][0] + dp[0][2][1] = 0 + 1 = 1
   dp[1][2][1] = dp[1][1][0] + dp[1][1][1] - dp[1][0][0] = 1+1-1 = 1
4. dp[2][1][0] = dp[1][1][0] + dp[1][1][1] - dp[0][1][1] = 1+1-1 = 1
   dp[2][1][1] = dp[2][0][0] + dp[2][0][1] = 1 + 0 = 1
5. dp[2][2][0] = dp[1][2][0] + dp[1][2][1] - dp[0][2][1] = 1+1-1 = 1
   dp[2][2][1] = dp[2][1][0] + dp[2][1][1] - dp[2][0][0] = 1+1-1 = 1
6. Result: 1 + 1 = 2 (arrays: [0,1,0,1] and [1,0,1,0])
```

---

## ⏱️ Time Complexity
```
O(zero * one) — double nested loop with O(1) transitions.
```

## 💾 Space Complexity
```
O(zero * one) for the DP table.
```

---

## ⚠️ Edge Cases
- `limit = 1`: only strictly alternating arrays are valid.
- `limit >= zero + one`: all arrangements of zeros and ones are valid.
- `|zero - one| > 1` with `limit = 1`: impossible (result is 0).

---

## 🎯 Interview Takeaways
- Inclusion-exclusion elegantly handles the "subtract overcounted long runs" transition.
- Bottom-up DP with O(1) per state transition scales to larger inputs.
- The correction term `dp[i-limit-1][j][1]` captures exactly the states where a run of 0s exceeded the limit.

---

## 📌 Key Pattern
👉 **"Bottom-up DP with inclusion-exclusion to enforce maximum run-length constraints"**

---

## 🔁 Related Problems
- 3129. Find All Possible Stable Binary Arrays I
- 552. Student Attendance Record II
- 1220. Count Vowels Permutation

---

## 🚀 Final Thoughts
This is the optimized version of 3129 that handles 10x larger constraints. The key upgrade is replacing the inner loop over run lengths with an O(1) inclusion-exclusion correction, reducing overall complexity from O(zero * one * limit) to O(zero * one).

---

✨ **Rule to remember:**
> When a DP counts arrangements with bounded runs, use inclusion-exclusion to subtract states with overlong runs in O(1) per transition.
