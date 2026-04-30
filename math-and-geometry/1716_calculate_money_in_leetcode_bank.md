# 1716. Calculate Money in Leetcode Bank

## 🔗 Problem Link
https://leetcode.com/problems/calculate-money-in-leetcode-bank/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Math, Simulation

---

## 🧩 Problem Summary
Hercy deposits money in the Leetcode bank every day. On Monday of the first week he deposits $1, Tuesday $2, ..., Sunday $7. On Monday of the second week he deposits $2, Tuesday $3, and so on (each week starts $1 higher than the previous week's Monday). Given `n` days, return the total amount of money deposited.

### 📌 Constraints
- `1 <= n <= 1000`

---

## 💭 Intuition
👉 Each complete week's sum is 28 plus 7 for each additional week number. Handle remaining days separately using the starting value of the final partial week.

---

## ⚡ Approach — Week-by-Week Summation

### 🧠 Idea
- The first full week totals 28 (1+2+...+7). Each subsequent week adds 7 more (since each day is $1 higher).
- Count the full weeks and remaining days.
- Sum up full weeks, then add the remaining days starting from `(week_count + 1)`.

---

## 💻 Code

```cpp
class Solution {
public:
    int totalMoney(int n) {
        int cur_week=28;
        int how_many_week=n/7;
        int how_many_rem_day=n%7;
        int cur_day=how_many_week+1;
        int ans=0;
        for(int i=0;i<how_many_week;i++)
        {
            ans+=cur_week;
            cur_week+=7;
        }
        for(int i=0;i<how_many_rem_day;i++)
        {
            ans+=cur_day;
            cur_day++;
        }
        return ans;
    }
};
```

---

## 🧠 Dry Run
### Input
```
n = 10
```
### Steps
```
how_many_week = 10/7 = 1
how_many_rem_day = 10%7 = 3
cur_week = 28, cur_day = 2

Week 1: ans += 28 → ans = 28, cur_week = 35
Remaining 3 days:
  day1: ans += 2 → 30
  day2: ans += 3 → 33
  day3: ans += 4 → 37

Result: 37
```

---

## ⏱️ Time Complexity
```
O(n/7 + n%7) = O(n) — but effectively O(1) since n ≤ 1000
```

## 💾 Space Complexity
```
O(1) — constant extra space
```

---

## ⚠️ Edge Cases
- `n = 1` → only Monday of week 1 → answer is 1.
- `n = 7` → exactly one week → answer is 28.
- `n = 1000` → 142 full weeks + 6 remaining days.

---

## 🎯 Interview Takeaways
- Recognise the arithmetic progression pattern in weekly deposits.
- Splitting into full weeks + remaining days simplifies the logic.
- Could also be solved with a closed-form formula using arithmetic series.

---

## 📌 Key Pattern
👉 **"Split into complete cycles (weeks) and a remainder, sum each part separately"**

---

## 🔁 Related Problems
- 1523. Count Odd Numbers in an Interval Range
- 2180. Count Integers With Even Digit Sum
- 1952. Three Divisors

---

## 🚀 Final Thoughts
A straightforward simulation problem. The pattern of increasing weekly deposits forms an arithmetic progression, and handling complete weeks separately from leftover days keeps the code clean.

---

✨ **Rule to remember:**
> When deposits follow a weekly pattern with increments, split into full weeks (arithmetic series) plus remaining days.
