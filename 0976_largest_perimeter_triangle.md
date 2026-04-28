# 976. Largest Perimeter Triangle

## 🔗 Problem Link
https://leetcode.com/problems/largest-perimeter-triangle/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Math, Greedy, Sorting

---

## 🧩 Problem Summary

Given an integer array `nums`, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of non-zero area, return 0.

### 📌 Constraints
- `3 <= nums.length <= 10^4`
- `1 <= nums[i] <= 10^6`

---

## 💭 Intuition

The triangle inequality states that for three sides to form a valid triangle, the sum of the two smaller sides must exceed the largest side. 👉 Sort the array and check consecutive triplets from the largest end — the first valid triplet gives the largest perimeter.

---

## ⚡ Approach — Sort + Greedy from Largest

### 🧠 Idea

- Sort the array in non-decreasing order.
- Iterate from the end (largest values) checking triplets `(nums[i-2], nums[i-1], nums[i])`.
- The first triplet satisfying `nums[i-2] + nums[i-1] > nums[i]` gives the answer.
- If no valid triplet exists, return 0.

---

## 💻 Code

```cpp
class Solution {
 public:
  int largestPerimeter(vector<int>& nums) {
    ranges::sort(nums);

    for (int i = nums.size() - 1; i > 1; --i)
      if (nums[i - 2] + nums[i - 1] > nums[i])
        return nums[i - 2] + nums[i - 1] + nums[i];

    return 0;
  }
};
```

---

## 🧠 Dry Run

### Input
```
nums = [2, 1, 2]
```

### Steps
```
After sort: [1, 2, 2]
i=2: nums[0]+nums[1] = 1+2 = 3 > nums[2]=2 → valid!
Return 1 + 2 + 2 = 5
```

---

## ⏱️ Time Complexity

```
O(n log n)
```

Dominated by the sorting step. The linear scan is O(n).

---

## 💾 Space Complexity

```
O(log n)
```

For the sorting algorithm's stack space (in-place sort).

---

## ⚠️ Edge Cases

- **All equal:** `[3, 3, 3]` → always valid → 9
- **Cannot form triangle:** `[1, 1, 3]` → 1+1 = 2 not > 3 → 0
- **Minimum size:** Exactly 3 elements → either forms a triangle or returns 0

---

## 🎯 Interview Takeaways

- Sorting + greedy is the optimal approach for "largest valid combination" problems.
- Only consecutive triplets in the sorted array need to be checked — if `a[i-2] + a[i-1] <= a[i]`, no smaller pair will help either.
- The triangle inequality only needs checking for the largest side (the other two inequalities are automatically satisfied).
- C++20 `ranges::sort` provides a clean syntax.

---

## 📌 Key Pattern

👉 **"Sort and greedily check consecutive triplets from the largest end for triangle inequality"**

---

## 🔁 Related Problems

- 611. Valid Triangle Number
- 812. Largest Triangle Area
- 2971. Find Polygon With the Largest Perimeter

---

## 🚀 Final Thoughts

A clean greedy problem. Sorting transforms the search space so that the first valid consecutive triplet from the right is guaranteed to be the answer.

---

✨ **Rule to remember:**
> Sort the sides, then check from the largest — the first consecutive triplet satisfying the triangle inequality wins.
