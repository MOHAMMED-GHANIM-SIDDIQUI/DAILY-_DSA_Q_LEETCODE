# 1922. Count Good Numbers

## 🔗 Problem Link
https://leetcode.com/problems/count-good-numbers/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Math, Recursion, Modular Exponentiation

---

## 🧩 Problem Summary
A digit string is "good" if digits at even indices are even (0,2,4,6,8 = 5 choices) and digits at odd indices are prime (2,3,5,7 = 4 choices). Given `n`, return the count of good strings of length `n`, modulo `10^9 + 7`.

### 📌 Constraints
- `1 <= n <= 10^15`

---

## 💭 Intuition
👉 Even positions have 5 choices, odd positions have 4 choices. For `n` digits, there are `ceil(n/2)` even positions and `floor(n/2)` odd positions. So the answer is `5^ceil(n/2) * 4^floor(n/2)` which simplifies to `20^(n/2) * (5 if n is odd, else 1)`.

---

## ⚡ Approach — Modular Exponentiation

### 🧠 Idea
- Combine the 5 choices (even index) and 4 choices (odd index) as pairs: `20^(n/2)`.
- If `n` is odd, there's one extra even-index position: multiply by 5.
- Use fast modular exponentiation to handle the large exponent.

---

## 💻 Code

```cpp
class Solution {
public:
    int countGoodNumbers(long long n) {
        // Calculate the result based on whether n is even or odd
        return modPow(20, n / 2) * (n % 2 == 0 ? 1 : 5) % kMod;
    }

private:
    static constexpr int kMod = 1'000'000'007;

    // Efficient exponentiation with modulo
    long modPow(long x, long n) {
        long result = 1;
        x = x % kMod; // Ensure x is within the modulus

        while (n > 0) {
            if (n % 2 == 1) {
                result = (result * x) % kMod; // Multiply when n is odd
            }
            x = (x * x) % kMod; // Square the base
            n /= 2; // Divide exponent by 2
        }
        return result;
    }
};
```

---

## 🧠 Dry Run
### Input
```
n = 4
```
### Steps
```
n/2 = 2, n%2 = 0
modPow(20, 2) = 400
Result = 400 * 1 = 400

Verification: 4 digits, positions 0,2 have 5 choices, positions 1,3 have 4 choices
Total = 5 * 4 * 5 * 4 = 400 ✓
```

---

## ⏱️ Time Complexity
```
O(log n) for modular exponentiation
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- `n = 1`: Only one even-index position, answer is 5.
- Very large `n` (up to 10^15): modular exponentiation handles this efficiently.

---

## 🎯 Interview Takeaways
- Counting problems with independent positions reduce to multiplication (product rule).
- Modular exponentiation is essential for large exponents.
- Pairing even/odd positions as `20^(n/2)` is a clean simplification.

---

## 📌 Key Pattern
👉 **"Independent position counting with modular fast exponentiation"**

---

## 🔁 Related Problems
- 50. Pow(x, n)
- 372. Super Pow
- 1952. Three Divisors

---

## 🚀 Final Thoughts
This problem is a straightforward application of combinatorics and modular arithmetic. The key insight is that positions are independent, so we just multiply the number of choices. Fast exponentiation makes it work even for astronomically large `n`.

---

✨ **Rule to remember:**
> "When positions have independent choices, multiply choice counts; use modular exponentiation for large n."
