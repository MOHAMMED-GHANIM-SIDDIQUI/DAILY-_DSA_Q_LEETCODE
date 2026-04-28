# 3637. Count Number of Balanced Permutations

## 🔗 Problem Link
https://leetcode.com/problems/count-number-of-balanced-permutations/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Greedy, Pattern Recognition

---

## 🧩 Problem Summary
Given an array `nums`, determine if it forms a "trionic" pattern (strictly increasing, then strictly decreasing, then strictly increasing — exactly 2 direction changes, starting with increase). A secondary function finds the maximum sum trionic subsequence.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## 💭 Intuition
👉 A trionic pattern has exactly 2 sign changes in consecutive differences, and must start increasing. Detect peaks and valleys to identify the inc-dec-inc pattern, then use prefix sums for efficient sum computation.

---

## ⚡ Approach — Peak/Valley Detection with Prefix Sums

### 🧠 Idea
- For `isTrionic`: count sign changes in consecutive differences; must equal exactly 2 and start positive. Array must have at least 4 elements.
- For `maxSumTrionic`: scan for inc-dec-inc patterns using greedy peak/valley detection, compute core sums with prefix arrays, and extend left/right greedily.

---

## 💻 Code

```python
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:
            return False

        count = 0
        prev_diff = nums[1] - nums[0]

        if prev_diff <= 0:
            return False  # must start increasing

        for i in range(1, n - 1):
            cur_diff = nums[i + 1] - nums[i]
            if cur_diff == 0:
                return False

            if prev_diff * cur_diff < 0:
                count += 1

            prev_diff = cur_diff

        return count == 2
```

```python
class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        ans = float("-inf")
        i = 0

        while i < n - 2:
            j = i + 1

            # inc
            while j < n and nums[j] > nums[j - 1]:
                j += 1
            p = j - 1
            if p == i:
                i += 1
                continue

            # dec
            while j < n and nums[j] < nums[j - 1]:
                j += 1
            q = j - 1
            if q == p:
                i += 1
                continue

            # inc
            while j < n and nums[j] > nums[j - 1]:
                j += 1
            r = j - 1
            if r == q:
                i += 1
                continue

            # core sum O(1)
            core_sum = pref[q + 1] - pref[p]

            # left max (only once per i → amortized O(n))
            max_left = 0
            cur = 0
            k = p - 1
            while k >= i:
                cur += nums[k]
                max_left = max(max_left, cur)
                k -= 1

            # right max (only once per i → amortized O(n))
            max_right = 0
            cur = 0
            k = q + 1
            while k <= r:
                cur += nums[k]
                max_right = max(max_right, cur)
                k += 1

            ans = max(ans, core_sum + max_left + max_right)

            # CRUCIAL: skip entire valley
            i = q

        return ans if ans != float("-inf") else -1
```

---

## 🧠 Dry Run
### Input
```
nums = [1, 3, 2, 4]
```
### Steps
```
isTrionic check:
  n=4, diffs: [2, -1, 2]
  prev_diff=2 (>0, starts increasing)
  i=1: cur_diff=-1, sign change → count=1
  i=2: cur_diff=2, sign change → count=2
  count==2 → True (inc: 1→3, dec: 3→2, inc: 2→4)

maxSumTrionic:
  pref = [0, 1, 4, 6, 10]
  i=0: inc to p=1 (3), dec to q=2 (2), inc to r=3 (4)
  core_sum = pref[3]-pref[1] = 6-1 = 5
  max_left: nums[0]=1 → 1
  max_right: nums[3]=4 → 4
  ans = 5 + 1 + 4 = 10

Result: 10
```

---

## ⏱️ Time Complexity
```
O(n) — single pass with amortized O(n) for left/right extension
```

## 💾 Space Complexity
```
O(n) — for the prefix sum array
```

---

## ⚠️ Edge Cases
- Array too short (< 4 elements) → cannot be trionic
- No trionic pattern exists → return -1
- All elements strictly increasing or decreasing → not trionic
- Flat segments (equal consecutive elements) → not trionic

---

## 🎯 Interview Takeaways
- Pattern detection via sign changes in differences is a powerful technique.
- Prefix sums enable O(1) range sum queries.
- Skipping to the valley index (`i = q`) is crucial for amortized O(n) complexity.

---

## 📌 Key Pattern
👉 **"Detect inc-dec-inc pattern via sign changes, use prefix sums for O(1) range sums, skip valleys for amortized linear time."**

---

## 🔁 Related Problems
- 941. Valid Mountain Array
- 845. Longest Mountain in Array
- 1095. Find in Mountain Array

---

## 🚀 Final Thoughts
The trionic pattern is a natural extension of the mountain (bitonic) pattern. The key optimization is the valley-skipping technique that ensures each element is processed a constant number of times, keeping the overall complexity linear.

---

✨ **Rule to remember:**
> "Count sign changes for pattern detection, use prefix sums for range queries, and skip processed regions for linear time."
