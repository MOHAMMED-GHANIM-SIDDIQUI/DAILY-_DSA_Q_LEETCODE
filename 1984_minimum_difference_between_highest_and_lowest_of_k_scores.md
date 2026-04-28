# 1984. Minimum Difference Between Highest and Lowest of K Scores

## 🔗 Problem Link
https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Sorting, Sliding Window

---

## 🧩 Problem Summary
Given an array of student scores and an integer `k`, pick `k` students such that the difference between the highest and lowest scores among them is minimized. Return that minimum difference.

### 📌 Constraints
- `1 <= k <= nums.length <= 1000`
- `0 <= nums[i] <= 10^5`

---

## 💭 Intuition
👉 After sorting, the optimal group of `k` students must be a contiguous subarray (since any gap would increase the range). So we slide a window of size `k` and find the minimum difference between the last and first elements.

---

## ⚡ Approach — Sort + Sliding Window

### 🧠 Idea
- Sort the array.
- Initialize the answer with the difference of the first window: `nums[k-1] - nums[0]`.
- Slide the window across the sorted array, updating the minimum difference.

---

## 💻 Code

```python
class Solution:
  def minimumDifference(self, nums: list[int], k: int) -> int:
    nums.sort()
    ans = nums[k - 1] - nums[0]

    for i in range(k, len(nums)):
      ans = min(ans, nums[i] - nums[i - k + 1])

    return ans
```

---

## 🧠 Dry Run
### Input
```
nums = [90, 2, 36, 1, 5], k = 3
```
### Steps
```
After sort: [1, 2, 5, 36, 90]
Initial: ans = nums[2] - nums[0] = 5 - 1 = 4
i=3: nums[3] - nums[1] = 36 - 2 = 34, ans = min(4, 34) = 4
i=4: nums[4] - nums[2] = 90 - 5 = 85, ans = min(4, 85) = 4
return 4
```

---

## ⏱️ Time Complexity
```
O(n log n) due to sorting
```

## 💾 Space Complexity
```
O(1) extra space (in-place sort)
```

---

## ⚠️ Edge Cases
- `k = 1` → difference is always 0
- `k = n` → difference is `nums[-1] - nums[0]`
- All elements are equal → difference is 0

---

## 🎯 Interview Takeaways
- Sorting reduces the problem from combinatorial to a simple sliding window.
- In a sorted array, the minimum range subarray of size `k` must be contiguous.

---

## 📌 Key Pattern
👉 **"Sort + fixed-size sliding window to minimize range"**

---

## 🔁 Related Problems
- 1877. Minimize Maximum Pair Sum in Array
- 2144. Minimum Cost of Buying Candies With Discount
- 904. Fruit Into Baskets

---

## 🚀 Final Thoughts
A classic easy problem that demonstrates how sorting simplifies selection problems. After sorting, the answer is just the minimum difference between endpoints of any window of size `k`.

---

✨ **Rule to remember:**
> To minimize the range of k selected elements, sort and slide a window of size k.
