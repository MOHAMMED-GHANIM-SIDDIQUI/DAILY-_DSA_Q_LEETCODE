# 2147. Number of Ways to Divide a Long Corridor

## 🔗 Problem Link
https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Math, String, Dynamic Programming

---

## 🧩 Problem Summary
Given a corridor represented as a string of 'S' (seats) and 'P' (plants), divide the corridor into non-overlapping sections using dividers such that each section contains exactly 2 seats. Return the number of ways to install dividers modulo 10^9 + 7.

### 📌 Constraints
- `1 <= corridor.length <= 10^5`
- `corridor[i]` is either `'S'` or `'P'`

---

## 💭 Intuition
👉 Between every pair of 2 seats (groups), the number of plants determines how many positions a divider can be placed. The answer is the product of gaps between consecutive pairs.

---

## ⚡ Approach — Greedy Multiplication of Gaps

### 🧠 Idea
- Count seats left to right; every time we start a new odd-numbered seat (3rd, 5th, ...), multiply the answer by the gap (distance) from the previous seat.
- If the total number of seats is odd or less than 2, return 0.

---

## 💻 Code

```python
class Solution:
  def numberOfWays(self, corridor: str) -> int:
    MOD = 1_000_000_007
    ans = 1
    prevSeat = -1
    numSeats = 0

    for i, c in enumerate(corridor):
      if c == 'S':
        numSeats += 1
        if numSeats > 2 and numSeats % 2 == 1:
          ans = ans * (i - prevSeat) % MOD
        prevSeat = i

    return ans if numSeats > 1 and numSeats % 2 == 0 else 0
```

---

## 🧠 Dry Run
### Input
```
corridor = "SSPPSPS"
```
### Steps
```
i=0, c='S', numSeats=1, prevSeat=0
i=1, c='S', numSeats=2, prevSeat=1
i=2, c='P'
i=3, c='P'
i=4, c='S', numSeats=3 (odd, >2), ans = 1 * (4-1) = 3, prevSeat=4
i=5, c='P'
i=6, c='S', numSeats=4, prevSeat=6
Total seats=4 (even, >1) → ans = 3
```

---

## ⏱️ Time Complexity
```
O(n) — single pass through the corridor string
```

## 💾 Space Complexity
```
O(1) — only a few variables used
```

---

## ⚠️ Edge Cases
- All plants, no seats → return 0
- Odd number of seats → return 0
- Exactly 2 seats → return 1
- No plants between pairs → only 1 way for that gap

---

## 🎯 Interview Takeaways
- Multiplicative counting of independent choices is a powerful combinatorial technique.
- Modular arithmetic must be applied at each multiplication step to avoid overflow.
- Greedy single-pass solutions can replace DP when structure is simple enough.

---

## 📌 Key Pattern
👉 **"Multiply the gaps between fixed groups to count arrangements"**

---

## 🔁 Related Problems
- 1423. Maximum Points You Can Obtain from Cards
- 1573. Number of Ways to Split a String
- 2033. Minimum Operations to Make a Uni-Value Grid

---

## 🚀 Final Thoughts
This problem elegantly reduces to counting the plants between consecutive seat-pairs and multiplying those gap sizes. Recognizing the multiplicative structure avoids complex DP entirely.

---

✨ **Rule to remember:**
> "Between every two seat-pairs, the number of divider positions equals the gap size — multiply all gaps for the answer."
