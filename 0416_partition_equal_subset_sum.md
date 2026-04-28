# 416. Partition Equal Subset Sum

## 🔗 Problem Link
https://leetcode.com/problems/partition-equal-subset-sum/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Dynamic Programming

---

## 🧩 Problem Summary
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of elements in both subsets is equal. This reduces to finding a subset with sum equal to totalSum / 2.

### 📌 Constraints
- `1 <= nums.length <= 200`
- `1 <= nums[i] <= 100`

---

## 💭 Intuition
👉 If the total sum is odd, partitioning is impossible. Otherwise, the problem reduces to the classic 0/1 knapsack: can we find a subset summing to totalSum / 2?

---

## ⚡ Approach — 1D DP (0/1 Knapsack)

### 🧠 Idea
- Compute total sum. If odd, return false immediately.
- Create a boolean DP array of size `targetSum + 1` where `dp[i]` indicates if sum `i` is achievable.
- Initialize `dp[0] = true` (empty subset has sum 0).
- For each number, iterate backwards from targetSum down to num, updating `dp[i] = dp[i] || dp[i - num]`.
- Return `dp[targetSum]`.

---

## 💻 Code

```cpp
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int totalSum = accumulate(nums.begin(), nums.end(), 0);
        // If the sum is odd, partition is not possible
        if (totalSum % 2 != 0) {
            return false;
        }
        // Check if it's possible to form a subset with sum totalSum / 2
        return canFormSubset(nums, totalSum / 2);
    }

private:
    bool canFormSubset(const vector<int>& nums, int targetSum) {
        vector<bool> dp(targetSum + 1, false);
        dp[0] = true;  // Base case: sum 0 is always possible (empty subset)

        for (int num : nums) {
            for (int i = targetSum; i >= num; --i) {
                dp[i] = dp[i] || dp[i - num];
            }
        }

        return dp[targetSum];
    }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [1, 5, 11, 5]
```
### Steps
```
totalSum = 22, targetSum = 11
dp = [T,F,F,F,F,F,F,F,F,F,F,F]

num=1: dp = [T,T,F,F,F,F,F,F,F,F,F,F]
num=5: dp = [T,T,F,F,F,T,T,F,F,F,F,F]
num=11: dp = [T,T,F,F,F,T,T,F,F,F,F,T]
num=5: dp = [T,T,F,F,F,T,T,F,F,F,T,T]

dp[11] = true => return true
```

---

## ⏱️ Time Complexity
```
O(n * target) where target = totalSum / 2
```

## 💾 Space Complexity
```
O(target) — 1D DP array
```

---

## ⚠️ Edge Cases
- Odd total sum — immediately return false.
- Single element — cannot partition.
- All elements equal — partition possible only if count is even.
- One element equals half the sum — immediately true.

---

## 🎯 Interview Takeaways
- Recognizing the reduction to subset sum / 0-1 knapsack is the key insight.
- Iterating backwards prevents using the same element twice (0/1 constraint).
- The 1D DP optimization saves space compared to the 2D version.

---

## 📌 Key Pattern
👉 **"Equal partition = subset sum for half the total — classic 0/1 knapsack"**

---

## 🔁 Related Problems
- 494. Target Sum
- 474. Ones and Zeroes
- 698. Partition to K Equal Sum Subsets

---

## 🚀 Final Thoughts
This is the quintessential subset sum / 0-1 knapsack problem. The critical insight is the reduction from partition to subset sum, and the backward iteration to maintain the 0/1 constraint in 1D DP.

---

✨ **Rule to remember:**
> "Equal partition? Find a subset summing to half — iterate backwards for 0/1 knapsack."
