# 3197. Find the Minimum Area to Cover All Ones II

## 🔗 Problem Link
https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Matrix, Enumeration, Geometry

---

## 🧩 Problem Summary
Given a 2D binary grid, find the minimum total area of exactly three non-overlapping axis-aligned rectangles that together cover all 1s in the grid. The rectangles must not overlap but can touch.

### 📌 Constraints
- 1 <= grid.length, grid[0].length <= 30
- grid[i][j] is 0 or 1

---

## 💭 Intuition
👉 Enumerate all ways to partition the grid into three regions using horizontal and vertical cuts. For each partition, compute the bounding box area of 1s in each region and take the minimum total.

---

## ⚡ Approach — Enumerate All 3-Partition Cuts

### 🧠 Idea
- Try all 6 types of 3-region partitions: two horizontal cuts, two vertical cuts, and four L-shaped splits (horizontal + vertical in each quadrant)
- For each partition, compute the minimum bounding rectangle area for the 1s in each region
- Return the overall minimum sum

---

## 💻 Code

```cpp
class Solution {
 public:
  int minimumSum(vector<vector<int>>& grid) {
    const int m = grid.size();
    const int n = grid[0].size();
    int ans = m * n;

    for (int i = 0; i < m; ++i) {
      const int top = minimumArea(grid, 0, i, 0, n - 1);
      for (int j = 0; j < n; ++j)
        ans = min(ans,
                  top + /*left*/ minimumArea(grid, i + 1, m - 1, 0, j) +
                      /*right*/ minimumArea(grid, i + 1, m - 1, j + 1, n - 1));
    }

    for (int i = 0; i < m; ++i) {
      const int bottom = minimumArea(grid, i, m - 1, 0, n - 1);
      for (int j = 0; j < n; ++j)
        ans = min(ans, bottom + /*left*/ minimumArea(grid, 0, i - 1, 0, j) +
                           /*right*/ minimumArea(grid, 0, i - 1, j + 1, n - 1));
    }

    for (int j = 0; j < n; ++j) {
      const int left = minimumArea(grid, 0, m - 1, 0, j);
      for (int i = 0; i < m; ++i)
        ans = min(ans,
                  left + /*top*/ minimumArea(grid, 0, i, j + 1, n - 1) +
                      /*bottom*/ minimumArea(grid, i + 1, m - 1, j + 1, n - 1));
    }

    for (int j = 0; j < n; ++j) {
      const int right = minimumArea(grid, 0, m - 1, j, n - 1);
      for (int i = 0; i < m; ++i)
        ans =
            min(ans, right + /*top*/ minimumArea(grid, 0, i, 0, j - 1) +
                         /*bottom*/ minimumArea(grid, i + 1, m - 1, 0, j - 1));
    }

    for (int i1 = 0; i1 < m; ++i1)
      for (int i2 = i1 + 1; i2 < m; ++i2)
        ans =
            min(ans, /*top*/ minimumArea(grid, 0, i1, 0, n - 1) +
                         /*middle*/ minimumArea(grid, i1 + 1, i2, 0, n - 1) +
                         /*bottom*/ minimumArea(grid, i2 + 1, m - 1, 0, n - 1));

    for (int j1 = 0; j1 < n; ++j1)
      for (int j2 = j1 + 1; j2 < n; ++j2)
        ans =
            min(ans, /*left*/ minimumArea(grid, 0, m - 1, 0, j1) +
                         /*middle*/ minimumArea(grid, 0, m - 1, j1 + 1, j2) +
                         /*right*/ minimumArea(grid, 0, m - 1, j2 + 1, n - 1));

    return ans;
  }

 private:
  int minimumArea(vector<vector<int>>& grid, int si, int ei, int sj, int ej) {
    int x1 = INT_MAX;
    int y1 = INT_MAX;
    int x2 = 0;
    int y2 = 0;
    for (int i = si; i <= ei; ++i)
      for (int j = sj; j <= ej; ++j)
        if (grid[i][j] == 1) {
          x1 = min(x1, i);
          y1 = min(y1, j);
          x2 = max(x2, i);
          y2 = max(y2, j);
        }
    return x1 == INT_MAX ? 0 : (x2 - x1 + 1) * (y2 - y1 + 1);
  }
};
```

---

## 🧠 Dry Run
### Input
```
grid = [[1,0,1],
        [1,1,1]]
```
### Steps
```
One possible partition: two vertical cuts at j1=0, j2=1
left = area(0,1,0,0) -> covers (0,0),(1,0) -> 2x1=2
middle = area(0,1,1,1) -> covers (1,1) -> 1x1=1
right = area(0,1,2,2) -> covers (0,2),(1,2) -> 2x1=2
Total = 5
Other partitions are explored; minimum is returned.
```

---

## ⏱️ Time Complexity
```
O(m^2 * n^2 * m * n) — enumerate cuts O(m*n or m^2) times, each bounding box is O(m*n)
```

## 💾 Space Complexity
```
O(1) — only tracking variables
```

---

## ⚠️ Edge Cases
- 1s clustered in three separate groups — optimal partition isolates each group
- All 1s in a single cell — three rectangles, two of area 0
- Regions with no 1s contribute 0 area

---

## 🎯 Interview Takeaways
- There are only 6 topological ways to cut a rectangle into 3 non-overlapping rectangles
- Brute-force enumeration is feasible when grid dimensions are small (<=30)
- Reusing the bounding box subroutine keeps the code clean

---

## 📌 Key Pattern
👉 **"Enumerate all 3-partition cuts of a grid and minimize total bounding box area"**

---

## 🔁 Related Problems
- 3195. Find the Minimum Area to Cover All Ones I
- 221. Maximal Square
- 85. Maximal Rectangle

---

## 🚀 Final Thoughts
The small grid size (30x30) permits brute-force enumeration of all partition types. The key insight is recognizing the 6 distinct ways to split a rectangle into 3 parts: two horizontal lines, two vertical lines, or one of each creating an L-shaped partition.

---

✨ **Rule to remember:**
> Six partition patterns cover all ways to split a grid into three rectangles — enumerate them all.
