# 2338. Count the Number of Ideal Arrays

## 🔗 Problem Link
https://leetcode.com/problems/count-the-number-of-ideal-arrays/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Math, Dynamic Programming, Combinatorics, Number Theory

---

## 🧩 Problem Summary
An array of length `n` is ideal if every element is between 1 and `maxValue`, and each element divides the next. Return the count of distinct ideal arrays modulo 10^9 + 7.

### 📌 Constraints
- `2 <= n <= 10^4`
- `1 <= maxValue <= 10^4`

---

## 💭 Intuition
👉 The strictly divisible chain of distinct values has at most ~log2(maxValue) ≈ 14 elements. We can count chains of each length using a sieve-like DP, then use combinations (stars and bars) to distribute the chain across `n` positions.

---

## ⚡ Approach — Divisor Chain DP + Combinatorics

### 🧠 Idea
- `dp[len][val]` = number of strictly increasing divisor chains of length `len` ending at `val`.
- Base case: `dp[1][v] = 1` for all v in [1, maxValue].
- Transition: for each value `i`, iterate over its multiples `j = 2i, 3i, ...` and update `dp[len][j] += dp[len-1][i]`.
- For a chain of length `len`, it can be placed into an array of length `n` using C(n-1, len-1) (choosing where to change values).
- Sum over all lengths and all ending values.

---

## 💻 Code

```cpp
class Solution {
public:
    const int MOD = 1e9 + 7;
    const int MAX = 10010; // Upper bound for n

    // Precompute nCr (combinations) using Pascal's triangle
    void computeCombinations(vector<vector<int>>& comb, int n) {
        for (int i = 0; i <= n; ++i) {
            comb[i][0] = 1;
            for (int j = 1; j < 20; ++j) {
                if (i >= j)
                    comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % MOD;
            }
        }
    }

    int idealArrays(int n, int maxValue) {
        vector<vector<int>> comb(MAX, vector<int>(20, 0));
        computeCombinations(comb, n);

        // dp[len][val] = number of arrays of length 'len' ending in 'val'
        vector<vector<int>> dp(20, vector<int>(maxValue + 1, 0));

        // Base case: 1-length arrays, 1 way for each value
        for (int i = 1; i <= maxValue; ++i)
            dp[1][i] = 1;

        // Fill DP table for lengths 2 to 19
        for (int len = 2; len < 20; ++len) {
            for (int i = 1; i <= maxValue; ++i) {
                for (int j = 2*i; j <= maxValue; j += i) {
                    dp[len][j] = (dp[len][j] + dp[len-1][i]) % MOD;
                }
            }
        }

        // Now sum the total ways using combinations
        int result = 0;
        for (int len = 1; len < 20; ++len) {
            for (int val = 1; val <= maxValue; ++val) {
                long long ways = dp[len][val];
                long long choose = comb[n-1][len-1]; // choose (len-1) positions from (n-1)
                result = (result + ways * choose % MOD) % MOD;
            }
        }

        return result;
    }
};
```

---

## 🧠 Dry Run
### Input
```
n = 2, maxValue = 5
```
### Steps
```
Chains of length 1: [1],[2],[3],[4],[5] → 5 chains, each with C(1,0)=1 → 5
Chains of length 2: [1,2],[1,3],[1,4],[1,5],[2,4] → 5 chains, each with C(1,1)=1 → 5
Total = 5 + 5 = 10
Result: 10
```

---

## ⏱️ Time Complexity
```
O(maxValue * log(maxValue) * 20 + n * 20) — sieve-like DP transitions plus combination precomputation.
```

## 💾 Space Complexity
```
O(n * 20 + maxValue * 20) — combination table and DP table.
```

---

## ⚠️ Edge Cases
- `maxValue = 1`: only one array [1,1,...,1].
- `n = 2`: chains can be at most length 2.
- Large `n` with small `maxValue`: most arrays repeat values.

---

## 🎯 Interview Takeaways
- Divisor chains have bounded length (~log2 of max value).
- Sieve-of-Eratosthenes style iteration efficiently builds divisor relationships.
- Stars and bars / combinations map chain length to array arrangements.

---

## 📌 Key Pattern
👉 **"Bounded-length divisor chains + combinatorics (stars and bars) to count placements."**

---

## 🔁 Related Problems
- 1735. Count Ways to Make Array With Product
- 2507. Smallest Value After Replacing With Sum of Prime Factors
- 368. Largest Divisible Subset

---

## 🚀 Final Thoughts
The insight that divisor chains are at most ~14 elements long transforms this from an intractable problem into an elegant DP + combinatorics solution. The sieve-like enumeration of multiples keeps transitions efficient.

---

✨ **Rule to remember:**
> "Divisor chains are short — enumerate chain shapes, then use combinations to place them."
