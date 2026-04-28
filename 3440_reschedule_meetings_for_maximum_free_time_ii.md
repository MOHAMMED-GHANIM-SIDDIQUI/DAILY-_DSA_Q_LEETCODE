# 3440. Reschedule Meetings for Maximum Free Time II

## 🔗 Problem Link
https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Greedy, Prefix/Suffix Max

---

## 🧩 Problem Summary
Given an event timeline with n scheduled meetings, you can reschedule at most one meeting by moving it to any free slot. Find the maximum contiguous free time achievable. The moved meeting must fit entirely within an existing gap.

### 📌 Constraints
- 1 <= eventTime <= 10^9
- 1 <= n <= 10^5
- Meetings are non-overlapping and sorted

---

## 💭 Intuition
👉 For each meeting i, removing it merges gaps[i] + gaps[i+1]. But the meeting can only be relocated if there exists another gap large enough to hold it. Use prefix-max and suffix-max arrays over the gaps to check if such a gap exists outside the adjacent gaps.

---

## ⚡ Approach — Prefix/Suffix Max on Gaps

### 🧠 Idea
- Build the gaps array (n+1 elements).
- Build maxLeft[i] = max of gaps[0..i] and maxRight[i] = max of gaps[i..n].
- For each meeting i, compute adjacentGapsSum = gaps[i] + gaps[i+1].
- Check if the meeting duration fits in max(maxLeft[i-1], maxRight[i+2]).
- If yes, the total free time = adjacentGapsSum + meetingDuration.
- Otherwise, total free time = adjacentGapsSum only.
- Return the maximum over all meetings.

---

## 💻 Code

```cpp
class Solution {
 public:
  int maxFreeTime(int eventTime, vector<int>& startTime, vector<int>& endTime) {
    const int n = startTime.size();
    const vector<int> gaps = getGaps(eventTime, startTime, endTime);
    int ans = 0;
    vector<int> maxLeft(n + 1);   // maxLeft[i] := max(gaps[0..i])
    vector<int> maxRight(n + 1);  // maxRight[i] := max(gaps[i..n])

    maxLeft[0] = gaps[0];
    maxRight[n] = gaps[n];

    for (int i = 1; i < n + 1; ++i)
      maxLeft[i] = max(gaps[i], maxLeft[i - 1]);

    for (int i = n - 1; i >= 0; --i)
      maxRight[i] = max(gaps[i], maxRight[i + 1]);

    for (int i = 0; i < n; ++i) {
      const int currMeetingTime = endTime[i] - startTime[i];
      const int adjacentGapsSum = gaps[i] + gaps[i + 1];
      const bool canMoveMeeting =
          currMeetingTime <= max(i > 0 ? maxLeft[i - 1] : 0,  //
                                 i + 2 < n + 1 ? maxRight[i + 2] : 0);
      ans = max(ans, adjacentGapsSum + (canMoveMeeting ? currMeetingTime : 0));
    }

    return ans;
  }

 private:
  vector<int> getGaps(int eventTime, const vector<int>& startTime,
                      const vector<int>& endTime) {
    vector<int> gaps{startTime[0]};
    for (int i = 1; i < startTime.size(); ++i)
      gaps.push_back(startTime[i] - endTime[i - 1]);
    gaps.push_back(eventTime - endTime.back());
    return gaps;
  }
};
```

---

## 🧠 Dry Run
### Input
```
eventTime = 14, startTime = [1, 5, 8], endTime = [3, 6, 13]
```
### Steps
```
gaps = [1, 2, 2, 1]
maxLeft  = [1, 2, 2, 2]
maxRight = [2, 2, 2, 1]

i=0: meeting dur=2, adjGaps=1+2=3
  canMove: max(0, maxRight[2])=max(0,2)=2 >= 2 → yes
  ans = max(0, 3+2) = 5

i=1: meeting dur=1, adjGaps=2+2=4
  canMove: max(maxLeft[0], maxRight[3])=max(1,1)=1 >= 1 → yes
  ans = max(5, 4+1) = 5

i=2: meeting dur=5, adjGaps=2+1=3
  canMove: max(maxLeft[1], 0)=max(2,0)=2 >= 5? No
  ans = max(5, 3+0) = 5

Result: 5
```

---

## ⏱️ Time Complexity
```
O(n) — linear scans for gaps, prefix/suffix max, and final check
```

## 💾 Space Complexity
```
O(n) — gaps, maxLeft, and maxRight arrays
```

---

## ⚠️ Edge Cases
- Only one meeting → removing it gives the entire eventTime minus 0 (if it can be relocated, answer is eventTime; but there's no other gap to move it to, so answer is max(gaps[0], gaps[1]))
- Meeting exactly fits in another gap → can be moved
- No gap large enough for any meeting → answer is max adjacent gap sum

---

## 🎯 Interview Takeaways
- Prefix-max and suffix-max arrays enable O(1) range-max queries.
- When "moving" an element, check if there's space elsewhere using precomputed structures.
- The gaps representation transforms scheduling problems into array problems.

---

## 📌 Key Pattern
👉 **"Gaps array + prefix/suffix max for single-move optimization"**

---

## 🔁 Related Problems
- 3439. Reschedule Meetings for Maximum Free Time I
- 1423. Maximum Points You Can Obtain from Cards

---

## 🚀 Final Thoughts
This extends the Part I problem by allowing only one meeting to be moved (not just removed). The prefix/suffix max check elegantly determines feasibility of relocation in O(1) per meeting.

---

✨ **Rule to remember:**
> To check if a removed meeting can be relocated, use prefix-max and suffix-max of gaps to find a suitable slot in O(1).
