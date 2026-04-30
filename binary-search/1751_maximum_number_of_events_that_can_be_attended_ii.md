# 1751. Maximum Number of Events That Can Be Attended II

## 🔗 Problem Link
https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Binary Search, Dynamic Programming, Sorting

---

## 🧩 Problem Summary
Given an array of `events` where `events[i] = [startDay, endDay, value]`, and an integer `k`, find the maximum sum of values from attending at most `k` non-overlapping events (you can only attend one event at a time, and attending an event occupies its full range of days).

### 📌 Constraints
- `1 <= k <= events.length <= 10^6`
- `1 <= k * events.length <= 10^6`
- `1 <= startDay <= endDay <= 10^9`
- `1 <= value <= 10^6`

---

## 💭 Intuition
👉 Sort events by start day. For each event, decide whether to attend it (and jump to the next non-overlapping event) or skip it. Use memoization to avoid recomputation, and binary search to find the next valid event efficiently.

---

## ⚡ Approach — DP with Binary Search

### 🧠 Idea
- Sort events by start day.
- Define `dp(i, k)` = max value from events `i..n` attending at most `k`.
- If we attend event `i`, binary search for the first event `j` where `start[j] > end[i]`, then recurse with `dp(j, k-1) + value[i]`.
- If we skip event `i`, recurse with `dp(i+1, k)`.
- Take the max of both choices.

---

## 💻 Code

```cpp
class Solution {
 public:
  int maxValue(vector<vector<int>>& events, int k) {
    vector<vector<int>> mem(events.size(), vector<int>(k + 1, -1));
    ranges::sort(events);
    return maxValue(events, 0, k, mem);
  }

 private:
  // Returns the maximum sum of values that you can receive by attending
  // events[i..n), where k is the maximum number of attendancevents.
  int maxValue(const vector<vector<int>>& events, int i, int k,
               vector<vector<int>>& mem) {
    if (k == 0 || i == events.size())
      return 0;
    if (mem[i][k] != -1)
      return mem[i][k];

    // Binary search `events` to find the first index j
    // s.t. events[j][0] > events[i][1].
    const auto it = upper_bound(
        events.begin() + i, events.end(), events[i][1],
        [](int end, const vector<int>& event) { return event[0] > end; });
    const int j = distance(events.begin(), it);
    return mem[i][k] = max(events[i][2] + maxValue(events, j, k - 1, mem),
                           maxValue(events, i + 1, k, mem));
  }
};
```

---

## 🧠 Dry Run
### Input
```
events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
```
### Steps
```
After sorting: [[1,2,4],[2,3,1],[3,4,3]]

dp(0,2): attend event[0] (val=4, end=2) → binary search start>2 → j=2
         = max(4 + dp(2,1), dp(1,2))
  dp(2,1): attend event[2] (val=3) → j=3 (out of bounds)
           = max(3+0, dp(3,1)=0) = 3
  dp(1,2): attend event[1] (val=1, end=3) → j=2
           = max(1 + dp(2,1)=3, dp(2,2))
    dp(2,2): = max(3+0, 0) = 3
           = max(4, 3) = 4
  dp(0,2) = max(4+3, 4) = 7

Result: 7
```

---

## ⏱️ Time Complexity
```
O(n * k * log n) — n*k states, each doing a binary search in O(log n)
```

## 💾 Space Complexity
```
O(n * k) — memoization table
```

---

## ⚠️ Edge Cases
- `k = 1` → pick the single event with the highest value.
- All events overlap → can only attend one, pick the most valuable.
- All events are non-overlapping → attend up to `k` most valuable ones.

---

## 🎯 Interview Takeaways
- Sorting + binary search + DP is a classic combo for interval scheduling with values.
- The binary search for the next non-overlapping event is the key optimisation over naive O(n^2).
- Memoisation turns exponential recursion into polynomial.

---

## 📌 Key Pattern
👉 **"Sort intervals, DP on (index, remaining picks), binary search for next non-overlapping event"**

---

## 🔁 Related Problems
- 1235. Maximum Profit in Job Scheduling
- 435. Non-overlapping Intervals
- 1353. Maximum Number of Events That Can Be Attended

---

## 🚀 Final Thoughts
This is the weighted interval scheduling problem generalised to at most `k` picks. The combination of sorting, binary search for the next valid event, and memoised recursion is both elegant and efficient.

---

✨ **Rule to remember:**
> For weighted interval scheduling with limited picks: sort by start, DP on (index, k), and binary search for the next non-overlapping event.
