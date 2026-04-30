# 66. Plus One (v2)

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

👉 This is a variation of the same string-conversion approach as v1, using a list comprehension instead of `map()`. The idea is identical: convert to integer, add one, convert back. The difference is purely stylistic.

---

## ⚡ Approach — String Conversion with List Comprehension

### 🧠 Idea

- Join all digits into a string using `map(str, digits)`.
- Convert the joined string to an integer and add 1.
- Convert the result back to a string and use a list comprehension to build the output list.

---

## 💻 Code

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
       return [int(i) for i in str(int(''.join(map(str,digits))) + 1) ]
```

---

## 🧠 Dry Run

### Input
```
digits = [9, 9]
```

### Steps
```
1. map(str, digits) → ['9', '9']
2. ''.join(...)    → '99'
3. int('99')       → 99
4. 99 + 1          → 100
5. str(100)        → '100'
6. [int(i) for i in '100'] → [1, 0, 0]
Return [1, 0, 0]
```

---

## ⏱️ Time Complexity

```
O(n)
```

Where n is the number of digits. All operations are linear.

---

## 💾 Space Complexity

```
O(n)
```

Space for the intermediate string and result list.

---

## ⚠️ Edge Cases

- **All nines:** `digits = [9, 9, 9]` → `[1, 0, 0, 0]`
- **Single zero:** `digits = [0]` → `[1]`
- **Large number:** `digits = [1,0,0,0,0,0,0,0,0,0]` → `[1,0,0,0,0,0,0,0,0,1]`

---

## 🎯 Interview Takeaways

- List comprehension `[int(i) for i in ...]` is often more readable than `list(map(int, ...))`.
- Both v1 and v2 rely on Python's unlimited integer precision.
- Interviewers may prefer the in-place carry propagation approach to test algorithmic thinking.
- Knowing multiple ways to express the same logic shows Python fluency.

---

## 📌 Key Pattern

👉 **"String conversion round-trip: digits → int → operate → digits."**

---

## 🔁 Related Problems

- 67. Add Binary
- 2. Add Two Numbers
- 369. Plus One Linked List
- 989. Add to Array-Form of Integer

---

## 🚀 Final Thoughts

This variant uses list comprehension for the final conversion step, which some find more Pythonic. Both v1 and v2 are functionally identical — choose based on style preference.

---

✨ **Rule to remember:**
> "List comprehensions and map() are interchangeable — pick the one your team reads fastest."
