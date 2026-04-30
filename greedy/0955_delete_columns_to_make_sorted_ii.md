# 955. Delete Columns to Make Sorted II

## 🔗 Problem Link
https://leetcode.com/problems/delete-columns-to-make-sorted-ii/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, String, Greedy

---

## 🧩 Problem Summary

Given an array of strings `strs` (all same length), delete the minimum number of columns so that the remaining columns, when read row-by-row as strings, form a lexicographically sorted sequence. Return the number of columns to delete.

### 📌 Constraints
- `n == strs.length`
- `1 <= n <= 100`
- `1 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters

---

## 💭 Intuition

Unlike problem 944 where each column is independent, here columns work together. 👉 Once a pair of adjacent rows is already strictly ordered by previous columns, we don't need to check that pair for the current column. We greedily keep a column if it doesn't create any new violations among the not-yet-resolved pairs.

---

## ⚡ Approach — Greedy with Sorted Tracking Array

### 🧠 Idea

- Maintain a boolean array `sorted_[i]` indicating whether `strs[i]` is already strictly less than `strs[i+1]` based on previously kept columns.
- For each column, check if keeping it would cause any violation among unresolved pairs.
- If a violation is found, delete the column (increment count).
- Otherwise, keep the column and update `sorted_` for pairs that become strictly ordered.

---

## 💻 Code

```python
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        ans = 0
        # sorted[i] := True if strs[i] < strs[i + 1]
        sorted_ = [False] * (n - 1)

        for j in range(len(strs[0])):  # Loop through each character in the column
            i = 0
            while i + 1 < n:
                if not sorted_[i] and strs[i][j] > strs[i + 1][j]:
                    ans += 1
                    break
                i += 1

            # Update the sorted array after comparing all pairs for this column
            if i + 1 == n:
                for i in range(n - 1):
                    sorted_[i] = sorted_[i] or strs[i][j] < strs[i + 1][j]

        return ans
```

---

## 🧠 Dry Run

### Input
```
strs = ["ca", "bb", "ac"]
```

### Steps
```
sorted_ = [False, False]

Column 0 ('c','b','a'):
  i=0: not sorted_[0] and 'c' > 'b' → violation! ans=1, delete column 0

Column 1 ('a','b','c'):
  i=0: not sorted_[0] and 'a' <= 'b' → OK
  i=1: not sorted_[1] and 'b' <= 'c' → OK
  i+1 == n → keep column
  Update: sorted_[0] = True ('a'<'b'), sorted_[1] = True ('b'<'c')

Return 1
```

---

## ⏱️ Time Complexity

```
O(n * m)
```

Where n is the number of strings and m is the length of each string.

---

## 💾 Space Complexity

```
O(n)
```

For the `sorted_` tracking array.

---

## ⚠️ Edge Cases

- **Already sorted rows:** No deletions needed → 0
- **Single row:** Always sorted → 0
- **All columns must be deleted except one:** Need at least one non-decreasing column

---

## 🎯 Interview Takeaways

- The "already resolved" concept is key — once two adjacent rows are strictly ordered, they stay ordered regardless of future columns.
- This greedy approach avoids exponential search by making local decisions per column.
- The `sorted_` array is the crucial state that tracks which pairs are already resolved.
- Understand the difference between this problem and 944 (independent columns) and 960 (subsequence).

---

## 📌 Key Pattern

👉 **"Greedily keep columns that don't violate unresolved adjacent pairs, tracking strict orderings"**

---

## 🔁 Related Problems

- 944. Delete Columns to Make Sorted
- 960. Delete Columns to Make Sorted III
- 1061. Lexicographically Smallest Equivalent String

---

## 🚀 Final Thoughts

A tricky greedy problem where the key insight is tracking which adjacent row pairs are already strictly ordered. Once a pair is resolved, it never needs checking again.

---

✨ **Rule to remember:**
> Once two rows are strictly ordered by earlier columns, they're resolved forever — only check unresolved pairs.
