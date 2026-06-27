# 3689. Maximum Total Subarray Value I

## 🔗 Problem Link
https://leetcode.com/problems/maximum-total-subarray-value-i/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Math

---

## 🧩 Problem Summary

You are given an array `nums` and an integer `k`. You must choose exactly `k` subarrays (repetitions of the same subarray are allowed). The value of a subarray is `max(subarray) - min(subarray)`. Return the maximum possible total value summed over the `k` chosen subarrays.

### 📌 Constraints
- `1 <= nums.length <= 5 * 10^4`
- `1 <= nums[i] <= 10^9`
- `1 <= k <= 10^5`

---

## 💭 Intuition

👉 Because the same subarray may be reused, the single best subarray value is just the whole-array spread `max(nums) - min(nums)` (no subarray can exceed the global max-min). Pick that subarray all `k` times → answer is `(max - min) * k`.

---

## ⚡ Approach — Closed-Form Spread

### 🧠 Idea
- The value of any subarray is at most `globalMax - globalMin`, achieved by a subarray that contains both the global max and global min (the entire array always works).
- Since repeats are allowed, the optimal strategy is to choose this maximum-spread subarray `k` times.
- Return `(max(nums) - min(nums)) * k` directly.

---

## 💻 Code

```python
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return (max(nums) - min(nums))* k
```

---

## 🧠 Dry Run

### Input
```
nums = [1, 3, 2, 7, 4], k = 3
```

### Steps
```
max(nums) = 7
min(nums) = 1
spread    = 7 - 1 = 6
answer    = 6 * k = 6 * 3 = 18
return 18
```

---

## ⏱️ Time Complexity
```
O(n)
```
One pass each for `max` and `min` over the array.

---

## 💾 Space Complexity
```
O(1)
```
Only constant extra space is used.

---

## ⚠️ Edge Cases
- All elements equal → spread is 0, answer is 0 regardless of `k`.
- Single-element array → max equals min, spread 0, answer 0.
- Large `k` and large values → Python big integers handle the product safely.

---

## 🎯 Interview Takeaways
- "Repeats allowed" collapses the problem: just maximize one subarray's value and multiply.
- The maximum subarray spread equals the global max minus the global min.
- Recognizing this avoids any per-subarray enumeration.

---

## 📌 Key Pattern
👉 **"Reuse-allowed selection reduces to best-single × k"**

---

## 🔁 Related Problems
- 0053 - Maximum Subarray
- 0152 - Maximum Product Subarray
- 2272 - Substring With Largest Variance

---

## 🚀 Final Thoughts
A deceptively short problem: the insight that allowing repeats makes the global spread optimal turns it into a one-liner.

---

✨ **Rule to remember:**
> "When you may pick the same item repeatedly, find the single best option and multiply by the count."
