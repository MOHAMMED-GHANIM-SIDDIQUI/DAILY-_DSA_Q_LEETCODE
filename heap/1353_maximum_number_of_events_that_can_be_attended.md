# 1353. Maximum Number of Events That Can Be Attended

## 🔗 Problem Link
https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Greedy, Sorting, Heap (Priority Queue)

---

## 🧩 Problem Summary
Given an array of events where `events[i] = [startDay, endDay]`, you can attend an event on any single day in its range `[startDay, endDay]`. You can only attend one event per day. Return the maximum number of events you can attend.

### 📌 Constraints
- `1 <= events.length <= 10^5`
- `events[i].length == 2`
- `1 <= startDayi <= endDayi <= 10^5`

---

## 💭 Intuition
👉 Greedily attend the event that ends the earliest on each day, because events ending sooner have fewer future opportunities. A min-heap on end days enables this efficiently.

---

## ⚡ Approach — Greedy + Min-Heap

### 🧠 Idea
- Sort events by start day.
- Iterate through days; on each day, push all newly available events (by end day) into a min-heap.
- Pop and attend the event with the smallest end day.
- Remove expired events (end day < current day) from the heap.
- If the heap is empty, jump to the next event's start day.

---

## 💻 Code

```cpp
class Solution {
 public:
  int maxEvents(vector<vector<int>>& events) {
    int ans = 0;
    int d = 0;  // the current day
    int i = 0;  // events' index
    priority_queue<int, vector<int>, greater<>> minHeap;

    ranges::sort(events);

    while (!minHeap.empty() || i < events.size()) {
      // If no events are available to attend today, let time flies to the next
      // available event.
      if (minHeap.empty())
        d = events[i][0];
      // All the events starting from today are newly available.
      while (i < events.size() && events[i][0] == d)
        minHeap.push(events[i++][1]);
      // Greedily attend the event that'll end the earliest since it has higher
      // chance can't be attended in the future.
      minHeap.pop();
      ++ans;
      ++d;
      // Pop the events that can't be attended.
      while (!minHeap.empty() && minHeap.top() < d)
        minHeap.pop();
    }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
events = [[1,2],[2,3],[3,4]]
```
### Steps
```
Sort → [[1,2],[2,3],[3,4]]
d=1: push end=2 → heap={2}, attend → ans=1, d=2
d=2: push end=3 → heap={3}, attend → ans=2, d=3
d=3: push end=4 → heap={4}, attend → ans=3, d=4
Result = 3
```

---

## ⏱️ Time Complexity
```
O(n log n) — sorting + heap operations
```

## 💾 Space Complexity
```
O(n) — for the heap
```

---

## ⚠️ Edge Cases
- All events on the same day → can only attend one
- Events with long ranges but overlapping start days
- Single event → always attend, answer is 1

---

## 🎯 Interview Takeaways
- "Earliest deadline first" is a classic greedy scheduling strategy.
- A min-heap efficiently tracks the event ending soonest.
- Skipping empty days avoids TLE on sparse timelines.

---

## 📌 Key Pattern
👉 **"Greedy scheduling with a min-heap on deadlines (earliest deadline first)."**

---

## 🔁 Related Problems
- 1235. Maximum Profit in Job Scheduling
- 253. Meeting Rooms II
- 452. Minimum Number of Arrows to Burst Balloons

---

## 🚀 Final Thoughts
A textbook greedy + priority queue problem. The key insight is always attending the event closest to expiring, and skipping days when no events are available.

---

✨ **Rule to remember:**
> When scheduling conflicting events, always prioritize the one ending soonest.
