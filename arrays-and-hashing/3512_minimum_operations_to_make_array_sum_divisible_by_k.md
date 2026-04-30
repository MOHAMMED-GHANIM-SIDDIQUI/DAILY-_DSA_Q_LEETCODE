# 3512. Minimum Operations to Make Array Sum Divisible by K

## 🔗 Problem Link
https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Hash Map, Prefix Sum, Modular Arithmetic

---

## 🧩 Problem Summary
Given an array `nums` and an integer `p`, find the minimum length of a subarray to remove so that the sum of the remaining elements is divisible by `p`. If no such subarray exists, return -1. You cannot remove the entire array.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= p <= 10^9`

---

## 💭 Intuition
👉 If `sum(nums) % p == r`, we need to find the shortest subarray whose sum is congruent to `r mod p`. This is a classic **prefix sum + hash map** problem where we track prefix sums modulo p.

---

## ⚡ Approach — Prefix Sum Modulo with HashMap

### 🧠 Idea
- Compute `remainder = sum(nums) % p`. If 0, return 0.
- Use a running prefix sum mod p and a hash map storing the last index of each prefix mod value.
- For each index, compute the target prefix mod we need to have seen earlier.
- Track the minimum subarray length.

---

## 💻 Code

```python
class Solution:
  def minSubarray(self, nums: list[int], p: int) -> int:
    summ = sum(nums)
    remainder = summ % p
    if remainder == 0:
      return 0

    ans = len(nums)
    prefix = 0
    prefixToIndex = {0: -1}

    for i, num in enumerate(nums):
      prefix += num
      prefix %= p
      target = (prefix - remainder + p) % p
      if target in prefixToIndex:
        ans = min(ans, i - prefixToIndex[target])
      prefixToIndex[prefix] = i

    return -1 if ans == len(nums) else ans
```

---

## 🧠 Dry Run
### Input
```
nums = [3, 1, 4, 2], p = 6
```
### Steps
```
sum = 10, remainder = 10 % 6 = 4
prefixToIndex = {0: -1}

i=0: prefix=3, target=(3-4+6)%6=5, not found. map={0:-1, 3:0}
i=1: prefix=4, target=(4-4+6)%6=0, found at -1. ans=min(4, 1-(-1))=2. map={0:-1, 3:0, 4:1}
i=2: prefix=2, target=(2-4+6)%6=4, found at 1. ans=min(2, 2-1)=1. map={0:-1, 3:0, 4:1, 2:2}
i=3: prefix=4, target=0, found at -1. ans=min(1, 3-(-1))=1. map={0:-1, 3:0, 4:3, 2:2}

Result: 1 (remove subarray [4] at index 2)
```

---

## ⏱️ Time Complexity
```
O(n) — single pass with hash map lookups
```

## 💾 Space Complexity
```
O(n) — for the hash map storing prefix mod indices
```

---

## ⚠️ Edge Cases
- Sum already divisible by p → return 0
- No valid subarray exists → return -1
- Cannot remove entire array → check ans < len(nums)

---

## 🎯 Interview Takeaways
- "Find subarray with sum congruent to X mod p" is a classic prefix sum + hash map pattern.
- The target formula `(prefix - remainder + p) % p` handles negative modular arithmetic.
- Always initialize the hash map with `{0: -1}` to handle subarrays starting from index 0.

---

## 📌 Key Pattern
👉 **"Prefix sum modulo with hash map to find shortest subarray with a target remainder."**

---

## 🔁 Related Problems
- 974. Subarray Sums Divisible by K
- 523. Continuous Subarray Sum
- 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum

---

## 🚀 Final Thoughts
This is a beautiful application of the prefix sum technique extended with modular arithmetic. The key transformation is realizing that removing a subarray with sum % p == remainder makes the rest divisible by p.

---

✨ **Rule to remember:**
> To make a sum divisible by p by removing a subarray, find the shortest subarray with prefix sum congruent to (total sum % p) using a hash map.
