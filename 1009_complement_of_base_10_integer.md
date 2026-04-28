# 1009. Complement of Base 10 Integer

## 🔗 Problem Link
https://leetcode.com/problems/complement-of-base-10-integer/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Bit Manipulation

---

## 🧩 Problem Summary

Given a positive integer `n`, return its complement — the integer you get by flipping every bit (0 becomes 1 and 1 becomes 0) in its binary representation.

### 📌 Constraints
- `0 <= n < 10^9`

---

## 💭 Intuition

👉 We need to flip each bit of `n`. Instead of XOR-ing with a full mask, we can build the result bit by bit: wherever `n` has a 0, the complement has a 1 at that position.

---

## ⚡ Approach — Bit-by-Bit Construction

### 🧠 Idea
- Special case: if `n == 0`, return 1.
- Process `n` one bit at a time (LSB first).
- If the current bit is 0, set the corresponding bit in the answer.
- Shift `n` right and increment the power/position counter.

---

## 💻 Code

```python
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        ans = 0
        power = 0
        while n:
            if (n & 1) == 0:
                ans += (1 << power)
            power += 1
            n >>= 1

        return ans
```

---

## 🧠 Dry Run

### Input
```
n = 5  (binary: 101)
```

### Steps
```
Iteration 1: n=5 (101), bit=1 → skip, power=1, n=2
Iteration 2: n=2 (10),  bit=0 → ans += 1<<1 = 2, power=2, n=1
Iteration 3: n=1 (1),   bit=1 → skip, power=3, n=0
ans = 2 (binary: 010)
Output: 2
```

---

## ⏱️ Time Complexity
```
O(log n)
```
We process each bit of `n` exactly once.

---

## 💾 Space Complexity
```
O(1)
```
Only a few integer variables are used.

---

## ⚠️ Edge Cases
- `n = 0` → complement is 1 (special case).
- `n = 1` → complement is 0.
- Powers of 2 minus 1 (e.g., `n = 7 = 111`) → complement is 0.

---

## 🎯 Interview Takeaways
- Handle `n = 0` as a special case since the loop wouldn't execute.
- Building the answer bit by bit avoids needing to compute a full bitmask.
- An alternative approach: XOR `n` with `(2^bitLength - 1)` to flip all bits.
- Bit manipulation fundamentals are essential for this type of problem.

---

## 📌 Key Pattern
👉 **"Flip bits by checking each bit position and constructing the complement from scratch."**

---

## 🔁 Related Problems
- 476 - Number Complement
- 1017 - Convert to Base -2
- 693 - Binary Number with Alternating Bits

---

## 🚀 Final Thoughts
A straightforward bit manipulation exercise. The key is processing each bit individually and building the result with shifted 1s wherever the original has 0s.

---

✨ **Rule to remember:**
> "To complement a number, flip only within its bit-length — not the full 32 bits."
