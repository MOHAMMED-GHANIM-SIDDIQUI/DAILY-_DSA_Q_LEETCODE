# 231. Power of Two

## 🔗 Problem Link
https://leetcode.com/problems/power-of-two/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Math, Bit Manipulation, Recursion

---

## 🧩 Problem Summary
Given an integer n, return true if it is a power of two. An integer n is a power of two if there exists an integer x such that n == 2^x.

### 📌 Constraints
- `-2^31 <= n <= 2^31 - 1`

---

## 💭 Intuition
👉 A power of two in binary has exactly one set bit. The expression `n & (n - 1)` clears the lowest set bit — if the result is 0, there was only one set bit.

---

## ⚡ Approach — Bit Manipulation

### 🧠 Idea
- Check that n is positive (powers of two are always positive).
- Use `n & (n - 1) == 0` to verify n has exactly one set bit.
- This works because subtracting 1 from a power of two flips all bits below the single set bit.

---

## 💻 Code

```cpp
class Solution {
public:
    bool isPowerOfTwo(int n) {
        return n > 0 && (n & (n - 1)) == 0;
    }
};
```

---

## 🧠 Dry Run
### Input
```
n = 16
```
### Steps
```
n = 16 = 10000 in binary
n - 1 = 15 = 01111 in binary
n & (n-1) = 10000 & 01111 = 00000 = 0
n > 0 && 0 == 0 => true
```

---

## ⏱️ Time Complexity
```
O(1)
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- `n = 0` — not a power of two.
- `n = 1` — 2^0 = 1, is a power of two.
- Negative numbers — never powers of two.
- `n = INT_MIN` — has one set bit but is negative, handled by `n > 0`.

---

## 🎯 Interview Takeaways
- `n & (n - 1)` is the classic trick to clear the lowest set bit.
- Always check for positive numbers when dealing with powers.
- This one-liner demonstrates elegant bit manipulation.

---

## 📌 Key Pattern
👉 **"n & (n - 1) == 0 checks if n has exactly one set bit (power of two)"**

---

## 🔁 Related Problems
- 326. Power of Three
- 342. Power of Four
- 191. Number of 1 Bits

---

## 🚀 Final Thoughts
This is the textbook bit manipulation problem. The `n & (n - 1)` trick is fundamental and appears in many other problems involving bit counting and manipulation.

---

✨ **Rule to remember:**
> "Powers of two have exactly one set bit — use n & (n-1) to check."
