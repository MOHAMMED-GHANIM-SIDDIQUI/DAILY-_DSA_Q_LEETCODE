# 342. Power of Four

## 🔗 Problem Link
https://leetcode.com/problems/power-of-four/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Math, Bit Manipulation, Recursion

---

## 🧩 Problem Summary
Given an integer n, return true if it is a power of four. An integer n is a power of four if there exists an integer x such that n == 4^x.

### 📌 Constraints
- `-2^31 <= n <= 2^31 - 1`

---

## 💭 Intuition
👉 A power of four must first be a power of two (single set bit), and additionally that set bit must be at an even position (bit 0, 2, 4, ...). The mask 0x55555555 has bits set at all even positions.

---

## ⚡ Approach — Bit Manipulation with Mask

### 🧠 Idea
- Check if n is positive.
- Check if n is a power of two using `n & (n - 1) == 0`.
- Check if the set bit is at an even position using `n & 0x55555555 != 0`.
- All three conditions together confirm n is a power of four.

---

## 💻 Code

```cpp
class Solution {
public:
    bool isPowerOfFour(int n) {
        if (n <= 0) return false;

        // Check power of two
        if ((n & (n - 1)) != 0) return false;

        // Ensure the only set bit is at an even position
        return (n & 0x55555555) != 0;
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
n = 16 = 10000 (binary)
n > 0: true
n & (n-1) = 10000 & 01111 = 0: power of two
0x55555555 = 01010101010101010101010101010101
n & 0x55555555 = 00000000000000000000000000010000 = 16 != 0: true
Result: true (16 = 4^2)
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
- `n = 1` — 4^0 = 1, is a power of four.
- `n = 2` — power of two but not power of four (bit at position 1, odd).
- `n = 0` and negative numbers — not powers of four.
- `n = 8` — power of two, bit at position 3 (odd), not power of four.

---

## 🎯 Interview Takeaways
- Building on the power-of-two check with an additional bit-position check is elegant.
- 0x55555555 is a useful bitmask for selecting even-positioned bits.
- Understanding binary representations of powers is crucial for bit manipulation problems.

---

## 📌 Key Pattern
👉 **"Power of four = power of two + set bit at even position (mask 0x55555555)"**

---

## 🔁 Related Problems
- 231. Power of Two
- 326. Power of Three

---

## 🚀 Final Thoughts
This problem nicely extends the power-of-two concept. The insight that powers of four have their single set bit at even positions (0, 2, 4, ...) makes the bitmask solution both efficient and elegant.

---

✨ **Rule to remember:**
> "Power of four = single set bit at an even position — check with 0x55555555."
