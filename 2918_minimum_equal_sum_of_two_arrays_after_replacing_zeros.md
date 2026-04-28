# 2918. Minimum Equal Sum of Two Arrays After Replacing Zeros

## 🔗 Problem Link
https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Greedy, Math

---

## 🧩 Problem Summary
Given two arrays `nums1` and `nums2` containing non-negative integers, replace every 0 with a strictly positive integer so that the sums of both arrays become equal. Return the minimum equal sum, or -1 if impossible.

### 📌 Constraints
- 1 <= nums1.length, nums2.length <= 10^5
- 0 <= nums1[i], nums2[i] <= 10^6

---

## 💭 Intuition
👉 Each zero must be replaced by at least 1 (since replacements must be strictly positive). So the minimum possible sum for each array is `currentSum + countOfZeros`. If an array has no zeros, its sum is fixed. Equality is possible only if the fixed sum is not smaller than the other array's minimum.

---

## ⚡ Approach — Greedy with Zero Counting

### 🧠 Idea
- Compute the sum and count of zeros for each array.
- The minimum achievable sum for each array is `sum + zeros` (each zero replaced by 1).
- If an array has no zeros and its sum is less than the other array's minimum, return -1.
- Otherwise, the answer is `max(sum1 + zero1, sum2 + zero2)`.

---

## 💻 Code

```cpp
class Solution {
 public:
  long long minSum(vector<int>& nums1, vector<int>& nums2) {
    const long sum1 = accumulate(nums1.begin(), nums1.end(), 0L);
    const long sum2 = accumulate(nums2.begin(), nums2.end(), 0L);
    const int zero1 = ranges::count(nums1, 0);
    const int zero2 = ranges::count(nums2, 0);
    if (zero1 == 0 && sum1 < sum2 + zero2)
      return -1;
    if (zero2 == 0 && sum2 < sum1 + zero1)
      return -1;
    return max(sum1 + zero1, sum2 + zero2);
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums1 = [3, 2, 0, 1, 0], nums2 = [6, 5, 0]
```
### Steps
```
sum1 = 3+2+0+1+0 = 6, zero1 = 2 → min sum1 = 6+2 = 8
sum2 = 6+5+0 = 11, zero2 = 1 → min sum2 = 11+1 = 12

zero1 != 0, zero2 != 0 → no impossibility
ans = max(8, 12) = 12

To achieve 12: nums1 zeros replaced by values summing to 6 (e.g., 3+3)
               nums2 zero replaced by 1

Output: 12
```

---

## ⏱️ Time Complexity
```
O(n + m) — where n and m are the lengths of the two arrays
```

## 💾 Space Complexity
```
O(1) — constant extra space
```

---

## ⚠️ Edge Cases
- No zeros in either array: sums must already be equal, otherwise -1.
- No zeros in one array but its sum equals the other's minimum: valid.
- All elements are zero: both arrays flexible, answer is `max(len1, len2)`.

---

## 🎯 Interview Takeaways
- Zeros provide flexibility — each zero adds at least 1 to the sum but can add more.
- An array with no zeros has a fixed sum and cannot be adjusted.
- The minimum equal sum is determined by the array with the larger minimum achievable sum.

---

## 📌 Key Pattern
👉 **"Greedy lower bound — zeros give flexibility, fixed sums constrain"**

---

## 🔁 Related Problems
- 1775. Equal Sum Arrays With Minimum Number of Operations
- 2602. Minimum Operations to Make All Array Elements Equal
- 1551. Minimum Operations to Make Array Equal

---

## 🚀 Final Thoughts
The key insight is that zeros provide upward flexibility (minimum replacement is 1, but can be any positive integer). The bottleneck is the array whose minimum sum is larger — the other array must match it using its zeros. If an array has no zeros and falls short, it's impossible.

---

✨ **Rule to remember:**
> When replacing zeros with positive integers, the minimum sum is currentSum + zeroCount, and the answer is the max of both arrays' minimums.
