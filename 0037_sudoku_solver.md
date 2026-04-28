# 37. Sudoku Solver

## 🔗 Problem Link
https://leetcode.com/problems/sudoku-solver/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Hash Table, Backtracking, Matrix

---

## 🧩 Problem Summary
Write a program to solve a Sudoku puzzle by filling the empty cells. The solution must satisfy all Sudoku rules: each row, column, and 3x3 sub-box must contain digits 1-9 exactly once. The input board contains `'.'` for empty cells.

### 📌 Constraints
- `board.length == 9`
- `board[i].length == 9`
- `board[i][j]` is a digit or `'.'`
- The input board has exactly one solution.

---

## 💭 Intuition
👉 Use backtracking to try each digit 1-9 in every empty cell. If a placement is valid, recurse to the next cell. If we hit a dead end, undo the placement and try the next digit.

---

## ⚡ Approach — Backtracking

### 🧠 Idea
- Linearize the 2D board into a 1D index (0 to 80).
- For each cell, if it's already filled, skip to the next.
- If empty, try digits '1' through '9', checking validity against row, column, and box constraints.
- If a valid placement leads to a complete solution (index 81), return true.
- Otherwise backtrack by resetting the cell to `'.'`.

---

## 💻 Code

```cpp
class Solution {
 public:
  void solveSudoku(vector<vector<char>>& board) {
    solve(board, 0);
  }

 private:
  bool solve(vector<vector<char>>& board, int s) {
    if (s == 81)
      return true;

    const int i = s / 9;
    const int j = s % 9;

    if (board[i][j] != '.')
      return solve(board, s + 1);

    for (char c = '1'; c <= '9'; ++c)
      if (isValid(board, i, j, c)) {
        board[i][j] = c;
        if (solve(board, s + 1))
          return true;
        board[i][j] = '.';
      }

    return false;
  }

  bool isValid(vector<vector<char>>& board, int row, int col, char c) {
    for (int i = 0; i < 9; ++i)
      if (board[i][col] == c || board[row][i] == c ||
          board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] == c)
        return false;
    return true;
  }
};
```

---

## 🧠 Dry Run
### Input
```
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
```
### Steps
```
s=0: board[0][0]='5' -> skip
s=1: board[0][1]='3' -> skip
s=2: board[0][2]='.' -> try '1': invalid (col has 1), try '4': valid -> place '4'
s=3: board[0][3]='.' -> try '6': valid -> place '6'
... (continues recursively until s=81, board is fully solved)
```

---

## ⏱️ Time Complexity
```
O(9^E) where E is the number of empty cells (worst case), but pruning makes it much faster in practice.
```

## 💾 Space Complexity
```
O(E) — recursion stack depth equals the number of empty cells.
```

---

## ⚠️ Edge Cases
- Board with very few clues (17 is the minimum for a unique solution).
- Board that is already complete — immediately returns at s=81.
- Large number of empty cells causing deep recursion.

---

## 🎯 Interview Takeaways
- Backtracking is the standard approach for constraint satisfaction problems.
- Linearizing a 2D index simplifies recursive traversal.
- The `isValid` function cleverly checks row, column, and box in a single loop using index arithmetic.

---

## 📌 Key Pattern
👉 **"Backtracking with constraint checking — try, validate, recurse, undo"**

---

## 🔁 Related Problems
- 36. Valid Sudoku
- 51. N-Queens
- 52. N-Queens II

---

## 🚀 Final Thoughts
Sudoku Solver is the quintessential backtracking problem. The key optimization is the `isValid` check which prunes invalid branches early. More advanced solutions use bitmasks for O(1) validity checks.

---

✨ **Rule to remember:**
> "Place, check, recurse, backtrack — the four pillars of constraint-based search."
