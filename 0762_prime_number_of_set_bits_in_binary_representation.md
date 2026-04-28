# 762. Prime Number of Set Bits in Binary Representation

## 🔗 Problem Link
https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Bit Manipulation, Math

---

## 🧩 Problem Summary

Given two integers `left` and `right`, return the count of numbers in the inclusive range `[left, right]` that have a prime number of set bits in their binary representation.

### 📌 Constraints
- `1 <= left <= right <= 10^6`
- `0 <= right - left <= 10^4`

---

## 💭 Intuition

Since `right <= 10^6 < 2^20`, the maximum number of set bits is 19. 👉 We only need to precompute which small numbers (up to 19) are prime, then count set bits for each number in the range and check membership.

---

## ⚡ Approach — Precomputed Prime Set + Bit Count

### 🧠 Idea

- Store all primes up to 19 in a set: {2, 3, 5, 7, 11, 13, 17, 19}.
- For each number in [left, right], count its set bits using `bit_count()`.
- If the count is in the prime set, increment the result.

---

## 💻 Code

```python
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        res = 0
        for i in range(left, right + 1):
            if (i.bit_count() in primes):
                res += 1
        return res
```

---

## 🧠 Dry Run

### Input
```
left = 6, right = 10
```

### Steps
```
6  = 110   → 2 set bits → 2 is prime ✓
7  = 111   → 3 set bits → 3 is prime ✓
8  = 1000  → 1 set bit  → 1 is NOT prime ✗
9  = 1001  → 2 set bits → 2 is prime ✓
10 = 1010  → 2 set bits → 2 is prime ✓
Result: 4
```

---

## ⏱️ Time Complexity

```
O(n)
```

Where n = right - left + 1. Each bit_count() call is O(1) for fixed-width integers.

---

## 💾 Space Complexity

```
O(1)
```

The prime set has a fixed constant size (8 elements).

---

## ⚠️ Edge Cases

- **Single element range:** `left = right = 1` → 1 set bit, not prime → 0
- **Power of 2:** has exactly 1 set bit, which is not prime → not counted
- **All bits set:** `left = right = 7` (111) → 3 set bits, prime → 1

---

## 🎯 Interview Takeaways

- Precomputing small primes in a set avoids repeated primality checks.
- Python's `int.bit_count()` (Python 3.10+) or `bin(n).count('1')` counts set bits efficiently.
- Knowing the constraint bounds (max 20 bits) simplifies the problem significantly.

---

## 📌 Key Pattern

👉 **"Precompute small primes in a set, then count set bits for each number"**

---

## 🔁 Related Problems

- 191. Number of 1 Bits
- 338. Counting Bits
- 868. Binary Gap

---

## 🚀 Final Thoughts

A simple problem that combines bit manipulation with basic number theory. The key optimization is recognizing that with bounded input, only a small fixed set of primes matters.

---

✨ **Rule to remember:**
> For numbers up to 10^6, set bits never exceed 19 — just hardcode the primes and count.
