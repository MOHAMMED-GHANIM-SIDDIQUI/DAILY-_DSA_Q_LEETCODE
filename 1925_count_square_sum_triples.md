# 1925. Count Square Sum Triples

## 🔗 Problem Link
https://leetcode.com/problems/count-square-sum-triples/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Math, Hash Table, Enumeration

---

## 🧩 Problem Summary
Given a positive integer `n`, return the number of square sum triples `(a, b, c)` where `1 <= a, b, c <= n` and `a^2 + b^2 = c^2`. Order matters, so `(a, b, c)` and `(b, a, c)` are counted separately if `a != b`.

### 📌 Constraints
- `1 <= n <= 250`

---

## 💭 Intuition
👉 Precompute all perfect squares up to `n^2`, store them in a set, then enumerate all pairs `(a^2, b^2)` and check if their sum is also in the set.

---

## ⚡ Approach — Hash Set of Squares

### 🧠 Idea
- Create a set of all `i^2` for `i` from 1 to `n`.
- For each pair of squares `(a, b)` in the set, check if `a + b` is also in the set.
- Count all such valid triples.

---

## 💻 Code

```cpp
class Solution {
 public:
  int countTriples(int n) {
    int ans = 0;
    unordered_set<int> squared;

    for (int i = 1; i <= n; ++i)
      squared.insert(i * i);

    for (const int a : squared)
      for (const int b : squared)
        if (squared.contains(a + b))
          ++ans;

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
n = 5
```
### Steps
```
squared = {1, 4, 9, 16, 25}

Check all pairs (a, b):
  (9, 16) -> 25 ∈ squared ✓ (3,4,5)
  (16, 9) -> 25 ∈ squared ✓ (4,3,5)

Result: 2
```

---

## ⏱️ Time Complexity
```
O(n^2) for checking all pairs of squares
```

## 💾 Space Complexity
```
O(n) for the set of squares
```

---

## ⚠️ Edge Cases
- `n < 5`: No Pythagorean triple exists with all values <= 4, return 0.
- `n = 5`: First triple is (3, 4, 5), count = 2 (includes (4, 3, 5)).

---

## 🎯 Interview Takeaways
- Precomputing a set of candidate values enables O(1) membership testing.
- Pythagorean triples are a classic math/enumeration problem.
- Using `contains()` (C++20) or `count()` for set membership is clean.

---

## 📌 Key Pattern
👉 **"Precompute a set of valid values, then enumerate pairs and check membership"**

---

## 🔁 Related Problems
- 633. Sum of Square Numbers
- 1. Two Sum
- 15. 3Sum

---

## 🚀 Final Thoughts
This is a straightforward enumeration problem. The hash set makes the inner check O(1), bringing the overall complexity to O(n^2). For the given constraints (n <= 250), this is very efficient.

---

✨ **Rule to remember:**
> "Store squares in a set, enumerate pairs, and check if the sum exists — a hash-set-based Pythagorean triple finder."
