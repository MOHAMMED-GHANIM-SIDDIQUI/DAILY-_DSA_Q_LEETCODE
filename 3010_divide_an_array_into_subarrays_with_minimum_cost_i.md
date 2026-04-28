# 3010. Divide an Array Into Subarrays With Minimum Cost I

## 🔗 Problem Link
https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Sorting, Enumeration

---

## 🧩 Problem Summary
Given an array `nums`, divide it into 3 contiguous subarrays. The cost of each subarray is its first element. Return the minimum possible sum of costs. The first subarray must start at index 0, so `nums[0]` is always included. We need to pick 2 split points to minimize the sum of the first elements of the 3 subarrays.

### 📌 Constraints
- `3 <= nums.length <= 50`
- `1 <= nums[i] <= 50`

---

## 💭 Intuition
👉 Since `nums[0]` is always the cost of the first subarray, we need to find the two smallest elements from `nums[1:]` to serve as the first elements of the second and third subarrays.

---

## ⚡ Approach — Two Minimum Tracking

### 🧠 Idea
- The first subarray always starts at index 0, so `nums[0]` is fixed.
- From indices 1 to n-1, find the two smallest values. These will be the optimal first elements for the second and third subarrays.
- Track `min1` and `min2` in a single pass.

---

## 💻 Code

```python
class Solution:
  def minimumCost(self, nums: list[int]) -> int:
    MAX = 50
    min1 = MAX
    min2 = MAX

    for i in range(1, len(nums)):
      if nums[i] < min1:
        min2 = min1
        min1 = nums[i]
      elif nums[i] < min2:
        min2 = nums[i]

    return nums[0] + min1 + min2
```

---

## 🧠 Dry Run
### Input
```
nums = [1, 2, 3, 12]
```
### Steps
```
1. nums[0] = 1 (fixed cost of first subarray)
2. Scan nums[1:] = [2, 3, 12]
3. i=1: nums[1]=2 < min1(50) => min2=50, min1=2
4. i=2: nums[2]=3 < min2(50) => min2=3
5. i=3: nums[3]=12 >= min2(3) => skip
6. Result = 1 + 2 + 3 = 6
```

---

## ⏱️ Time Complexity
```
O(n) — single pass through the array.
```

## 💾 Space Complexity
```
O(1) — only two extra variables.
```

---

## ⚠️ Edge Cases
- Array of exactly 3 elements: each subarray has one element, answer is sum of all.
- All elements are the same: answer is `3 * nums[0]`.

---

## 🎯 Interview Takeaways
- When the first element is fixed, the problem reduces to finding the k smallest values in the remainder.
- Tracking top-k minimums in a single pass avoids sorting overhead.

---

## 📌 Key Pattern
👉 **"Fixed first element + find k smallest in the rest"**

---

## 🔁 Related Problems
- 3013. Divide an Array Into Subarrays With Minimum Cost II
- 2099. Find Subsequence of Length K With the Largest Sum

---

## 🚀 Final Thoughts
A clean easy problem that tests the ability to recognize that the first element is fixed and the remaining optimization is simply finding two minimums. The constraints are small, but the single-pass approach is elegant.

---

✨ **Rule to remember:**
> When splitting into k contiguous subarrays where cost = first element, fix the first subarray and pick the (k-1) smallest elements from the rest.
