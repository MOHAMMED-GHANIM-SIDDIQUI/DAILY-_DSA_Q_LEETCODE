# 1411. Number of Ways to Paint N × 3 Grid

## 🔗 Problem Link
https://leetcode.com/problems/number-of-ways-to-paint-n-x-3-grid/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Dynamic Programming, Math

---

## 🧩 Problem Summary
Given an `n x 3` grid, paint each cell with one of three colors (red, yellow, green) such that no two adjacent cells (sharing an edge) have the same color. Return the number of ways to paint the grid modulo `10^9 + 7`.

### 📌 Constraints
- `1 <= n <= 5000`

---

## 💭 Intuition
👉 Each row of 3 cells can be colored in patterns with either 2 distinct colors (like ABA) or 3 distinct colors (like ABC). The transitions between consecutive rows follow fixed multipliers: a 2-color row can be followed by 3 two-color and 2 three-color patterns, and a 3-color row can be followed by 2 two-color and 2 three-color patterns.

---

## ⚡ Approach — DP with Pattern Counting

### 🧠 Idea
- For the first row: there are 6 two-color patterns (ABA type) and 6 three-color patterns (ABC type).
- Transition rules:
  - `nextColor2 = color2 * 3 + color3 * 2`
  - `nextColor3 = color2 * 2 + color3 * 2`
- Iterate for `n` rows, applying transitions with modular arithmetic.

---

## 💻 Code

```python
class Solution:
    def numOfWays(self, n: int) -> int:
        kMod = 1_000_000_007

        color2 = 6   # patterns like 121, 131, ...
        color3 = 6   # patterns like 123, 132, ...

        for _ in range(1, n):
            nextColor2 = color2 * 3 + color3 * 2
            nextColor3 = color2 * 2 + color3 * 2

            color2 = nextColor2 % kMod
            color3 = nextColor3 % kMod

        return (color2 + color3) % kMod
```

---

## 🧠 Dry Run
### Input
```
n = 2
```
### Steps
```
Initial: color2=6, color3=6
Row 2:
  nextColor2 = 6*3 + 6*2 = 18 + 12 = 30
  nextColor3 = 6*2 + 6*2 = 12 + 12 = 24
  color2=30, color3=24
Result = (30 + 24) % MOD = 54
```

---

## ⏱️ Time Complexity
```
O(n)
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- `n = 1` → 6 + 6 = 12 ways
- Large `n = 5000` → modular arithmetic prevents overflow
- The transition coefficients (3,2,2,2) are derived mathematically and are constant

---

## 🎯 Interview Takeaways
- Categorizing row patterns into 2-color and 3-color types simplifies the DP enormously.
- Fixed transition coefficients turn a complex coloring problem into a simple recurrence.
- Modular arithmetic is essential for large `n`.

---

## 📌 Key Pattern
👉 **"Categorize states into equivalence classes (2-color vs 3-color) and derive transition coefficients."**

---

## 🔁 Related Problems
- 256. Paint House
- 265. Paint House II
- 1931. Painting a Grid With Three Different Colors

---

## 🚀 Final Thoughts
A beautiful combinatorics + DP problem. The key breakthrough is recognizing that all valid row patterns fall into just two categories with fixed transition rules, reducing the state space dramatically.

---

✨ **Rule to remember:**
> For n×3 grid coloring: track 2-color and 3-color pattern counts with transitions (3,2) and (2,2).
