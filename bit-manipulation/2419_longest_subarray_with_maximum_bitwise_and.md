# 2419. Longest Subarray With Maximum Bitwise AND

## 🔗 Problem Link
https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Bit Manipulation, Brainteaser

---

## 🧩 Problem Summary
Given an integer array `nums`, find the length of the longest subarray where the bitwise AND equals the maximum possible AND value of any subarray.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^6`

---

## 💭 Intuition
👉 The AND of a subarray can only decrease or stay the same as the subarray grows. The maximum AND is simply the maximum element in the array. The answer is the longest consecutive run of that maximum element.

---

## ⚡ Approach — Find Max Element, Then Longest Run

### 🧠 Idea
- The maximum possible AND value is `max(nums)`, since AND can never exceed any individual element.
- Find the longest consecutive subarray where every element equals `max(nums)`.
- Track the current run length and the global maximum run length.

---

## 💻 Code

```cpp
class Solution {
 public:
  int longestSubarray(vector<int>& nums) {
    int ans = 0;
    int maxIndex = 0;
    int sameNumLength = 0;

    for (int i = 0; i < nums.size(); ++i)
      if (nums[i] == nums[maxIndex]) {
        ans = max(ans, ++sameNumLength);
      } else if (nums[i] > nums[maxIndex]) {
        maxIndex = i;
        sameNumLength = 1;
        ans = 1;
      } else {
        sameNumLength = 0;
      }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [1,2,3,3,2,2]
```
### Steps
```
i=0: nums[0]=1, maxIndex=0, sameNumLength=1, ans=1
i=1: nums[1]=2 > nums[0]=1 → maxIndex=1, sameNumLength=1, ans=1
i=2: nums[2]=3 > nums[1]=2 → maxIndex=2, sameNumLength=1, ans=1
i=3: nums[3]=3 == nums[2]=3 → sameNumLength=2, ans=2
i=4: nums[4]=2 < 3 → sameNumLength=0
i=5: nums[5]=2 < 3 → sameNumLength=0

Result: 2
```

---

## ⏱️ Time Complexity
```
O(n) — single pass through the array.
```

## 💾 Space Complexity
```
O(1) — only a few variables.
```

---

## ⚠️ Edge Cases
- All elements are the same: answer is n.
- Maximum element appears only once.
- Maximum element appears in multiple separate runs.

---

## 🎯 Interview Takeaways
- AND is monotonically non-increasing: adding elements can only turn off bits.
- The maximum AND of any subarray is always `max(nums)`.
- This reduces the problem to finding the longest consecutive run of the max element.

---

## 📌 Key Pattern
👉 **"AND is non-increasing — maximum AND equals the array maximum, find its longest run."**

---

## 🔁 Related Problems
- 485. Max Consecutive Ones
- 1446. Consecutive Characters
- 2401. Longest Nice Subarray

---

## 🚀 Final Thoughts
The key mathematical insight is that AND cannot exceed any individual element, so the maximum AND is `max(nums)`. This transforms a seemingly complex bitwise problem into a simple run-length counting exercise.

---

✨ **Rule to remember:**
> "AND only shrinks — the max AND is the max element, so find its longest streak."
