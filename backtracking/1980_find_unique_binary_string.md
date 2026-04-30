# 1980. Find Unique Binary String

## 🔗 Problem Link
https://leetcode.com/problems/find-unique-binary-string/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, String, Hash Table, Backtracking

---

## 🧩 Problem Summary
Given an array of `n` unique binary strings, each of length `n`, return a binary string of length `n` that does not appear in `nums`. There are multiple valid answers.

### 📌 Constraints
- `n == nums.length`
- `1 <= n <= 16`
- `nums[i].length == n`
- `nums[i]` is either `'0'` or `'1'`
- All strings in `nums` are unique

---

## 💭 Intuition
👉 Use Cantor's diagonal argument: construct a string that differs from the i-th string at position i. This guarantees the result differs from every string in the array.

---

## ⚡ Approach — Cantor's Diagonalization

### 🧠 Idea
- For each index `i`, look at `nums[i][i]` (the diagonal element).
- Flip it: if it's `'0'`, use `'1'`; if it's `'1'`, use `'0'`.
- The resulting string differs from `nums[i]` at position `i`, so it cannot equal any string in the array.

---

## 💻 Code

```python
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return ''.join('1' if nums[i][i] == '0' else '0' for i in range(len(nums)))
```

---

## 🧠 Dry Run
### Input
```
nums = ["01", "10"]
```
### Steps
```
i=0: nums[0][0] = '0' → use '1'
i=1: nums[1][1] = '0' → use '1'
Result: "11"

Verify: "11" ≠ "01" (differs at index 0)
         "11" ≠ "10" (differs at index 1)
```

---

## ⏱️ Time Complexity
```
O(n), where n is the length of the array
```

## 💾 Space Complexity
```
O(n) for the result string
```

---

## ⚠️ Edge Cases
- `n = 1`: `nums = ["0"]` → return `"1"`, or vice versa
- All diagonal elements are the same → result is all one character
- The diagonal string itself is in `nums` → impossible by construction

---

## 🎯 Interview Takeaways
- Cantor's diagonal argument is a powerful technique from set theory applied to CS.
- This is one of the most elegant one-liner solutions in LeetCode.
- The approach guarantees correctness without needing a hash set or brute force.

---

## 📌 Key Pattern
👉 **"Cantor's Diagonalization — differ from the i-th element at position i"**

---

## 🔁 Related Problems
- 268. Missing Number
- 448. Find All Numbers Disappeared in an Array
- 41. First Missing Positive

---

## 🚀 Final Thoughts
This is a beautiful application of a mathematical concept to a programming problem. By flipping the diagonal, we construct a string that is provably absent from the input — no searching or hashing required.

---

✨ **Rule to remember:**
> Flip the diagonal: differ from string `i` at index `i` to guarantee uniqueness.
