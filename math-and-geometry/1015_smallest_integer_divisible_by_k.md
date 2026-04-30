# 1015. Smallest Integer Divisible By K

## 🔗 Problem Link
https://leetcode.com/problems/smallest-repunit-divisible-by-k/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Math, Hash Table

---

## 🧩 Problem Summary

Given a positive integer `k`, return the length of the smallest positive integer `n` such that `n` is divisible by `k` and `n` only contains the digit `1` (a repunit). If no such `n` exists, return -1.

### 📌 Constraints
- `1 <= k <= 10^5`

---

## 💭 Intuition

👉 A repunit of length L can be built iteratively: `n = n * 10 + 1`. We only need to track `n % k` since we only care about divisibility.

👉 If `k` is even or divisible by 5, no repunit can be divisible by `k` (repunits always end in 1).

👉 By pigeonhole principle, if we see a repeated remainder, we'll loop forever and should return -1.

---

## ⚡ Approach — Remainder Tracking with Early Termination

### 🧠 Idea
- Immediately return -1 if `k` ends in 0, 2, 4, 5, 6, or 8.
- Build repunits modularly: `n = (n * 10 + 1) % k`.
- If remainder becomes 0, return the current length.
- If a remainder repeats, return -1 (cycle detected).

---

## 💻 Code

```cpp
class Solution {
 public:
  int smallestRepunitDivByK(int k) {
    if (k % 10 != 1 && k % 10 != 3 && k % 10 != 7 && k % 10 != 9)
      return -1;

    unordered_set<int> seen;
    int n = 0;

    for (int length = 1; length <= k; ++length) {
      n = (n * 10 + 1) % k;
      if (n == 0)
        return length;
      if (seen.contains(n))
        return -1;
      seen.insert(n);
    }

    return -1;
  }
};
```

---

## 🧠 Dry Run

### Input
```
k = 3
```

### Steps
```
length=1: n = (0*10 + 1) % 3 = 1, seen={1}
length=2: n = (1*10 + 1) % 3 = 11 % 3 = 2, seen={1,2}
length=3: n = (2*10 + 1) % 3 = 21 % 3 = 0 → return 3

Answer: 3 (111 / 3 = 37)
```

---

## ⏱️ Time Complexity
```
O(k)
```
At most `k` unique remainders exist, so we iterate at most `k` times.

---

## 💾 Space Complexity
```
O(k)
```
The hash set stores at most `k` remainders.

---

## ⚠️ Edge Cases
- `k = 1` → answer is 1 (the number 1 itself).
- `k` is even → return -1 immediately.
- `k = 5` or multiples of 5 → return -1.

---

## 🎯 Interview Takeaways
- Modular arithmetic avoids dealing with massive numbers.
- The pigeonhole principle guarantees termination — remainders mod k can only take k distinct values.
- Filtering by last digit is a quick optimization.
- Building numbers iteratively via `n = n * 10 + 1` is a common trick.

---

## 📌 Key Pattern
👉 **"Use modular arithmetic to simulate large number divisibility without storing the actual number."**

---

## 🔁 Related Problems
- 202 - Happy Number (cycle detection with remainders)
- 166 - Fraction to Recurring Decimal
- 1071 - Greatest Common Divisor of Strings

---

## 🚀 Final Thoughts
An elegant math problem where modular arithmetic and cycle detection combine. The early filter on last digits and the pigeonhole-based termination make this efficient.

---

✨ **Rule to remember:**
> "When checking divisibility of huge constructed numbers, track only the remainder — the full number is never needed."
