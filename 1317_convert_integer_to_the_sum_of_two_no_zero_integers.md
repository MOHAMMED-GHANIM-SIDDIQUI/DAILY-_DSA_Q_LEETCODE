# 1317. Convert Integer to the Sum of Two No-Zero Integers

## 🔗 Problem Link
https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Math

---

## 🧩 Problem Summary
Given an integer `n`, return two integers `a` and `b` such that `a + b = n` and neither `a` nor `b` contains the digit `0` in their decimal representation. These are called "No-Zero integers."

### 📌 Constraints
- `2 <= n <= 10^4`

---

## 💭 Intuition
👉 Start by splitting `n` into two halves and adjust one down / the other up until both numbers contain no zero digit. Since `n` is at most 10^4, this brute-force adjustment converges quickly.

---

## ⚡ Approach — Two-Pointer Adjustment

### 🧠 Idea
- Start with `fno = n / 2` and `sno = n - fno`.
- Check each digit of both numbers for zeros using a helper `isValid`.
- If either contains a `0`, decrement `fno` and increment `sno`; repeat.
- Return the valid pair.

---

## 💻 Code

```cpp
class Solution {
public:
    vector<int> getNoZeroIntegers(int n) {
        int fno = n / 2;
        int sno = n - fno;

        // Adjust until both are valid
        while (!isValid(fno) || !isValid(sno)) {
            fno--;
            sno++;
        }

        return {fno, sno};
    }

private:
    bool isValid(int num) {
        while (num > 0) {
            if (num % 10 == 0) return false;
            num /= 10;
        }
        return true;
    }
};
```

---

## 🧠 Dry Run
### Input
```
n = 11
```
### Steps
```
fno = 5, sno = 6
isValid(5) = true, isValid(6) = true
Both valid → return [5, 6]
```

---

## ⏱️ Time Complexity
```
O(n * d) where d is the number of digits — effectively O(n) since d ≤ 5
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- `n = 2` → return `[1, 1]`
- Numbers like `n = 10` where naive split `(5,5)` works immediately
- Numbers where the first split has a zero digit, e.g., `n = 101` → adjust until no zeros

---

## 🎯 Interview Takeaways
- A simple digit-check helper keeps the solution clean.
- Brute-force adjustment from the midpoint is efficient for small constraints.
- Always verify each digit — zero can appear anywhere in a number.

---

## 📌 Key Pattern
👉 **"Validate digit-by-digit and adjust candidates until constraints are satisfied."**

---

## 🔁 Related Problems
- 1304. Find N Unique Integers Sum up to Zero
- 258. Add Digits

---

## 🚀 Final Thoughts
A simple problem best solved with brute-force adjustment. The key is writing a clean `isValid` helper to check for the absence of digit zero.

---

✨ **Rule to remember:**
> Split `n` from the middle and shift until both parts are zero-digit-free.
