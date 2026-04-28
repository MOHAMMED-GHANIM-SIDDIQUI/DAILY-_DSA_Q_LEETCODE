# 3719. Count Connected Components in LCM Graph

## 🔗 Problem Link
https://leetcode.com/problems/count-connected-components-in-lcm-graph/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Hash Table, Brute Force, Set

---

## 🧩 Problem Summary
Given an array `nums`, find the length of the longest subarray where the number of distinct even values equals the number of distinct odd values. The solution enumerates all subarrays and tracks even and odd distinct value sets.

### 📌 Constraints
- `1 <= len(nums) <= 10^5`
- `1 <= nums[i] <= 10^9`

---

## 💭 Intuition
👉 A subarray is "balanced" when it has the same number of distinct even values as distinct odd values. Track two separate sets (even and odd) while expanding the window, and update the answer whenever their sizes match.

---

## ⚡ Approach — Brute Force with Two Sets

### 🧠 Idea
- Use two nested loops to enumerate all subarrays `[i..j]`.
- Maintain an `even_set` and `odd_set` for distinct values in the current window.
- For each new element `nums[j]`, add it to the appropriate set based on parity.
- If `len(even_set) == len(odd_set)`, update the answer with the current subarray length.

---

## 💻 Code

```python
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            even_set = set()
            odd_set = set()

            for j in range(i, n):
                if nums[j] % 2 == 0:
                    even_set.add(nums[j])
                else:
                    odd_set.add(nums[j])

                if len(even_set) == len(odd_set):
                    ans = max(ans, j - i + 1)

        return ans
```

---

## 🧠 Dry Run
### Input
```
nums = [1, 2, 3, 4]
```
### Steps
```
i=0:
  j=0: odd_set={1}, even_set={} → 1!=0 ✗
  j=1: odd_set={1}, even_set={2} → 1==1 ✓ → ans=2
  j=2: odd_set={1,3}, even_set={2} → 2!=1 ✗
  j=3: odd_set={1,3}, even_set={2,4} → 2==2 ✓ → ans=4

i=1:
  j=1: even_set={2}, odd_set={} → 1!=0 ✗
  j=2: even_set={2}, odd_set={3} → 1==1 ✓ → ans=4
  j=3: even_set={2,4}, odd_set={3} → 2!=1 ✗

i=2:
  j=2: odd_set={3}, even_set={} → 1!=0 ✗
  j=3: odd_set={3}, even_set={4} → 1==1 ✓ → ans=4

i=3:
  j=3: even_set={4}, odd_set={} → 1!=0 ✗

Result: 4
```

---

## ⏱️ Time Complexity
```
O(n^2) — two nested loops, set operations are O(1) amortized
```

## 💾 Space Complexity
```
O(n) — each set can hold up to n elements
```

---

## ⚠️ Edge Cases
- All elements are even → answer is 0 (no odd values to balance)
- All elements are odd → answer is 0 (no even values to balance)
- Alternating even/odd values → many balanced subarrays
- Array with duplicate values → sets handle deduplication

---

## 🎯 Interview Takeaways
- Using separate sets for even and odd values cleanly separates the counting logic.
- The "distinct count" requirement makes sets the natural data structure.
- This brute force is straightforward but O(n^2) — for larger inputs, a prefix-sum approach on the difference of distinct even/odd counts could optimize it.

---

## 📌 Key Pattern
👉 **"Track distinct even and odd values in two sets — balance means equal set sizes."**

---

## 🔁 Related Problems
- 525. Contiguous Array
- 2006. Count Number of Pairs With Absolute Difference K
- 1248. Count Number of Nice Subarrays

---

## 🚀 Final Thoughts
This brute force approach is clean and correct for smaller inputs. The use of two sets to track distinct even and odd values makes the balance condition trivial to check. For optimization, consider converting to a prefix-difference problem where the difference between cumulative distinct even and odd counts is tracked.

---

✨ **Rule to remember:**
> "When balancing two categories of distinct elements, use two sets and compare their sizes — simplicity beats complexity for correctness."
