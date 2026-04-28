# 1877. Minimize Maximum Pair Sum in Array

## 🔗 Problem Link
https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Two Pointers, Greedy, Sorting

---

## 🧩 Problem Summary
Given an array `nums` of even length, pair up elements such that each element belongs to exactly one pair and the maximum pair sum is minimized. Return the minimized maximum pair sum.

### 📌 Constraints
- `n == nums.length`
- `2 <= n <= 10^5`
- `n` is even
- `1 <= nums[i] <= 10^5`

---

## 💭 Intuition
👉 To minimize the maximum pair sum, pair the smallest with the largest, second smallest with second largest, and so on. Sorting + two pointers achieves this optimally.

---

## ⚡ Approach — Sort + Two Pointers (Greedy)

### 🧠 Idea
- Sort the array.
- Use two pointers: one at the start (`l`) and one at the end (`r`).
- Pair `nums[l]` with `nums[r]`, track the maximum pair sum.
- Move both pointers inward.

---

## 💻 Code

```python
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=len(nums) - 1
        max_sum=-float('inf')
        while l<r:
            cur_sum = nums[l]+nums[r]
            if cur_sum>max_sum:
                max_sum = cur_sum
            l+=1
            r-=1
        return max_sum
```

---

## 🧠 Dry Run
### Input
```
nums = [3, 5, 2, 3]
```
### Steps
```
After sort: [2, 3, 3, 5]
l=0, r=3: pair (2,5) → sum=7, max_sum=7
l=1, r=2: pair (3,3) → sum=6, max_sum=7
return 7
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
- Array of length 2 → only one pair
- All elements are the same → any pairing gives the same result
- Already sorted input

---

## 🎯 Interview Takeaways
- Greedy pairing (smallest + largest) minimizes the maximum sum — this is provable by contradiction.
- Sorting transforms a complex combinatorial problem into a simple two-pointer scan.

---

## 📌 Key Pattern
👉 **"Sort and pair extremes to minimize the maximum pair sum"**

---

## 🔁 Related Problems
- 881. Boats to Save People
- 1984. Minimum Difference Between Highest and Lowest of K Scores
- 2144. Minimum Cost of Buying Candies With Discount

---

## 🚀 Final Thoughts
This is a classic greedy problem. The proof is intuitive: pairing the largest with the smallest "absorbs" the large value with the smallest possible partner, preventing it from making another pair even larger.

---

✨ **Rule to remember:**
> To minimize the maximum pair sum, always pair the smallest with the largest.
