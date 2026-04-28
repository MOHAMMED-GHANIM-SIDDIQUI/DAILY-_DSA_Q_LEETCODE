# 2092. Find All People With Secret

## 🔗 Problem Link
https://leetcode.com/problems/find-all-people-with-secret/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Union Find, Graph, Sorting

---

## 🧩 Problem Summary
Given `n` people numbered 0 to n-1, person 0 has a secret and shares it with `firstPerson` at time 0. A list of meetings `[xi, yi, timei]` indicates that persons xi and yi meet at time timei. A person who knows the secret shares it with everyone they meet. Find all people who know the secret after all meetings.

### 📌 Constraints
- `2 <= n <= 10^5`
- `1 <= meetings.length <= 10^5`
- `meetings[i].length == 3`
- `0 <= xi, yi <= n - 1`, `xi != yi`
- `1 <= timei <= 10^5`

---

## 💭 Intuition
👉 Process meetings in chronological order. At each timestamp, union all people who meet. After processing a timestamp, anyone not connected to person 0 must have their union reset — they did not learn the secret at this time.

---

## ⚡ Approach — Union-Find with Time-Based Reset

### 🧠 Idea
- Use Union-Find to group people who share the secret.
- Union person 0 and `firstPerson` initially.
- Group meetings by time, process each time group in order.
- At each time step, union all meeting participants, then reset anyone not connected to person 0.
- Finally, collect all people connected to person 0.

---

## 💻 Code

```cpp
class UnionFind {
 public:
  UnionFind(int n) : id(n), rank(n) {
    iota(id.begin(), id.end(), 0);
  }

  void unionByRank(int u, int v) {
    const int i = find(u);
    const int j = find(v);
    if (i == j)
      return;
    if (rank[i] < rank[j]) {
      id[i] = j;
    } else if (rank[i] > rank[j]) {
      id[j] = i;
    } else {
      id[i] = j;
      ++rank[j];
    }
  }

  bool connected(int u, int v) {
    return find(u) == find(v);
  }

  void reset(int u) {
    id[u] = u;
  }

 private:
  vector<int> id;
  vector<int> rank;

  int find(int u) {
    return id[u] == u ? u : id[u] = find(id[u]);
  }
};

class Solution {
 public:
  vector<int> findAllPeople(int n, vector<vector<int>>& meetings,
                            int firstPerson) {
    vector<int> ans;
    UnionFind uf(n);
    map<int, vector<pair<int, int>>> timeToPairs;

    uf.unionByRank(0, firstPerson);

    for (const vector<int>& meeting : meetings) {
      const int x = meeting[0];
      const int y = meeting[1];
      const int time = meeting[2];
      timeToPairs[time].push_back({x, y});
    }

    for (const auto& [_, pairs] : timeToPairs) {
      unordered_set<int> peopleUnioned;
      for (const auto& [x, y] : pairs) {
        uf.unionByRank(x, y);
        peopleUnioned.insert(x);
        peopleUnioned.insert(y);
      }
      for (const int person : peopleUnioned)
        if (!uf.connected(person, 0))
          uf.reset(person);
    }

    for (int i = 0; i < n; ++i)
      if (uf.connected(i, 0))
        ans.push_back(i);

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
n = 6, meetings = [[1,2,5],[2,3,8],[1,5,10]], firstPerson = 1
```
### Steps
```
Union(0, 1) → {0,1} know the secret

Time 5: Union(1,2) → {0,1,2} know secret
  Check: 1 connected to 0? yes. 2 connected to 0? yes. No resets.

Time 8: Union(2,3) → {0,1,2,3} know secret
  Check: all connected to 0. No resets.

Time 10: Union(1,5) → {0,1,2,3,5} know secret
  Check: all connected to 0. No resets.

Result: [0, 1, 2, 3, 5]
```

---

## ⏱️ Time Complexity
```
O(m log m + m * α(n)) where m = number of meetings, α = inverse Ackermann (nearly constant).
Sorting meetings by time dominates: O(m log m).
```

## 💾 Space Complexity
```
O(n + m) — Union-Find structure plus the time-to-pairs map.
```

---

## ⚠️ Edge Cases
- All meetings at the same time: process them all together, then reset non-connected.
- A person meets someone with the secret, then later meets someone without — the secret still spreads.
- `firstPerson` is the only one who ever knows the secret.

---

## 🎯 Interview Takeaways
- Union-Find with selective reset is a powerful pattern for time-layered connectivity.
- Processing events in sorted time order is essential for correctness.
- Resetting nodes that failed to connect to the source prevents false propagation.

---

## 📌 Key Pattern
👉 **"Union-Find with time-based grouping and selective reset for transient connectivity."**

---

## 🔁 Related Problems
- 547. Number of Provinces
- 1319. Number of Operations to Make Network Connected
- 839. Similar String Groups

---

## 🚀 Final Thoughts
The key challenge is that meetings at the same time happen simultaneously, so you must union all participants at a given time before checking connectivity. The reset step ensures that people who only met each other (but none connected to person 0) don't falsely carry the secret forward.

---

✨ **Rule to remember:**
> "Union at each time step, then reset anyone not connected to the source."
