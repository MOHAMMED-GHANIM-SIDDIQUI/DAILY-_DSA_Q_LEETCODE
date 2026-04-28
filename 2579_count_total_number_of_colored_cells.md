# 2579. Count Total Number of Colored Cells

## 🔗 Problem Link
https://leetcode.com/problems/count-total-number-of-colored-cells/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Math

---

## 🧩 Problem Summary
There is an infinitely large 2D grid of uncolored unit cells. At minute 1, one cell is colored. Each subsequent minute, every uncolored cell that shares a border with a colored cell gets colored. Return the number of colored cells after `n` minutes.

### 📌 Constraints
- `1 <= n <= 10^5`

---

## 💭 Intuition
👉 The colored region forms a diamond (rotated square). After `n` minutes, the diamond has a mathematical formula: it's two overlapping squares of sizes `n` and `n-1`, giving `n^2 + (n-1)^2`.

---

## ⚡ Approach — Mathematical Formula

### 🧠 Idea
- The colored cells form a diamond shape.
- The count follows the formula: `n^2 + (n-1)^2`.
- This can be derived by observing that the diamond has `2n-1` rows, with row widths `1, 3, 5, ..., 2n-1, ..., 5, 3, 1`.

---

## 💻 Code

```cpp
class Solution {
public:
    long long coloredCells(int n) {
        long long nLong = static_cast<long long>(n);
        return nLong * nLong + (nLong - 1) * (nLong - 1);
    }
};
```

---

## 🧠 Dry Run
### Input
```
n = 3
```
### Steps
```
n = 3
n^2 = 9
(n-1)^2 = 4
Total = 9 + 4 = 13

Visual (diamond):
    X
   XXX
  XXXXX
   XXX
    X
Count: 1 + 3 + 5 + 3 + 1 = 13 ✓
```

---

## ⏱️ Time Complexity
```
O(1)
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- `n = 1`: only 1 cell colored, formula gives `1 + 0 = 1` ✓
- Large `n`: need `long long` to avoid overflow

---

## 🎯 Interview Takeaways
- Pattern recognition and deriving closed-form formulas can turn O(n) simulation into O(1).
- Always consider integer overflow when dealing with squared terms.

---

## 📌 Key Pattern
👉 **"Derive a closed-form mathematical formula from geometric patterns"**

---

## 🔁 Related Problems
- 1828. Queries on Number of Points Inside a Circle
- 1401. Circle and Rectangle Overlapping

---

## 🚀 Final Thoughts
A pure math problem where recognizing the diamond pattern leads to the elegant formula `n^2 + (n-1)^2`. The hardest part is the derivation; the implementation is trivial.

---

✨ **Rule to remember:**
> A diamond pattern growing by one layer each step has `n^2 + (n-1)^2` cells after n steps.
