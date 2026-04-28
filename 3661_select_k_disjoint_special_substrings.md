# 3661. Select K Disjoint Special Substrings

## 🔗 Problem Link
https://leetcode.com/problems/select-k-disjoint-special-substrings/

## ⚡ Difficulty
Hard

## 🏷️ Topics
String, BFS, Graph, SortedList

---

## 🧩 Problem Summary
Given a binary string `s` and an integer `k`, find the minimum number of operations to transform `s` so that the number of '0's becomes 0. Each operation selects a contiguous segment and flips bits according to specific rules. Use BFS on a state space where each state represents the count of '0's remaining.

### 📌 Constraints
- `1 <= s.length <= 10^5`
- `1 <= k <= s.length`

---

## 💭 Intuition
👉 Model the problem as a BFS on the number of '0's. From state `m` (current count of 0s), compute which states are reachable in one operation, and find the shortest path to state 0. Use a SortedList to efficiently skip visited states.

---

## ⚡ Approach — BFS with SortedList for Unvisited State Management

### 🧠 Idea
- Start BFS from the initial count of '0's.
- For each state `m`, compute the range of reachable next states based on operation constraints.
- Use a SortedList to track unvisited states and efficiently find the next unvisited state in range.
- Pop states from the SortedList as they are visited to avoid revisiting.

---

## 💻 Code

```python
class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n, m = len(s), s.count("0")
        dist = [math.inf] * (n + 1)
        nodeSets = [
            SortedList(range(0, n + 1, 2)),
            SortedList(range(1, n + 1, 2)),
        ]
        q = deque([m])
        dist[m] = 0
        nodeSets[m % 2].remove(m)
        while q:
            m = q.popleft()
            c1, c2 = max(k - n + m, 0), min(m, k)
            lnode, rnode = m + k - 2 * c2, m + k - 2 * c1
            nodeSet = nodeSets[lnode % 2]
            idx = nodeSet.bisect_left(lnode)
            while idx < len(nodeSet) and nodeSet[idx] <= rnode:
                m2 = nodeSet[idx]
                dist[m2] = dist[m] + 1
                q.append(m2)
                nodeSet.pop(idx)
        return -1 if dist[0] == math.inf else dist[0]
```

---

## 🧠 Dry Run
### Input
```
s = "0110", k = 2
```
### Steps
```
n=4, m=s.count("0")=2
dist = [inf]*5, nodeSets = [SortedList([0,2,4]), SortedList([1,3])]
Remove 2 from even set: nodeSets[0] = [0, 4]
q = deque([2]), dist[2] = 0

Pop m=2:
  c1 = max(2-4+2, 0) = 0, c2 = min(2, 2) = 2
  lnode = 2+2-4 = 0, rnode = 2+2-0 = 4
  nodeSet = nodeSets[0] (even), check [0, 4]
  idx=0: nodeSet[0]=0 ≤ 4 → dist[0]=1, push 0
  idx=0: nodeSet[0]=4 ≤ 4 → dist[4]=1, push 4

dist[0] = 1 → return 1
```

---

## ⏱️ Time Complexity
```
O(n log n) — each state is visited once, SortedList operations are O(log n)
```

## 💾 Space Complexity
```
O(n) — for dist array and SortedLists
```

---

## ⚠️ Edge Cases
- Already all 1s (m=0) → return 0
- Impossible to reach 0 → return -1
- k equals string length → single operation affects everything
- k=1 → each operation flips one bit

---

## 🎯 Interview Takeaways
- BFS on abstract state spaces (not just graphs) is a powerful technique.
- SortedList enables efficient "find and remove next unvisited" operations.
- Separating even/odd states into two SortedLists exploits the parity structure of transitions.

---

## 📌 Key Pattern
👉 **"BFS on state space with SortedList for efficient unvisited state management — O(n log n) total."**

---

## 🔁 Related Problems
- 752. Open the Lock
- 127. Word Ladder
- 1263. Minimum Moves to Move a Box to Their Target Location

---

## 🚀 Final Thoughts
This is an elegant BFS problem where the "graph" is implicit — states are counts of 0s, and edges represent valid operations. The SortedList trick for managing unvisited states ensures each state is processed exactly once, giving optimal complexity.

---

✨ **Rule to remember:**
> "When BFS on a state space has many reachable neighbors, use a SortedList to efficiently enumerate and remove unvisited states."
