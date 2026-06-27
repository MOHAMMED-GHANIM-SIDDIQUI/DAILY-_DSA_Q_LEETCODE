# 3737. Count Subarrays With Majority Element I

## 🔗 Problem Link
https://leetcode.com/problems/count-subarrays-with-majority-element-i/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Hash Table, Counting

---

## 🧩 Problem Summary

Given an array `nums` and a value `target`, count the number of subarrays in which `target` is a strict majority element — meaning it appears strictly more than half the length of that subarray. Return the total count of such subarrays.

### 📌 Constraints
- `1 <= nums.length <= 2000`
- `1 <= nums[i] <= 10^9`
- `1 <= target <= 10^9`

---

## 💭 Intuition

👉 For a subarray of length `L`, `target` is a strict majority when its count `> L // 2`. Fix the left endpoint, extend the right endpoint one element at a time while maintaining the running count of `target`, and check the majority condition at every step.

---

## ⚡ Approach — Brute Force Double Loop

### 🧠 Idea
- Outer loop fixes left index `i`.
- Reset `cnt_target = 0` for each new `i`.
- Inner loop extends right index `j` from `i` to `n-1`:
  - If `nums[j] == target`, increment `cnt_target`.
  - The current subarray length is `j - i + 1`; if `cnt_target > (j - i + 1) // 2`, the subarray qualifies → increment `ans`.
- Return `ans` after all pairs are examined.

---

## 💻 Code

```python
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            cnt_target = 0
            for j in range(i,n):
                if nums[j] == target:
                    cnt_target +=1
                if cnt_target > (j-i+1)//2:
                    ans+=1
        return ans
```

---

## 🧠 Dry Run

### Input
```
nums = [1, 2, 1], target = 1
```

### Steps
```
i=0, cnt=0
  j=0 nums[0]=1 -> cnt=1, len=1, 1 > 0 -> ans=1
  j=1 nums[1]=2 -> cnt=1, len=2, 1 > 1? no
  j=2 nums[2]=1 -> cnt=2, len=3, 2 > 1 -> ans=2
i=1, cnt=0
  j=1 nums[1]=2 -> cnt=0, len=1, 0 > 0? no
  j=2 nums[2]=1 -> cnt=1, len=2, 1 > 1? no
i=2, cnt=0
  j=2 nums[2]=1 -> cnt=1, len=1, 1 > 0 -> ans=3
return 3
```

---

## ⏱️ Time Complexity
```
O(n^2)
```
Every pair of start/end indices is examined once.

---

## 💾 Space Complexity
```
O(1)
```
Only a running counter and the answer are stored.

---

## ⚠️ Edge Cases
- `target` not present at all → no subarray qualifies, answer is 0.
- Every element equals `target` → all `n*(n+1)/2` subarrays qualify.
- Single-element array equal to target → counts as 1 (1 > 0).

---

## 🎯 Interview Takeaways
- Strict majority means `count > length // 2`; the integer division handles both odd and even lengths correctly.
- Extending one element at a time lets you keep the count incrementally instead of recomputing.
- This O(n^2) approach is fine for the "I" version (n ≤ 2000); a harder variant would need a prefix-sum/+1-−1 transform trick.

---

## 📌 Key Pattern
👉 **"Fix-left, extend-right with incremental count"**

---

## 🔁 Related Problems
- 0169 - Majority Element
- 2845 - Count of Interesting Subarrays
- 0560 - Subarray Sum Equals K

---

## 🚀 Final Thoughts
A clean brute-force counting exercise where the key is maintaining the target count as the window grows and applying the strict-majority test `cnt > L // 2` at each step.

---

✨ **Rule to remember:**
> "For majority subarrays, fix the left end, grow the right end, and keep a running count to test `cnt > length // 2`."
