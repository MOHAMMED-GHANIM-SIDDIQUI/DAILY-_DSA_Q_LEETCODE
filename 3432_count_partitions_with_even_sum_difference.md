# 3432. Count Partitions with Even Sum Difference

## 🔗 Problem Link
https://leetcode.com/problems/count-partitions-with-even-sum-difference/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Prefix Sum, Math

---

## 🧩 Problem Summary
Given an integer array, count the number of partitions into two non-empty contiguous parts (left and right) such that the difference between the left sum and right sum is even.

### 📌 Constraints
- 2 <= nums.length <= 100
- 1 <= nums[i] <= 100

---

## 💭 Intuition
👉 The difference (left_sum - right_sum) is even if and only if both sums have the same parity, which happens when total_sum is even. But since the difference depends on the partition point, we check each split.

---

## ⚡ Approach — Prefix Sum

### 🧠 Idea
- Compute total sum.
- Iterate through possible partition points (i from 0 to n-2).
- Maintain running left_sum; right_sum = total - left_sum.
- Check if (left_sum - right_sum) % 2 == 0.
- Count valid partitions.

---

## 💻 Code

```cpp
class Solution {
public:
    int countPartitions(vector<int>& nums) {
          int sum=accumulate(nums.begin(),nums.end(),0);
          int left_sum=0;
          int n=nums.size();
          int ans=0;
          for(int i=0;i<n-1;i++)
          {
            left_sum+=nums[i];
            int right_sum=sum-left_sum;
            if( (left_sum- right_sum) % 2 ==0)
                ans+=1;
          }
          return ans;
    }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [1, 2, 3, 4]
```
### Steps
```
sum = 10

i=0: left=1, right=9, diff=1-9=-8, -8%2==0 → ans=1
i=1: left=3, right=7, diff=3-7=-4, -4%2==0 → ans=2
i=2: left=6, right=4, diff=6-4=2, 2%2==0 → ans=3

Result: 3
```

---

## ⏱️ Time Complexity
```
O(n) — single pass after computing total sum
```

## 💾 Space Complexity
```
O(1) — constant extra space
```

---

## ⚠️ Edge Cases
- Array of 2 elements → only one partition
- All elements have the same parity → all partitions may be valid
- Total sum is odd → left_sum - right_sum = 2*left_sum - total_sum, even iff total_sum is even (which it isn't), so it depends on left_sum parity

---

## 🎯 Interview Takeaways
- (a - b) is even iff a and b have the same parity, iff (a + b) is even.
- Since a + b = total_sum, all partitions are valid when total_sum is even, and none when odd.
- The prefix-sum approach works generally even without this mathematical shortcut.

---

## 📌 Key Pattern
👉 **"Prefix sum with parity check for partition problems"**

---

## 🔁 Related Problems
- 2270. Number of Ways to Split Array
- 1013. Partition Array Into Three Parts With Equal Sum

---

## 🚀 Final Thoughts
A straightforward prefix-sum problem. The mathematical insight that the answer is either n-1 (total sum even) or 0 (total sum odd) can simplify the code, but the iterative approach is more intuitive.

---

✨ **Rule to remember:**
> Left-right sum difference is even iff total sum is even — all partition points work or none do.
