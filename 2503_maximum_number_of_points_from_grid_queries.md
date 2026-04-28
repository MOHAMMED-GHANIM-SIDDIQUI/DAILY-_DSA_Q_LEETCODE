# 2503. Maximum Number of Points From Grid Queries

## 🔗 Problem Link
https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Breadth-First Search, Sorting, Heap (Priority Queue), Union Find, Matrix

---

## 🧩 Problem Summary
Given an `m x n` grid and an array of queries, for each query value `q`, starting from `(0,0)`, count how many cells you can reach by only moving to adjacent cells with values strictly less than `q`. Return the answer for each query.

### 📌 Constraints
- `m == grid.length`
- `n == grid[i].length`
- `2 <= m, n <= 1000`
- `4 <= m * n <= 10^5`
- `1 <= grid[i][j], queries[i] <= 10^6`

---

## 💭 Intuition
👉 Sort queries and process them in ascending order. Use a min-heap BFS: expand from (0,0), adding cells with value < current query. Since queries are sorted, previously reached cells remain valid — just keep expanding.

---

## ⚡ Approach — Offline Processing with Sorted Queries + Min-Heap BFS

### 🧠 Idea
- Create indexed queries and sort them by value.
- Use a min-heap starting from `(0,0)` to greedily expand to cells with the smallest values first.
- For each query (in sorted order), pop cells from the heap while their value < query value, counting reachable cells.
- Map results back to original query indices.

---

## 💻 Code

```cpp
struct IndexedQuery {
  int queryIndex;
  int query;
};

struct T {
  int i;
  int j;
  int val;  // grid[i][j]
};

class Solution {
 public:
  vector<int> maxPoints(vector<vector<int>>& grid, vector<int>& queries) {
    constexpr int kDirs[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    const int m = grid.size();
    const int n = grid[0].size();
    vector<int> ans(queries.size());
    auto compare = [](const T& a, const T& b) { return a.val > b.val; };
    priority_queue<T, vector<T>, decltype(compare)> minHeap(compare);
    vector<vector<bool>> seen(m, vector<bool>(n));

    minHeap.emplace(0, 0, grid[0][0]);
    seen[0][0] = true;
    int accumulate = 0;

    for (const auto& [queryIndex, query] : getIndexedQueries(queries)) {
      while (!minHeap.empty()) {
        const auto [i, j, val] = minHeap.top();
        minHeap.pop();
        if (val >= query) {
          // The smallest neighbor is still larger than `query`, so no need to
          // keep exploring. Re-push (i, j, grid[i][j]) back to the `minHeap`.
          minHeap.emplace(i, j, val);
          break;
        }
        ++accumulate;
        for (const auto& [dx, dy] : kDirs) {
          const int x = i + dx;
          const int y = j + dy;
          if (x < 0 || x == m || y < 0 || y == n)
            continue;
          if (seen[x][y])
            continue;
          minHeap.emplace(x, y, grid[x][y]);
          seen[x][y] = true;
        }
      }
      ans[queryIndex] = accumulate;
    }

    return ans;
  }

 private:
  vector<IndexedQuery> getIndexedQueries(const vector<int>& queries) {
    vector<IndexedQuery> indexedQueries;
    for (int i = 0; i < queries.size(); ++i)
      indexedQueries.push_back({i, queries[i]});
    ranges::sort(
        indexedQueries, ranges::less{},
        [](const IndexedQuery& indexedQuery) { return indexedQuery.query; });
    return indexedQueries;
  }
};
```

---

## 🧠 Dry Run
### Input
```
grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
```
### Steps
```
Sorted indexed queries: [(2,2), (0,5), (1,6)]

Query 2: expand from (0,0) val=1 < 2 → count=1. Push neighbors.
  Pop (0,1) val=2, (1,0) val=2 — both >= 2 → re-push, stop. ans[2]=1

Query 5: pop (0,1) val=2 < 5 → count=2. pop (1,0) val=2 < 5 → count=3.
  Continue expanding... pop cells with val < 5. ans[0]=...

Query 6: continue from where query 5 left off. ans[1]=...

Result mapped back to original order.
```

---

## ⏱️ Time Complexity
```
O(m*n*log(m*n) + q*log(q)) — each cell is pushed/popped from heap once, queries sorted once.
```

## 💾 Space Complexity
```
O(m*n + q) — heap, seen matrix, and answer array.
```

---

## ⚠️ Edge Cases
- Query value <= grid[0][0]: cannot reach any cell, answer is 0.
- All grid values are the same: either all reachable or none.
- Single query vs. many queries.

---

## 🎯 Interview Takeaways
- Offline query processing (sort queries) avoids redundant BFS computations.
- Min-heap BFS naturally explores cells in order of their values.
- Accumulative counting across sorted queries is a powerful technique.

---

## 📌 Key Pattern
👉 **"Sort queries offline + min-heap BFS for progressive grid exploration."**

---

## 🔁 Related Problems
- 1631. Path With Minimum Effort
- 778. Swim in Rising Water
- 2258. Escape the Spreading Fire

---

## 🚀 Final Thoughts
The offline approach transforms independent queries into a single progressive BFS. Each cell is processed at most once across all queries, making the total work proportional to the grid size rather than grid size times number of queries.

---

✨ **Rule to remember:**
> "Sort queries, expand BFS progressively — each cell visited once across all queries."
