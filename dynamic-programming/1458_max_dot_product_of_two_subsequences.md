# 1458. Max Dot Product of Two Subsequences

## 🔗 Problem Link
https://leetcode.com/problems/max-dot-product-of-two-subsequences/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Dynamic Programming, Array

---

## 🧩 Problem Summary
Given two arrays `nums1` and `nums2`, select non-empty subsequences from each (of equal length) and compute the dot product. Return the maximum dot product possible among all such pairs of subsequences.

### 📌 Constraints
- `1 <= nums1.length, nums2.length <= 500`
- `-1000 <= nums1[i], nums2[j] <= 1000`

---

## 💭 Intuition
👉 This is a 2D DP problem similar to Longest Common Subsequence. At each pair `(i, j)`, we decide whether to include `A[i] * B[j]` in our dot product (possibly extending a previous subsequence or starting fresh), or skip one of the elements. Using `max(0, dp[i][j])` ensures we can start a new subsequence if the accumulated product so far is negative.

---

## ⚡ Approach — 2D Dynamic Programming

### 🧠 Idea
- Define `dp[i][j]` as the maximum dot product using `A[0..i)` and `B[0..j)`.
- Initialize all values to `-inf` to handle the case where all products are negative.
- Transition: `dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j], max(0, dp[i][j]) + A[i]*B[j])`.
- The answer is `dp[m][n]`.

---

## 💻 Code

```python
class Solution:
  def maxDotProduct(self, A: list[int], B: list[int]) -> int:
    m = len(A)
    n = len(B)
    # dp[i][j] := the maximum dot product of the two subsequences nums[0..i)
    # and nums2[0..j)
    dp = [[-math.inf] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
      for j in range(n):
        dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j],
                               max(0, dp[i][j]) + A[i] * B[j])

    return dp[m][n]
```

---

## 🧠 Dry Run
### Input
```
A = [2, 1, -2, 5], B = [3, 0, -6]
```
### Steps
```
dp initialized to -inf grid of size 5x4
i=0, j=0: dp[1][1] = max(-inf, -inf, max(0,-inf)+2*3) = 6
i=0, j=1: dp[1][2] = max(-inf, 6, max(0,-inf)+2*0) = 6
i=0, j=2: dp[1][3] = max(-inf, 6, max(0,-inf)+2*(-6)) = 6
i=1, j=0: dp[2][1] = max(6, -inf, max(0,-inf)+1*3) = 6
...
i=3, j=0: includes 5*3 = 15
Final dp[4][3] = 18 (selecting [2,5] and [3,0] → 2*3 + 5*0 = 6, or better combos)
Answer: 18
```

---

## ⏱️ Time Complexity
```
O(m * n), where m and n are the lengths of the two arrays
```

## 💾 Space Complexity
```
O(m * n) for the DP table
```

---

## ⚠️ Edge Cases
- All elements of one array are positive and all of the other are negative — must still pick at least one pair.
- Single-element arrays — return `A[0] * B[0]`.
- Large negative products — the `-inf` initialization ensures correct handling.

---

## 🎯 Interview Takeaways
- Recognizing the LCS-style 2D DP pattern is key.
- Using `max(0, dp[i][j])` allows starting a fresh subsequence when the accumulated product is negative.
- Initializing with `-inf` forces at least one element to be selected.

---

## 📌 Key Pattern
👉 **"2D DP with optional subsequence extension — similar to LCS but with product accumulation"**

---

## 🔁 Related Problems
- 1143 — Longest Common Subsequence
- 72 — Edit Distance
- 516 — Longest Palindromic Subsequence

---

## 🚀 Final Thoughts
This problem elegantly extends the LCS framework to handle dot products. The trick of using `max(0, dp[i][j])` to optionally reset the accumulated value is a powerful technique for subsequence DP problems where starting fresh might be better than continuing.

---

✨ **Rule to remember:**
> "When computing max dot product of subsequences, treat it like LCS but allow fresh starts with `max(0, prev) + product`."
