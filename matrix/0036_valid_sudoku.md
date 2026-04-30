# 36. Valid Sudoku

## 🔗 Problem Link
https://leetcode.com/problems/valid-sudoku/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Hash Table, Matrix

---

## 🧩 Problem Summary
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the rules: each row, column, and 3x3 sub-box must contain the digits 1-9 without repetition.

### 📌 Constraints
- `board.length == 9`
- `board[i].length == 9`
- `board[i][j]` is a digit `1-9` or `'.'`

---

## 💭 Intuition
👉 Use a single hash set to track all seen digits with encoded keys that represent which row, column, or box a digit belongs to. If any insertion fails, the board is invalid.

---

## ⚡ Approach — Hash Set with Encoded Keys

### 🧠 Idea
- Iterate through every cell in the 9x9 board.
- For each non-empty cell, create three encoded strings: one for the row, one for the column, and one for the 3x3 box.
- Attempt to insert each string into a set. If any insertion fails (duplicate), return false.
- If all cells pass, return true.

---

## 💻 Code

```cpp
class Solution {
 public:
  bool isValidSudoku(vector<vector<char>>& board) {
    unordered_set<string> seen;

    for (int i = 0; i < 9; ++i)
      for (int j = 0; j < 9; ++j) {
        if (board[i][j] == '.')
          continue;
        const string c(1, board[i][j]);
        if (!seen.insert(c + "@row" + to_string(i)).second ||
            !seen.insert(c + "@col" + to_string(j)).second ||
            !seen.insert(c + "@box" + to_string(i / 3) + to_string(j / 3))
                 .second)
          return false;
      }

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
i=0,j=0: '5' -> insert "5@row0", "5@col0", "5@box00" => all succeed
i=0,j=1: '3' -> insert "3@row0", "3@col1", "3@box00" => all succeed
i=0,j=4: '7' -> insert "7@row0", "7@col4", "7@box01" => all succeed
... (all insertions succeed)
Result: true
```

---

## ⏱️ Time Complexity
```
O(81) = O(1) — fixed 9x9 board
```

## 💾 Space Complexity
```
O(81) = O(1) — at most 3 * 81 entries in the set
```

---

## ⚠️ Edge Cases
- Board with all `'.'` — valid by default.
- Board with duplicate in a single 3x3 box but different rows/columns.
- Board with a single filled cell — always valid.

---

## 🎯 Interview Takeaways
- Encoding multiple constraints into a single set with string keys is a clean approach.
- The `insert().second` pattern in C++ elegantly checks for duplicates in one step.
- Using `i/3` and `j/3` maps any cell to its 3x3 box index.

---

## 📌 Key Pattern
👉 **"Encode constraints into hash set keys to validate uniqueness across multiple dimensions"**

---

## 🔁 Related Problems
- 37. Sudoku Solver
- 2133. Check if Every Row and Every Column Contains All Numbers

---

## 🚀 Final Thoughts
This problem is a classic validation exercise. The encoded-key hash set approach is elegant and avoids the need for separate data structures per row, column, and box.

---

✨ **Rule to remember:**
> "One set, three keys per cell — row, column, and box — catches all Sudoku violations."
