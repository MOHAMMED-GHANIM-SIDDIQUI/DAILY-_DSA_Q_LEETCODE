# 1523. Count Odd Numbers in an Interval Range

## 🔗 Problem Link
https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Math

---

## 🧩 Problem Summary
Given two non-negative integers `low` and `high`, return the count of odd numbers between `low` and `high` (inclusive).

### 📌 Constraints
- `0 <= low <= high <= 10^9`

---

## 💭 Intuition
👉 In any range of consecutive integers, roughly half are odd. If either endpoint is odd, there is one extra odd number compared to the even count. The formula `(high - low) / 2 + 1` works when at least one endpoint is odd, and `(high - low) / 2` when both are even.

---

## ⚡ Approach — Math Formula

### 🧠 Idea
- If either `low` or `high` is odd, the count is `(high - low) / 2 + 1`.
- If both are even, the count is `(high - low) / 2`.
- This works because integer division naturally floors the result.

---

## 💻 Code

```cpp
class Solution {
public:
    int countOdds(int low, int high) {
        if (low%2 || high%2)
        {
            return ((high-low)/2)+1;
        }
        return (high-low)/2;
    }
};
```

---

## 🧠 Dry Run
### Input
```
low = 3, high = 7
```
### Steps
```
low % 2 = 1 (odd) → enter if branch
(7 - 3) / 2 + 1 = 4/2 + 1 = 2 + 1 = 3
Odd numbers: 3, 5, 7 → Answer: 3
```

---

## ⏱️ Time Complexity
```
O(1)
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- `low == high` and both odd — answer is 1.
- `low == high` and both even — answer is 0.
- `low = 0, high = 0` — answer is 0.
- Very large range (up to 10^9) — formula handles it in O(1).

---

## 🎯 Interview Takeaways
- Simple math problems should be solved with formulas, not loops.
- The parity of endpoints determines whether to add 1 to the half-count.
- An alternative formula: `(high + 1) / 2 - low / 2` works universally without branching.

---

## 📌 Key Pattern
👉 **"Count elements with a property in a range using a closed-form formula based on endpoints"**

---

## 🔁 Related Problems
- 1281 — Subtract the Product and Sum of Digits
- 1342 — Number of Steps to Reduce a Number to Zero
- 2894 — Divisible and Non-divisible Sums Difference

---

## 🚀 Final Thoughts
This is a pure math problem. The key insight is that odd numbers alternate with even numbers, so the count depends only on the range length and the parity of endpoints. No iteration needed.

---

✨ **Rule to remember:**
> "Odd count in [low, high] = (high - low) / 2 + 1 if either endpoint is odd, else (high - low) / 2."
