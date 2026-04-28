# 3562. Maximum Profit from Trading Stocks with Discounts

## 🔗 Problem Link
https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Tree, Dynamic Programming, Knapsack, DFS

---

## 🧩 Problem Summary
Given `n` stocks organized in a tree hierarchy, with present and future prices, and a budget, maximize profit by buying stocks. A stock can be bought at full price, or at half price if its parent in the hierarchy is also bought. Each stock can only be bought once.

### 📌 Constraints
- `2 <= n <= 10^4`
- `1 <= present[i], future[i] <= 10^4`
- `0 <= budget <= 10^4`
- The hierarchy forms a tree

---

## 💭 Intuition
👉 This is a tree DP knapsack problem — for each node, decide whether to buy it (at full or half price), and merge children's knapsack arrays using convolution. Track two states: with and without a discount available from the parent.

---

## ⚡ Approach — Tree DP with Knapsack Merge

### 🧠 Idea
- Build the tree from the hierarchy edges.
- DFS from root, returning two knapsack arrays per node: `noDiscount[b]` (best profit using budget `b` without buying current node at discount) and `withDiscount[b]` (with discount available).
- Merge children's knapsack arrays via convolution (subset-sum style).
- For each node, try buying at full cost or half cost, updating the appropriate DP array.

---

## 💻 Code

```python
class Solution:
  def maxProfit(
      self,
      n: int,
      present: list[int],
      future: list[int],
      hierarchy: list[list[int]],
      budget: int,
  ) -> int:
    tree = [[] for _ in range(n)]

    for u, v in hierarchy:
      tree[u - 1].append(v - 1)

    @functools.lru_cache(None)
    def dp(u: int, parent: int) -> tuple[list[int], list[int]]:
      noDiscount = [0] * (budget + 1)
      withDiscount = [0] * (budget + 1)

      for v in tree[u]:
        if v == parent:
          continue
        childNoDiscount, childWithDiscount = dp(v, u)
        noDiscount = self._merge(noDiscount, childNoDiscount)
        withDiscount = self._merge(withDiscount, childWithDiscount)

      newDp0 = noDiscount[:]
      newDp1 = noDiscount[:]

      # 1. Buy current node at full cost (no discount)
      fullCost = present[u]
      for b in range(fullCost, budget + 1):
        profit = future[u] - fullCost
        newDp0[b] = max(newDp0[b], withDiscount[b - fullCost] + profit)

      # 2. Buy current node at half cost (discounted by parent)
      halfCost = present[u] // 2
      for b in range(halfCost, budget + 1):
        profit = future[u] - halfCost
        newDp1[b] = max(newDp1[b], withDiscount[b - halfCost] + profit)

      return newDp0, newDp1

    return max(dp(0, -1)[0])

  def _merge(self, dpA: list[int], dpB: list[int]) -> list[int]:
    merged = [-math.inf] * len(dpA)
    for i, a in enumerate(dpA):
      for j in range(len(dpA) - i):
        merged[i + j] = max(merged[i + j], a + dpB[j])
    return merged
```

---

## 🧠 Dry Run
### Input
```
n=3, present=[4,2,6], future=[6,3,8], hierarchy=[[1,2],[1,3]], budget=5
```
### Steps
```
Tree: 0→[1,2]

dp(1, 0): leaf node
  noDiscount=[0]*6, withDiscount=[0]*6
  Buy at full (cost=2, profit=1): newDp0[2..5] = max(0, 0+1)=1
  Buy at half (cost=1, profit=2): newDp1[1..5] = max(0, 0+2)=2
  return ([0,0,1,1,1,1], [0,2,2,2,2,2])

dp(2, 0): leaf node
  Buy at full (cost=6, profit=2): only if budget≥6, not applicable
  return ([0,0,0,0,0,0], [0,0,0,2,2,2,2])

dp(0, -1): merge children, then buy self
  After merging and buying at full (cost=4, profit=2):
  Best profit at budget=5 → consider combinations

Result: max profit within budget
```

---

## ⏱️ Time Complexity
```
O(n * budget^2) — merging knapsacks at each node costs O(budget^2), done n times
```

## 💾 Space Complexity
```
O(n * budget) — for the DP arrays at each node
```

---

## ⚠️ Edge Cases
- Budget is 0 → profit is 0
- Future price less than present price → buying that stock is never profitable
- All stocks have same cost → straightforward knapsack
- Deep tree → recursion depth concern (use sys.setrecursionlimit)

---

## 🎯 Interview Takeaways
- Tree knapsack requires merging children DP arrays via convolution.
- Tracking two states (with/without discount) elegantly handles the parent-child discount relationship.
- The merge operation is the bottleneck — O(budget^2) per node.

---

## 📌 Key Pattern
👉 **"Tree DP knapsack — merge children via convolution, track discount state from parent."**

---

## 🔁 Related Problems
- 494. Target Sum
- 1269. Number of Ways to Stay in the Same Place After Some Steps
- 2246. Longest Path With Different Adjacent Characters

---

## 🚀 Final Thoughts
This problem combines tree DFS with the classic knapsack pattern. The discount mechanism adds an elegant twist: buying a parent unlocks half-price for children, requiring two parallel DP tracks that interact during the merge phase.

---

✨ **Rule to remember:**
> "Tree knapsack with parent-child dependency: track discounted and non-discounted states, merge children via convolution."
