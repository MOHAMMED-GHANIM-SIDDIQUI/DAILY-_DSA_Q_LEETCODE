# 190. Reverse Bits

## 🔗 Problem Link
https://leetcode.com/problems/reverse-bits/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Divide and Conquer, Bit Manipulation

---

## 🧩 Problem Summary

Reverse the bits of a given 32-bit unsigned integer. For example, the input `00000010100101000001111010011100` becomes `00111001011110000010100101000000`, which is `964176192`.

### 📌 Constraints
- The input must be a binary string of length 32

---

## 💭 Intuition

👉 Process each bit from right to left. For each of the 32 bits, shift the answer left by 1 to make room, then OR it with the least significant bit of `n`. Then shift `n` right by 1 to move to the next bit. After 32 iterations, the bits are reversed.

---

## ⚡ Approach — Bit-by-Bit Reversal

### 🧠 Idea

- Initialize `ans = 0`.
- Loop 32 times:
  - Left-shift `ans` by 1 (make room for the next bit).
  - OR `ans` with the last bit of `n` (`n & 1`).
  - Right-shift `n` by 1 (move to the next bit).
- After 32 iterations, `ans` contains the reversed bits.

---

## 💻 Code

```python
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            ans = (ans<<1) | (n&1)
            n = n>>1
        return ans
```

---

## 🧠 Dry Run

### Input
```
n = 0b00000000000000000000000000001011 (decimal 11)
```

### Steps
```
Iteration 1:  ans=0<<1|1=1,       n=5      (bit: 1)
Iteration 2:  ans=1<<1|1=3,       n=2      (bit: 1)
Iteration 3:  ans=3<<1|0=6,       n=1      (bit: 0)
Iteration 4:  ans=6<<1|1=13,      n=0      (bit: 1)
Iterations 5-32: ans keeps shifting left, n&1=0
Final ans = 13 << 28 = 3489660928

Result: 0b11010000000000000000000000000000 = 3489660928
```

---

## ⏱️ Time Complexity

```
O(1)
```

Always exactly 32 iterations regardless of input.

---

## 💾 Space Complexity

```
O(1)
```

Only a constant number of variables.

---

## ⚠️ Edge Cases

- **All zeros:** `n = 0` → `0`
- **All ones:** `n = 0xFFFFFFFF` → `0xFFFFFFFF` (palindrome in binary)
- **Single bit set:** `n = 1` → `2^31 = 2147483648`

---

## 🎯 Interview Takeaways

- Bit manipulation basics: `&1` extracts the last bit, `<<1` shifts left, `>>1` shifts right.
- This pattern of "build result bit-by-bit" appears in many bit manipulation problems.
- The fixed 32-iteration loop makes both time and space O(1).
- Follow-up: if called many times, precompute reversed bytes in a lookup table for O(1) per call.

---

## 📌 Key Pattern

👉 **"Build the reversed number bit-by-bit: shift answer left, OR in the last bit, shift input right."**

---

## 🔁 Related Problems

- 191. Number of 1 Bits
- 7. Reverse Integer
- 371. Sum of Two Integers
- 338. Counting Bits

---

## 🚀 Final Thoughts

Reverse Bits is a fundamental bit manipulation problem. The bit-by-bit construction pattern is simple, elegant, and runs in constant time. It is a building block for understanding more complex bitwise operations.

---

✨ **Rule to remember:**
> "To reverse bits: shift answer left and input right, transferring one bit at a time for exactly 32 steps."
