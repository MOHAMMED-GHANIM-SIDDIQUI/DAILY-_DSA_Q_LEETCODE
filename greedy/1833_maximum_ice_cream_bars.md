# 1833. Maximum Ice Cream Bars

## 🔗 Problem Link
https://leetcode.com/problems/maximum-ice-cream-bars/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Greedy, Sorting

---

## 🧩 Problem Summary

A boy has `coins` coins and wants to buy as many ice cream bars as possible. The price of the `i`-th bar is `costs[i]`. The bars can be bought in any order. Return the **maximum number of bars** he can buy with `coins` coins. (Note: he cannot buy a fraction of a bar.)

### 📌 Constraints
- `1 <= costs.length <= 10^5`.
- `1 <= costs[i] <= 10^5`.
- `1 <= coins <= 10^8`.

---

## 💭 Intuition

👉 To maximize the **count** of items bought under a budget, always spend on the **cheapest** items first. Sorting prices ascending and buying greedily from the front guarantees the most bars, because swapping any bought item for a cheaper unbought one would never reduce the count.

---

## ⚡ Approach — Greedy: Buy Cheapest First

### 🧠 Idea
- Sort `costs` in ascending order.
- Walk through the sorted prices, accumulating `cur_cost`.
- The moment `cur_cost` exceeds `coins`, we can't afford this bar → return the count bought so far.
- Otherwise increment the count `ans` and continue.
- If all bars are affordable, return `ans` (= total number of bars).

---

## 💻 Code

```python
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        cur_cost = 0
        ans = 0
        for cost in costs:
            cur_cost+=cost
            if coins<cur_cost:
                return ans
            ans +=1
            
        return ans
```

---

## 🧠 Dry Run

### Input
```
costs = [1, 3, 2, 4, 1], coins = 7
```

### Steps
```
sort -> costs = [1, 1, 2, 3, 4]
cur_cost = 0, ans = 0

cost = 1: cur_cost = 1, 7 < 1? no  -> ans = 1
cost = 1: cur_cost = 2, 7 < 2? no  -> ans = 2
cost = 2: cur_cost = 4, 7 < 4? no  -> ans = 3
cost = 3: cur_cost = 7, 7 < 7? no  -> ans = 4
cost = 4: cur_cost = 11, 7 < 11? yes -> return ans = 4
```

---

## ⏱️ Time Complexity
```
O(n log n)
```
Dominated by sorting the `costs` array; the single greedy pass is `O(n)`.

---

## 💾 Space Complexity
```
O(1)
```
Sorting is done in place and only a few scalar accumulators are used (ignoring sort's internal overhead).

---

## ⚠️ Edge Cases
- The cheapest bar already costs more than `coins` → returns `0` on the first iteration.
- Exactly enough coins for a bar (`cur_cost == coins`) → the strict `coins < cur_cost` test is false, so the bar is bought.
- All bars affordable → loop finishes and returns the full length.

---

## 🎯 Interview Takeaways
- Maximizing item count under a budget is a classic "sort ascending + greedy" pattern.
- The strict `<` comparison correctly treats spending the exact budget as affordable.
- A counting-sort variant gives `O(n + max_cost)` since prices are bounded by `10^5`.

---

## 📌 Key Pattern
👉 **"To buy the most items on a budget, sort by price and take the cheapest first."**

---

## 🔁 Related Problems
- 455. Assign Cookies
- 2233. Maximum Product After K Increments
- 2542. Maximum Subsequence Score
- 561. Array Partition

---

## 🚀 Final Thoughts
A textbook greedy problem: the exchange argument proves that prioritizing cheaper bars is optimal for maximizing count. Sorting makes the greedy choice trivial, and the early `return` keeps the scan tight. Because costs are bounded, a bucket/counting sort could shave the log factor if performance ever mattered.

---

✨ **Rule to remember:**
> "Most items for the money = sort ascending and grab cheapest first until the wallet runs dry."
