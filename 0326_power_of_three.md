# 326. Power of Three

## 🔗 Problem Link
https://leetcode.com/problems/power-of-three/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Math, Recursion

---

## 🧩 Problem Summary
Given an integer n, return true if it is a power of three. An integer n is a power of three if there exists an integer x such that n == 3^x.

### 📌 Constraints
- `-2^31 <= n <= 2^31 - 1`

---

## 💭 Intuition
👉 The largest power of 3 that fits in a 32-bit integer is 3^19 = 1162261467. If n is a power of 3, then 3^19 must be divisible by n.

---

## ⚡ Approach — Maximum Power Divisibility

### 🧠 Idea
- Compute 3^19 (the largest power of 3 within int range).
- If n is positive and 3^19 % n == 0, then n is a power of three.
- This works because 3 is prime, so the only divisors of 3^19 are powers of 3.

---

## 💻 Code

```cpp
class Solution {
 public:
  bool isPowerOfThree(int n) {
    return n > 0 && static_cast<int>(pow(3, 19)) % n == 0;
  }
};
```

---

## 🧠 Dry Run
### Input
```
n = 27
```
### Steps
```
3^19 = 1162261467
n = 27 = 3^3
1162261467 % 27 = 0
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
- `n = 0` — not a power of three.
- `n = 1` — 3^0 = 1, is a power of three.
- Negative numbers — never powers of three.
- `n = 6` — not a power of 3 (1162261467 % 6 != 0).

---

## 🎯 Interview Takeaways
- The "largest power" divisibility trick only works for prime bases.
- No loops or recursion needed — pure math solution.
- Understanding why primality matters is key to explaining this approach.

---

## 📌 Key Pattern
👉 **"For prime base b, n is a power of b iff b^max % n == 0"**

---

## 🔁 Related Problems
- 231. Power of Two
- 342. Power of Four

---

## 🚀 Final Thoughts
This elegant O(1) solution leverages the mathematical property of prime numbers. Since 3 is prime, the only factors of 3^19 are 3^0, 3^1, ..., 3^19.

---

✨ **Rule to remember:**
> "For a prime base, the largest power within range is divisible only by smaller powers of the same base."
