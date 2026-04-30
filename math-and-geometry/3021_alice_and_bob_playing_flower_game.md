# 3021. Alice and Bob Playing Flower Game

## 🔗 Problem Link
https://leetcode.com/problems/alice-and-bob-playing-flower-game/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Math

---

## 🧩 Problem Summary
Alice and Bob play a game with flowers arranged in a line. Alice picks `x` flowers from one end and Bob picks `y` from the other (1 <= x <= n, 1 <= y <= m). Alice wins if `x + y` is odd. Count the number of `(x, y)` pairs where Alice wins.

### 📌 Constraints
- 1 <= n, m <= 10^5

---

## 💭 Intuition
👉 `x + y` is odd when exactly one of them is even and the other is odd. Count even/odd numbers in each range and multiply: `(even_x * odd_y) + (odd_x * even_y)`.

---

## ⚡ Approach — Parity Counting

### 🧠 Idea
- Count even numbers in [1, n]: `n / 2`.
- Count odd numbers in [1, n]: `(n + 1) / 2`.
- Similarly for [1, m].
- Alice wins when x is even and y is odd, or x is odd and y is even.
- Answer = `xEven * yOdd + yEven * xOdd`.

---

## 💻 Code

```cpp
class Solution {
 public:
  long long flowerGame(int n, int m) {
    // Alice wins if x + y is odd, occurring when:
    //   1. x is even and y is odd, or
    //   2. y is even and x is odd.
    const int xEven = n / 2;
    const int yEven = m / 2;
    const int xOdd = (n + 1) / 2;
    const int yOdd = (m + 1) / 2;
    return static_cast<long>(xEven) * yOdd + static_cast<long>(yEven) * xOdd;
  }
};
```

---

## 🧠 Dry Run
### Input
```
n = 3, m = 2
```
### Steps
```
xEven = 3/2 = 1 (x=2)
xOdd = (3+1)/2 = 2 (x=1,3)
yEven = 2/2 = 1 (y=2)
yOdd = (2+1)/2 = 1 (y=1)

Alice wins: xEven*yOdd + yEven*xOdd = 1*1 + 1*2 = 3

Valid pairs: (2,1), (1,2), (3,2) → all have odd sum ✓

Output: 3
```

---

## ⏱️ Time Complexity
```
O(1) — pure arithmetic
```

## 💾 Space Complexity
```
O(1) — no extra space
```

---

## ⚠️ Edge Cases
- `n = 1, m = 1`: Only pair is (1,1), sum=2 (even), Alice loses. Answer: 0.
- `n = 1`: Only odd x values, so only yEven matters.
- Large n and m: use `long` to avoid overflow in multiplication.

---

## 🎯 Interview Takeaways
- Parity-based counting is a powerful O(1) technique.
- `x + y` is odd if and only if exactly one is even and the other is odd.
- Count of even numbers in [1, n] = `n/2`, odd numbers = `(n+1)/2`.

---

## 📌 Key Pattern
👉 **"Parity counting — odd sum requires one even and one odd"**

---

## 🔁 Related Problems
- 1154. Day of the Year
- 2485. Find the Pivot Integer
- 1523. Count Odd Numbers in an Interval Range

---

## 🚀 Final Thoughts
A clean math problem that reduces to parity counting. The key insight that `x + y` is odd when exactly one is even makes this an O(1) computation. Always cast to `long` when multiplying values that could overflow 32-bit integers.

---

✨ **Rule to remember:**
> Sum of two integers is odd if and only if one is even and the other is odd — count each parity separately and multiply.
