# 2016. Maximum Difference Between Increasing Elements

## 🔗 Problem Link
https://leetcode.com/problems/maximum-difference-between-increasing-elements/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Greedy

---

## 🧩 Problem Summary
Given a 0-indexed integer array `nums` of size `n`, find the maximum difference between `nums[j] - nums[i]` such that `0 <= i < j < n` and `nums[i] < nums[j]`. Return `-1` if no such pair exists.

### 📌 Constraints
- `n == nums.length`
- `2 <= n <= 1000`
- `1 <= nums[i] <= 10^9`

---

## 💭 Intuition
👉 Track the minimum value seen so far while iterating. For each element, if it is greater than the current minimum, compute the difference and update the answer.

---

## ⚡ Approach — Single Pass with Running Minimum

### 🧠 Idea
- Initialize `minVal` to `nums[0]` and `maxDiff` to `-1`.
- Iterate from index 1 onward.
- If `nums[i] > minVal`, update `maxDiff` with `nums[i] - minVal`.
- Otherwise, update `minVal` to `nums[i]`.

---

## 💻 Code

```cpp
class Solution {
public:
    int maximumDifference(vector<int>& nums) {
        int minVal = nums[0];
        int maxDiff = -1;

        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] > minVal) {
                maxDiff = max(maxDiff, nums[i] - minVal);
            } else {
                minVal = nums[i];
            }
        }

        return maxDiff;
    }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [7, 1, 5, 4]
```
### Steps
```
i=0: minVal=7
i=1: nums[1]=1 <= 7, minVal=1
i=2: nums[2]=5 > 1, maxDiff = max(-1, 5-1) = 4
i=3: nums[3]=4 > 1, maxDiff = max(4, 4-1) = 4
Return 4
```

---

## ⏱️ Time Complexity
```
O(n), single pass through the array
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- Strictly decreasing array: return -1
- All elements equal: return -1
- Only two elements: return difference if increasing, else -1
- Maximum difference at the very end

---

## 🎯 Interview Takeaways
- This is the classic "best time to buy and sell stock" pattern.
- Tracking a running minimum allows O(1) space and O(n) time.
- Return -1 instead of 0 when no valid pair exists.

---

## 📌 Key Pattern
👉 **"Running minimum to find the maximum increasing difference"**

---

## 🔁 Related Problems
- 121. Best Time to Buy and Sell Stock
- 53. Maximum Subarray
- 2078. Two Furthest Houses With Different Colors

---

## 🚀 Final Thoughts
This is essentially the "Best Time to Buy and Sell Stock" problem with the twist of returning -1 when no strictly increasing pair exists. The single-pass running minimum approach is optimal.

---

✨ **Rule to remember:**
> Track the running minimum and compute the difference at each step -- the classic stock-buy pattern.
