# 790. Domino and Tromino Tiling

## 🔗 Problem Link
https://leetcode.com/problems/domino-and-tromino-tiling/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Dynamic Programming, Math

---

## 🧩 Problem Summary
Given a `2 x n` board, find the number of ways to tile it using dominoes (2x1) and trominoes (L-shaped). Return the result modulo `10^9 + 7`.

### 📌 Constraints
- `1 <= n <= 1000`

---

## 💭 Intuition
👉 Through mathematical derivation or observation, the recurrence relation is `dp[i] = 2 * dp[i-1] + dp[i-3]`. This captures all possible placements of dominoes and trominoes that complete column `i`.

---

## ⚡ Approach — Dynamic Programming with Recurrence

### 🧠 Idea
- Base cases: `dp[1] = 1`, `dp[2] = 2`, `dp[3] = 5`.
- For `i >= 4`: `dp[i] = 2 * dp[i-1] + dp[i-3]`.
- The factor of 2 accounts for adding a vertical domino or a pair of trominoes, while `dp[i-3]` accounts for the new tromino configurations.

---

## 💻 Code

```cpp
class Solution {
 public:
  int numTilings(int n) {
    constexpr int kMod = 1'000'000'007;
    vector<long> dp(1001);
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 5;

    for (int i = 4; i <= n; ++i)
      dp[i] = (2 * dp[i - 1] + dp[i - 3]) % kMod;

    return dp[n];
  }
};
```

---

## 🧠 Dry Run
### Input
```
n = 4
```
### Steps
```
dp[1] = 1
dp[2] = 2
dp[3] = 5
dp[4] = 2 * dp[3] + dp[1] = 2*5 + 1 = 11

Result: 11
```

---

## ⏱️ Time Complexity
```
O(n)
```

## 💾 Space Complexity
```
O(n), can be reduced to O(1) with rolling variables
```

---

## ⚠️ Edge Cases
- `n = 1`: Only one vertical domino, answer is 1.
- `n = 2`: Two vertical or two horizontal dominoes, answer is 2.
- Large `n`: Modular arithmetic prevents overflow.

---

## 🎯 Interview Takeaways
- Tiling problems often have elegant recurrence relations that can be derived from observing small cases.
- Always look for patterns in the first few values before coding.
- Modular arithmetic is essential for large DP results.

---

## 📌 Key Pattern
👉 **"Tiling DP with a derived recurrence relation: dp[i] = 2*dp[i-1] + dp[i-3]"**

---

## 🔁 Related Problems
- 70. Climbing Stairs
- 1411. Number of Ways to Paint N x 3 Grid
- 2400. Number of Ways to Reach a Position After Exactly k Steps

---

## 🚀 Final Thoughts
This problem is a beautiful example of finding a recurrence from pattern observation. The key challenge is deriving the formula, which can be done by enumerating cases for small `n` values and noticing the relationship.

---

✨ **Rule to remember:**
> "For 2xN tiling with dominoes and trominoes: dp[i] = 2*dp[i-1] + dp[i-3]."
