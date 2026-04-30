# 2977. Minimum Cost to Convert String II

## 🔗 Problem Link
https://leetcode.com/problems/minimum-cost-to-convert-string-ii/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Graph, Shortest Path, Floyd-Warshall, Dynamic Programming, String

---

## 🧩 Problem Summary
Given two strings `source` and `target` of the same length, and arrays `original`, `changed`, and `cost` where each entry defines a substring-level conversion. Return the minimum cost to convert `source` into `target`, or -1 if impossible. Unlike Problem 2976, conversions operate on substrings rather than single characters.

### 📌 Constraints
- `1 <= source.length == target.length <= 1000`
- `source`, `target` consist of lowercase English letters
- `1 <= cost.length == original.length == changed.length <= 100`
- `1 <= original[i].length == changed[i].length <= source.length`
- `original[i]`, `changed[i]` consist of lowercase English letters
- `1 <= cost[i] <= 10^6`

---

## 💭 Intuition
👉 This extends Problem 2976 from single characters to substrings. We assign an ID to each unique substring, build a shortest-path matrix over those IDs using Floyd-Warshall, then use DP to find the minimum cost to transform the entire source to target.

---

## ⚡ Approach — Floyd-Warshall + DP

### 🧠 Idea
- Map each unique substring from `original` and `changed` to an integer ID.
- Build a distance matrix over these IDs and run Floyd-Warshall.
- Use `dp[i]` to represent the minimum cost to convert the first `i` characters of `source` into `target`.
- For each position, try all possible substring lengths that appear in the conversion rules.
- If `source[i] == target[i]`, we can also advance one character with no cost.

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
    subLengths = set(len(s) for s in original)
    subToId = self._getSubToId(original, changed)
    subCount = len(subToId)
    # dist[u][v] := the minimum distance to change the substring with id u to
    # the substring with id v
    dist = [[math.inf for _ in range(subCount)] for _ in range(subCount)]
    # dp[i] := the minimum cost to change the first i letters of `source` into
    # `target`, leaving the suffix untouched
    dp = [math.inf for _ in range(len(source) + 1)]

    for a, b, c in zip(original, changed, cost):
      u = subToId[a]
      v = subToId[b]
      dist[u][v] = min(dist[u][v], c)

    for k in range(subCount):
      for i in range(subCount):
        if dist[i][k] < math.inf:
          for j in range(subCount):
            if dist[k][j] < math.inf:
              dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    dp[0] = 0

    for i, (s, t) in enumerate(zip(source, target)):
      if dp[i] == math.inf:
        continue
      if s == t:
        dp[i + 1] = min(dp[i + 1], dp[i])
      for subLength in subLengths:
        if i + subLength > len(source):
          continue
        subSource = source[i:i + subLength]
        subTarget = target[i:i + subLength]
        if subSource not in subToId or subTarget not in subToId:
          continue
        u = subToId[subSource]
        v = subToId[subTarget]
        if dist[u][v] != math.inf:
          dp[i + subLength] = min(dp[i + subLength], dp[i] + dist[u][v])

    return -1 if dp[len(source)] == math.inf else dp[len(source)]

  def _getSubToId(self, original: str, changed: str) -> dict[str, int]:
    subToId = {}
    for s in original + changed:
      if s not in subToId:
        subToId[s] = len(subToId)
    return subToId
```

---

## 🧠 Dry Run
### Input
```
source = "abcd", target = "acbe"
original = ["ab","cd"], changed = ["ac","be"], cost = [1,2]
```
### Steps
```
1. subLengths = {2}, subToId = {"ab":0, "cd":1, "ac":2, "be":3}
2. Build dist: dist[0][2]=1, dist[1][3]=2. Floyd-Warshall runs.
3. dp[0] = 0
4. i=0: source[0:2]="ab" -> target[0:2]="ac", dist[0][2]=1 => dp[2] = 1
5. i=2: source[2:4]="cd" -> target[2:4]="be", dist[1][3]=2 => dp[4] = 3
6. Return dp[4] = 3
```

---

## ⏱️ Time Complexity
```
O(S^3 + n * L) where S is the number of unique substrings, n is the string length, and L is the number of distinct substring lengths.
```

## 💾 Space Complexity
```
O(S^2 + n) for the distance matrix and DP array.
```

---

## ⚠️ Edge Cases
- Source equals target: return 0 (dp propagates with zero cost).
- No conversion covers a differing position: return -1.
- Overlapping substring lengths: the DP naturally picks the optimal choice.

---

## 🎯 Interview Takeaways
- Extending single-character conversion to substring conversion requires DP on positions.
- Assign IDs to substrings to keep the Floyd-Warshall matrix manageable.
- The combination of shortest path + DP is a powerful pattern for transformation problems.

---

## 📌 Key Pattern
👉 **"Floyd-Warshall on substring IDs + positional DP for minimum-cost string transformation"**

---

## 🔁 Related Problems
- 2976. Minimum Cost to Convert String I
- 72. Edit Distance
- 1187. Make Array Strictly Increasing

---

## 🚀 Final Thoughts
This hard variant adds substring-level transformations, requiring an additional DP layer on top of Floyd-Warshall. The key is efficiently mapping substrings to IDs and recognizing that Floyd-Warshall still applies to the substring graph.

---

✨ **Rule to remember:**
> For substring-level conversions with costs, combine Floyd-Warshall on a substring ID graph with positional DP to find the global minimum cost.
