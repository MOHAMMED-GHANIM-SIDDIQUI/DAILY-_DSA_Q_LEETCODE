# 1518. Water Bottles

## 🔗 Problem Link
https://leetcode.com/problems/water-bottles/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Math, Simulation

---

## 🧩 Problem Summary
You have `numBottles` full water bottles. You can exchange `numExchange` empty bottles for one full water bottle. Return the maximum number of water bottles you can drink.

### 📌 Constraints
- `1 <= numBottles <= 100`
- `2 <= numExchange <= 100`

---

## 💭 Intuition
👉 After drinking all bottles, you have that many empties. Keep exchanging empties for full bottles (and drinking them) until you don't have enough empties to exchange. Track the remainder empties that carry over.

---

## ⚡ Approach — Simulation

### 🧠 Idea
- Start with `ans = numBottles` (drink all initial bottles).
- Track `empty = numBottles` (all become empty after drinking).
- While `empty >= numExchange`: exchange to get `empty / numExchange` new full bottles.
- Drink the new bottles (add to `ans`), update empties as `remainder + newBottles`.
- Repeat until not enough empties to exchange.

---

## 💻 Code

```cpp
class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int ans = numBottles;
        int empty = numBottles;

        while (empty >= numExchange) {
            int newBottles = empty / numExchange;
            ans += newBottles;
            empty = empty % numExchange + newBottles; // leftover + new empty bottles
        }

        return ans;
    }
};
```

---

## 🧠 Dry Run
### Input
```
numBottles = 9, numExchange = 3
```
### Steps
```
Initial: ans = 9, empty = 9
Round 1: newBottles = 9/3 = 3, ans = 12, empty = 0 + 3 = 3
Round 2: newBottles = 3/3 = 1, ans = 13, empty = 0 + 1 = 1
empty(1) < numExchange(3) → stop
Answer: 13
```

---

## ⏱️ Time Complexity
```
O(log_{numExchange}(numBottles)), as empties reduce by a factor each round
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- `numBottles < numExchange` — no exchanges possible, answer is `numBottles`.
- `numExchange = 2` — maximum exchanges, answer is `2 * numBottles - 1`.
- `numBottles = 1` — answer is 1.

---

## 🎯 Interview Takeaways
- Simple simulation problems should be solved cleanly without overcomplicating.
- Track both the integer division (new bottles) and remainder (leftover empties).
- A mathematical formula also exists: `ans = numBottles + (numBottles - 1) / (numExchange - 1)`.

---

## 📌 Key Pattern
👉 **"Simulate the exchange loop: divide empties, carry over remainder"**

---

## 🔁 Related Problems
- 1342 — Number of Steps to Reduce a Number to Zero
- 1281 — Subtract the Product and Sum of Digits

---

## 🚀 Final Thoughts
A straightforward simulation problem. The key is correctly handling the leftover empties that carry forward to the next round. The loop terminates quickly since the number of empties decreases geometrically.

---

✨ **Rule to remember:**
> "Exchange empties for full bottles, drink them, and carry the remainder — repeat until you can't exchange."
