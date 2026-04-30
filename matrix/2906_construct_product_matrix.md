# 2906. Construct Product Matrix

## 🔗 Problem Link
https://leetcode.com/problems/construct-product-matrix/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Matrix, Prefix Product, Math

---

## 🧩 Problem Summary
Given a 2D grid of integers, construct a product matrix `p` where `p[i][j]` is the product of all elements in the grid except `grid[i][j]`, taken modulo 12345. This is essentially "product of array except self" but on a 2D grid with a specific modulus.

### 📌 Constraints
- `1 <= n * m <= 10^5`
- `1 <= grid[i][j] <= 10^9`

---

## 💭 Intuition
👉 Flatten the 2D grid conceptually and apply the prefix-suffix product technique. Compute prefix products left-to-right and suffix products right-to-left, then multiply them for each cell. This avoids division entirely, which is critical since we work modulo 12345.

---

## ⚡ Approach — Prefix-Suffix Product (2D)

### 🧠 Idea
- First pass (left to right, top to bottom): compute prefix product for each cell, storing the product of all elements before it.
- Second pass (right to left, bottom to top): compute suffix product and multiply with the stored prefix product.
- Each cell ends up with the product of all other elements, mod 12345.

---

## 💻 Code

```python
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n, m = len(grid), len(grid[0])
        p = [[0] * m for _ in range(n)]

        # Step 1: prefix
        prefix = 1
        for i in range(n):
            for j in range(m):
                p[i][j] = prefix
                prefix = (prefix * grid[i][j]) % MOD

        # Step 2: suffix
        suffix = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                p[i][j] = (p[i][j] * suffix) % MOD
                suffix = (suffix * grid[i][j]) % MOD

        return p
```

---

## 🧠 Dry Run
### Input
```
grid = [[1, 2], [3, 4]]
```
### Steps
```
MOD = 12345

Prefix pass (left to right):
  p[0][0] = 1,        prefix = 1*1 = 1
  p[0][1] = 1,        prefix = 1*2 = 2
  p[1][0] = 2,        prefix = 2*3 = 6
  p[1][1] = 6,        prefix = 6*4 = 24

Suffix pass (right to left):
  p[1][1] = 6*1 = 6,  suffix = 1*4 = 4
  p[1][0] = 2*4 = 8,  suffix = 4*3 = 12
  p[0][1] = 1*12 = 12, suffix = 12*2 = 24
  p[0][0] = 1*24 = 24, suffix = 24*1 = 24

Result: [[24, 12], [8, 6]]
(24=2*3*4, 12=1*3*4, 8=1*2*4, 6=1*2*3) ✓
```

---

## ⏱️ Time Complexity
```
O(n * m) — two passes over all elements.
```

## 💾 Space Complexity
```
O(n * m) — for the output matrix (no extra space beyond that).
```

---

## ⚠️ Edge Cases
- Single element grid: product of "everything else" is 1.
- Grid with zeros: handled correctly since we never divide.
- Large values: modulo 12345 keeps numbers small.

---

## 🎯 Interview Takeaways
- "Product except self" extends naturally to 2D by treating the grid as a flat array.
- Prefix-suffix technique avoids division, which is essential when working with modular arithmetic.
- Two passes (forward and backward) is a powerful pattern for "exclude self" computations.

---

## 📌 Key Pattern
👉 **"Prefix-suffix product: forward pass stores prefix, backward pass multiplies by suffix."**

---

## 🔁 Related Problems
- 238. Product of Array Except Self
- 1352. Product of the Last K Numbers
- 2906. Construct Product Matrix

---

## 🚀 Final Thoughts
This is the 2D generalization of LeetCode 238 (Product of Array Except Self) with modular arithmetic. The prefix-suffix approach is clean, avoids division, and handles the modulus naturally. A must-know pattern for interviews.

---

✨ **Rule to remember:**
> "Product except self = prefix * suffix — no division needed."
