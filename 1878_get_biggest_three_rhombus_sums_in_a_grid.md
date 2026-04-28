# 1878. Get Biggest Three Rhombus Sums in a Grid

## 🔗 Problem Link
https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Math, Matrix, Sorting, Simulation

---

## 🧩 Problem Summary
Given an `m x n` grid of integers, find the biggest three distinct rhombus sums. A rhombus sum is the sum of elements on the border of a rhombus centered at `(r, c)` with a given side length. A single cell is a rhombus of side 0. Return the result in descending order.

### 📌 Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 50`
- `1 <= grid[i][j] <= 10^5`

---

## 💭 Intuition
👉 For each cell as the center, enumerate all possible rhombus sizes. Trace the four sides of the rhombus border and sum up the values. Use a set to maintain the top 3 distinct sums.

---

## ⚡ Approach — Brute Force Enumeration with Top-3 Set

### 🧠 Idea
- For each cell `(r, c)`, treat it as a rhombus center.
- Start with side length 0 (the cell itself), then expand outward.
- For each valid side length, trace the four diagonals of the rhombus border.
- Maintain a set of sums; if the set exceeds size 3, remove the minimum.
- Return the set sorted in descending order.

---

## 💻 Code

```python
class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        st = set()

        def addToSet(val):
            st.add(val)
            if len(st) > 3:
                st.remove(min(st))

        for r in range(m):
            for c in range(n):

                # every cell itself (side = 0 rhombus)
                addToSet(grid[r][c])

                side = 1
                while r - side >= 0 and r + side < m and c - side >= 0 and c + side < n:
                    s = 0

                    for k in range(side):
                        s += grid[r - side + k][c + k]     # top → right
                        s += grid[r + k][c + side - k]     # right → bottom
                        s += grid[r + side - k][c - k]     # bottom → left
                        s += grid[r - k][c - side + k]     # left → top

                    addToSet(s)
                    side += 1

        return sorted(st, reverse=True)
```

---

## 🧠 Dry Run
### Input
```
grid = [[3,4,5,1,3],
        [3,3,4,2,3],
        [20,30,200,40,10],
        [1,5,5,60,2],
        [1,1,3,1,1]]
```
### Steps
```
Center (2,2), side=1:
  top→right: grid[1][3]=2
  right→bottom: grid[3][2]=5 (k=0 only partial trace)
  ... sum of border = 4+2+40+5+5+3+3+30 (varies by k)

Center (2,2), side=2:
  Full border trace covers all edge cells of a size-2 rhombus.

All sums collected in set, top 3 returned in descending order.
```

---

## ⏱️ Time Complexity
```
O(m * n * min(m, n)^2), where m and n are grid dimensions
```

## 💾 Space Complexity
```
O(1) extra space (set bounded at size 4)
```

---

## ⚠️ Edge Cases
- Grid is 1x1 → return the single element
- All cells have the same value → return a list with one element
- Less than 3 distinct rhombus sums exist

---

## 🎯 Interview Takeaways
- Rhombus border traversal uses four diagonal directions, each traced for `side` steps.
- Using a bounded set (size 3) avoids sorting a large collection of sums.
- Brute force is acceptable when grid dimensions are small (up to 50).

---

## 📌 Key Pattern
👉 **"Enumerate all rhombus centers and sizes, trace borders using four diagonal directions"**

---

## 🔁 Related Problems
- 1314. Matrix Block Sum
- 221. Maximal Square
- 764. Largest Plus Sign

---

## 🚀 Final Thoughts
This problem is a geometry simulation on a grid. The main challenge is correctly tracing the four sides of a rhombus border. The bounded set trick efficiently maintains only the top 3 values without extra sorting overhead.

---

✨ **Rule to remember:**
> A rhombus in a grid has four diagonal sides — trace each for `side` steps to compute the border sum.
