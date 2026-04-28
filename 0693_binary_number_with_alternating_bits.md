# 693. Binary Number with Alternating Bits

## 🔗 Problem Link
https://leetcode.com/problems/binary-number-with-alternating-bits/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Bit Manipulation

---

## 🧩 Problem Summary

Given a positive integer `n`, check whether it has alternating bits: namely, if two adjacent bits will always have different values in its binary representation.

### 📌 Constraints
- `1 <= n <= 2^31 - 1`

---

## 💭 Intuition

If we look at the binary representation bit by bit from right to left, each bit should differ from the previous one. 👉 Compare the current least significant bit with the previous bit; if they ever match, return False.

---

## ⚡ Approach — Bit-by-Bit Check

### 🧠 Idea

- Extract the last bit as `prev`.
- Right-shift `n` by 1.
- While `n` is non-zero, compare the current last bit with `prev`. If equal, return False.
- Update `prev` and right-shift again.
- If we exhaust all bits without a match, return True.

---

## 💻 Code

```python
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = n % 2
        n >>=1
        while n:
            if (n%2) == prev :
                return False
            prev = n%2
            n>>=1
        return True
```

---

## 🧠 Dry Run

### Input
```
n = 5  (binary: 101)
```

### Steps
```
prev = 1, n = 2 (binary: 10)
n%2 = 0 != prev(1) → OK, prev = 0, n = 1 (binary: 1)
n%2 = 1 != prev(0) → OK, prev = 1, n = 0
Loop ends → return True
```

---

## ⏱️ Time Complexity

```
O(log n)
```

We process each bit of n exactly once.

---

## 💾 Space Complexity

```
O(1)
```

Only a couple of variables are used.

---

## ⚠️ Edge Cases

- **n = 1** (binary `1`) → `True` (single bit is trivially alternating)
- **n = 7** (binary `111`) → `False` (all same bits)
- **n = 10** (binary `1010`) → `True`

---

## 🎯 Interview Takeaways

- Bit manipulation with right-shift and modulo is a standard technique for inspecting bits.
- An alternative trick: `n ^ (n >> 1)` should give all 1s if bits alternate, then check if that value is of the form `2^k - 1`.
- Always consider edge cases like single-bit numbers.

---

## 📌 Key Pattern

👉 **"Compare adjacent bits by tracking the previous bit while right-shifting"**

---

## 🔁 Related Problems

- 191. Number of 1 Bits
- 461. Hamming Distance
- 868. Binary Gap

---

## 🚀 Final Thoughts

A clean bit manipulation problem. Iterating through bits one at a time and comparing neighbors is the simplest and most intuitive approach.

---

✨ **Rule to remember:**
> For alternating bits, every adjacent pair must differ — just compare each bit to its predecessor.
