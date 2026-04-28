# 474. Ones and Zeroes

## 🔗 Problem Link
https://leetcode.com/problems/ones-and-zeroes/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, String, Dynamic Programming

---

## 🧩 Problem Summary
Given an array of binary strings strs and two integers m (max 0s) and n (max 1s), return the size of the largest subset of strs such that there are at most m 0s and n 1s in the subset combined.

### 📌 Constraints
- `1 <= strs.length <= 600`
- `1 <= strs[i].length <= 100`
- `strs[i]` consists only of '0' and '1'
- `1 <= m, n <= 100`

---

## 💭 Intuition
👉 This is a 2D 0/1 knapsack problem where the two "weights" are the count of 0s and 1s in each string, and we want to maximize the number of items (strings) we can pick.

---

## ⚡ Approach — 2D Knapsack DP

### 🧠 Idea
- Create a 2D DP table `dp[i][j]` = max subset size with i 0s and j 1s available.
- For each string, count its 0s and 1s.
- Iterate backwards through the DP table (to maintain 0/1 constraint).
- Update: `dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)`.

---

## 💻 Code

```cpp
class Solution {
 public:
  int findMaxForm(vector<string>& strs, int m, int n) {
    // dp[i][j] := the maximum size of the subset given i 0s and j 1s are
    // available
    vector<vector<int>> dp(m + 1, vector<int>(n + 1));

    for (const string& s : strs) {
      const int zeros = ranges::count(s, '0');
      const int ones = s.length() - zeros;
      for (int i = m; i >= zeros; --i)
        for (int j = n; j >= ones; --j)
          dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1);
    }

    return dp[m][n];
  }
};
```

---

## 🧠 Dry Run
### Input
```
strs = ["10","0001","111001","1","0"], m = 5, n = 3
```
### Steps
```
"10": zeros=1, ones=1 -> update dp for i>=1, j>=1
"0001": zeros=3, ones=1 -> update dp for i>=3, j>=1
"111001": zeros=2, ones=4 -> j>=4 but n=3, skip all updates
"1": zeros=0, ones=1 -> update dp for i>=0, j>=1
"0": zeros=1, ones=0 -> update dp for i>=1, j>=0
dp[5][3] = 4 (pick "10","0001","1","0")
```

---

## ⏱️ Time Complexity
```
O(l * m * n) where l = number of strings
```

## 💾 Space Complexity
```
O(m * n) — 2D DP table
```

---

## ⚠️ Edge Cases
- String with all 0s or all 1s.
- m = 0 or n = 0 — can only pick strings with no 0s or no 1s respectively.
- Single string — pick it if it fits within m and n.
- String too large to fit — automatically skipped by loop bounds.

---

## 🎯 Interview Takeaways
- Recognizing the 2D knapsack structure is the key insight.
- Backward iteration prevents using the same string twice.
- This generalizes the classic 0/1 knapsack to two dimensions.

---

## 📌 Key Pattern
👉 **"2D 0/1 knapsack — two resource constraints (0s and 1s) with item maximization"**

---

## 🔁 Related Problems
- 416. Partition Equal Subset Sum
- 494. Target Sum
- 322. Coin Change

---

## 🚀 Final Thoughts
This is a clean extension of the classic knapsack problem to two dimensions. The same backward-iteration trick ensures the 0/1 constraint, and the DP table naturally handles both resource limits.

---

✨ **Rule to remember:**
> "Two resource limits? Use a 2D knapsack — iterate backwards on both dimensions."
