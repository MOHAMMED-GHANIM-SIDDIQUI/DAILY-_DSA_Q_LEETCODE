# 66. Plus One

## 🔗 Problem Link
https://leetcode.com/problems/plus-one/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Math

---

## 🧩 Problem Summary

You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the i-th digit of the integer. The digits are ordered from most significant to least significant. Increment the large integer by one and return the resulting array of digits.

### 📌 Constraints
- `1 <= digits.length <= 100`
- `0 <= digits[i] <= 9`
- `digits` does not contain any leading 0's (except the number 0 itself)

---

## 💭 Intuition

👉 Instead of manually handling carry propagation, this approach converts the digit array to a full integer, adds one, and converts back to a list of digits. This is a clean Pythonic shortcut leveraging Python's arbitrary precision integers.

---

## ⚡ Approach — String Conversion

### 🧠 Idea

- Join all digits into a string, convert to integer.
- Add 1 to the integer.
- Convert the result back to a string, then map each character back to an integer in a list.

---

## 💻 Code

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
            return list(map(int, str(int(''.join(map(str, digits))) + 1)))
```

---

## 🧠 Dry Run

### Input
```
digits = [1, 2, 9]
```

### Steps
```
1. map(str, digits) → ['1', '2', '9']
2. ''.join(...)    → '129'
3. int('129')      → 129
4. 129 + 1         → 130
5. str(130)        → '130'
6. map(int, '130') → [1, 3, 0]
Return [1, 3, 0]
```

---

## ⏱️ Time Complexity

```
O(n)
```

Where n is the number of digits. String join, conversion, and mapping are all linear.

---

## 💾 Space Complexity

```
O(n)
```

Space for the intermediate string and result list.

---

## ⚠️ Edge Cases

- **All nines:** `digits = [9, 9, 9]` → `[1, 0, 0, 0]` (length increases by 1)
- **Single digit:** `digits = [0]` → `[1]`
- **No carry:** `digits = [1, 2, 3]` → `[1, 2, 4]`

---

## 🎯 Interview Takeaways

- Python's arbitrary precision integers make digit-array math trivial via string conversion.
- This approach trades algorithmic elegance for brevity — great for Python but not transferable to languages with fixed integer sizes.
- Know the manual carry-propagation approach too, as interviewers may ask for it.
- One-liners can be impressive but ensure readability.

---

## 📌 Key Pattern

👉 **"Convert digits to integer, operate, convert back — leverage Python's big integers."**

---

## 🔁 Related Problems

- 67. Add Binary
- 2. Add Two Numbers
- 369. Plus One Linked List
- 989. Add to Array-Form of Integer

---

## 🚀 Final Thoughts

Plus One is a simple problem that can be solved elegantly with Python's string and integer conversion. However, understanding the manual carry-propagation approach is essential for interviews.

---

✨ **Rule to remember:**
> "When digits form a number, sometimes the fastest path is: array → number → operate → array."
