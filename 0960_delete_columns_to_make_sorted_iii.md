# 960. Delete Columns to Make Sorted III

## 🔗 Problem Link
https://leetcode.com/problems/delete-columns-to-make-sorted-iii/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, String, Dynamic Programming

---

## 🧩 Problem Summary

Given an array of strings `strs` (all same length), delete the minimum number of columns such that the remaining columns form a subsequence where each row is individually sorted in non-decreasing order. Return the number of columns to delete.

### 📌 Constraints
- `n == strs.length`
- `1 <= n <= 100`
- `1 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters

---

## 💭 Intuition

This is equivalent to finding the Longest Increasing Subsequence (LIS) of columns, where column `j` can follow column `i` only if `strs[r][i] <= strs[r][j]` for ALL rows `r`. 👉 The answer is total columns minus the length of the longest valid column subsequence.

---

## ⚡ Approach — LIS on Columns

### 🧠 Idea

- Define `dp[i]` as the length of the longest valid subsequence of columns ending at column `i`.
- For each pair of columns `(j, i)` where `j < i`, check if column `j` can precede column `i` (i.e., `s[j] <= s[i]` for all strings `s`).
- If yes, `dp[i] = max(dp[i], dp[j] + 1)`.
- Answer is `k - max(dp)` where `k` is the total number of columns.

---

## 💻 Code

```python
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        k = len(strs[0])
        # dp[i]: length of LIS ending at column i
        dp = [1] * k

        for i in range(1, k):
            for j in range(i):
                # check if column j <= column i for all rows
                if all(s[j] <= s[i] for s in strs):
                    dp[i] = max(dp[i], dp[j] + 1)

        return k - max(dp)
```

---

## 🧠 Dry Run

### Input
```
strs = ["babca", "bbazb"]
```

### Steps
```
k = 5, dp = [1, 1, 1, 1, 1]

i=1: j=0: col0=['b','b'], col1=['a','b'] → 'b'>'a' fails → skip
i=2: j=0: col0=['b','b'], col2=['b','a'] → 'b'>'a' fails → skip
     j=1: col1=['a','b'], col2=['b','a'] → 'b'>'a' fails → skip
i=3: j=0: col0=['b','b'], col3=['c','z'] → 'b'<='c' and 'b'<='z' ✓ → dp[3]=2
     j=1: col1=['a','b'], col3=['c','z'] → 'a'<='c' and 'b'<='z' ✓ → dp[3]=2
     j=2: col2=['b','a'], col3=['c','z'] → 'b'<='c' and 'a'<='z' ✓ → dp[3]=2
i=4: j=0: 'b'>'a' and 'b'>'b' fails → skip
     j=1: 'a'<='a' and 'b'<='b' ✓ → dp[4]=2
     j=2: 'b'>'a' fails → skip
     j=3: 'c'>'a' fails → skip

dp = [1, 1, 1, 2, 2], max = 2
Return 5 - 2 = 3
```

---

## ⏱️ Time Complexity

```
O(n * k^2)
```

Where k is the column count and n is the number of rows. For each pair of columns, we check all n rows.

---

## 💾 Space Complexity

```
O(k)
```

For the DP array of length k.

---

## ⚠️ Edge Cases

- **Single column:** No deletions possible → 0
- **All columns identical across all rows:** All columns are compatible → 0
- **Completely unsorted:** Only keep the longest valid single column → delete k-1

---

## 🎯 Interview Takeaways

- Recognizing this as an LIS variant on columns is the critical insight.
- The "compatibility" check between two columns requires ALL rows to satisfy the ordering.
- This is the hardest of the three "Delete Columns" problems (944 → 955 → 960).
- The `all()` function in Python provides a clean way to check multi-row constraints.

---

## 📌 Key Pattern

👉 **"LIS on columns where compatibility requires all rows to be non-decreasing"**

---

## 🔁 Related Problems

- 300. Longest Increasing Subsequence
- 944. Delete Columns to Make Sorted
- 955. Delete Columns to Make Sorted II

---

## 🚀 Final Thoughts

A beautiful application of the LIS pattern to a 2D setting. The key transformation is viewing columns as elements and defining a partial order where column `j <= i` means all rows agree.

---

✨ **Rule to remember:**
> Minimum deletions to make columns sorted = total columns minus the longest compatible column subsequence (LIS).
