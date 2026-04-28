# 85. Maximal Rectangle

## 🔗 Problem Link
https://leetcode.com/problems/maximal-rectangle/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Dynamic Programming, Stack, Matrix, Monotonic Stack

---

## 🧩 Problem Summary

Given a 2D binary matrix filled with `'0'`s and `'1'`s, find the largest rectangle containing only `'1'`s and return its area. This extends the "Largest Rectangle in Histogram" problem to two dimensions.

### 📌 Constraints
- `rows == matrix.length`
- `cols == matrix[i].length`
- `1 <= rows, cols <= 200`
- `matrix[i][j]` is `'0'` or `'1'`

---

## 💭 Intuition

👉 The key insight is to reduce this 2D problem to multiple 1D "Largest Rectangle in Histogram" problems. For each row, we build a histogram where the bar height at column `j` is the number of consecutive `'1'`s above (and including) the current row. Then we apply the classic monotonic stack histogram algorithm to each row's histogram.

---

## ⚡ Approach — Histogram + Monotonic Stack

### 🧠 Idea

- Maintain a histogram array `hist` of length `cols`.
- For each row, update `hist[i]`: if `matrix[row][i] == '1'`, increment `hist[i]`; otherwise reset to 0.
- Apply the Largest Rectangle in Histogram algorithm using a monotonic stack on the current histogram.
- Track the global maximum area across all rows.

---

## 💻 Code

```python
class Solution:
  def maximalRectangle(self, matrix: list[list[str]]) -> int:
    if not matrix:
      return 0

    ans = 0
    hist = [0] * len(matrix[0])

    def largestRectangleArea(heights: list[int]) -> int:
      ans = 0
      stack = []

      for i in range(len(heights) + 1):
        while stack and (i == len(heights) or heights[stack[-1]] > heights[i]):
          h = heights[stack.pop()]
          w = i - stack[-1] - 1 if stack else i
          ans = max(ans, h * w)
        stack.append(i)

      return ans

    for row in matrix:
      for i, num in enumerate(row):
        hist[i] = 0 if num == '0' else hist[i] + 1
      ans = max(ans, largestRectangleArea(hist))

    return ans
```

---

## 🧠 Dry Run

### Input
```
matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
```

### Steps
```
Row 0: hist = [1,0,1,0,0] → largestRectangleArea → 1
Row 1: hist = [2,0,2,1,1] → largestRectangleArea → 3 (1*3 from cols 2-4)
Row 2: hist = [3,1,3,2,2] → largestRectangleArea → 6 (2*3 from cols 2-4)
Row 3: hist = [4,0,0,3,0] → largestRectangleArea → 4 (4*1 from col 0)
Global max = 6
```

---

## ⏱️ Time Complexity

```
O(rows * cols)
```

For each row, we build the histogram in O(cols) and run the stack algorithm in O(cols). Total: O(rows * cols).

---

## 💾 Space Complexity

```
O(cols)
```

The histogram array and the stack each use O(cols) space.

---

## ⚠️ Edge Cases

- **Empty matrix:** `matrix = []` → return 0
- **All zeros:** `matrix = [["0","0"],["0","0"]]` → return 0
- **Single cell:** `matrix = [["1"]]` → return 1

---

## 🎯 Interview Takeaways

- Reducing a 2D problem to repeated 1D subproblems is a powerful technique.
- The monotonic stack for "Largest Rectangle in Histogram" is a must-know pattern.
- Building histograms row-by-row avoids redundant computation.
- This problem combines DP (histogram building) with stack-based area calculation.

---

## 📌 Key Pattern

👉 **"Convert 2D matrix to row-wise histograms, then solve each as Largest Rectangle in Histogram with a monotonic stack."**

---

## 🔁 Related Problems

- 84. Largest Rectangle in Histogram
- 221. Maximal Square
- 304. Range Sum Query 2D – Immutable
- 1504. Count Submatrices With All Ones

---

## 🚀 Final Thoughts

Maximal Rectangle is a classic hard problem that elegantly combines histogram construction with monotonic stack processing. Mastering Problem 84 (Largest Rectangle in Histogram) is a prerequisite.

---

✨ **Rule to remember:**
> "Turn a 2D rectangle problem into stacked 1D histogram problems — then let the monotonic stack do the heavy lifting."
