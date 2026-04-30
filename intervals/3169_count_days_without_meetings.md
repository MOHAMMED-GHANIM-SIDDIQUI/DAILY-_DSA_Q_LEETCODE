# 3169. Count Days Without Meetings

## 🔗 Problem Link
https://leetcode.com/problems/count-days-without-meetings/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Sorting, Intervals

---

## 🧩 Problem Summary
Given a total number of `days` and a list of meeting intervals, count the number of days that are free (not covered by any meeting). Meetings can overlap.

### 📌 Constraints
- 1 <= days <= 10^9
- 1 <= meetings.length <= 10^5
- meetings[i].length == 2
- 1 <= meetings[i][0] <= meetings[i][1] <= days

---

## 💭 Intuition
👉 Sort meetings by start time, merge overlapping intervals, and count the gaps between them plus any remaining days after the last meeting.

---

## ⚡ Approach — Sort and Sweep

### 🧠 Idea
- Sort meetings by start time
- Track the latest end time seen (prevEnd)
- For each meeting, if it starts after prevEnd, add the gap to freeDays
- Update prevEnd to the max of itself and the current meeting's end
- After all meetings, add remaining days after prevEnd

---

## 💻 Code

```cpp
class Solution {
public:
    int countDays(int days, vector<vector<int>>& meetings) {
        int freeDays = 0;
        int prevEnd = 0;

        // Sort meetings by start time
        sort(meetings.begin(), meetings.end());

        // Loop through each meeting
        for (const vector<int>& meeting : meetings) {
            const int start = meeting[0];
            const int end = meeting[1];

            // Calculate free days between prevEnd and the current meeting's start
            if (start > prevEnd) {
                freeDays += start - prevEnd - 1;
            }

            // Update prevEnd to the latest end time
            prevEnd = max(prevEnd, end);
        }

        // Account for any remaining free days after the last meeting
        return freeDays + max(0, days - prevEnd);
    }
};
```

---

## 🧠 Dry Run
### Input
```
days = 10, meetings = [[5,7],[1,3],[9,10]]
```
### Steps
```
After sort: [[1,3],[5,7],[9,10]]
prevEnd=0
[1,3]: 1>0 -> freeDays += 1-0-1=0, prevEnd=3
[5,7]: 5>3 -> freeDays += 5-3-1=1, prevEnd=7
[9,10]: 9>7 -> freeDays += 9-7-1=1, prevEnd=10
Remaining: max(0, 10-10) = 0
Result: 2
```

---

## ⏱️ Time Complexity
```
O(n log n) — dominated by sorting the meetings
```

## 💾 Space Complexity
```
O(1) — only a few tracking variables (ignoring sort space)
```

---

## ⚠️ Edge Cases
- No meetings — all days are free
- Meetings cover all days — 0 free days
- Fully overlapping meetings — treated as one merged interval
- Single day meetings

---

## 🎯 Interview Takeaways
- Interval gap counting is a classic pattern: sort, sweep, count gaps
- Always handle the tail end (days after last meeting)
- Using prevEnd = 0 as initial handles the gap before the first meeting naturally

---

## 📌 Key Pattern
👉 **"Sort intervals, sweep to count gaps"**

---

## 🔁 Related Problems
- 56. Merge Intervals
- 57. Insert Interval
- 252. Meeting Rooms

---

## 🚀 Final Thoughts
A textbook interval sweep problem. The trick is initializing prevEnd to 0 so the gap before the first meeting is automatically captured, and remembering to handle remaining days after the last meeting.

---

✨ **Rule to remember:**
> Sort intervals by start, sweep with prevEnd, count gaps and the tail.
