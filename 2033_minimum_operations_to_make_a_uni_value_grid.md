# 2033. Minimum Operations to Make a Uni-Value Grid

## 🔗 Problem Link
https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Math, Sorting, Matrix

---

## 🧩 Problem Summary
Given a 2D grid of integers and an integer `x`, in one operation you can add or subtract `x` from any element. Return the minimum number of operations to make all elements equal, or -1 if it is impossible.

### 📌 Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 10^5`
- `1 <= m * n <= 10^5`
- `1 <= x, grid[i][j] <= 10^4`

---

## 💭 Intuition
👉 All elements must have the same remainder when divided by `x` — otherwise it is impossible. The optimal target is the median of the flattened array, which minimizes total absolute deviation.

---

## ⚡ Approach — Median + Modular Check

### 🧠 Idea
- Flatten the grid into a 1D array.
- Check that all elements have the same `% x` remainder; if not, return -1.
- Sort and find the median.
- Sum up `abs(num - median) // x` for all elements.

---

## 💻 Code

```python
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Flatten grid
        all_nums = [num for row in grid for num in row]

        # Check if all elements have same remainder mod x
        rem = all_nums[0] % x
        for num in all_nums:
            if num % x != rem:
                return -1

        # Find median
        all_nums.sort()
        median = all_nums[len(all_nums) // 2]

        # Calculate operations
        ans = 0
        for num in all_nums:
            ans += abs(num - median) // x

        return ans
```

---

## 🧠 Dry Run
### Input
```
grid = [[2,4],[6,8]], x = 2
```
### Steps
```
Flatten: [2, 4, 6, 8]
Remainders: all % 2 == 0 ✓
Sort: [2, 4, 6, 8]
Median: all_nums[2] = 6
Operations: |2-6|/2 + |4-6|/2 + |6-6|/2 + |8-6|/2 = 2 + 1 + 0 + 1 = 4
return 4
```

---

## ⏱️ Time Complexity
```
O(m*n * log(m*n)) due to sorting
```

## 💾 Space Complexity
```
O(m*n) for the flattened array
```

---

## ⚠️ Edge Cases
- Different remainders mod `x` → return -1
- Grid has only one element → 0 operations
- All elements already equal → 0 operations
- `x = 1` → always possible

---

## 🎯 Interview Takeaways
- The median minimizes the sum of absolute deviations — a fundamental statistics result.
- Checking modular compatibility is the key feasibility condition.
- Flattening a 2D grid into 1D simplifies the problem.

---

## 📌 Key Pattern
👉 **"Median minimizes total absolute deviation; mod check ensures feasibility"**

---

## 🔁 Related Problems
- 462. Minimum Moves to Equal Array Elements II
- 2448. Minimum Cost to Make Array Equal
- 1551. Minimum Operations to Make Array Equal

---

## 🚀 Final Thoughts
This problem combines a feasibility check (modular arithmetic) with an optimization insight (median minimizes L1 distance). It is a great example of how mathematical knowledge simplifies algorithmic problems.

---

✨ **Rule to remember:**
> To equalize elements with fixed-step operations, check mod compatibility first, then converge to the median.
