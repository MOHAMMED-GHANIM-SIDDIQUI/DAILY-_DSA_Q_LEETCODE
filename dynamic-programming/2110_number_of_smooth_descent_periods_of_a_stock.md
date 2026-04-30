# 2110. Number of Smooth Descent Periods of a Stock

## 🔗 Problem Link
https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Dynamic Programming, Math

---

## 🧩 Problem Summary
Given an array `prices` where `prices[i]` is the stock price on day `i`, a smooth descent period is a contiguous subarray where each element is exactly 1 less than the previous. A single day is also a smooth descent period. Return the total number of smooth descent periods.

### 📌 Constraints
- `1 <= prices.length <= 10^5`
- `1 <= prices[i] <= 10^5`

---

## 💭 Intuition
👉 If day `i` continues a smooth descent (prices[i] == prices[i-1] - 1), then it extends all descent periods ending at day `i-1` and adds one new single-day period. We can track the current streak length with a simple counter.

---

## ⚡ Approach — Dynamic Programming (Running Counter)

### 🧠 Idea
- Maintain `dp` as the length of the current smooth descent streak ending at index `i`.
- If `prices[i] == prices[i-1] - 1`, increment `dp`; otherwise reset to 1.
- Add `dp` to the answer at each step (dp counts all subarrays ending at i).

---

## 💻 Code

```python
class Solution:
  def getDescentPeriods(self, prices: list[int]) -> int:
    ans = 1  # prices[0]
    dp = 1

    for i in range(1, len(prices)):
      if prices[i] == prices[i - 1] - 1:
        dp += 1
      else:
        dp = 1
      ans += dp

    return ans
```

---

## 🧠 Dry Run
### Input
```
prices = [3, 2, 1, 4]
```
### Steps
```
i=0: dp=1, ans=1
i=1: prices[1]=2 == prices[0]-1=2 → dp=2, ans=1+2=3
i=2: prices[2]=1 == prices[1]-1=1 → dp=3, ans=3+3=6
i=3: prices[3]=4 != prices[2]-1=0 → dp=1, ans=6+1=7

Subarrays: [3],[2],[1],[4],[3,2],[2,1],[3,2,1] → 7
```

---

## ⏱️ Time Complexity
```
O(n) — single pass through the prices array.
```

## 💾 Space Complexity
```
O(1) — only two variables used.
```

---

## ⚠️ Edge Cases
- Single element: returns 1.
- All prices the same: each day is its own period, returns n.
- Entire array is a smooth descent: returns n*(n+1)/2.

---

## 🎯 Interview Takeaways
- Counting subarrays ending at each position is a classic DP pattern.
- A running counter avoids the need for a full DP array.
- The trick of "streak length = number of subarrays ending here" appears in many problems.

---

## 📌 Key Pattern
👉 **"Count subarrays by tracking the streak length ending at each position."**

---

## 🔁 Related Problems
- 413. Arithmetic Slices
- 978. Longest Turbulent Subarray
- 1759. Count Number of Homogenous Substrings

---

## 🚀 Final Thoughts
This is a textbook example of the "running counter" DP pattern. By maintaining the current streak length, each position contributes exactly `dp` new subarrays to the total count, giving us an elegant O(n) solution.

---

✨ **Rule to remember:**
> "Each extension of a streak by 1 adds exactly (streak length) new subarrays."
