# 3651. Transforming a Grid to Binary with Minimum Cost

## 🔗 Problem Link
https://leetcode.com/problems/transforming-a-grid-to-binary-with-minimum-cost/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Simulation

---

## 🧩 Problem Summary
Given an array `nums` and a list of queries `[l, r, k, v]`, for each query multiply every k-th element in `nums[l..r]` by `v` (mod 10^9+7). After all queries, return the XOR of all elements.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `1 <= queries.length <= 10^5`
- `0 <= l <= r < n`
- `1 <= k <= n`
- `1 <= v <= 10^9`

---

## 💭 Intuition
👉 For the brute-force version, simply iterate through each query and apply the multiplication at every k-th index. Then XOR all final values.

---

## ⚡ Approach — Direct Simulation

### 🧠 Idea
- For each query `[l, r, k, v]`, iterate from index `l` to `r` with step `k`, multiplying each element by `v` modulo 10^9+7.
- After processing all queries, XOR all elements together.

---

## 💻 Code

```python
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
      for l , r , k , v in queries:
        for i in range(l,r+1,k):
          nums[i]=(nums[i] * v) % (10**9 + 7)
      ans = 0
      for val in nums:
        ans ^= val
      return ans
```

---

## 🧠 Dry Run
### Input
```
nums = [1, 2, 3, 4], queries = [[0, 3, 2, 5]]
```
### Steps
```
Query [0, 3, 2, 5]:
  i=0: nums[0] = (1 * 5) % MOD = 5
  i=2: nums[2] = (3 * 5) % MOD = 15

nums = [5, 2, 15, 4]
XOR: 5 ^ 2 ^ 15 ^ 4 = 0101 ^ 0010 ^ 1111 ^ 0100 = 1000 = 8

Result: 8
```

---

## ⏱️ Time Complexity
```
O(q * n/k) — for each query, iterate over at most n/k elements
```

## 💾 Space Complexity
```
O(1) — in-place modification
```

---

## ⚠️ Edge Cases
- k = 1 → every element in range is multiplied
- k = n → only one element per query
- v = 1 → no change
- Single element array
- Overflow handled by modular arithmetic

---

## 🎯 Interview Takeaways
- Brute-force simulation works when constraints allow it.
- Modular arithmetic must be applied at each step to prevent overflow.
- XOR is its own inverse — useful for aggregation problems.

---

## 📌 Key Pattern
👉 **"Apply range updates with stride k, then aggregate with XOR — simulate directly for small inputs."**

---

## 🔁 Related Problems
- 3653. Find the Count of Good Integers (optimized version)
- 370. Range Addition
- 1109. Corporate Flight Bookings

---

## 🚀 Final Thoughts
This brute-force approach is straightforward but doesn't scale for large inputs. The optimized version (3653) uses sqrt decomposition to handle small and large strides differently.

---

✨ **Rule to remember:**
> "For stride-based range updates, brute force works for small inputs — optimize with sqrt decomposition for large ones."
