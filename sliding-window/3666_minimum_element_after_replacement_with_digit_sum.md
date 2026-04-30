# 3666. Minimum Element After Replacement with Digit Sum

## 🔗 Problem Link
https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Counting, Sliding Window

---

## 🧩 Problem Summary
Given an array `nums` and an integer `k`, count the number of partitions of the array into contiguous subarrays such that the difference between the maximum and minimum element in each subarray is at most `k`.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `0 <= k <= 10^9`

---

## 💭 Intuition
👉 This problem maps to counting the number of ways to partition an array where each segment satisfies a max-min constraint — but the provided solution addresses a related problem of minimum removals using sort + sliding window to find the longest valid subset.

---

## ⚡ Approach — Sort + Sliding Window

### 🧠 Idea
- Sort the array so that max and min of any contiguous window are at the endpoints.
- Use two pointers to find the longest window where `nums[j] <= k * nums[i]`.
- The answer is `n - maxWindowLength` (minimum elements to remove).

---

## 💻 Code

```python
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        L = 1
        i = 0

        for j in range(n):
            maxEl = nums[j]

            while i < j and maxEl > k * nums[i]:
                i += 1

            L = max(L, j - i + 1)

        return n - L
```

---

## 🧠 Dry Run
### Input
```
nums = [1, 2, 3, 10, 20], k = 3
```
### Steps
```
Sorted: [1, 2, 3, 10, 20]

j=0: maxEl=1, i=0, L=max(1,1)=1
j=1: maxEl=2, 2<=3*1? Yes, L=max(1,2)=2
j=2: maxEl=3, 3<=3*1? Yes, L=max(2,3)=3
j=3: maxEl=10, 10<=3*1? No→i=1, 10<=3*2? No→i=2, 10<=3*3? Yes, L=max(3,2)=3
j=4: maxEl=20, 20<=3*3? No→i=3, 20<=3*10? Yes, L=max(3,2)=3

Result: 5 - 3 = 2
```

---

## ⏱️ Time Complexity
```
O(n log n) — dominated by sorting
```

## 💾 Space Complexity
```
O(1) — in-place sorting with constant extra space
```

---

## ⚠️ Edge Cases
- k = 0 → only identical elements can be kept
- All elements are the same → remove 0
- Single element → remove 0
- k very large → entire array is valid

---

## 🎯 Interview Takeaways
- Sorting converts a subset problem into a subarray problem.
- Two-pointer technique on sorted arrays efficiently finds longest valid windows.
- "Minimum removals" = "n minus longest valid subset."

---

## 📌 Key Pattern
👉 **"Sort + sliding window — find the longest valid window and subtract from n."**

---

## 🔁 Related Problems
- 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
- 2779. Maximum Beauty of an Array After Applying Operation
- 3634. Count Partitions with Max-Min Difference at Most K

---

## 🚀 Final Thoughts
The sort + sliding window pattern is a versatile tool for problems involving min/max constraints on subsets. By sorting, we ensure the constraint is only checked at window boundaries, making the two-pointer approach both correct and efficient.

---

✨ **Rule to remember:**
> "Sort to bring extremes to endpoints, then slide a window to find the longest valid range."
