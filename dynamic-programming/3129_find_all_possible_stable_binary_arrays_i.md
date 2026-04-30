# 3129. Find All Possible Stable Binary Arrays I

## 🔗 Problem Link
https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Dynamic Programming, Memoization, Combinatorics

---

## 🧩 Problem Summary
A binary array is called stable if no subarray of length greater than `limit` consists of only 0s or only 1s. Given `zero` (number of 0s), `one` (number of 1s), and `limit`, return the number of stable binary arrays modulo 10^9 + 7.

### 📌 Constraints
- `1 <= zero, one, limit <= 200`

---

## 💭 Intuition
👉 Think of building the array by placing consecutive runs of 0s or 1s alternately. Each run can be between 1 and `limit` in length. Use memoized recursion to count the number of valid arrangements.

---

## ⚡ Approach — Memoized DFS (Top-Down DP)

### 🧠 Idea
- Use `solve(onesLeft, zerosLeft, lastWasOne)` to count valid arrays.
- If `lastWasOne` is true, the next run must be 0s (length 1 to min(zerosLeft, limit)).
- If `lastWasOne` is false, the next run must be 1s (length 1 to min(onesLeft, limit)).
- Base case: both counts are 0 => 1 valid arrangement found.
- Start with both possibilities (first run is 1s or 0s).

---

## 💻 Code

```python
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7

        # memo table
        dp = [[[-1]*2 for _ in range(201)] for __ in range(201)]

        def solve(onesLeft, zerosLeft, lastWasOne):
            if onesLeft == 0 and zerosLeft == 0:
                return 1

            if dp[onesLeft][zerosLeft][lastWasOne] != -1:
                return dp[onesLeft][zerosLeft][lastWasOne]

            result = 0

            if lastWasOne:  # explore 0s
                for length in range(1, min(zerosLeft, limit) + 1):
                    result = (result + solve(onesLeft, zerosLeft - length, 0)) % MOD
            else:  # explore 1s
                for length in range(1, min(onesLeft, limit) + 1):
                    result = (result + solve(onesLeft - length, zerosLeft, 1)) % MOD

            dp[onesLeft][zerosLeft][lastWasOne] = result
            return result

        startWithOne = solve(one, zero, 0)
        startWithZero = solve(one, zero, 1)

        return (startWithOne + startWithZero) % MOD
```

---

## 🧠 Dry Run
### Input
```
zero = 1, one = 1, limit = 2
```
### Steps
```
1. startWithOne: solve(1, 1, 0) — first run is 1s
   - length=1: solve(0, 1, 1) — now place 0s
     - length=1: solve(0, 0, 0) = 1
   => 1
2. startWithZero: solve(1, 1, 1) — first run is 0s
   - length=1: solve(1, 0, 0) — now place 1s
     - length=1: solve(0, 0, 1) = 1
   => 1
3. Result: 1 + 1 = 2 (arrays: [0,1] and [1,0])
```

---

## ⏱️ Time Complexity
```
O(zero * one * limit * 2) — each state is computed once, each state iterates up to `limit`.
```

## 💾 Space Complexity
```
O(zero * one * 2) for the memoization table.
```

---

## ⚠️ Edge Cases
- `limit >= zero + one`: no constraint on runs, answer is C(zero+one, zero).
- `limit = 1`: strictly alternating arrays only.
- `zero = 0` or `one = 0`: only valid if the count <= limit.

---

## 🎯 Interview Takeaways
- Modeling runs of consecutive identical elements as the building block simplifies the state.
- Memoization with a 3D state (onesLeft, zerosLeft, lastType) captures all necessary information.
- Starting from both possible first-run types handles the initial condition cleanly.

---

## 📌 Key Pattern
👉 **"Run-length-based DP for counting arrays with bounded consecutive elements"**

---

## 🔁 Related Problems
- 3130. Find All Possible Stable Binary Arrays II
- 1220. Count Vowels Permutation
- 552. Student Attendance Record II

---

## 🚀 Final Thoughts
The top-down approach with memoization is intuitive for this problem. By thinking in terms of alternating runs, we reduce the complexity and make the state transitions clear. The constraint `limit <= 200` keeps the approach feasible.

---

✨ **Rule to remember:**
> For counting arrays with bounded consecutive elements, think in runs — each run alternates and has length 1 to limit.
