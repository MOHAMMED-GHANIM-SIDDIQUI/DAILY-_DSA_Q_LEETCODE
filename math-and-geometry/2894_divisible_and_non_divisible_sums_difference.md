# 2894. Divisible and Non-Divisible Sums Difference

## 🔗 Problem Link
https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Math

---

## 🧩 Problem Summary
Given two positive integers `n` and `m`, find the difference between the sum of integers in `[1, n]` that are NOT divisible by `m` (num1) and the sum of integers in `[1, n]` that ARE divisible by `m` (num2). Return `num1 - num2`.

### 📌 Constraints
- 1 <= n, m <= 1000

---

## 💭 Intuition
👉 Instead of iterating through all numbers, compute the total sum with the formula `n*(n+1)/2`, then compute the sum of multiples of `m` using arithmetic series. The answer is `totalSum - 2 * divisibleSum`.

---

## ⚡ Approach — Math (Arithmetic Series)

### 🧠 Idea
- Compute `sum = n*(n+1)/2` (total sum of 1 to n).
- Compute `num2` = sum of all multiples of `m` in `[1, n]` using arithmetic series formula.
- `num1 = sum - num2`.
- Return `num1 - num2 = sum - 2*num2`.

---

## 💻 Code

```cpp
class Solution {
 public:
  int differenceOfSums(int n, int m) {
    const int sum = (1 + n) * n / 2;
    const int num2 = getDivisibleSum(n, m);
    const int num1 = sum - num2;
    return num1 - num2;
  }

 private:
  // Returns the sum of all the integers in [1, n] that are divisible by m.
  int getDivisibleSum(int n, int m) {
    const int last = n / m * m;
    if (last == 0)
      return 0;
    const int first = m;
    const int count = (last - first) / m + 1;
    return (first + last) * count / 2;
  }
};
```

---

## 🧠 Dry Run
### Input
```
n = 10, m = 3
```
### Steps
```
sum = (1+10)*10/2 = 55
getDivisibleSum(10, 3):
  last = 10/3*3 = 9
  first = 3
  count = (9-3)/3 + 1 = 3
  divisibleSum = (3+9)*3/2 = 18

num1 = 55 - 18 = 37
num2 = 18
ans = 37 - 18 = 19

Output: 19
```

---

## ⏱️ Time Complexity
```
O(1) — pure mathematical computation
```

## 💾 Space Complexity
```
O(1) — no extra space used
```

---

## ⚠️ Edge Cases
- `m > n`: No number in `[1, n]` is divisible by `m`, so `num2 = 0` and answer is `sum`.
- `m = 1`: All numbers are divisible, so `num1 = 0` and answer is `-sum`.
- `n = 1, m = 1`: answer is -1.

---

## 🎯 Interview Takeaways
- Arithmetic series formulas avoid unnecessary iteration.
- The sum of multiples of `m` up to `n` is a classic math trick.
- `num1 - num2 = sum - 2*num2` simplifies the computation.

---

## 📌 Key Pattern
👉 **"Arithmetic Series for sum of multiples — O(1) math solution"**

---

## 🔁 Related Problems
- 1programmers. Fizz Buzz
- 1281. Subtract the Product and Sum of Digits of an Integer
- 2427. Number of Common Factors

---

## 🚀 Final Thoughts
A straightforward math problem that rewards knowing the arithmetic series formula. The O(1) solution is elegant and avoids any loops. The key identity `num1 - num2 = totalSum - 2 * divisibleSum` makes the code concise.

---

✨ **Rule to remember:**
> Sum of multiples of m up to n = m * count * (count+1) / 2 where count = floor(n/m).
