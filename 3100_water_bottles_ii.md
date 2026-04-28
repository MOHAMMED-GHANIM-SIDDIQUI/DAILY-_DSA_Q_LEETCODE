# 3100. Water Bottles II

## 🔗 Problem Link
https://leetcode.com/problems/water-bottles-ii/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Math, Simulation

---

## 🧩 Problem Summary
You have `numBottles` full water bottles and can exchange `numExchange` empty bottles for one full bottle, but after each exchange the cost increases by 1. Return the maximum number of bottles you can drink.

### 📌 Constraints
- 1 <= numBottles <= 100
- 3 <= numExchange <= 100

---

## 💭 Intuition
👉 Simulate the process: drink all bottles, exchange empties when possible, and increment the exchange cost after each trade.

---

## ⚡ Approach — Simulation

### 🧠 Idea
- Start with ans = numBottles (drink them all)
- While you have enough empties to exchange: trade numExchange empties for 1 bottle, drink it, increase the exchange rate
- The remaining empties after each exchange = numBottles - numExchange + 1

---

## 💻 Code

```cpp
class Solution {
 public:
  int maxBottlesDrunk(int numBottles, int numExchange) {
    int ans = numBottles;

    while (numBottles >= numExchange) {
      numBottles = (numBottles - numExchange + 1);
      ++numExchange;
      ++ans;
    }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
numBottles = 13, numExchange = 6
```
### Steps
```
ans=13, bottles=13, exchange=6
bottles=13>=6: bottles=13-6+1=8, exchange=7, ans=14
bottles=8>=7:  bottles=8-7+1=2,  exchange=8, ans=15
bottles=2<8:   stop
Result: 15
```

---

## ⏱️ Time Complexity
```
O(sqrt(numBottles)) — each exchange increases cost, so iterations are limited
```

## 💾 Space Complexity
```
O(1) — constant extra space
```

---

## ⚠️ Edge Cases
- numBottles < numExchange — no exchange possible, answer is numBottles
- numBottles = 1 — just drink the one bottle
- Large numBottles with small numExchange — many exchanges but cost grows fast

---

## 🎯 Interview Takeaways
- Simple simulation problems should be solved directly without overcomplicating
- The increasing exchange rate ensures the loop terminates quickly
- Track state carefully: bottles remaining vs. bottles drunk

---

## 📌 Key Pattern
👉 **"Simulate with increasing cost until resources are exhausted"**

---

## 🔁 Related Problems
- 1518. Water Bottles
- 1342. Number of Steps to Reduce a Number to Zero

---

## 🚀 Final Thoughts
This is a straightforward simulation problem. The key difference from the classic Water Bottles problem is the increasing exchange rate, which naturally bounds the number of iterations and simplifies the solution.

---

✨ **Rule to remember:**
> Simulate exchanges with increasing cost; each round: subtract, add one, increment rate.
