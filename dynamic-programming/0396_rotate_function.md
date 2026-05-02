# 396. Rotate Function

## 🔗 Problem Link
https://leetcode.com/problems/rotate-function/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Math, Dynamic Programming

---

## 🧩 Problem Summary

You are given an integer array `nums` of length `n`. Define the rotation function `F(k)` on the array as:

```
F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1]
```

where `arrk` is the array `nums` rotated by `k` positions clockwise. Return the **maximum value** of `F(0), F(1), ..., F(n - 1)`.

### 📌 Constraints
- `n == nums.length`
- `1 <= n <= 10^5`
- `-100 <= nums[i] <= 100`

---

## 💭 Intuition

👉 The brute-force approach is to compute each `F(k)` from scratch in O(n), giving O(n²). That fails for `n = 10^5`. But if we look at how `F(k)` differs from `F(k - 1)`, every element except the one being wrapped around contributes one **extra** copy of itself to the new sum, while the element that wraps to the front loses its previously-large coefficient. That gives a clean O(1) transition between consecutive `F(k)` values — so we can compute all of them in O(n) total.

---

## ⚡ Approach — Rolling Sum Recurrence

### 🧠 Idea

- Let `S = sum(nums)` and `F(0) = Σ i * nums[i]`.
- When we rotate one step (clockwise), every index's coefficient effectively goes up by 1, **except** the element that moves from the back to the front, which drops from coefficient `n - 1` down to `0`.
- That gives the recurrence:
  ```
  F(k) = F(k - 1) + S - n * nums[n - k]
  ```
- Iterate `k = 1 .. n - 1`, maintain a running `prev` for `F(k - 1)`, and track the max.

---

## 💻 Code

```python
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
      prev = 0 
      n = len(nums)
      num_sum = sum(nums)
      for idx , val in enumerate(nums):
        prev+=(idx*val)
      ans = prev 

      for i in range(n-1 , 0 , -1):
        prev = prev + num_sum - (n ) * nums[i]
        ans = max(ans , prev)
      return ans
```

---

## 🧠 Dry Run

### Input
```
nums = [4, 3, 2, 6]   →   n = 4, num_sum = 15
```

### Steps
```
F(0) = 0*4 + 1*3 + 2*2 + 3*6 = 0 + 3 + 4 + 18 = 25
prev = 25, ans = 25

i = 3 (subtract n * nums[3] = 4*6 = 24):
  prev = 25 + 15 - 24 = 16   → F(1) = 16
  ans  = max(25, 16) = 25

i = 2 (subtract n * nums[2] = 4*2 = 8):
  prev = 16 + 15 - 8 = 23    → F(2) = 23
  ans  = max(25, 23) = 25

i = 1 (subtract n * nums[1] = 4*3 = 12):
  prev = 23 + 15 - 12 = 26   → F(3) = 26
  ans  = max(25, 26) = 26

return 26
```

---

## ⏱️ Time Complexity

```
O(n)
```

One pass to build `F(0)` and one pass for the recurrence.

---

## 💾 Space Complexity

```
O(1)
```

Only a handful of scalars (`prev`, `ans`, `num_sum`, `n`).

---

## ⚠️ Edge Cases

- **Single element:** `n = 1` → only `F(0) = 0`, the inner loop does not execute.
- **All zeros:** every `F(k) = 0` — the rolling update keeps `prev` at 0 throughout.
- **Negative values:** the recurrence is purely arithmetic, so negatives are handled naturally.
- **Large `n` (10^5):** O(n²) brute force times out; the O(n) recurrence is required.

---

## 🎯 Interview Takeaways

- When a problem asks for the max over many "shifted" versions of the same aggregate, look for a closed-form transition between consecutive shifts instead of recomputing.
- Deriving `F(k) - F(k - 1)` on paper is the whole trick — once written down, the O(n) loop falls out.
- Iterating `i` from `n - 1` down to `1` is just a way to feed the recurrence the element that wraps to the front at each rotation step.

---

## 📌 Key Pattern

👉 **"When successive answers differ by a constant-time delta, roll the previous answer forward instead of recomputing."**

---

## 🔁 Related Problems

- 198. House Robber
- 918. Maximum Sum Circular Subarray
- 1856. Maximum Subarray Min-Product
- 53. Maximum Subarray

---

## 🚀 Final Thoughts

Rotate Function is a tidy example of turning an O(n²) "try every rotation" idea into O(n) by writing down the algebraic delta between consecutive states. The recurrence `F(k) = F(k-1) + S - n * nums[n-k]` is worth committing to memory — the same "rolling delta" mindset shows up across array, prefix-sum, and DP problems.

---

✨ **Rule to remember:**
> "If two adjacent states share most of their work, compute the difference, not the whole thing."
