# 1780. Check if Number is a Sum of Powers of Three

## 🔗 Problem Link
https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Math

---

## 🧩 Problem Summary
Given an integer `n`, return `true` if it is possible to represent `n` as the sum of distinct powers of three, otherwise return `false`. Each power of three can be used at most once.

### 📌 Constraints
- `1 <= n <= 10^7`

---

## 💭 Intuition
👉 This is equivalent to checking if `n` in base 3 contains only digits 0 and 1. If any digit is 2, it means a power of three would need to be used twice, which is not allowed.

---

## ⚡ Approach — Base-3 Digit Check

### 🧠 Idea
- Repeatedly divide `n` by 3.
- If at any point the remainder is 2, return `false`.
- If all remainders are 0 or 1, return `true`.

---

## 💻 Code

```cpp
class Solution {
public:
    bool checkPowersOfThree(int n) {
        while (n > 0) {
            if (n % 3 == 2) {
                return false;  // If the remainder is 2, it's not a valid sum of powers of 3
            }
            n /= 3;  // Divide n by 3 to move to the next power of 3
        }
        return true;
    }
};
```

---

## 🧠 Dry Run
### Input
```
n = 12
```
### Steps
```
n=12: 12%3=0 → ok, n=4
n=4:  4%3=1  → ok, n=1
n=1:  1%3=1  → ok, n=0

Return true
12 = 3^0 + 3^2 = 1 + 9 ... wait, 1+9=10 ≠ 12
12 = 3 + 9 = 3^1 + 3^2 = 12 ✓
Base 3 of 12: 110 (digits are 1,1,0) → all ≤ 1 ✓
```

---

## ⏱️ Time Complexity
```
O(log₃ n) — each iteration divides n by 3
```

## 💾 Space Complexity
```
O(1) — constant extra space
```

---

## ⚠️ Edge Cases
- `n = 1` → `3^0 = 1`, return true.
- `n = 2` → remainder is 2, return false.
- `n = 3` → `3^1`, return true.
- Large `n` near `10^7` → at most ~15 iterations.

---

## 🎯 Interview Takeaways
- "Sum of distinct powers of base k" is equivalent to "base-k representation has only 0s and 1s."
- This generalises: for base 2 it's always true (every number is a sum of distinct powers of 2).
- Simple modular arithmetic provides an elegant solution.

---

## 📌 Key Pattern
👉 **"Check if the base-k representation contains only digits 0 and 1 — ensures each power is used at most once"**

---

## 🔁 Related Problems
- 231. Power of Two
- 326. Power of Three
- 342. Power of Four

---

## 🚀 Final Thoughts
A beautiful math problem with a concise solution. The connection between "distinct powers" and "base representation with digits ≤ 1" is the key insight that makes this problem trivial once understood.

---

✨ **Rule to remember:**
> A number is a sum of distinct powers of 3 if and only if its base-3 representation contains no digit equal to 2.
