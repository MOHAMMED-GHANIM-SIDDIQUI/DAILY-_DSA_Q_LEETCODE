# 3195. Find the Minimum Area to Cover All Ones I

## 🔗 Problem Link
https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Matrix

---

## 🧩 Problem Summary
Given a 2D binary grid, find the minimum area of a rectangle that covers all the 1s in the grid. The rectangle sides must be parallel to the axes.

### 📌 Constraints
- 1 <= grid.length, grid[0].length <= 1000
- grid[i][j] is 0 or 1
- There is at least one 1 in the grid

---

## 💭 Intuition
👉 Find the bounding box of all 1s by tracking the min/max row and column indices, then compute the area.

---

## ⚡ Approach — Bounding Box

### 🧠 Idea
- Scan the entire grid
- Track minimum and maximum row (x1, x2) and column (y1, y2) of cells containing 1
- The minimum area is (x2 - x1 + 1) * (y2 - y1 + 1)

---

## 💻 Code

```cpp
class Solution {
 public:
  int minimumArea(vector<vector<int>>& grid) {
    int x1 = INT_MAX;
    int y1 = INT_MAX;
    int x2 = 0;
    int y2 = 0;

    for (int i = 0; i < grid.size(); ++i)
      for (int j = 0; j < grid[0].size(); ++j)
        if (grid[i][j] == 1) {
          x1 = min(x1, i);
          y1 = min(y1, j);
          x2 = max(x2, i);
          y2 = max(y2, j);
        }

    return (x2 - x1 + 1) * (y2 - y1 + 1);
  }
};
```

---

## 🧠 Dry Run
### Input
```
grid = [[0,1,0],
        [1,0,1]]
```
### Steps
```
(0,1)=1: x1=0, y1=1, x2=0, y2=1
(1,0)=1: x1=0, y1=0, x2=1, y2=1
(1,2)=1: x1=0, y1=0, x2=1, y2=2
Area = (1-0+1) * (2-0+1) = 2 * 3 = 6
```

---

## ⏱️ Time Complexity
```
O(m * n) — scan every cell in the grid
```

## 💾 Space Complexity
```
O(1) — only four tracking variables
```

---

## ⚠️ Edge Cases
- Single 1 in the grid — area is 1
- All cells are 1 — area is m * n
- 1s only in one row or column — rectangle degenerates to a line (width or height = 1)

---

## 🎯 Interview Takeaways
- Bounding box is the simplest approach for axis-aligned enclosing rectangles
- No sorting or complex data structures needed
- Always consider the +1 offset when computing inclusive ranges

---

## 📌 Key Pattern
👉 **"Bounding box via min/max of row and column indices"**

---

## 🔁 Related Problems
- 3197. Find the Minimum Area to Cover All Ones II
- 302. Smallest Rectangle Enclosing Black Pixels
- 999. Available Captures for Rook

---

## 🚀 Final Thoughts
A simple but fundamental pattern. Finding the bounding box of active cells is a building block for more complex problems like 3197, where you need to partition the grid into three rectangles.

---

✨ **Rule to remember:**
> Bounding box = track min/max row and column of all 1s, then multiply dimensions.
