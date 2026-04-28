# 944. Delete Columns to Make Sorted

## 🔗 Problem Link
https://leetcode.com/problems/delete-columns-to-make-sorted/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, String

---

## 🧩 Problem Summary

You are given an array of `n` strings `strs`, all of the same length. You want to delete some columns so that each remaining column is sorted in non-decreasing order. Return the number of columns you need to delete.

### 📌 Constraints
- `n == strs.length`
- `1 <= n <= 100`
- `1 <= strs[i].length <= 1000`
- `strs[i]` consists of lowercase English letters

---

## 💭 Intuition

A column is "unsorted" if any adjacent pair of rows has the character in the upper row greater than the character in the lower row. 👉 For each column, check all consecutive row pairs — if any violation is found, that column must be deleted.

---

## ⚡ Approach — Column-by-Column Check

### 🧠 Idea

- Iterate over each column index `j`.
- For each column, compare `strs[i][j]` with `strs[i+1][j]` for all adjacent rows.
- If any pair is out of order, increment the count and break (no need to check further in that column).

---

## 💻 Code

```python
class Solution:
  def minDeletionSize(self, strs: list[str]) -> int:
    ans = 0

    for j in range(len(strs[0])):
      for i in range(len(strs) - 1):
        if strs[i][j] > strs[i + 1][j]:
          ans += 1
          break

    return ans
```

---

## 🧠 Dry Run

### Input
```
strs = ["cba", "daf", "ghi"]
```

### Steps
```
Column 0: 'c' <= 'd' <= 'g' → sorted ✓
Column 1: 'b' > 'a' → unsorted ✗ → ans = 1
Column 2: 'a' <= 'f' <= 'i' → sorted ✓
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
O(1)
```

No extra space beyond a counter.

---

## ⚠️ Edge Cases

- **Single string:** No adjacent pairs to compare → 0 deletions
- **All columns sorted:** Answer is 0
- **All columns unsorted:** Answer equals the string length

---

## 🎯 Interview Takeaways

- Think of the problem as checking sortedness per column, not per row.
- Early `break` when a violation is found saves unnecessary comparisons.
- This is part of a series (944, 955, 960) with increasing difficulty.

---

## 📌 Key Pattern

👉 **"Check each column independently for sorted order among rows"**

---

## 🔁 Related Problems

- 955. Delete Columns to Make Sorted II
- 960. Delete Columns to Make Sorted III
- 1051. Height Checker

---

## 🚀 Final Thoughts

A simple column-wise check problem. The key observation is that each column can be evaluated independently — if any adjacent pair violates the order, the whole column is deleted.

---

✨ **Rule to remember:**
> A column needs deletion if even one adjacent row pair is out of order — check and break early.
