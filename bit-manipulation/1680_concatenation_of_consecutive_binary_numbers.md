# 1680. Concatenation of Consecutive Binary Numbers

## 🔗 Problem Link
https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Math, Bit Manipulation, Simulation

---

## 🧩 Problem Summary
Given an integer `n`, return the decimal value of the binary string formed by concatenating the binary representations of `1, 2, ..., n` in order, modulo `10^9 + 7`.

### 📌 Constraints
- `1 <= n <= 10^5`

---

## 💭 Intuition
👉 To append a number `i` to the running result, shift the result left by the number of bits in `i`, then OR (or add) `i`. This simulates binary concatenation without actually building the string.

---

## ⚡ Approach — Bit Shift Simulation

### 🧠 Idea
- Iterate from 1 to n.
- For each number `i`, compute its bit length.
- Shift `ans` left by that many bits and OR with `i`.
- Take modulo at each step.

---

## 💻 Code

```python
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = 0
        MOD = 10**9 + 7

        for i in range(1, n + 1):
            # number of bits in i
            bits = i.bit_length()

            # shift ans left and add i
            ans = ((ans << bits) | i) % MOD

        return ans
```

---

## 🧠 Dry Run
### Input
```
n = 3
```
### Steps
```
i=1: bits=1, ans = (0 << 1) | 1 = 1          → binary: "1"
i=2: bits=2, ans = (1 << 2) | 2 = 4+2 = 6    → binary: "110"
i=3: bits=2, ans = (6 << 2) | 3 = 24+3 = 27  → binary: "11011"

Result: 27
Verify: "1" + "10" + "11" = "11011" = 27 ✓
```

---

## ⏱️ Time Complexity
```
O(n) — single pass from 1 to n
```

## 💾 Space Complexity
```
O(1) — only a few variables
```

---

## ⚠️ Edge Cases
- `n = 1` → result is 1.
- Large `n = 10^5` → modular arithmetic keeps values manageable.

---

## 🎯 Interview Takeaways
- `bit_length()` in Python gives the number of bits needed to represent a number.
- Left-shifting and OR-ing is the standard way to "append" binary representations.
- Always apply modulo after each operation to prevent overflow (relevant in languages with fixed-size integers).

---

## 📌 Key Pattern
👉 **"Simulate binary concatenation using left-shift by bit_length and OR"**

---

## 🔁 Related Problems
- 1318. Minimum Flips to Make a OR b Equal to c
- 67. Add Binary
- 477. Total Hamming Distance

---

## 🚀 Final Thoughts
A satisfying medium problem where understanding binary operations leads to an O(n) solution. The key is recognising that "concatenation in binary" is just shifting and adding.

---

✨ **Rule to remember:**
> To concatenate number `i` in binary, left-shift the accumulator by `i.bit_length()` and OR with `i`.
