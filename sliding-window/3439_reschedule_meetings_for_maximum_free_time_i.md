# 3439. Reschedule Meetings for Maximum Free Time I

## 🔗 Problem Link
https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Sliding Window, Greedy

---

## 🧩 Problem Summary
Given an event timeline of length eventTime with n scheduled meetings (defined by startTime and endTime arrays), you can reschedule at most k meetings (move them to other free slots). Find the maximum contiguous free time achievable.

### 📌 Constraints
- 1 <= eventTime <= 10^9
- 1 <= n <= 10^5
- 0 <= k <= n

---

## 💭 Intuition
👉 Compute the gaps between consecutive meetings (including before the first and after the last). Removing k consecutive meetings merges k+1 consecutive gaps. Use a sliding window of size k+1 over the gaps array to find the maximum sum.

---

## ⚡ Approach — Sliding Window on Gaps

### 🧠 Idea
- Build a gaps array: gap before meeting 0, gaps between consecutive meetings, gap after last meeting.
- The gaps array has n+1 elements.
- Moving k meetings is equivalent to merging k+1 consecutive gaps (the meetings between them are relocated).
- Slide a window of size k+1 and find the maximum sum.

---

## 💻 Code

```cpp
class Solution {
 public:
  int maxFreeTime(int eventTime, int k, vector<int>& startTime,
                  vector<int>& endTime) {
    const vector<int> gaps = getGaps(eventTime, startTime, endTime);
    int windowSum = accumulate(gaps.begin(), gaps.begin() + k + 1, 0);
    int ans = windowSum;

    for (int i = k + 1; i < gaps.size(); ++i) {
      windowSum += gaps[i] - gaps[i - k - 1];
      ans = max(ans, windowSum);
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
eventTime = 10, k = 1, startTime = [1, 4, 7], endTime = [2, 5, 8]
```
### Steps
```
gaps = [1, 2, 2, 2]  (before m0, m0-m1, m1-m2, after m2)

Window size = k+1 = 2
Initial window [0..1]: sum = 1+2 = 3, ans = 3
i=2: sum = 3 + 2 - 1 = 4, ans = 4
i=3: sum = 4 + 2 - 2 = 4, ans = 4

Result: 4
```

---

## ⏱️ Time Complexity
```
O(n) — building gaps and sliding window
```

## 💾 Space Complexity
```
O(n) — for the gaps array
```

---

## ⚠️ Edge Cases
- k = 0 → maximum single gap
- k >= n → all meetings removed, answer = eventTime - total meeting time
- Only one meeting → gaps = [startTime[0], eventTime - endTime[0]]

---

## 🎯 Interview Takeaways
- Converting a meeting schedule to a "gaps" representation simplifies many problems.
- Removing k consecutive items between gaps merges k+1 gaps — this is the key insight.
- Fixed-size sliding window is the go-to technique for maximum sum of k+1 consecutive elements.

---

## 📌 Key Pattern
👉 **"Gaps array + fixed-size sliding window"**

---

## 🔁 Related Problems
- 3440. Reschedule Meetings for Maximum Free Time II
- 1423. Maximum Points You Can Obtain from Cards

---

## 🚀 Final Thoughts
The clever reduction from "reschedule k meetings" to "find the maximum sum of k+1 consecutive gaps" makes this problem solvable in linear time with a simple sliding window.

---

✨ **Rule to remember:**
> Rescheduling k meetings merges k+1 adjacent gaps — slide a window of size k+1 over the gaps array.
