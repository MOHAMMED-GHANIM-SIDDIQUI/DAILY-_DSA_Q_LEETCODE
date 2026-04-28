# 2873. Maximum Value of an Ordered Triplet I

## 🔗 Problem Link
https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Greedy

---

## 🧩 Problem Summary
Given a 0-indexed integer array `nums`, find the maximum value of `(nums[i] - nums[j]) * nums[k]` over all triplets `(i, j, k)` with `i < j < k`. Return 0 if all triplet values are negative.

### 📌 Constraints
- 3 <= nums.length <= 100
- 1 <= nums[i] <= 10^6

---

## 💭 Intuition
👉 As we scan from left to right, each element can serve as `nums[k]`. We want the maximum `(nums[i] - nums[j])` seen so far to the left. We track the running maximum element (`maxNum` for `nums[i]`) and the running maximum difference (`maxDiff` for `nums[i] - nums[j]`).

---

## ⚡ Approach — Single Pass with Running Max

### 🧠 Idea
- Iterate through the array; for each element `num`:
  - Update `ans` using `maxDiff * num` (treating `num` as `nums[k]`).
  - Update `maxDiff` using `maxNum - num` (treating `num` as `nums[j]`).
  - Update `maxNum` with `num` (treating `num` as `nums[i]`).
- The order of updates ensures correct index ordering.

---

## 💻 Code

```cpp
class Solution {
 public:
  long long maximumTripletValue(vector<int>& nums) {
    long ans = 0;
    int maxDiff = 0;  // max(nums[i] - nums[j])
    int maxNum = 0;   // max(nums[i])

    for (const int num : nums) {
      ans = max(ans, static_cast<long>(maxDiff) * num);  // num := nums[k]
      maxDiff = max(maxDiff, maxNum - num);              // num := nums[j]
      maxNum = max(maxNum, num);                         // num := nums[i]
    }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [12, 6, 1, 2, 7]
```
### Steps
```
Initial: ans=0, maxDiff=0, maxNum=0

num=12: ans=max(0, 0*12)=0, maxDiff=max(0, 0-12)=0, maxNum=12
num=6:  ans=max(0, 0*6)=0,  maxDiff=max(0, 12-6)=6,  maxNum=12
num=1:  ans=max(0, 6*1)=6,  maxDiff=max(6, 12-1)=11, maxNum=12
num=2:  ans=max(6, 11*2)=22, maxDiff=max(11,12-2)=11, maxNum=12
num=7:  ans=max(22, 11*7)=77, maxDiff=max(11,12-7)=11, maxNum=12

Output: 77
```

---

## ⏱️ Time Complexity
```
O(n) — single pass through the array
```

## 💾 Space Complexity
```
O(1) — only three variables maintained
```

---

## ⚠️ Edge Cases
- All elements are equal: answer is 0.
- Strictly increasing array: all differences are negative, answer is 0.
- Strictly decreasing array: `maxDiff` is large but no good `nums[k]` to multiply.

---

## 🎯 Interview Takeaways
- Track multiple running aggregates (max element, max difference) in a single pass.
- The order of updates within the loop is critical to maintain index ordering constraints.
- Returning 0 when no positive triplet exists is handled naturally by initializing `ans = 0`.

---

## 📌 Key Pattern
👉 **"Single-pass with running max values to optimize ordered triplet problems"**

---

## 🔁 Related Problems
- 2874. Maximum Value of an Ordered Triplet II
- 121. Best Time to Buy and Sell Stock
- 152. Maximum Product Subarray

---

## 🚀 Final Thoughts
This elegant O(n) solution avoids brute force by maintaining two running maximums. The key insight is that by the time we reach element `k`, we already know the best `(nums[i] - nums[j])` from all valid pairs before it.

---

✨ **Rule to remember:**
> For ordered triplet optimization, maintain running max values in the correct update order to ensure index constraints are respected.
