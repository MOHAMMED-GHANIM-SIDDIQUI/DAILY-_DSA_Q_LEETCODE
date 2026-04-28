# 712. Minimum ASCII Delete Sum for Two Strings

## 🔗 Problem Link
https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

## ⚡ Difficulty
Medium

## 🏷️ Topics
String, Dynamic Programming

---

## 🧩 Problem Summary

Given two strings `s1` and `s2`, return the lowest ASCII sum of deleted characters to make the two strings equal. You can delete characters from either string to achieve equality.

### 📌 Constraints
- `1 <= s1.length, s2.length <= 1000`
- `s1` and `s2` consist of lowercase English letters

---

## 💭 Intuition

This is a variation of the Longest Common Subsequence (LCS) problem but weighted by ASCII values. 👉 Instead of maximizing subsequence length, we minimize the total ASCII cost of deletions using a 2D DP table where `dp[i][j]` represents the minimum deletion cost to make `s1[0:i]` and `s2[0:j]` equal.

---

## ⚡ Approach — 2D Dynamic Programming

### 🧠 Idea

- Build a DP table of size `(m+1) x (n+1)`.
- Base cases: deleting all of `s1` or all of `s2` costs the sum of their ASCII values.
- If characters match (`s1[i-1] == s2[j-1]`), no deletion needed: `dp[i][j] = dp[i-1][j-1]`.
- Otherwise, take the minimum of deleting from `s1` or `s2`.
- Answer is `dp[m][n]`.

---

## 💻 Code

```python
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)

        # dp[i][j] = minimum ASCII delete sum to make s1[0:i] and s2[0:j] equal
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Delete all characters from s1
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])

        # Delete all characters from s2
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + ord(s1[i - 1]),  # delete from s1
                        dp[i][j - 1] + ord(s2[j - 1])   # delete from s2
                    )

        return dp[m][n]
```

---

## 🧠 Dry Run

### Input
```
s1 = "sea", s2 = "eat"
```

### Steps
```
dp table (4x4):
       ""    e     a     t
""   [ 0,  101,  198,  314]
s    [115, 116,  213,  329]
e    [216, 115,  213,  329]
a    [313, 212,  115,  231]

dp[3][3] = 231
Delete 's' (115) from s1 and 't' (116) from s2 → 115 + 116 = 231
```

---

## ⏱️ Time Complexity

```
O(m * n)
```

We fill a 2D table of size (m+1) x (n+1).

---

## 💾 Space Complexity

```
O(m * n)
```

For the 2D DP table. Can be optimized to O(n) with a rolling array.

---

## ⚠️ Edge Cases

- **One empty string:** All characters of the other string must be deleted.
- **Identical strings:** No deletions needed, answer is 0.
- **No common characters:** Sum of all ASCII values of both strings.

---

## 🎯 Interview Takeaways

- This is a weighted variant of Edit Distance / LCS — a classic DP pattern.
- The transition depends on character equality, similar to LCS.
- Understanding ord() values and how they affect costs is key.
- Can be space-optimized to 1D since each row only depends on the previous row.

---

## 📌 Key Pattern

👉 **"Weighted LCS variant — minimize ASCII cost of deletions with 2D DP"**

---

## 🔁 Related Problems

- 583. Delete Operation for Two Strings
- 1143. Longest Common Subsequence
- 72. Edit Distance
- 1092. Shortest Common Supersequence

---

## 🚀 Final Thoughts

A great DP problem that extends the classic LCS concept by adding weights (ASCII values) to deletions. The DP recurrence is elegant and mirrors the LCS structure.

---

✨ **Rule to remember:**
> When characters match, carry forward the cost; when they don't, pick the cheaper deletion.
