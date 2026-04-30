# 3350. Adjacent Increasing Subarrays Detection II

## 🔗 Problem Link
https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Binary Search

---

## 🧩 Problem Summary
Given an array `nums`, find the maximum value of `k` such that there exist two adjacent strictly increasing subarrays, each of length at least `k`. This is the optimization version of problem 3349.

### 📌 Constraints
- `2 <= nums.length <= 2 * 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## 💭 Intuition
👉 Same logic as 3349, but instead of checking a fixed `k`, maximize `k` across all positions. At each position, `k` can be `increasing / 2` (split a single run) or `min(prevIncreasing, increasing)` (two adjacent runs).

---

## ⚡ Approach — Maximize Over Current and Previous Run Lengths

### 🧠 Idea
- Track `increasing` and `prevIncreasing` as in 3349.
- At each position, update `ans = max(ans, increasing / 2, min(prevIncreasing, increasing))`.

---

## 💻 Code

```cpp
class Solution {
 public:
  // Similar to 3349. Adjacent Increasing Subarrays Detection I
  int maxIncreasingSubarrays(vector<int>& nums) {
    int ans = 0;
    int increasing = 1;
    int prevIncreasing = 0;

    for (int i = 1; i < nums.size(); ++i) {
      if (nums[i] > nums[i - 1]) {
        ++increasing;
      } else {
        prevIncreasing = increasing;
        increasing = 1;
      }
      ans = max(ans, increasing / 2);
      ans = max(ans, min(prevIncreasing, increasing));
    }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [2, 5, 7, 8, 9, 2, 3, 4, 3, 1]
```
### Steps
```
i=1: increasing=2, ans=max(0, 1, min(0,2))=1
i=2: increasing=3, ans=max(1, 1, 0)=1
i=3: increasing=4, ans=max(1, 2, 0)=2
i=4: increasing=5, ans=max(2, 2, 0)=2
i=5: prev=5, increasing=1, ans=max(2, 0, min(5,1))=2
i=6: increasing=2, ans=max(2, 1, min(5,2))=2
i=7: increasing=3, ans=max(2, 1, min(5,3))=3
i=8: prev=3, increasing=1, ans=max(3, 0, min(3,1))=3
i=9: prev=1, increasing=1, ans=3
Result: 3
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
- All elements are strictly increasing → answer is `n / 2`
- All elements are the same → answer is 0
- Length 2 → answer is 0 or 1

---

## 🎯 Interview Takeaways
- Converting a decision problem (3349) to an optimization problem often just requires replacing the check with a max.
- The two-run-length tracking pattern is versatile.

---

## 📌 Key Pattern
👉 **"Maximize adjacent run-based metric using current and previous run lengths"**

---

## 🔁 Related Problems
- 3349. Adjacent Increasing Subarrays Detection I
- 674. Longest Continuous Increasing Subsequence

---

## 🚀 Final Thoughts
A direct optimization of the detection version. The O(n) single-pass approach makes it efficient even for large inputs. The key is recognizing that only two consecutive runs matter at any point.

---

✨ **Rule to remember:**
> "To maximize adjacent increasing subarray length, track two consecutive runs and take the best of split and pair."
