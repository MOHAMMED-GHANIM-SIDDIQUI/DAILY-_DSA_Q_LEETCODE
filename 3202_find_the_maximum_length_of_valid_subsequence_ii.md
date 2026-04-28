# 3202. Find the Maximum Length of Valid Subsequence II

## 🔗 Problem Link
https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Dynamic Programming

---

## 🧩 Problem Summary
Given an integer array `nums` and an integer `k`, find the maximum length of a subsequence where the sum of every two consecutive elements has the same remainder when divided by k. The pattern alternates: (a+b) mod k = (b+c) mod k = ...

### 📌 Constraints
- 2 <= nums.length <= 10^3
- 1 <= nums[i] <= 10^7
- 1 <= k <= 10^3

---

## 💭 Intuition
👉 If consecutive sums have the same remainder mod k, the subsequence follows an alternating pattern xyxyxy... in terms of mod-k values. Use a 2D DP table indexed by (last mod, next desired mod).

---

## ⚡ Approach — 2D DP on Mod Values

### 🧠 Idea
- dp[i][j] = max length of valid subsequence where the last element is i (mod k) and next desired element is j (mod k)
- For each number x in nums, for each possible "partner" y (0 to k-1), extend dp[x%k][y] = dp[y][x%k] + 1
- The answer is the maximum across all dp entries

---

## 💻 Code

```cpp
class Solution {
 public:
  // Similar to 3201. Find the Maximum Length of Valid Subsequence I
  int maximumLength(vector<int>& nums, int k) {
    // dp[i][j] := the maximum length of a valid subsequence, where the last
    // number mod k equal to i and the next desired number mod k equal to j
    vector<vector<int>> dp(k, vector<int>(k));

    // Extend the pattern xyxyxy...xy.
    for (const int x : nums)
      for (int y = 0; y < k; ++y)
        dp[x % k][y] = dp[y][x % k] + 1;

    return accumulate(dp.begin(), dp.end(), 0,
                      [](int acc, const vector<int>& row) {
      return max(acc, ranges::max(row));
    });
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [1, 2, 3, 4, 5], k = 2
```
### Steps
```
All mod 2: [1, 0, 1, 0, 1]
x=1 (mod 1): for y=0: dp[1][0]=dp[0][1]+1=1; y=1: dp[1][1]=dp[1][1]+1=1
x=2 (mod 0): for y=0: dp[0][0]=dp[0][0]+1=1; y=1: dp[0][1]=dp[1][0]+1=2
x=3 (mod 1): for y=0: dp[1][0]=dp[0][1]+1=3; y=1: dp[1][1]=dp[1][1]+1=2
x=4 (mod 0): for y=0: dp[0][0]=dp[0][0]+1=2; y=1: dp[0][1]=dp[1][0]+1=4
x=5 (mod 1): for y=0: dp[1][0]=dp[0][1]+1=5; y=1: dp[1][1]=dp[1][1]+1=3
max = 5
```

---

## ⏱️ Time Complexity
```
O(n * k) — for each of n elements, iterate over k possible partners
```

## 💾 Space Complexity
```
O(k^2) — 2D DP table of size k x k
```

---

## ⚠️ Edge Cases
- k = 1 — all sums have remainder 0, entire array is valid
- All elements have the same mod-k value — valid subsequence of full length
- Array of length 2 — always valid

---

## 🎯 Interview Takeaways
- The key observation is that consecutive sum mod k being constant implies alternating mod-k values
- The dp transition dp[x%k][y] = dp[y][x%k] + 1 elegantly captures the alternating pattern
- This generalizes problem 3201 from k=2 to arbitrary k

---

## 📌 Key Pattern
👉 **"Alternating-pattern DP on mod-k residues"**

---

## 🔁 Related Problems
- 3201. Find the Maximum Length of Valid Subsequence I
- 300. Longest Increasing Subsequence
- 1218. Longest Arithmetic Subsequence of Given Difference

---

## 🚀 Final Thoughts
The elegant dp[x%k][y] = dp[y][x%k] + 1 transition captures the alternating nature of the pattern. By working in mod-k space, the problem becomes manageable even for large values of nums[i].

---

✨ **Rule to remember:**
> Alternating mod-k pattern: dp[last_mod][next_mod] = dp[next_mod][last_mod] + 1.
