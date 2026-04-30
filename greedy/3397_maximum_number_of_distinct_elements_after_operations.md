# 3397. Maximum Number of Distinct Elements After Operations

## 🔗 Problem Link
https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Sorting, Greedy

---

## 🧩 Problem Summary
Given an integer array and an integer k, you can change each element nums[i] to any value in the range [nums[i] - k, nums[i] + k]. Find the maximum number of distinct elements achievable after all operations.

### 📌 Constraints
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 0 <= k <= 10^9

---

## 💭 Intuition
👉 Sort the array. Greedily assign each element the smallest possible value in its range [num-k, num+k] that is strictly greater than the previously assigned value. This maximizes room for future elements.

---

## ⚡ Approach — Greedy with Sorting

### 🧠 Idea
- Sort the array.
- Track the last "occupied" value (initialized to INT_MIN).
- For each number, try to place it at max(occupied + 1, num - k).
- If this placement is within [num - k, num + k], accept it and update occupied.
- Otherwise, skip (cannot make this element distinct).

---

## 💻 Code

```cpp
class Solution {
 public:
  int maxDistinctElements(vector<int>& nums, int k) {
    int ans = 0;
    int occupied = INT_MIN;

    ranges::sort(nums);

    for (const int num : nums)
      if (occupied < num + k) {
        occupied = max(occupied + 1, num - k);
        ++ans;
      }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [4, 4, 4, 4], k = 1
```
### Steps
```
Sorted: [4, 4, 4, 4]
occupied = INT_MIN

num=4: occupied < 5 → occupied = max(INT_MIN+1, 3) = 3, ans=1
num=4: occupied=3 < 5 → occupied = max(4, 3) = 4, ans=2
num=4: occupied=4 < 5 → occupied = max(5, 3) = 5, ans=3
num=4: occupied=5 < 5? No → skip

Result: 3
```

---

## ⏱️ Time Complexity
```
O(n log n) — dominated by sorting
```

## 💾 Space Complexity
```
O(1) — sorting in-place (or O(log n) for sort stack)
```

---

## ⚠️ Edge Cases
- k = 0 → answer is the count of distinct elements
- All elements identical → answer is min(n, 2*k + 1)
- Large k → all elements can be made distinct

---

## 🎯 Interview Takeaways
- Sort + greedy assignment is a powerful technique for "maximize distinct values" problems.
- Always assign the smallest feasible value to leave maximum room for subsequent elements.
- The condition `occupied < num + k` elegantly handles the feasibility check.

---

## 📌 Key Pattern
👉 **"Sort and greedily assign the smallest valid value"**

---

## 🔁 Related Problems
- 945. Minimum Increment to Make Array Unique
- 1846. Maximum Element After Decreasing and Rearranging

---

## 🚀 Final Thoughts
This greedy approach is optimal because sorting ensures we process elements in order and assigning the smallest valid value maximizes the number of distinct slots available for later elements.

---

✨ **Rule to remember:**
> Sort, then greedily pick the smallest available value in each element's range to maximize distinctness.
