# 2874. Maximum Value of an Ordered Triplet II

## 🔗 Problem Link
https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Greedy

---

## 🧩 Problem Summary
Given a 0-indexed integer array `nums`, find the maximum value of `(nums[i] - nums[j]) * nums[k]` over all triplets `(i, j, k)` with `i < j < k`. This is the same as problem 2873 but with larger constraints requiring an efficient solution.

### 📌 Constraints
- 3 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^6

---

## 💭 Intuition
👉 Identical logic to problem 2873 — the O(n) single-pass approach handles the larger constraints naturally. Track the maximum element seen so far (`maxNum`) and the maximum difference (`maxDiff = maxNum - nums[j]`) to compute the answer in one sweep.

---

## ⚡ Approach — Single Pass with Running Max

### 🧠 Idea
- For each element `num` in the array:
  - Try it as `nums[k]`: update answer with `maxDiff * num`.
  - Try it as `nums[j]`: update `maxDiff` with `maxNum - num`.
  - Try it as `nums[i]`: update `maxNum` with `num`.
- This ensures O(n) time which handles 10^5 elements easily.

---

## 💻 Code

```cpp
class Solution {
 public:
  // Same as 2873. Maximum Value of an Ordered Triplet I
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
nums = [1, 10, 3, 4, 19]
```
### Steps
```
Initial: ans=0, maxDiff=0, maxNum=0

num=1:  ans=max(0, 0*1)=0,   maxDiff=max(0, 0-1)=0,   maxNum=1
num=10: ans=max(0, 0*10)=0,  maxDiff=max(0, 1-10)=0,   maxNum=10
num=3:  ans=max(0, 0*3)=0,   maxDiff=max(0, 10-3)=7,   maxNum=10
num=4:  ans=max(0, 7*4)=28,  maxDiff=max(7, 10-4)=7,   maxNum=10
num=19: ans=max(28, 7*19)=133, maxDiff=max(7, 10-19)=7, maxNum=19

Output: 133
```

---

## ⏱️ Time Complexity
```
O(n) — single pass through the array
```

## 💾 Space Complexity
```
O(1) — constant extra space
```

---

## ⚠️ Edge Cases
- Very large array (10^5 elements): handled efficiently in O(n).
- All elements identical: answer is 0.
- Maximum values at boundaries of the array.

---

## 🎯 Interview Takeaways
- Same algorithm works for both small and large constraints — a well-designed O(n) solution scales naturally.
- Always use `long` for intermediate products to avoid overflow.
- The update order within the loop enforces the `i < j < k` constraint implicitly.

---

## 📌 Key Pattern
👉 **"Single-pass greedy with running aggregates for ordered triplet problems"**

---

## 🔁 Related Problems
- 2873. Maximum Value of an Ordered Triplet I
- 121. Best Time to Buy and Sell Stock
- 42. Trapping Rain Water

---

## 🚀 Final Thoughts
This problem demonstrates that a clean O(n) approach designed for the easy version scales perfectly to harder constraints. The running max technique is a powerful pattern for problems involving ordered subsequences.

---

✨ **Rule to remember:**
> Design for efficiency from the start — an O(n) single-pass solution handles both small and large inputs without modification.
