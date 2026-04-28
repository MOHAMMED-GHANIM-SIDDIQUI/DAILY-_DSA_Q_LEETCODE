# 3423. Maximum Difference Between Adjacent Elements in a Circular Array

## 🔗 Problem Link
https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array

---

## 🧩 Problem Summary
Given a circular array of integers, find the maximum absolute difference between any two adjacent elements. In a circular array, the first and last elements are also considered adjacent.

### 📌 Constraints
- 2 <= nums.length <= 100
- -100 <= nums[i] <= 100

---

## 💭 Intuition
👉 Simply iterate through all adjacent pairs (including the wrap-around pair of last and first elements) and track the maximum absolute difference.

---

## ⚡ Approach — Linear Scan

### 🧠 Idea
- Iterate through the array.
- For each index i, compute |nums[i] - nums[i+1]|.
- For the last element, compute |nums[n-1] - nums[0]|.
- Return the maximum value found.

---

## 💻 Code

```cpp
class Solution {
public:
    int maxAdjacentDistance(vector<int>& nums) {
        int n=nums.size();
        int ans=INT_MIN;
        for( int i=0;i<n;i++)
        {
            if (i==n-1)
                ans=max(ans,abs(nums[n-1]-nums[0]));
            else
                ans=max(ans,abs(nums[i]-nums[i+1]));
        }

        return ans;
    }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [1, 5, 2, 8]
```
### Steps
```
i=0: |1-5| = 4, ans=4
i=1: |5-2| = 3, ans=4
i=2: |2-8| = 6, ans=6
i=3: |8-1| = 7, ans=7 (circular wrap-around)

Result: 7
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
- Array of 2 elements → only one pair (same pair for both directions)
- All elements identical → answer is 0
- Maximum difference is at the circular boundary (last-first)

---

## 🎯 Interview Takeaways
- Circular arrays require handling the wrap-around case (last to first element).
- Using modular indexing (i+1) % n is an alternative to the if-else approach.
- Always use absolute difference when the problem asks for "difference."

---

## 📌 Key Pattern
👉 **"Circular array traversal with wrap-around comparison"**

---

## 🔁 Related Problems
- 918. Maximum Sum Circular Subarray
- 503. Next Greater Element II

---

## 🚀 Final Thoughts
A simple warm-up problem that tests understanding of circular array indexing. The key is not forgetting the wrap-around pair between the last and first elements.

---

✨ **Rule to remember:**
> In circular arrays, always handle the wrap-around: compare the last element with the first.
