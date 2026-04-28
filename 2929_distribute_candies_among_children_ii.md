# 2929. Distribute Candies Among Children II

## 🔗 Problem Link
https://leetcode.com/problems/distribute-candies-among-children-ii/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Math, Combinatorics, Inclusion-Exclusion Principle

---

## 🧩 Problem Summary
Distribute `n` candies among 3 children such that no child gets more than `limit` candies. Return the total number of ways to do this.

### 📌 Constraints
- 1 <= n <= 10^6
- 1 <= limit <= 10^6

---

## 💭 Intuition
👉 Use the Stars and Bars method to count unrestricted distributions, then apply the Inclusion-Exclusion Principle (PIE) to subtract cases where one or more children exceed the limit.

---

## ⚡ Approach — Inclusion-Exclusion Principle

### 🧠 Idea
- `ways(n)` = C(n+2, 2) = number of ways to distribute `n` candies to 3 children (no upper limit).
- Subtract cases where at least 1 child exceeds `limit` (gets > limit, i.e., at least limit+1).
- Add back cases where at least 2 children exceed limit (overcounted).
- Subtract cases where all 3 exceed (over-added back).

---

## 💻 Code

```cpp
class Solution {
 public:
  // Same as 2927. Distribute Candies Among Children III
  long long distributeCandies(int n, int limit) {
    const int limitPlusOne = limit + 1;
    const long oneChildExceedsLimit = ways(n - limitPlusOne);
    const long twoChildrenExceedLimit = ways(n - 2 * limitPlusOne);
    const long threeChildrenExceedLimit = ways(n - 3 * limitPlusOne);
    // Principle of Inclusion-Exclusion (PIE)
    return ways(n) - 3 * oneChildExceedsLimit + 3 * twoChildrenExceedLimit -
           threeChildrenExceedLimit;
  }

 private:
  // Returns the number of ways to distribute n candies to 3 children.
  long ways(int n) {
    if (n < 0)
      return 0;
    // Stars and bars method:
    // e.g. '**|**|*' means to distribute 5 candies to 3 children, where
    // stars (*) := candies and bars (|) := dividers between children.
    return nCk(n + 2, 2);
  }

  long nCk(int n, int k) {
    long res = 1;
    for (int i = 1; i <= k; ++i)
      res = res * (n - i + 1) / i;
    return res;
  }
};
```

---

## 🧠 Dry Run
### Input
```
n = 5, limit = 2
```
### Steps
```
limitPlusOne = 3

ways(5) = C(7,2) = 21
oneChild = ways(5-3) = ways(2) = C(4,2) = 6
twoChildren = ways(5-6) = ways(-1) = 0
threeChildren = ways(5-9) = ways(-4) = 0

PIE: 21 - 3*6 + 3*0 - 0 = 21 - 18 = 3

Output: 3
(Valid: {1,2,2}, {2,1,2}, {2,2,1})
```

---

## ⏱️ Time Complexity
```
O(1) — constant number of combinatorial computations
```

## 💾 Space Complexity
```
O(1) — no extra space
```

---

## ⚠️ Edge Cases
- `n = 0`: Only one way (give 0 to each child).
- `limit >= n`: No child can exceed anyway, answer is C(n+2, 2).
- `n > 3 * limit`: Impossible to distribute, answer is 0.

---

## 🎯 Interview Takeaways
- Stars and Bars gives unrestricted distribution count: C(n+k-1, k-1) for k children.
- Inclusion-Exclusion handles upper bound constraints elegantly.
- The substitution trick: "child gets > limit" is equivalent to "pre-assign limit+1, distribute rest."

---

## 📌 Key Pattern
👉 **"Stars and Bars + Inclusion-Exclusion for bounded distribution counting"**

---

## 🔁 Related Problems
- 2927. Distribute Candies Among Children III
- 1692. Count Ways to Distribute Candies
- 1621. Number of Sets of K Non-Overlapping Line Segments

---

## 🚀 Final Thoughts
This is a textbook application of combinatorics. The Inclusion-Exclusion Principle turns a constrained counting problem into a few unconstrained ones. The O(1) solution is far superior to brute force enumeration.

---

✨ **Rule to remember:**
> For distributing n items to k bins with upper limits, use Stars-and-Bars minus PIE corrections for exceeded limits.
