# 2483. Minimum Penalty for a Shop

## 🔗 Problem Link
https://leetcode.com/problems/minimum-penalty-for-a-shop/

## ⚡ Difficulty
Medium

## 🏷️ Topics
String, Prefix Sum, Greedy

---

## 🧩 Problem Summary
A shop has a `customers` string where `customers[i]` is `'Y'` if customers come at hour `i` and `'N'` if not. If the shop closes at hour `j`, the penalty is the number of `'Y'`s at or after hour `j` plus the number of `'N'`s before hour `j`. Find the earliest hour at which closing gives the minimum penalty.

### 📌 Constraints
- `1 <= customers.length <= 10^5`
- `customers[i]` is either `'Y'` or `'N'`.

---

## 💭 Intuition
👉 Instead of computing penalties directly, flip the perspective: treat `'Y'` as +1 profit and `'N'` as -1. The optimal closing time is right after the point where cumulative profit is maximized — this is equivalent to the maximum subarray prefix sum problem.

---

## ⚡ Approach — Maximum Profit (Greedy)

### 🧠 Idea
- Iterate through the string, maintaining a running profit: +1 for 'Y', -1 for 'N'.
- Track the maximum profit seen and the index where it occurs.
- The closing hour is `maxProfitIndex + 1` (close after the last profitable hour).

---

## 💻 Code

```python
class Solution:
  def bestClosingTime(self, customers: str) -> int:
    # Instead of computing the minimum penalty, we can compute the maximum profit.
    ans = 0
    profit = 0
    maxProfit = 0

    for i, customer in enumerate(customers):
      profit += 1 if customer == 'Y' else -1
      if profit > maxProfit:
        maxProfit = profit
        ans = i + 1

    return ans
```

---

## 🧠 Dry Run
### Input
```
customers = "YYNY"
```
### Steps
```
i=0, 'Y': profit=1, maxProfit=1, ans=1
i=1, 'Y': profit=2, maxProfit=2, ans=2
i=2, 'N': profit=1, no update
i=3, 'Y': profit=2, not > maxProfit, no update

Result: 2 (close at hour 2)
```

---

## ⏱️ Time Complexity
```
O(n) — single pass through the customers string.
```

## 💾 Space Complexity
```
O(1) — constant extra space.
```

---

## ⚠️ Edge Cases
- All 'Y': close at the end (hour n).
- All 'N': close at hour 0 (never open).
- Tie in penalty: return the earliest hour.

---

## 🎯 Interview Takeaways
- Reframing penalty minimization as profit maximization simplifies the logic.
- This is essentially a variant of Kadane's algorithm for prefix sums.
- Greedy single-pass solutions are often possible when the objective is monotonic.

---

## 📌 Key Pattern
👉 **"Reframe min-penalty as max-profit and track the prefix sum peak."**

---

## 🔁 Related Problems
- 53. Maximum Subarray
- 121. Best Time to Buy and Sell Stock
- 1423. Maximum Points You Can Obtain from Cards

---

## 🚀 Final Thoughts
The elegant insight here is that minimizing penalty and maximizing profit are dual perspectives of the same problem. By converting to the profit view, we get a clean O(n) single-pass solution without needing prefix/suffix arrays.

---

✨ **Rule to remember:**
> "When minimizing cost, try flipping to maximize profit — it often simplifies the solution."
