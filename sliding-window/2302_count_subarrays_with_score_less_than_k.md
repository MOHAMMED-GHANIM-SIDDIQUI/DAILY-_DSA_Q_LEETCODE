# 2302. Count Subarrays With Score Less Than K

## 🔗 Problem Link
https://leetcode.com/problems/count-subarrays-with-score-less-than-k/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Sliding Window, Prefix Sum, Binary Search

---

## 🧩 Problem Summary
The score of a subarray is defined as `sum(subarray) * length(subarray)`. Count the number of non-empty subarrays whose score is strictly less than `k`.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`
- `1 <= k <= 10^15`

---

## 💭 Intuition
👉 Use a sliding window: as we extend the right end, if the score becomes >= k, shrink from the left. All subarrays ending at `r` with left endpoints in `[l, r]` are valid.

---

## ⚡ Approach — Sliding Window

### 🧠 Idea
- Maintain a window `[l, r]` and running sum.
- For each `r`, add `nums[r]` to the sum.
- While `sum * (r - l + 1) >= k`, shrink from the left.
- Add `(r - l + 1)` to the answer (all valid subarrays ending at `r`).

---

## 💻 Code

```cpp
class Solution {
 public:
  long long countSubarrays(vector<int>& nums, long long k) {
    long ans = 0;
    long sum = 0;

    for (int l = 0, r = 0; r < nums.size(); ++r) {
      sum += nums[r];
      while (sum * (r - l + 1) >= k)
        sum -= nums[l++];
      ans += r - l + 1;
    }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [2, 1, 4, 3, 5], k = 10
```
### Steps
```
r=0: sum=2, score=2*1=2 < 10, ans+=1 → ans=1
r=1: sum=3, score=3*2=6 < 10, ans+=2 → ans=3
r=2: sum=7, score=7*3=21 >= 10 → shrink l=1, sum=5, score=5*2=10 >= 10 → shrink l=2, sum=4, score=4*1=4 < 10, ans+=1 → ans=4
r=3: sum=7, score=7*2=14 >= 10 → shrink l=3, sum=3, score=3*1=3 < 10, ans+=1 → ans=5
r=4: sum=8, score=8*2=16 >= 10 → shrink l=4, sum=5, score=5*1=5 < 10, ans+=1 → ans=6
Result: 6
```

---

## ⏱️ Time Complexity
```
O(n) — each element is added and removed from the window at most once
```

## 💾 Space Complexity
```
O(1) — constant extra space
```

---

## ⚠️ Edge Cases
- k = 1 → no subarray with sum * length < 1 (all nums >= 1), return 0
- All elements are 1 → many valid subarrays
- Single element >= k → that subarray is excluded

---

## 🎯 Interview Takeaways
- The score function `sum * length` is monotonically non-decreasing as the window expands — this justifies the sliding window.
- Counting valid subarrays ending at each `r` is `(r - l + 1)`.
- Sliding window achieves O(n) by amortized pointer movement.

---

## 📌 Key Pattern
👉 **"Sliding window for counting subarrays with a monotonic aggregate constraint"**

---

## 🔁 Related Problems
- 713. Subarray Product Less Than K
- 209. Minimum Size Subarray Sum
- 2261. K Divisible Elements Subarrays

---

## 🚀 Final Thoughts
The sliding window works because both sum and length increase when expanding, making the score monotonically non-decreasing. This property is essential for the correctness of the shrinking step.

---

✨ **Rule to remember:**
> "When the score (sum * length) is monotonic with window size, use sliding window to count valid subarrays in O(n)."
