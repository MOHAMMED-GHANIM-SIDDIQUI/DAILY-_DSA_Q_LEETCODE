# 3653. Find the Count of Good Integers

## 🔗 Problem Link
https://leetcode.com/problems/find-the-count-of-good-integers/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Math, Square Root Decomposition, Modular Arithmetic

---

## 🧩 Problem Summary
Given an array `nums` and queries `[l, r, k, v]`, multiply every k-th element in `nums[l..r]` by `v` (mod 10^9+7). After all queries, return the XOR of all elements. This is the optimized version using sqrt decomposition to handle queries with small `k` efficiently.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `1 <= queries.length <= 10^5`
- `1 <= k <= n`
- `1 <= v <= 10^9`

---

## 💭 Intuition
👉 Split queries by stride `k`: large strides (k >= sqrt(n)) are applied directly, small strides (k < sqrt(n)) are batched using a multiplicative difference array with modular inverse for efficient range processing.

---

## ⚡ Approach — Square Root Decomposition

### 🧠 Idea
- For queries with `k >= sqrt(n)`: directly iterate and multiply (at most sqrt(n) elements per query).
- For queries with `k < sqrt(n)`: group by `k`, use a multiplicative difference array. Mark start with `*v` and end+k with `*v^(-1)` (modular inverse). Compute cumulative products with stride `k`, then apply to `nums`.
- Finally XOR all elements.

---

## 💻 Code

```python
import math
from collections import defaultdict

class Solution:
    def __init__(self):
        self.M = 10**9 + 7

    # Binary Exponentiation (Fermat's Little Theorem)
    def power(self, a, b):
        if b == 0:
            return 1
        half = self.power(a, b // 2)
        result = (half * half) % self.M
        if b % 2 == 1:
            result = (result * a) % self.M
        return result

    def xorAfterQueries(self, nums, queries):
        n = len(nums)
        blockSize = math.ceil(math.sqrt(n))

        smallKMap = defaultdict(list)

        for query in queries:
            L, R, K, V = query

            if K >= blockSize:
                for i in range(L, R + 1, K):
                    nums[i] = (nums[i] * V) % self.M
            else:
                smallKMap[K].append(query)

        for K, allQueries in smallKMap.items():
            diff = [1] * n

            for query in allQueries:
                L, R, _, V = query

                diff[L] = (diff[L] * V) % self.M

                steps = (R - L) // K
                next_idx = L + (steps + 1) * K

                if next_idx < n:
                    diff[next_idx] = (diff[next_idx] * self.power(V, self.M - 2)) % self.M

            # Cumulative product
            for i in range(n):
                if i - K >= 0:
                    diff[i] = (diff[i] * diff[i - K]) % self.M

            # Apply diff to nums
            for i in range(n):
                nums[i] = (nums[i] * diff[i]) % self.M

        result = 0
        for num in nums:
            result ^= num

        return result
```

---

## 🧠 Dry Run
### Input
```
nums = [2, 3, 4, 5, 6], queries = [[0, 4, 2, 3]]
```
### Steps
```
n=5, blockSize=ceil(sqrt(5))=3
K=2 < 3, so grouped as small K

For K=2:
  diff = [1, 1, 1, 1, 1]
  Query [0, 4, 2, 3]:
    diff[0] *= 3 → diff = [3, 1, 1, 1, 1]
    steps = (4-0)//2 = 2, next_idx = 0 + 3*2 = 6 ≥ 5, skip

  Cumulative product (stride 2):
    i=2: diff[2] *= diff[0] = 3
    i=3: diff[3] *= diff[1] = 1
    i=4: diff[4] *= diff[2] = 3

  diff = [3, 1, 3, 1, 3]
  Apply: nums = [6, 3, 12, 5, 18]

XOR: 6 ^ 3 ^ 12 ^ 5 ^ 18 = 0110 ^ 0011 ^ 1100 ^ 0101 ^ 10010 = ...

Result: XOR of final nums
```

---

## ⏱️ Time Complexity
```
O((n + q) * sqrt(n)) — large-k queries take O(n/k) each, small-k queries are batched O(n) per stride value
```

## 💾 Space Complexity
```
O(n) — for the difference array
```

---

## ⚠️ Edge Cases
- All queries have k=1 → all small, batched efficiently
- All queries have k=n → all large, O(1) each
- v=1 → no-op queries
- Modular inverse needed only for boundary markers in diff array

---

## 🎯 Interview Takeaways
- Sqrt decomposition splits cases by threshold for balanced complexity.
- Multiplicative difference arrays with modular inverse handle batched stride updates.
- Fermat's little theorem provides modular inverse for prime moduli.

---

## 📌 Key Pattern
👉 **"Sqrt decomposition: large strides brute-force, small strides batch with multiplicative diff array and modular inverse."**

---

## 🔁 Related Problems
- 3651. Transforming a Grid to Binary with Minimum Cost (brute force version)
- 370. Range Addition
- 307. Range Sum Query - Mutable

---

## 🚀 Final Thoughts
This is an elegant application of sqrt decomposition. The multiplicative difference array technique — marking range starts and ends with multipliers and inverse multipliers — is a powerful tool for batched multiplicative range updates.

---

✨ **Rule to remember:**
> "Sqrt decomposition: brute-force large strides, batch small strides with multiplicative diff arrays and modular inverse."
