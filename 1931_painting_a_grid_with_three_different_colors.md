# 1931. Painting a Grid With Three Different Colors

## 🔗 Problem Link
https://leetcode.com/problems/painting-a-grid-with-three-different-colors/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Dynamic Programming, Bitmask, Math

---

## 🧩 Problem Summary
Given an `m x n` grid, paint each cell with one of three colors such that no two adjacent cells (horizontally or vertically) share the same color. Return the number of valid colorings modulo `10^9 + 7`.

### 📌 Constraints
- `1 <= m <= 5`
- `1 <= n <= 1000`

---

## 💭 Intuition
👉 Since `m` is very small (at most 5), we can encode each column's coloring as a bitmask (2 bits per cell for 3 colors). We use DP column by column, checking that each column is internally valid and compatible with the previous column.

---

## ⚡ Approach — Bitmask DP Column by Column

### 🧠 Idea
- Encode colors as 2-bit values in a bitmask: 1=red, 2=green, 3=blue.
- For each cell, try all 3 colors, ensuring no conflict with the cell above (same column) or the cell to the left (previous column's mask).
- Use memoization on `(column, previousColumnMask)`.
- Build the grid column by column.

---

## 💻 Code

```cpp
class Solution {
 public:
  int colorTheGrid(int m, int n) {
    this->m = m;
    this->n = n;
    return dp(0, 0, 0, 0);
  }

 private:
  static constexpr int kMod = 1'000'000'007;
  int m;
  int n;
  vector<vector<int>> mem = vector<vector<int>>(1000, vector<int>(1024));

  int dp(int r, int c, int prevColMask, int currColMask) {
    if (c == n)
      return 1;
    if (mem[c][prevColMask])
      return mem[c][prevColMask];
    if (r == m)
      return dp(0, c + 1, currColMask, 0);

    int ans = 0;

    // 1 := red, 2 := green, 3 := blue
    for (int color = 1; color <= 3; ++color) {
      if (getColor(prevColMask, r) == color)
        continue;
      if (r > 0 && getColor(currColMask, r - 1) == color)
        continue;
      ans += dp(r + 1, c, prevColMask, setColor(currColMask, r, color));
      ans %= kMod;
    }

    if (r == 0)
      mem[c][prevColMask] = ans;

    return ans;
  }

  // e.g. __ __ __ __ __
  //      01 10 11 11 11
  //      R  G  B  B  B
  // getColor(0110111111, 3) -> G
  int getColor(int mask, int r) {
    return mask >> r * 2 & 3;
  }

  int setColor(int mask, int r, int color) {
    return mask | color << r * 2;
  }
};
```

---

## 🧠 Dry Run
### Input
```
m = 1, n = 2
```
### Steps
```
Column 0: 3 choices (R, G, or B)
Column 1: For each choice in column 0, 2 valid choices (any color except the one used in column 0)
Total = 3 * 2 = 6
```

---

## ⏱️ Time Complexity
```
O(n * 3^m * 3^m) in the worst case, but memoization reduces repeated states significantly
```

## 💾 Space Complexity
```
O(n * 4^m) for the memoization table (2 bits per cell, m cells)
```

---

## ⚠️ Edge Cases
- `m = 1`: Each column has 3 choices, adjacent columns must differ: `3 * 2^(n-1)`.
- `n = 1`: Just count valid column colorings with no two adjacent same color.
- `m = 5`: Maximum bitmask size is `2^10 = 1024`.

---

## 🎯 Interview Takeaways
- Bitmask DP is ideal when one dimension is very small (m <= 5).
- Encoding multi-valued states in a bitmask (2 bits per cell) extends standard bitmask DP.
- Building column by column with memoization on the previous column mask is a clean pattern.

---

## 📌 Key Pattern
👉 **"Bitmask DP over small-dimension grids: encode column state and transition column by column"**

---

## 🔁 Related Problems
- 1411. Number of Ways to Paint N x 3 Grid
- 1349. Maximum Students Taking Exam
- 2172. Maximum AND Sum of Array

---

## 🚀 Final Thoughts
This problem leverages the small `m` constraint to make bitmask DP feasible. The encoding of three colors in 2-bit slots is a nice generalization of binary bitmask DP. The column-by-column approach with memoization on the previous column's mask is both elegant and efficient.

---

✨ **Rule to remember:**
> "When one grid dimension is tiny, encode the state as a bitmask and DP across the other dimension."
