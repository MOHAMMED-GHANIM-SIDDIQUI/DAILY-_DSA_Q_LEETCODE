# 840. Magic Squares In Grid

## 🔗 Problem Link
https://leetcode.com/problems/magic-squares-in-grid/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Math, Matrix

---

## 🧩 Problem Summary

Given a grid of integers, return the number of 3x3 "magic square" subgrids. A magic square is a 3x3 grid filled with distinct numbers from 1 to 9 where every row, column, and both diagonals sum to 15.

### 📌 Constraints
- `row == grid.length`
- `col == grid[i].length`
- `1 <= row, col <= 10`
- `0 <= grid[i][j] <= 15`

---

## 💭 Intuition

A 3x3 magic square using digits 1-9 always has 5 in the center. 👉 The border sequence of a valid magic square (reading clockwise) must be a rotation of the string "43816729" or its reverse. This gives a very elegant O(1) per-subgrid check.

---

## ⚡ Approach — Pattern Matching on Border Sequence

### 🧠 Idea

- For each possible 3x3 subgrid, first check if the top-left corner is even and center is 5 (quick filters).
- Read the 8 border cells in clockwise order as a string.
- Check if this string appears in "43816729" repeated twice (or its reverse repeated twice) to handle rotations.

---

## 💻 Code

```python
class Solution:
  def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
    def isMagic(i: int, j: int) -> int:
      s = "".join(str(grid[i + num // 3][j + num % 3])
                  for num in [0, 1, 2, 5, 8, 7, 6, 3])
      return s in "43816729" * 2 or s in "43816729"[::-1] * 2

    ans = 0

    for i in range(len(grid) - 2):
      for j in range(len(grid[0]) - 2):
        if grid[i][j] % 2 == 0 and grid[i + 1][j + 1] == 5:
          ans += isMagic(i, j)

    return ans
```

---

## 🧠 Dry Run

### Input
```
grid = [[2,7,6],[9,5,1],[4,3,8]]
```

### Steps
```
i=0, j=0: grid[0][0]=2 (even) ✓, grid[1][1]=5 ✓
Border sequence (clockwise): 2,7,6,1,8,3,4,9 → "27618349"
Check "27618349" in "4381672943816729" → No
Check "27618349" in "9276183492761834" → Yes ✓
ans = 1
Result: 1
```

---

## ⏱️ Time Complexity

```
O(m * n)
```

Where m and n are grid dimensions. Each 3x3 check is O(1).

---

## 💾 Space Complexity

```
O(1)
```

Only constant extra space for the border string.

---

## ⚠️ Edge Cases

- **Grid smaller than 3x3:** No magic squares possible → 0
- **No center = 5:** Quickly filtered, saving computation
- **Values outside 1-9:** Cannot form a valid magic square

---

## 🎯 Interview Takeaways

- All 3x3 magic squares with digits 1-9 share the same structure — 5 in center, even numbers at corners.
- Using string rotation matching is an elegant alternative to brute-force row/column/diagonal sum checks.
- Pre-filtering with simple conditions (center = 5, corner is even) avoids unnecessary work.

---

## 📌 Key Pattern

👉 **"All 3x3 magic squares have a fixed border pattern — match rotations of '43816729'"**

---

## 🔁 Related Problems

- 59. Spiral Matrix II
- 48. Rotate Image
- 1895. Largest Magic Square

---

## 🚀 Final Thoughts

A clever problem that rewards mathematical insight. Knowing that all 3x3 magic squares over 1-9 are rotations/reflections of a single base pattern leads to an extremely elegant solution.

---

✨ **Rule to remember:**
> Every 3x3 magic square (1-9) has 5 at center and its border is a rotation of "43816729".
