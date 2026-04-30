# 3650. Longest Subsequence with Decreasing Adjacent Difference

## 🔗 Problem Link
https://leetcode.com/problems/longest-subsequence-with-decreasing-adjacent-difference/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Matrix, Sorting, Dynamic Programming, Greedy

---

## 🧩 Problem Summary
Given a grid of integers with `n` rows and `m` columns, find the minimum cost to transform it into a binary grid (all 0s and 1s) by changing cell values. Cells are sorted by value and processed with a bottom-right to top-left DP, with `k` allowed "free" transformations where cells with the same value can share costs.

### 📌 Constraints
- `1 <= n, m <= 1000`
- `n * m <= 10^5`
- `0 <= grid[i][j] <= 10^9`
- `0 <= k <= n * m`

---

## 💭 Intuition
👉 Sort all cells by value, then run a DP from bottom-right to top-left. After each "round" of k steps, propagate cost reductions among cells with identical values — cells sharing the same value can be grouped for free transformations.

---

## ⚡ Approach — Sorted Cells with Iterative DP

### 🧠 Idea
- Create a cost matrix initialized to infinity, with `cost[n-1][m-1] = 0`.
- Sort all cells by their grid value.
- For `k+1` iterations, sweep through same-value groups to propagate the best cost, then run a bottom-right to top-left DP pass updating costs from right and bottom neighbors.

---

## 💻 Code

```cpp
class Solution {
public:
    int minCost(vector<vector<int>>& grid, int k) {
        int n = grid.size();
        int m = grid[0].size();


        vector<vector<int>> cost(n, vector<int>(m, 1e9));


        vector<pair<int,int>> cells;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cells.push_back({i, j});
            }
        }


        sort(cells.begin(), cells.end(),
             [&](auto a, auto b) {
                 return grid[a.first][a.second] <
                        grid[b.first][b.second];
             });


        for (int step = 0; step <= k; step++) {


            int best = 1e9;

            for (int idx = 0; idx < cells.size(); idx++) {
                int r = cells[idx].first;
                int c = cells[idx].second;

                best = min(best, cost[r][c]);


                if (idx + 1 < cells.size() &&
                    grid[r][c] ==
                    grid[cells[idx+1].first][cells[idx+1].second]) {
                    continue;
                }


                int back = idx;
                while (back >= 0 &&
                       grid[cells[back].first][cells[back].second]
                       == grid[r][c]) {
                    cost[cells[back].first][cells[back].second] = best;
                    back--;
                }
            }


            for (int i = n - 1; i >= 0; i--) {
                for (int j = m - 1; j >= 0; j--) {

                    if (i == n - 1 && j == m - 1) {
                        cost[i][j] = 0;
                        continue;
                    }

                    if (i + 1 < n)
                        cost[i][j] = min(cost[i][j],
                                         cost[i+1][j] + grid[i+1][j]);

                    if (j + 1 < m)
                        cost[i][j] = min(cost[i][j],
                                         cost[i][j+1] + grid[i][j+1]);
                }
            }




        }

        return cost[0][0];
    }
};
```

---

## 🧠 Dry Run
### Input
```
grid = [[1, 2],
        [3, 0]], k = 1
```
### Steps
```
Cells sorted by value: (1,1,val=0), (0,0,val=1), (0,1,val=2), (1,0,val=3)

Step 0:
  Group propagation: each cell gets best cost within same-value group
  DP pass (bottom-right to top-left):
    cost[1][1] = 0
    cost[1][0] = cost[1][1] + grid[1][1] = 0
    cost[0][1] = cost[1][1] + grid[1][1] = 0
    cost[0][0] = min(cost[1][0]+grid[1][0], cost[0][1]+grid[0][1]) = min(3, 2) = 2

Step 1: repeat with updated costs

Result: cost[0][0]
```

---

## ⏱️ Time Complexity
```
O(k * n * m) — k iterations of O(n*m) DP passes
```

## 💾 Space Complexity
```
O(n * m) — for the cost matrix and cells array
```

---

## ⚠️ Edge Cases
- k = 0 → standard DP without free transformations
- 1x1 grid → cost is always 0
- All cells have the same value → all can share costs
- Grid already binary → may still need cost for path

---

## 🎯 Interview Takeaways
- Sorting cells by value enables efficient group processing.
- Iterative DP with k rounds handles the "free transformation" budget.
- Propagating minimum cost within same-value groups is the key optimization.

---

## 📌 Key Pattern
👉 **"Sort cells by value, iteratively run DP passes with group-based cost propagation for k free transformations."**

---

## 🔁 Related Problems
- 1368. Minimum Cost to Make at Least One Valid Path in a Grid
- 1293. Shortest Path in a Grid with Obstacles Elimination
- 2290. Minimum Obstacle Removal to Reach Corner

---

## 🚀 Final Thoughts
This problem combines grid DP with a clever grouping mechanism. The iterative approach of running k+1 DP passes, each time propagating costs among same-value cells, ensures that the free transformations are optimally utilized.

---

✨ **Rule to remember:**
> "When k free operations are allowed, iterate DP k+1 times with cost propagation among equivalent groups."
