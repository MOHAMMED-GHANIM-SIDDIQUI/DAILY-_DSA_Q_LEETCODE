# 1722. Minimize Hamming Distance After Swap Operations

## 🔗 Problem Link
https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Union-Find, Depth-First Search

---

## 🧩 Problem Summary
Given arrays `source` and `target` of the same length, and a list of `allowedSwaps` (pairs of indices), you can swap elements in `source` at allowed indices any number of times. Return the minimum Hamming distance (number of positions where `source[i] != target[i]`) achievable.

### 📌 Constraints
- `n == source.length == target.length`
- `1 <= n <= 10^5`
- `1 <= source[i], target[i] <= 10^5`
- `0 <= allowedSwaps.length <= 10^5`
- `allowedSwaps[i].length == 2`
- `0 <= ai, bi <= n - 1`

---

## 💭 Intuition
👉 Indices connected by swaps form groups where elements can be freely rearranged. Within each group, we can match as many source values to target values as possible — unmatched values contribute to the Hamming distance.

---

## ⚡ Approach — Union-Find with Frequency Counting

### 🧠 Idea
- Use Union-Find to group indices connected by allowed swaps.
- For each group, count the frequency of each value in `source`.
- For each index, check if the `target` value exists in the same group's frequency map; if so, "use" one occurrence; otherwise, increment Hamming distance.

---

## 💻 Code

```python
class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        n = len(source)

        parent = list(range(n))
        rank = [0] * n

        # Find with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # Union by rank
        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return

            if rank[rootX] < rank[rootY]:
                rootX, rootY = rootY, rootX

            parent[rootY] = rootX

            if rank[rootX] == rank[rootY]:
                rank[rootX] += 1

        # Step 1: Build components
        for x, y in allowedSwaps:
            union(x, y)

        # Step 2: Count frequency per group
        from collections import defaultdict

        groupFreq = defaultdict(lambda: defaultdict(int))

        for i in range(n):
            p = find(i)
            groupFreq[p][source[i]] += 1

        # Step 3: Calculate Hamming distance
        hamming = 0

        for i in range(n):
            p = find(i)
            if groupFreq[p][target[i]] > 0:
                groupFreq[p][target[i]] -= 1
            else:
                hamming += 1

        return hamming
```

---

## 🧠 Dry Run
### Input
```
source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
```
### Steps
```
Union(0,1) → group {0,1}
Union(2,3) → group {2,3}

Group 0: source values {1:1, 2:1}
Group 2: source values {3:1, 4:1}

i=0: target=2, group 0 has 2 → use it, freq={1:1, 2:0}
i=1: target=1, group 0 has 1 → use it, freq={1:0, 2:0}
i=2: target=4, group 2 has 4 → use it, freq={3:1, 4:0}
i=3: target=5, group 2 no 5 → hamming=1

Result: 1
```

---

## ⏱️ Time Complexity
```
O(n * α(n)) — nearly O(n) with path compression and union by rank
```

## 💾 Space Complexity
```
O(n) — for parent array and frequency maps
```

---

## ⚠️ Edge Cases
- No allowed swaps → Hamming distance is the direct mismatch count.
- All indices are connected → elements can be freely rearranged, minimum Hamming is determined by value multiset difference.
- Duplicate values in source/target → frequency counting handles them correctly.

---

## 🎯 Interview Takeaways
- Union-Find is the natural tool when swaps define equivalence classes.
- Within each connected component, elements are freely permutable.
- Frequency matching within groups gives the optimal assignment.

---

## 📌 Key Pattern
👉 **"Union-Find to group swappable indices, then frequency-match within each group"**

---

## 🔁 Related Problems
- 1202. Smallest String With Swaps
- 947. Most Stones Removed with Same Row or Column
- 765. Couples Holding Hands

---

## 🚀 Final Thoughts
A classic Union-Find application. The key insight is that transitivity of swaps means any permutation within a connected component is achievable, reducing the problem to a per-group frequency matching exercise.

---

✨ **Rule to remember:**
> Swap chains create equivalence classes — use Union-Find to group them, then match values within each group.
