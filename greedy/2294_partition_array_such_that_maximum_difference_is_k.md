# 2294. Partition Array Such That Maximum Difference Is K

## 🔗 Problem Link
https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Sorting, Greedy

---

## 🧩 Problem Summary
Given an integer array `nums` and an integer `k`, partition the array into the minimum number of subsequences such that the difference between the maximum and minimum values in each subsequence is at most `k`.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^5`
- `0 <= k <= 10^5`

---

## 💭 Intuition
👉 Sort the array. Then greedily extend each group starting from the smallest unassigned element until the range exceeds `k`.

---

## ⚡ Approach — Sort + Greedy

### 🧠 Idea
- Sort `nums`.
- Start a new group with the current minimum.
- Extend the group until `nums[i] - min > k`, then start a new group.
- Count the number of groups.

---

## 💻 Code

```cpp
class Solution {
 public:
  int partitionArray(vector<int>& nums, int k) {
    ranges::sort(nums);

    int ans = 1;
    int mn = nums[0];

    for (int i = 1; i < nums.size(); ++i)
      if (mn + k < nums[i]) {
        ++ans;
        mn = nums[i];
      }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [3, 6, 1, 2, 5], k = 2
```
### Steps
```
Sorted: [1, 2, 3, 5, 6]
Group 1: mn=1, i=1 (2: 1+2>=2 ✓), i=2 (3: 1+2>=3 ✓), i=3 (5: 1+2<5 → new group)
Group 2: mn=5, i=4 (6: 5+2>=6 ✓)
ans = 2
```

---

## ⏱️ Time Complexity
```
O(n log n) — dominated by sorting
```

## 💾 Space Complexity
```
O(1) — in-place sort, constant extra space
```

---

## ⚠️ Edge Cases
- k = 0 → each group contains only equal elements
- All elements are the same → one group
- k >= max - min → entire array in one group

---

## 🎯 Interview Takeaways
- Sorting transforms a subsequence problem into a contiguous subarray problem.
- Greedy from the smallest element ensures minimum groups.
- The condition `mn + k < nums[i]` cleanly detects when a new group is needed.

---

## 📌 Key Pattern
👉 **"Sort + greedy grouping by range constraint"**

---

## 🔁 Related Problems
- 2279. Maximum Bags With Full Capacity of Rocks
- 945. Minimum Increment to Make Array Unique
- 1296. Divide Array in Sets of K Consecutive Numbers

---

## 🚀 Final Thoughts
Sorting is the key insight — once sorted, the greedy approach of extending groups until the range exceeds `k` is both optimal and trivial to implement.

---

✨ **Rule to remember:**
> "Sort and greedily group: start a new group whenever the range exceeds k."
