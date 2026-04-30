# 3495. Minimum Operations to Make Binary Array Elements Equal to One I

## 🔗 Problem Link
https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Math, Number Theory

---

## 🧩 Problem Summary
Given a list of queries where each query is a range [l, r], compute the total minimum number of operations to reduce all numbers in each range to 1. An operation divides a number by its smallest prime factor. Numbers that are powers of 4 require progressively more operations.

### 📌 Constraints
- `1 <= queries.length <= 10^5`
- `1 <= l <= r <= 10^9`

---

## 💭 Intuition
👉 The number of operations for a number n equals the count of times you can take log base 4 (i.e., which power-of-4 range it falls in). By computing a prefix sum of operations from 1 to n grouped by powers of 4, we can answer each range query in O(log n) time.

---

## ⚡ Approach — Prefix Sum over Powers of 4

### 🧠 Idea
- Define `getOperations(n)` = total operations for all numbers in [1, n].
- Numbers in the range [4^(k-1), 4^k - 1] require k operations each.
- For each query [l, r], the answer is `(getOperations(r) - getOperations(l-1) + 1) / 2`.

---

## 💻 Code

```cpp
class Solution {
 public:
  long long minOperations(vector<vector<int>>& queries) {
    long ans = 0;
    for (const vector<int>& query : queries) {
      const int l = query[0];
      const int r = query[1];
      ans += (getOperations(r) - getOperations(l - 1) + 1) / 2;
    }
    return ans;
  }

 private:
  // Returns the number of operations required for [1, n].
  long getOperations(int n) {
    long res = 0;
    int ops = 0;
    for (int powerOfFour = 1; powerOfFour <= n; powerOfFour *= 4) {
      const int l = powerOfFour;
      const int r = min(n, powerOfFour * 4 - 1);
      res += static_cast<long>(r - l + 1) * ++ops;
    }
    return res;
  }
};
```

---

## 🧠 Dry Run
### Input
```
queries = [[1, 4]]
```
### Steps
```
getOperations(4):
  pow4=1: l=1, r=3, ops=1 -> res += 3*1 = 3
  pow4=4: l=4, r=4, ops=2 -> res += 1*2 = 2
  res = 5

getOperations(0): res = 0

ans += (5 - 0 + 1) / 2 = 3

Result: 3
```

---

## ⏱️ Time Complexity
```
O(q * log(max_val)) — each query processes O(log4(r)) power-of-4 ranges
```

## 💾 Space Complexity
```
O(1) — constant extra space
```

---

## ⚠️ Edge Cases
- l = r = 1 → 0 operations needed
- Very large ranges → use long to avoid overflow
- l = 1 → getOperations(0) = 0

---

## 🎯 Interview Takeaways
- Grouping numbers by power-of-4 ranges transforms a per-element computation into a range formula.
- Prefix sum trick: range [l, r] answer = prefix(r) - prefix(l-1).
- Ceiling division via `(x + 1) / 2` is a clean pattern.

---

## 📌 Key Pattern
👉 **"Group by exponential ranges and use prefix sums for efficient range queries."**

---

## 🔁 Related Problems
- 1558. Minimum Numbers of Function Calls to Make Target Array
- 2338. Count the Number of Ideal Arrays
- 233. Number of Digit One

---

## 🚀 Final Thoughts
The key insight is recognizing the power-of-4 structure in the operation count. This allows a closed-form prefix sum computation, making each query O(log n) instead of O(n).

---

✨ **Rule to remember:**
> When operation counts follow exponential groupings, compute prefix sums over those groups for O(log n) range queries.
