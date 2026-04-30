# 1611. Minimum One Bit Operations to Make Integers Zero

## 🔗 Problem Link
https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Dynamic Programming, Bit Manipulation, Memoization, Recursion

---

## 🧩 Problem Summary
Given an integer `n`, you must transform it to `0` using two operations: (1) flip the rightmost bit, or (2) flip the i-th bit if the (i-1)-th bit is 1 and all bits below (i-1) are 0. Return the minimum number of operations.

### 📌 Constraints
- `0 <= n <= 10^9`

---

## 💭 Intuition
👉 Observe that converting `2^k` to `0` takes exactly `2^(k+1) - 1` operations (Gray code property). The problem reduces recursively: to zero out the highest set bit, first arrange the lower bits into the right pattern, then flip, then zero out the remainder.

---

## ⚡ Approach — Recursive Gray Code Reduction

### 🧠 Idea
- Find the largest power of two `x = 2^k` that fits in `n`.
- To eliminate this bit: transform `n` into `x | (x >> 1)` = `11000...0` pattern, which costs `minimumOneBitOperations(n ^ (x | x >> 1))` operations.
- Then one operation converts `11...` to `01...`, and `x - 1` more operations zero out `x >> 1`.
- Total: `f(n ^ (x | x>>1)) + 1 + (x - 1)`.

---

## 💻 Code

```cpp
class Solution {
 public:
  int minimumOneBitOperations(int n) {
    // Observation: e.g. n = 2^2
    //        100 (2^2 needs 2^3 - 1 ops)
    // op1 -> 101
    // op2 -> 111
    // op1 -> 110
    // op2 -> 010 (2^1 needs 2^2 - 1 ops)
    // op1 -> 011
    // op2 -> 001 (2^0 needs 2^1 - 1 ops)
    // op1 -> 000
    //
    // So 2^k needs 2^(k + 1) - 1 ops. Note this is reversible, i.e., 0 -> 2^k
    // also takes 2^(k + 1) - 1 ops.

    // e.g. n = 1XXX, our first goal is to change 1XXX -> 1100.
    //   - If the second bit is 1, you only need to consider the cost of turning
    //     the last 2 bits to 0.
    //   - If the second bit is 0, you need to add up the cost of flipping the
    //     second bit from 0 to 1.
    // XOR determines the cost minimumOneBitOperations(1XXX^1100) accordingly.
    // Then, 1100 -> 0100 needs 1 op. Finally, 0100 -> 0 needs 2^3 - 1 ops.
    if (n == 0)
      return 0;
    // x is the largest 2^k <= n.
    // x | x >> 1 -> x >> 1 needs 1 op.
    //     x >> 1 -> 0      needs x = 2^k - 1 ops.
    int x = 1;
    while (x * 2 <= n)
      x <<= 1;
    return minimumOneBitOperations(n ^ (x | x >> 1)) + 1 + x - 1;
  }
};
```

---

## 🧠 Dry Run
### Input
```
n = 6 (binary: 110)
```
### Steps
```
x = 4 (2^2)
x | x>>1 = 4|2 = 6
n ^ 6 = 6 ^ 6 = 0
f(0) + 1 + 4 - 1 = 0 + 1 + 3 = 4

Verify: 110 → 111 → 101 → 100 → 000 (needs intermediate)
Actually: 110 → 010 → 011 → 001 → 000 = 4 ops ✓
```

---

## ⏱️ Time Complexity
```
O(log n) — each recursive call reduces the highest bit
```

## 💾 Space Complexity
```
O(log n) — recursion depth proportional to number of bits
```

---

## ⚠️ Edge Cases
- `n = 0` → already zero, return 0.
- `n` is a power of two → return `2 * n - 1`.
- Large `n` near 10^9 → fits in 30 bits, recursion depth is manageable.

---

## 🎯 Interview Takeaways
- This problem is deeply connected to Gray codes.
- Recognising the pattern `2^k → 0 costs 2^(k+1) - 1` is the breakthrough insight.
- Recursive decomposition by the highest set bit is a powerful bit-manipulation technique.

---

## 📌 Key Pattern
👉 **"Recursive bit decomposition using Gray code properties"**

---

## 🔁 Related Problems
- 89. Gray Code
- 1009. Complement of Base 10 Integer
- 338. Counting Bits

---

## 🚀 Final Thoughts
This is a hard problem that becomes elegant once you recognise the Gray code connection. The recursive formula neatly breaks the problem into: handle the lower bits, then use the known cost for a single power of two.

---

✨ **Rule to remember:**
> Converting `2^k` to 0 costs `2^(k+1) - 1` operations — the rest is recursive decomposition via XOR.
