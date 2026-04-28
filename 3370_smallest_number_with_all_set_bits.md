# 3370. Smallest Number With All Set Bits

## 🔗 Problem Link
https://leetcode.com/problems/smallest-number-with-all-set-bits/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Bit Manipulation, Math

---

## 🧩 Problem Summary
Given a positive integer `n`, find the smallest number greater than or equal to `n` whose binary representation consists entirely of set bits (i.e., all 1s). For example, 7 = `111`, 15 = `1111`, 31 = `11111`.

### 📌 Constraints
- `1 <= n <= 1000`

---

## 💭 Intuition
👉 A number with all set bits has the form `2^k - 1` (e.g., 1, 3, 7, 15, 31, ...). Alternatively, check if `n & (n+1) == 0` which is true only when all bits are set. Find the smallest such number >= n.

---

## ⚡ Approach — Linear Search for All-Set-Bits Number

### 🧠 Idea
- Starting from `n`, check each number to see if all its bits are set.
- A number has all bits set if `(n & (n + 1)) == 0`.
- Return the first such number found.

---

## 💻 Code

```cpp
class Solution {
    bool is_all_set(int n)
    {
        return (n&n+1)==0;
    }
    // 01111-->15
    // 10000-->16
public:
    int smallestNumber(int n) {
        for(int i=n;i<INT_MAX;i++)
        {
            if(is_all_set(i))
            return i;
        }
        return -1;
    }
};
```

---

## 🧠 Dry Run
### Input
```
n = 10
```
### Steps
```
i=10: 1010 & 1011 = 1010 != 0 → skip
i=11: 1011 & 1100 = 1000 != 0 → skip
i=12: 1100 & 1101 = 1100 != 0 → skip
i=13: 1101 & 1110 = 1100 != 0 → skip
i=14: 1110 & 1111 = 1110 != 0 → skip
i=15: 1111 & 10000 = 0 → return 15
```

---

## ⏱️ Time Complexity
```
O(n) — in the worst case, scan up to the next power of 2
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- `n = 1` → already all set bits, return 1
- `n = 3` → already all set bits, return 3
- `n` is already a Mersenne number (2^k - 1) → return n itself

---

## 🎯 Interview Takeaways
- The `n & (n + 1) == 0` trick detects numbers with all bits set.
- An alternative O(1) approach: find the bit length and return `(1 << bitLength) - 1`.

---

## 📌 Key Pattern
👉 **"n & (n + 1) == 0 identifies numbers with all bits set (Mersenne-like)"**

---

## 🔁 Related Problems
- 231. Power of Two
- 342. Power of Four
- 476. Number Complement

---

## 🚀 Final Thoughts
While a linear scan works for the small constraint (n <= 1000), the optimal approach computes the answer directly: find the highest bit position and return `2^(bits) - 1`. The bit trick `n & (n+1) == 0` is a useful tool to remember.

---

✨ **Rule to remember:**
> "All-set-bits numbers satisfy n & (n + 1) == 0, and the smallest one >= n is (1 << ceil(log2(n+1))) - 1."
