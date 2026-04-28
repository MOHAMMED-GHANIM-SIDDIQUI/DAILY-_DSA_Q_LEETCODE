# 3761. Maximum and Minimum Sums of At Most Size K Subsequences

## 🔗 Problem Link
https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Hash Table, String Reversal

---

## 🧩 Problem Summary
Given an array `nums`, find the minimum distance between two indices `i` and `j` such that the reverse of `nums[i]` equals `nums[j]`. For each element, reverse its digits and store the current index. When later encountering a value that matches a previously stored reversed value, compute the distance and track the minimum.

### 📌 Constraints
- `1 <= len(nums) <= 10^5`
- `1 <= nums[i] <= 10^9`

---

## 💭 Intuition
👉 For each number, its reverse (as an integer) is a potential "mirror partner." If we've seen a value before that is the reverse of the current number, the distance between their indices is a candidate answer. Store each number's reverse mapped to its index as we scan left to right.

---

## ⚡ Approach — Single Pass with Reverse Lookup

### 🧠 Idea
- Maintain a dictionary `tracker` mapping values to the most recent index where their reverse was seen.
- For each element `nums[i]`, check if `nums[i]` exists as a key in `tracker` (meaning some earlier element's reverse equals `nums[i]`).
- If found, compute the distance `|tracker[nums[i]] - i|` and update the minimum.
- Then compute `rev = reverse(nums[i])` and store `tracker[rev] = i`.

---

## 💻 Code

```python
class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
      tracker = {}
      min_dist = float('inf')
      for idx , val in enumerate(nums):
        if val in tracker:
          cur_dist = abs(tracker[val] - idx )
          min_dist = min(min_dist , cur_dist)
        rev = int(str(val)[::-1])
        tracker[rev] = idx
      return min_dist if min_dist != float('inf') else -1
```

---

## 🧠 Dry Run
### Input
```
nums = [13, 31, 12]
```
### Steps
```
tracker = {}

idx=0, val=13:
  13 not in tracker → skip
  rev = int("31") = 31
  tracker = {31: 0}

idx=1, val=31:
  31 in tracker → cur_dist = |0 - 1| = 1
  min_dist = 1
  rev = int("13") = 13
  tracker = {31: 0, 13: 1}

idx=2, val=12:
  12 not in tracker → skip
  rev = int("21") = 21
  tracker = {31: 0, 13: 1, 21: 2}

Result: 1
```

---

## ⏱️ Time Complexity
```
O(n * d) — where d is the average number of digits (for string reversal), effectively O(n) since d <= 10
```

## 💾 Space Complexity
```
O(n) — for the tracker dictionary
```

---

## ⚠️ Edge Cases
- Numbers that are palindromes (e.g., 121) → their reverse equals themselves, so `val` would be in `tracker` if seen before
- Numbers with trailing zeros (e.g., 100 reversed is 1) → handled by `int()` stripping leading zeros
- No mirror pair exists → return `-1`
- Single element array → return `-1`

---

## 🎯 Interview Takeaways
- Reversing a number via `int(str(val)[::-1])` is concise and handles leading zeros automatically.
- Storing the reverse as the key (not the original value) lets us check future values in O(1).
- The single-pass approach is optimal — no need to compare all pairs.

---

## 📌 Key Pattern
👉 **"Store the reverse of each number mapped to its index — when a future value matches a stored reverse, you've found a mirror pair."**

---

## 🔁 Related Problems
- 1. Two Sum
- 2395. Find Subarrays With Equal Sum
- 2815. Max Pair Sum in an Array

---

## 🚀 Final Thoughts
This problem is a clever twist on the classic Two Sum pattern. Instead of looking for `target - val`, we look for `reverse(val)`. The single-pass hash map approach keeps it efficient and clean. The key subtlety is that we store `reverse(val) → index` (not `val → index`), so future lookups find mirror matches naturally.

---

✨ **Rule to remember:**
> "Store the reverse, match the original — a single-pass hash map turns mirror-pair search into constant-time lookups."
