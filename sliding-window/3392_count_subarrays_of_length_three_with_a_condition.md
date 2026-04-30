# 3392. Count Subarrays of Length Three With a Condition

## 🔗 Problem Link
https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Sliding Window

---

## 🧩 Problem Summary
Given an integer array, count the number of subarrays of length 3 where the middle element is exactly half the sum of the first and last elements. In other words, nums[i] == 2 * (nums[i-1] + nums[i+1]).

### 📌 Constraints
- 3 <= nums.length <= 100
- 1 <= nums[i] <= 1000

---

## 💭 Intuition
👉 Simply iterate through each triplet and check if the middle element equals twice the sum of its neighbors. The condition `nums[i] == (nums[i-1] + nums[i+1]) * 2` is checked directly.

---

## ⚡ Approach — Linear Scan

### 🧠 Idea
- Iterate i from 1 to n-2.
- For each i, check if nums[i] == (nums[i-1] + nums[i+1]) * 2.
- Increment counter if condition holds.

---

## 💻 Code

```cpp
class Solution {
 public:
  int countSubarrays(vector<int>& nums) {
    int ans = 0;

    for (int i = 1; i + 1 < nums.size(); ++i)
      if (nums[i] == (nums[i - 1] + nums[i + 1]) * 2)
        ++ans;

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [1, 4, 2, 1, 8]
```
### Steps
```
i=1: nums[1]=4, (nums[0]+nums[2])*2 = (1+2)*2 = 6 → 4 != 6 → skip
i=2: nums[2]=2, (nums[1]+nums[3])*2 = (4+1)*2 = 10 → 2 != 10 → skip
i=3: nums[3]=1, (nums[2]+nums[4])*2 = (2+8)*2 = 20 → 1 != 20 → skip
Result: 0
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
- Array of exactly 3 elements → only one triplet to check
- No triplet satisfies the condition → return 0
- All triplets satisfy the condition

---

## 🎯 Interview Takeaways
- Fixed-length subarray problems often reduce to a simple linear scan.
- Always verify the mathematical condition carefully (multiplication vs division to avoid floating-point issues).

---

## 📌 Key Pattern
👉 **"Fixed-size sliding window with arithmetic condition"**

---

## 🔁 Related Problems
- 1550. Three Consecutive Odds
- 2760. Longest Even Odd Subarray With Threshold

---

## 🚀 Final Thoughts
A straightforward problem that tests basic array traversal and condition checking. The key is correctly interpreting the arithmetic relationship between the three elements.

---

✨ **Rule to remember:**
> For fixed-length subarray conditions, a single linear scan with direct condition checking is always sufficient.
