# 2221. Find Triangular Sum of an Array

## 🔗 Problem Link
https://leetcode.com/problems/find-triangular-sum-of-an-array/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Math, Simulation

---

## 🧩 Problem Summary
Given an array `nums`, repeatedly replace the array with a new array where each element is `(nums[i] + nums[i+1]) % 10`, reducing the size by 1 each time, until one element remains. Return that element.

### 📌 Constraints
- `1 <= nums.length <= 1000`
- `0 <= nums[i] <= 9`

---

## 💭 Intuition
👉 This is a direct simulation — repeatedly reduce the array by summing adjacent pairs modulo 10 until one element remains.

---

## ⚡ Approach — In-Place Simulation

### 🧠 Idea
- For each size from `n` down to 1, replace each `nums[i]` with `(nums[i] + nums[i+1]) % 10`.
- After all rounds, `nums[0]` holds the triangular sum.

---

## 💻 Code

```cpp
class Solution {
 public:
  int triangularSum(vector<int>& nums) {
    for (int sz = nums.size(); sz > 0; --sz)
      for (int i = 0; i + 1 < sz; ++i)
        nums[i] = (nums[i] + nums[i + 1]) % 10;
    return nums[0];
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [1, 2, 3, 4, 5]
```
### Steps
```
Round 1: [3, 5, 7, 9]
Round 2: [8, 2, 6]
Round 3: [0, 8]
Round 4: [8]
Return 8
```

---

## ⏱️ Time Complexity
```
O(n^2) — n rounds, each processing up to n elements
```

## 💾 Space Complexity
```
O(1) — in-place modification
```

---

## ⚠️ Edge Cases
- Single element → return it directly
- All zeros → result is 0
- All nines → intermediate sums wrap around via mod 10

---

## 🎯 Interview Takeaways
- In-place simulation avoids extra space allocation.
- The modulo 10 operation prevents overflow and is applied at each step.
- This is related to Pascal's triangle with mod 10 arithmetic.

---

## 📌 Key Pattern
👉 **"Iterative reduction by pairwise combination until single element remains"**

---

## 🔁 Related Problems
- 118. Pascal's Triangle
- 119. Pascal's Triangle II
- 1823. Find the Winner of the Circular Game

---

## 🚀 Final Thoughts
A straightforward simulation problem. The connection to Pascal's triangle (with mod 10) is interesting — each element's contribution to the final result is weighted by its binomial coefficient mod 10.

---

✨ **Rule to remember:**
> "Reduce the array by summing adjacent pairs mod 10 — it is Pascal's triangle in disguise."
