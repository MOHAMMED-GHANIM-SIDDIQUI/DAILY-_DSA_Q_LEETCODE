# 3075. Maximize Happiness of Selected Children

## 🔗 Problem Link
https://leetcode.com/problems/maximize-happiness-of-selected-children/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Greedy, Sorting

---

## 🧩 Problem Summary
Given an array `happiness` of children's happiness values and an integer `k`, select `k` children one by one. Each time you select a child, the happiness of all remaining (unselected) children decreases by 1. A child's happiness cannot go below 0. Return the maximum total happiness you can achieve.

### 📌 Constraints
- `1 <= n <= 2 * 10^5`
- `1 <= happiness[i] <= 10^8`
- `1 <= k <= n`

---

## 💭 Intuition
👉 Sort in descending order and always pick the happiest remaining child. The i-th child selected (0-indexed) loses `i` happiness due to previous selections. Stop early if the adjusted happiness becomes non-positive.

---

## ⚡ Approach — Greedy with Sorting

### 🧠 Idea
- Sort `happiness` in descending order.
- For the i-th selection, the effective happiness is `happiness[i] - i`.
- If the effective happiness drops to 0 or below, stop (further selections add nothing).
- Sum up all positive effective happiness values.

---

## 💻 Code

```python
class Solution:
  def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        happiness.sort(reverse = True)

        res = 0

        for i in range(k):
            gain = happiness[i] - i

            if gain <= 0:
                return res

            res += gain

        return res
```

---

## 🧠 Dry Run
### Input
```
happiness = [1, 2, 3], k = 2
```
### Steps
```
1. Sort descending: [3, 2, 1]
2. i=0: gain = 3 - 0 = 3, res = 3
3. i=1: gain = 2 - 1 = 1, res = 4
Result: 4
```

---

## ⏱️ Time Complexity
```
O(n log n) for sorting.
```

## 💾 Space Complexity
```
O(1) extra space (in-place sort).
```

---

## ⚠️ Edge Cases
- `k == 1`: just return the maximum happiness value.
- All happiness values are 1 and k > 1: only the first selection contributes.
- Very large happiness values: no early termination, sum all k adjusted values.

---

## 🎯 Interview Takeaways
- When each subsequent selection has a penalty, sort greedily and account for the penalty.
- The "decreasing happiness" translates to a simple index-based penalty after sorting.
- Early termination when gain <= 0 is an important optimization.

---

## 📌 Key Pattern
👉 **"Greedy selection with diminishing returns — sort descending and subtract index penalty"**

---

## 🔁 Related Problems
- 1029. Two City Scheduling
- 455. Assign Cookies
- 2144. Minimum Cost of Buying Candies With Discount

---

## 🚀 Final Thoughts
The key insight is that the happiness penalty for the i-th pick is exactly `i`, because `i` rounds of decrement have occurred. Sorting descending ensures we always maximize the net gain at each step.

---

✨ **Rule to remember:**
> When each pick reduces future values by 1, sort descending and subtract the pick index — stop when the net gain hits zero.
