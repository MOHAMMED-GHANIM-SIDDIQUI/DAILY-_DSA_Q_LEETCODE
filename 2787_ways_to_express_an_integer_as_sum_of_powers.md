# 2787. Ways to Express an Integer as Sum of Powers

## 🔗 Problem Link
https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Dynamic Programming, Math

---

## 🧩 Problem Summary
Given two positive integers `n` and `x`, return the number of ways `n` can be expressed as the sum of the x-th power of unique positive integers, modulo 10^9 + 7. Each integer can be used at most once.

### 📌 Constraints
- `1 <= n <= 300`
- `1 <= x <= 5`

---

## 💭 Intuition
👉 This is a variant of the subset sum / 0-1 knapsack problem. The "items" are `1^x, 2^x, 3^x, ...` (as long as they don't exceed `n`), and we want to count the number of subsets that sum to exactly `n`.

---

## ⚡ Approach — 0-1 Knapsack DP

### 🧠 Idea
- `dp[i]` = number of ways to form sum `i` using powers considered so far.
- For each base `a = 1, 2, 3, ...` where `a^x <= n`, iterate `dp` in reverse (standard 0-1 knapsack) and add `dp[i - a^x]` to `dp[i]`.

---

## 💻 Code

```cpp
class Solution {
 public:
  int numberOfWays(int n, int x) {
    constexpr int kMod = 1'000'000'007;
    // dp[i] := the number of ways to express i
    vector<int> dp(n + 1);
    int ax;  // a^x

    dp[0] = 1;

    for (int a = 1; (ax = pow(a, x)) <= n; ++a)
      for (int i = n; i >= ax; --i) {
        dp[i] += dp[i - ax];
        dp[i] %= kMod;
      }

    return dp[n];
  }
};
```

---

## 🧠 Dry Run
### Input
```
n = 10, x = 2
```
### Steps
```
Powers: 1^2=1, 2^2=4, 3^2=9 (4^2=16 > 10, stop)

After a=1 (power=1): dp updates for using 1
  dp = [1,1,0,0,0,0,0,0,0,0,0]

After a=2 (power=4): dp updates for using 4
  dp = [1,1,0,0,1,1,0,0,0,0,0]

After a=3 (power=9): dp updates for using 9
  dp = [1,1,0,0,1,1,0,0,0,1,1]

dp[10] = 1 (only way: 1 + 9 = 1^2 + 3^2)
```

---

## ⏱️ Time Complexity
```
O(n * n^(1/x)) — for each base up to n^(1/x), iterate dp of size n
```

## 💾 Space Complexity
```
O(n)
```

---

## ⚠️ Edge Cases
- `n = 1, x = 1`: only one way (1^1 = 1)
- `x` is large: very few valid bases (e.g., x=5, only bases 1 and 2 for n <= 300)
- No valid combination exists — return 0

---

## 🎯 Interview Takeaways
- The 0-1 knapsack pattern with reverse iteration ensures each item is used at most once.
- Recognizing this as a subset sum variant is the key insight.

---

## 📌 Key Pattern
👉 **"0-1 Knapsack / Subset Sum with custom item values (powers of integers)"**

---

## 🔁 Related Problems
- 416. Partition Equal Subset Sum
- 494. Target Sum
- 518. Coin Change II

---

## 🚀 Final Thoughts
A clean application of the 0-1 knapsack pattern. The items are x-th powers of unique integers, and the target sum is `n`. The reverse iteration in the inner loop ensures each power is used at most once.

---

✨ **Rule to remember:**
> For counting subsets summing to a target where each element is used at most once, use the 0-1 knapsack DP with reverse iteration.
