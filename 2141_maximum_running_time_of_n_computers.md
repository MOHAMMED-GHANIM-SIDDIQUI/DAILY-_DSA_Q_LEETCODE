# 2141. Maximum Running Time of N Computers

## 🔗 Problem Link
https://leetcode.com/problems/maximum-running-time-of-n-computers/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Binary Search, Greedy, Sorting

---

## 🧩 Problem Summary
You have `n` computers and an array `batteries` where `batteries[i]` is the number of minutes the i-th battery can run a computer. You can swap batteries between computers at any time. All `n` computers must run simultaneously for the same amount of time. Return the maximum number of minutes all `n` computers can run simultaneously.

### 📌 Constraints
- `1 <= n <= batteries.length <= 10^5`
- `1 <= batteries[i] <= 10^9`

---

## 💭 Intuition
👉 If the largest battery exceeds the average running time per computer, it will be "dedicated" to one computer. Remove it and reduce `n` by 1. Repeat until the largest battery fits within the average, then the answer is `total_sum / n`.

---

## ⚡ Approach — Greedy Reduction

### 🧠 Idea
- Sort the batteries.
- While the largest battery exceeds `sum / n`, it must power one computer alone. Remove it, decrement `n`, and subtract it from the sum.
- Once no battery exceeds the average, all batteries can be shared optimally, and the answer is `sum // n`.

---

## 💻 Code

```python
class Solution:
  def maxRunTime(self, n: int, batteries: list[int]) -> int:
    summ = sum(batteries)

    batteries.sort()

    # The maximum battery is greater than the average, so it can last forever.
    # Reduce the problem from size n to size n - 1.
    while batteries[-1] > summ // n:
      summ -= batteries.pop()
      n -= 1

    # If the maximum battery <= average running time, it won't be waste, and so
    # do smaller batteries.
    return summ // n
```

---

## 🧠 Dry Run
### Input
```
n = 2, batteries = [1, 1, 1, 1]
```
### Steps
```
summ = 4, sorted batteries = [1, 1, 1, 1]
batteries[-1] = 1, summ // n = 4 // 2 = 2
1 <= 2 -> while loop doesn't execute
Return 4 // 2 = 2
```

---

## ⏱️ Time Complexity
```
O(m log m), where m is the number of batteries (due to sorting)
```

## 💾 Space Complexity
```
O(1) extra space (sorting in place)
```

---

## ⚠️ Edge Cases
- One computer: answer is the sum of all batteries
- Each computer gets exactly one battery: answer is the minimum battery
- All batteries are equal: answer is `total / n`
- One very large battery: it powers one computer, rest share remaining

---

## 🎯 Interview Takeaways
- The greedy insight: a battery larger than the average must be assigned to one computer.
- Once all batteries are <= average, they can be perfectly shared.
- This is simpler than binary search and runs in O(m log m).

---

## 📌 Key Pattern
👉 **"Remove oversized items that exceed the average, then distribute the rest evenly"**

---

## 🔁 Related Problems
- 2071. Maximum Number of Tasks You Can Assign
- 1648. Sell Diminishing-Valued Colored Balls
- 2064. Minimized Maximum of Products Distributed to Any Store

---

## 🚀 Final Thoughts
This problem has an elegant greedy solution that avoids the complexity of binary search. The key observation is that a battery exceeding the average must be dedicated to one computer, reducing the problem size. The final answer is simply the total remaining energy divided by the remaining computers.

---

✨ **Rule to remember:**
> When the largest item exceeds the average, it gets its own slot; once all fit within the average, distribute evenly.
