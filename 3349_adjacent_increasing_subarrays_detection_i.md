# 3349. Adjacent Increasing Subarrays Detection I

## 🔗 Problem Link
https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array

---

## 🧩 Problem Summary
Given an array `nums` and an integer `k`, determine if there exist two adjacent strictly increasing subarrays, each of length at least `k`. The two subarrays must be contiguous (the second starts right after the first ends).

### 📌 Constraints
- `2 <= nums.length <= 100`
- `1 <= k <= nums.length / 2`
- `-10^8 <= nums[i] <= 10^8`

---

## 💭 Intuition
👉 Track the current and previous increasing run lengths. Two adjacent increasing subarrays of length `k` exist if: (1) a single run has length >= 2k (split in half), or (2) the previous run and current run are both >= k.

---

## ⚡ Approach — Track Current and Previous Increasing Runs

### 🧠 Idea
- Maintain `increasing` (current run length) and `prevIncreasing` (previous run length).
- When the increasing streak breaks, save the current as previous and reset.
- Check if `increasing / 2 >= k` or `min(prevIncreasing, increasing) >= k`.

---

## 💻 Code

```cpp
class Solution {
 public:
  bool hasIncreasingSubarrays(vector<int>& nums, int k) {
    int increasing = 1;
    int prevIncreasing = 0;

    for (int i = 1; i < nums.size(); ++i) {
      if (nums[i] > nums[i - 1]) {
        ++increasing;
      } else {
        prevIncreasing = increasing;
        increasing = 1;
      }
      if (increasing / 2 >= k || min(prevIncreasing, increasing) >= k)
        return true;
    }

    return false;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [2, 5, 7, 8, 9, 2, 3, 4, 3, 1], k = 3
```
### Steps
```
i=1: 5>2 → increasing=2
i=2: 7>5 → increasing=3
i=3: 8>7 → increasing=4, 4/2=2 < 3
i=4: 9>8 → increasing=5, 5/2=2 < 3
i=5: 2<9 → prev=5, increasing=1
i=6: 3>2 → increasing=2
i=7: 4>3 → increasing=3, min(5,3)=3 >= 3 → return true
```

---

## ⏱️ Time Complexity
```
O(n) — single pass
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- `k = 1` → any two adjacent elements where a decrease happens between two increasing pairs
- Entire array is strictly increasing → check if length >= 2k
- Alternating increase/decrease → depends on run lengths

---

## 🎯 Interview Takeaways
- Tracking current and previous run lengths is a common pattern for "adjacent subarray" problems.
- Splitting a single long run into two halves is an easy-to-miss case.

---

## 📌 Key Pattern
👉 **"Track current and previous run lengths for adjacent subarray detection"**

---

## 🔁 Related Problems
- 3350. Adjacent Increasing Subarrays Detection II
- 674. Longest Continuous Increasing Subsequence

---

## 🚀 Final Thoughts
A clean O(n) solution that checks both possible configurations: two separate adjacent runs and one long run split in half. The `min(prev, curr) >= k` check elegantly handles the boundary.

---

✨ **Rule to remember:**
> "For adjacent increasing subarrays, track two consecutive run lengths and check both split and combined cases."
