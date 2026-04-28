# 2749. Minimum Operations to Make the Integer Zero

## 🔗 Problem Link
https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Math, Bit Manipulation, Brainteaser

---

## 🧩 Problem Summary
Given two integers `num1` and `num2`, in one operation you choose an integer `i` in `[0, 60]` and subtract `2^i + num2` from `num1`. Return the minimum number of operations to make `num1` equal to 0, or -1 if impossible.

### 📌 Constraints
- `1 <= num1 <= 10^9`
- `-10^9 <= num2 <= 10^9`

---

## 💭 Intuition
👉 After `k` operations, we have `num1 - k * num2 = 2^{i_1} + 2^{i_2} + ... + 2^{i_k}`. The right side is a sum of `k` powers of 2. The minimum number of powers of 2 to represent a number `x` is `popcount(x)`, and the maximum is `x` itself (all 2^0). So we need `popcount(target) <= k <= target`.

---

## ⚡ Approach — Iterate Operations Count

### 🧠 Idea
- For each `k` from 0 to 60, compute `target = num1 - k * num2`.
- Check if `target` can be expressed as a sum of exactly `k` powers of 2: this requires `popcount(target) <= k <= target`.
- Return the first valid `k`.

---

## 💻 Code

```cpp
class Solution {
 public:
  int makeTheIntegerZero(int num1, int num2) {
    // If k operations are used, num1 - [(num2 + 2^{i_1}) + (num2 + 2^{i_2}) +
    // ... + (num2 + 2^{i_k})] = 0. So, num1 - k * num2 = (2^{i_1} + 2^{i_2} +
    // ... + 2^{i_k}), where i_1, i_2, ..., i_k are in the range [0, 60].
    // Note that for any number x, we can use "x's bit count" operations to make
    // x equal to 0. Additionally, we can also use x operations to deduct x by
    // 2^0 (x times), which also results in 0.

    for (long ops = 0; ops <= 60; ++ops) {
      const long target = num1 - ops * num2;
      if (__builtin_popcountl(target) <= ops && ops <= target)
        return ops;
    }

    return -1;
  }
};
```

---

## 🧠 Dry Run
### Input
```
num1 = 3, num2 = -2
```
### Steps
```
ops=0: target=3, popcount(3)=2, 2<=0? No
ops=1: target=3-(-2)=5, popcount(5)=2, 2<=1? No
ops=2: target=3-2*(-2)=7, popcount(7)=3, 3<=2? No
ops=3: target=3-3*(-2)=9, popcount(9)=2, 2<=3 and 3<=9? Yes!
Return 3
```

---

## ⏱️ Time Complexity
```
O(1) — at most 61 iterations, each with O(1) popcount
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- `num2 = 0`: target is always `num1`, need `popcount(num1)` operations
- `num2 > 0`: target decreases, might become negative (impossible)
- `num2 < 0`: target increases, eventually `ops <= target` will hold

---

## 🎯 Interview Takeaways
- Decomposing a number into a sum of powers of 2 requires at least `popcount` terms and at most `value` terms.
- Iterating over a small fixed range (0 to 60) is effectively O(1).

---

## 📌 Key Pattern
👉 **"Representing a number as a sum of k powers of 2 — bounded by popcount and value"**

---

## 🔁 Related Problems
- 397. Integer Replacement
- 1611. Minimum One Bit Operations to Make Integers Zero

---

## 🚀 Final Thoughts
The mathematical insight is elegant: after `k` operations, the remaining value must be expressible as exactly `k` powers of 2. The popcount gives the minimum decomposition, and the value itself gives the maximum (all 1s). This constraint makes the problem solvable in constant time.

---

✨ **Rule to remember:**
> A positive integer x can be written as a sum of exactly k powers of 2 if and only if popcount(x) <= k <= x.
