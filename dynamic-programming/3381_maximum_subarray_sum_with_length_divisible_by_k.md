# 3381. Maximum Subarray Sum With Length Divisible by K

## 🔗 Problem Link
https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Prefix Sum, Dynamic Programming

---

## 🧩 Problem Summary
Given an integer array nums and an integer k, find the maximum sum of a subarray whose length is divisible by k. A subarray is a contiguous non-empty sequence of elements.

### 📌 Constraints
- 1 <= k <= nums.length <= 2 * 10^5
- -10^9 <= nums[i] <= 10^9

---

## 💭 Intuition
👉 A subarray from index l+1 to r has length r-l, which is divisible by k iff l % k == r % k. So we track the minimum prefix sum for each remainder class modulo k.

---

## ⚡ Approach — Prefix Sum with Modular Tracking

### 🧠 Idea
- Compute a running prefix sum.
- Maintain an array `minPrefix[r]` storing the minimum prefix sum seen so far where the index mod k equals r.
- For each index i, the best subarray ending at i with length divisible by k is `prefix[i] - minPrefix[i % k]`.
- Initialize `minPrefix[k-1] = 0` (empty prefix before index 0 has remainder k-1 in 0-indexed terms).

---

## 💻 Code

```cpp
class Solution {
 public:
  long long maxSubarraySum(std::vector<int>& nums, int k) {
    long ans = LONG_MIN;
    long prefix = 0;
    // minPrefix[i % k] := the minimum prefix sum of the first i numbers
    vector<long> minPrefix(k, LONG_MAX / 2);
    minPrefix[k - 1] = 0;

    for (int i = 0; i < nums.size(); ++i) {
      prefix += nums[i];
      ans = max(ans, prefix - minPrefix[i % k]);
      minPrefix[i % k] = min(minPrefix[i % k], prefix);
    }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [1, 2, -1, 4, -2, 3], k = 3
```
### Steps
```
minPrefix = [INF, INF, 0]  (k-1 = 2 initialized to 0)

i=0: prefix=1,  i%3=0, ans=max(-INF, 1-INF)=-INF, minPrefix[0]=1
i=1: prefix=3,  i%3=1, ans=max(-INF, 3-INF)=-INF, minPrefix[1]=3
i=2: prefix=2,  i%3=2, ans=max(-INF, 2-0)=2,      minPrefix[2]=0
i=3: prefix=6,  i%3=0, ans=max(2, 6-1)=5,          minPrefix[0]=1
i=4: prefix=4,  i%3=1, ans=max(5, 4-3)=5,          minPrefix[1]=3
i=5: prefix=7,  i%3=2, ans=max(5, 7-0)=7,          minPrefix[2]=0

Result: 7 (subarray [1,2,-1,4,-2,3] of length 6)
```

---

## ⏱️ Time Complexity
```
O(n) — single pass through the array
```

## 💾 Space Complexity
```
O(k) — for the minPrefix array
```

---

## ⚠️ Edge Cases
- All negative numbers → must still pick a subarray of length divisible by k
- k = 1 → equivalent to maximum subarray sum (any length)
- k = n → only one valid subarray (the entire array)

---

## 🎯 Interview Takeaways
- Prefix sums combined with modular arithmetic elegantly handle "length divisible by k" constraints.
- Tracking minimum prefix per remainder class avoids O(n^2) enumeration.
- Initializing minPrefix[k-1] = 0 represents the empty prefix before the array starts.

---

## 📌 Key Pattern
👉 **"Prefix sum + modular grouping for divisibility constraints"**

---

## 🔁 Related Problems
- 53. Maximum Subarray
- 523. Continuous Subarray Sum
- 974. Subarray Sums Divisible by K

---

## 🚀 Final Thoughts
This is a beautiful extension of the classic maximum subarray problem. The key insight is that subarray length divisibility by k translates to matching prefix-sum indices modulo k.

---

✨ **Rule to remember:**
> Subarray length divisible by k means prefix indices share the same remainder mod k — track the minimum prefix per remainder.
