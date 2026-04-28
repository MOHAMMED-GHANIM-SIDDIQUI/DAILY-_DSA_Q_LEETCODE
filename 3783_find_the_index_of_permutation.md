# 3783. Find the Index of Permutation

## 🔗 Problem Link
https://leetcode.com/problems/find-the-index-of-permutation/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Math, String

---

## 🧩 Problem Summary
Given an integer `n`, return the absolute difference between `n` and its digit-reversed form. This computes the "mirror distance" of a number from its reverse.

### 📌 Constraints
- `0 <= n <= 10^9`

---

## 💭 Intuition
👉 Simply reverse the digits of `n` by converting to a string, reversing it, converting back to an integer, and taking the absolute difference with the original.

---

## ⚡ Approach — String Reversal and Subtraction

### 🧠 Idea
- Convert `n` to a string.
- Reverse the string.
- Convert back to integer (automatically removes leading zeros).
- Return the absolute difference: `|n - reversed_n|`.

---

## 💻 Code

```python
class Solution:
    def mirrorDistance(self, n: int) -> int:
      return abs((n - int(str(n)[::-1])))
```

---

## 🧠 Dry Run
### Input
```
n = 123
```
### Steps
```
str(123) = "123"
"123"[::-1] = "321"
int("321") = 321
abs(123 - 321) = abs(-198) = 198

Result: 198
```

---

## ⏱️ Time Complexity
```
O(d) — where d is the number of digits in n (for string conversion and reversal)
```

## 💾 Space Complexity
```
O(d) — for the string representation
```

---

## ⚠️ Edge Cases
- `n = 0` → reverse is 0, difference is 0
- Palindromic numbers (e.g., 121) → reverse equals itself, difference is 0
- Numbers ending in zeros (e.g., 100) → reverse is 1, difference is 99
- Single digit numbers → always return 0

---

## 🎯 Interview Takeaways
- Python's `str(n)[::-1]` is a concise way to reverse digits.
- `int()` on the reversed string automatically strips leading zeros.
- This is a one-liner problem — clarity and correctness matter more than complexity here.

---

## 📌 Key Pattern
👉 **"Reverse digits via string slicing and compute the absolute difference — a classic number manipulation pattern."**

---

## 🔁 Related Problems
- 7. Reverse Integer
- 9. Palindrome Number
- 2119. A Number After a Double Reversal

---

## 🚀 Final Thoughts
This is a straightforward problem that tests basic number-to-string manipulation. The one-liner solution is as clean as it gets. The main subtlety is that `int()` handles leading zeros in the reversed string, so numbers like 100 (reversed to "001" = 1) work correctly.

---

✨ **Rule to remember:**
> "To find the mirror distance: reverse the digits, subtract, take absolute value — Python's string slicing makes it a one-liner."
