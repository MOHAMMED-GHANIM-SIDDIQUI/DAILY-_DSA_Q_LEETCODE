# 1356. Sort Integers by The Number of 1 Bits

## 🔗 Problem Link
https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Sorting, Bit Manipulation

---

## 🧩 Problem Summary
Given an integer array `arr`, sort it in ascending order by the number of `1`s in the binary representation. For integers with the same number of `1`s, sort them in ascending order by value.

### 📌 Constraints
- `1 <= arr.length <= 500`
- `0 <= arr[i] <= 10^4`

---

## 💭 Intuition
👉 Use a custom sort key that first compares by bit count, then by value. Python's `bit_count()` and tuple-based sorting make this a one-liner.

---

## ⚡ Approach — Custom Sort with Bit Count

### 🧠 Idea
- Sort using a key function that returns `(bit_count, value)`.
- Python's `sorted` is stable and handles tuple comparison lexicographically.
- `bit_count()` returns the number of set bits in O(1).

---

## 💻 Code

```python
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (x.bit_count(), x))
```

---

## 🧠 Dry Run
### Input
```
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
```
### Steps
```
bit_count: 0→0, 1→1, 2→1, 3→2, 4→1, 5→2, 6→2, 7→3, 8→1
Sort by (bits, value):
(0,0), (1,1), (1,2), (1,4), (1,8), (2,3), (2,5), (2,6), (3,7)
Result = [0, 1, 2, 4, 8, 3, 5, 6, 7]
```

---

## ⏱️ Time Complexity
```
O(n log n) — dominated by sorting
```

## 💾 Space Complexity
```
O(n) — for the sorted output
```

---

## ⚠️ Edge Cases
- `arr = [0]` → return `[0]` (zero set bits)
- All elements have the same bit count → sort by value
- All elements are the same → unchanged

---

## 🎯 Interview Takeaways
- Python's `sorted` with tuple keys is extremely expressive.
- `bit_count()` (Python 3.10+) is the modern way to count set bits.
- Custom sort keys are a frequent interview pattern.

---

## 📌 Key Pattern
👉 **"Custom sort with a composite key — (primary criterion, tiebreaker)."**

---

## 🔁 Related Problems
- 191. Number of 1 Bits
- 338. Counting Bits
- 1342. Number of Steps to Reduce a Number to Zero

---

## 🚀 Final Thoughts
An elegant one-liner leveraging Python's powerful sorting and built-in bit operations. The composite key pattern is a must-know for custom sorting problems.

---

✨ **Rule to remember:**
> Sort by `(bit_count, value)` — Python tuples compare lexicographically by default.
