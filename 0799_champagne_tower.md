# 799. Champagne Tower

## 🔗 Problem Link
https://leetcode.com/problems/champagne-tower/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Dynamic Programming, Simulation

---

## 🧩 Problem Summary

We stack glasses in a champagne tower (row 0 has 1 glass, row 1 has 2, etc.). We pour `poured` cups of champagne into the top glass. When a glass overflows, excess splits equally to the two glasses below it. Return how full the glass at `(query_row, query_glass)` is (capped at 1.0).

### 📌 Constraints
- `0 <= poured <= 10^9`
- `0 <= query_glass <= query_row < 100`

---

## 💭 Intuition

This is a simulation/DP problem. 👉 We can model each glass as a cell in a 2D array, pour all champagne into the top, and simulate the overflow row by row. Any glass with more than 1.0 unit overflows equally to its two children below.

---

## ⚡ Approach — Row-by-Row Simulation (DP)

### 🧠 Idea

- Create a 2D array `dp` where `dp[i][j]` tracks the total champagne that flows into glass `(i, j)`.
- Set `dp[0][0] = poured`.
- For each glass that has more than 1 unit, compute the overflow and distribute half to each child.
- The answer is `min(1.0, dp[query_row][query_glass])`.

---

## 💻 Code

```python
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # dp[i][j] = amount of champagne in row i, glass j
        dp = [[0.0] * (query_row + 1) for _ in range(query_row + 1)]
        dp[0][0] = poured

        for i in range(query_row):
            for j in range(i + 1):
                if dp[i][j] > 1:
                    overflow = (dp[i][j] - 1) / 2.0
                    dp[i + 1][j] += overflow
                    dp[i + 1][j + 1] += overflow

        return min(1.0, dp[query_row][query_glass])
```

---

## 🧠 Dry Run

### Input
```
poured = 2, query_row = 1, query_glass = 1
```

### Steps
```
dp[0][0] = 2
Row 0: dp[0][0] = 2 > 1 → overflow = 0.5
  dp[1][0] += 0.5 → 0.5
  dp[1][1] += 0.5 → 0.5
Return min(1.0, dp[1][1]) = 0.5
```

---

## ⏱️ Time Complexity

```
O(query_row^2)
```

We iterate through all glasses up to the query row.

---

## 💾 Space Complexity

```
O(query_row^2)
```

For the 2D DP array. Can be optimized to O(query_row) with a rolling array.

---

## ⚠️ Edge Cases

- **poured = 0:** All glasses are empty → 0.0
- **query_row = 0, query_glass = 0:** Direct pour → `min(1.0, poured)`
- **Very large pour:** Overflow cascades deep, but answer is always capped at 1.0

---

## 🎯 Interview Takeaways

- Simulation problems often translate naturally into DP.
- The overflow mechanism (split excess equally) is a common pattern in cascading simulations.
- Always cap the final result — the glass can hold at most 1 unit.
- Think of the champagne tower as Pascal's triangle with overflow logic.

---

## 📌 Key Pattern

👉 **"Simulate cascading overflow row-by-row using a 2D DP grid"**

---

## 🔁 Related Problems

- 118. Pascal's Triangle
- 119. Pascal's Triangle II
- 120. Triangle

---

## 🚀 Final Thoughts

An elegant simulation problem that models a real-world process. The key is to think of it as a top-down flow where each overflow distributes equally, and to cap the result at 1.0.

---

✨ **Rule to remember:**
> Pour from the top, overflow splits evenly to children — simulate row by row and cap at 1.
