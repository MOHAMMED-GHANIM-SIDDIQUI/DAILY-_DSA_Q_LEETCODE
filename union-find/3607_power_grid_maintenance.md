# 3607. Power Grid Maintenance

## 🔗 Problem Link
https://leetcode.com/problems/power-grid-maintenance/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Union-Find, Graph, Set, Simulation

---

## 🧩 Problem Summary
Design a system for a power grid with `c` stations connected by cables. Support two query types: (1) given a station x, find the smallest-ID online station in its connected component (or -1 if none), and (2) take a station offline. Connections are fixed; only station availability changes.

### 📌 Constraints
- `1 <= c <= 10^5`
- `1 <= connections.length <= 10^5`
- `1 <= queries.length <= 10^5`

---

## 💭 Intuition
👉 Use **Union-Find** to group connected stations, and maintain a **sorted set** per component of online stations. When querying, find the component root and return the smallest element in its set. When taking a station offline, remove it from the component's set.

---

## ⚡ Approach — Union-Find with Per-Component Sorted Sets

### 🧠 Idea
- Initialize Union-Find with each station as its own parent.
- Build connectivity by uniting stations along each connection.
- Each component maintains a sorted set of online stations.
- Query type 1: find root, return smallest in set (or -1 if empty).
- Query type 2: mark station offline and remove from its component's set.
- When merging, merge smaller set into larger (union by size).

---

## 💻 Code

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findp(int x) {
        return parent[x] == x ? x : parent[x] = findp(parent[x]);
    }

    void unite(int a, int b) {
        int pa = findp(a), pb = findp(b);
        if (pa == pb) return;
        if (pa < pb) {
            parent[pb] = pa;
            // merge set pb into pa
            if (compSet[pb].size() > compSet[pa].size()) {
                compSet[pa].swap(compSet[pb]);
            }
            for (int v : compSet[pb]) compSet[pa].insert(v);
            compSet[pb].clear();
        } else {
            parent[pa] = pb;
            if (compSet[pa].size() > compSet[pb].size()) {
                compSet[pb].swap(compSet[pa]);
            }
            for (int v : compSet[pa]) compSet[pb].insert(v);
            compSet[pa].clear();
        }
    }

    vector<int> processQueries(int c, vector<vector<int>>& connections, vector<vector<int>>& queries) {
        parent.assign(c + 1, 0);
        compSet.assign(c + 1, set<int>());
        online.assign(c + 1, true);

        // Initialize
        for (int i = 1; i <= c; i++) {
            parent[i] = i;
            compSet[i].insert(i);
            online[i] = true;
        }

        // Build connectivity
        for (auto &e : connections) {
            int u = e[0], v = e[1];
            unite(u, v);
        }

        vector<int> ans;

        // Process queries
        for (auto &q : queries) {
            int type = q[0], x = q[1];
            if (type == 1) {
                if (online[x]) {
                    // station x resolves it itself
                    ans.push_back(x);
                } else {
                    int px = findp(x);
                    if (compSet[px].empty()) {
                        ans.push_back(-1);
                    } else {
                        // smallest id in the same component that is online
                        ans.push_back(*compSet[px].begin());
                    }
                }
            } else { // type == 2
                if (online[x]) {
                    online[x] = false;
                    int px = findp(x);
                    auto it = compSet[px].find(x);
                    if (it != compSet[px].end()) compSet[px].erase(it);
                }
            }
        }

        return ans;
    }

private:
    vector<int> parent;
    vector< set<int> > compSet;
    vector<bool> online;
};
```

---

## 🧠 Dry Run
### Input
```
c = 4, connections = [[1,2],[2,3]], queries = [[1,1],[2,1],[1,2],[2,2],[1,3]]
```
### Steps
```
Init: parent=[_,1,2,3,4], each has its own set
Unite(1,2): parent[2]=1, compSet[1]={1,2}
Unite(2,3): findp(2)=1, findp(3)=3, parent[3]=1, compSet[1]={1,2,3}

Query [1,1]: online[1]=true -> ans=[1]
Query [2,1]: online[1]=false, remove 1 from compSet[1]={2,3}
Query [1,2]: online[2]=true -> ans=[1,2]
Query [2,2]: online[2]=false, compSet[1]={3}
Query [1,3]: online[3]=true -> ans=[1,2,3]

Result: [1, 2, 3]
```

---

## ⏱️ Time Complexity
```
O((c + m) * alpha(c) + q * log(c)) — Union-Find with path compression + set operations
```

## 💾 Space Complexity
```
O(c + m) — for Union-Find structures and sets
```

---

## ⚠️ Edge Cases
- Station queried after all in its component are offline → return -1
- Station already offline being taken offline again → no-op
- Disconnected components → each handles independently

---

## 🎯 Interview Takeaways
- Combining Union-Find with auxiliary data structures (sets) extends its power.
- Sorted sets per component enable min-queries in O(log n).
- Path compression + union by smaller-ID ensures correctness of root lookups.

---

## 📌 Key Pattern
👉 **"Union-Find with per-component sorted sets for dynamic connectivity with min-queries."**

---

## 🔁 Related Problems
- 721. Accounts Merge
- 1202. Smallest String With Swaps
- 305. Number of Islands II

---

## 🚀 Final Thoughts
This problem combines Union-Find for static connectivity with dynamic availability tracking via sets. The key design choice is maintaining sorted sets at the root level for efficient minimum lookups.

---

✨ **Rule to remember:**
> When you need connectivity queries plus per-component aggregation, augment Union-Find with a data structure at each root.
