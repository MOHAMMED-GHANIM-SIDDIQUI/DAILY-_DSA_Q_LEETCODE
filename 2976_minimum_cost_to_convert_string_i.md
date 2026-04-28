# 2976. Minimum Cost to Convert String I

## 🔗 Problem Link
https://leetcode.com/problems/minimum-cost-to-convert-string-i/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Graph, Shortest Path, Floyd-Warshall, String

---

## 🧩 Problem Summary
You are given two strings `source` and `target` of the same length, along with arrays `original`, `changed`, and `cost`. Each entry defines a character conversion from `original[i]` to `changed[i]` at cost `cost[i]`. Return the minimum cost to convert `source` into `target`, or -1 if impossible.

### 📌 Constraints
- `1 <= source.length == target.length <= 10^5`
- `source`, `target` consist of lowercase English letters
- `1 <= cost.length == original.length == changed.length <= 2000`
- `original[i]`, `changed[i]` are lowercase English letters
- `1 <= cost[i] <= 10^6`

---

## 💭 Intuition
👉 Since characters are lowercase English letters (only 26), we can model the problem as a graph with 26 nodes and use Floyd-Warshall to find the shortest conversion cost between any two characters.

---

## ⚡ Approach — Floyd-Warshall All-Pairs Shortest Path

### 🧠 Idea
- Build a 26x26 distance matrix where `dist[u][v]` represents the minimum cost to convert character `u` to character `v`.
- Initialize the matrix with the given conversions, keeping the minimum cost for duplicate edges.
- Run Floyd-Warshall to compute the shortest path between all character pairs.
- Iterate through `source` and `target`, summing up the conversion costs. Return -1 if any conversion is impossible.

---

## 💻 Code

```python
class Solution:
  def minimumCost(
      self,
      source: str,
      target: str,
      original: list[str],
      changed: list[str],
      cost: list[int],
  ) -> int:
    ans = 0
    # dist[u][v] := the minimum distance to change ('a' + u) to ('a' + v)
    dist = [[math.inf] * 26 for _ in range(26)]

    for a, b, c in zip(original, changed, cost):
      u = ord(a) - ord('a')
      v = ord(b) - ord('a')
      dist[u][v] = min(dist[u][v], c)

    for k in range(26):
      for i in range(26):
        if dist[i][k] < math.inf:
          for j in range(26):
            if dist[k][j] < math.inf:
              dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    for s, t in zip(source, target):
      if s == t:
        continue
      u = ord(s) - ord('a')
      v = ord(t) - ord('a')
      if dist[u][v] == math.inf:
        return -1
      ans += dist[u][v]

    return ans
```

---

## 🧠 Dry Run
### Input
```
source = "abcd", target = "acbe"
original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]
```
### Steps
```
1. Build dist matrix with given conversions.
2. Floyd-Warshall computes all-pairs shortest paths among 26 characters.
3. Position 0: 'a' -> 'a' => skip (same)
4. Position 1: 'b' -> 'c' => dist[1][2] = 5 => ans = 5
5. Position 2: 'c' -> 'b' => dist[2][1] = 5 => ans = 10
6. Position 3: 'd' -> 'e' => dist[3][4] = 20 => ans = 30
   But indirect path d->e might be cheaper via Floyd-Warshall.
Result: 28
```

---

## ⏱️ Time Complexity
```
O(26^3 + n) where n is the length of source/target. Floyd-Warshall on 26 nodes is O(26^3) = O(1).
```

## 💾 Space Complexity
```
O(26^2) = O(1) for the distance matrix.
```

---

## ⚠️ Edge Cases
- Source and target are identical: return 0.
- A conversion is impossible for some character pair: return -1.
- Multiple edges between the same character pair: take the minimum cost.

---

## 🎯 Interview Takeaways
- Floyd-Warshall is ideal when the graph is small (26 nodes for lowercase letters).
- Recognizing the problem as an all-pairs shortest path problem is the key insight.
- Always handle the case where source and target characters are the same (skip, no cost).

---

## 📌 Key Pattern
👉 **"Small-graph Floyd-Warshall for character conversion costs"**

---

## 🔁 Related Problems
- 2977. Minimum Cost to Convert String II
- 743. Network Delay Time
- 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance

---

## 🚀 Final Thoughts
This problem elegantly reduces to a shortest path problem on a tiny graph. The 26-node constraint makes Floyd-Warshall extremely efficient, turning what could be a complex string transformation into a simple graph problem.

---

✨ **Rule to remember:**
> When character conversions have costs, build a shortest-path graph over the alphabet and use Floyd-Warshall for all-pairs minimum costs.
