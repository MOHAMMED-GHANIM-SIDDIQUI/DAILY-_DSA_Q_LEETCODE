# 2054. Two Best Non-Overlapping Events

## 🔗 Problem Link
https://leetcode.com/problems/two-best-non-overlapping-events/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Sorting, Dynamic Programming, Line Sweep

---

## 🧩 Problem Summary
Given events represented as `[startTime, endTime, value]`, choose at most two non-overlapping events such that the sum of their values is maximized. Return the maximum sum.

### 📌 Constraints
- `2 <= events.length <= 10^5`
- `events[i].length == 3`
- `1 <= startTime_i <= endTime_i <= 10^9`
- `1 <= value_i <= 10^6`

---

## 💭 Intuition
👉 Use a line sweep approach: create time points for event starts and event ends (shifted by +1 to avoid overlap). Sort all time points. When an event ends, update the best single-event value seen so far. When an event starts, combine its value with the best previous non-overlapping event.

---

## ⚡ Approach — Line Sweep with Start/End Events

### 🧠 Idea
- For each event `[s, e, v]`, create two entries: `(s, 1, v)` for the start and `(e + 1, 0, v)` for the end (+1 to ensure non-overlap).
- Sort all entries. When times are equal, process ends before starts (isStart=0 comes before isStart=1).
- Maintain `maxValue` = best value of any event that has already ended.
- For each start event, update `ans = max(ans, value + maxValue)`.
- For each end event, update `maxValue = max(maxValue, value)`.

---

## 💻 Code

```python
class Solution:
  def maxTwoEvents(self, events: list[list[int]]) -> int:
    ans = 0
    maxValue = 0
    evts = []  # (time, isStart, value)

    for s, e, v in events:
      evts.append((s, 1, v))
      evts.append((e + 1, 0, v))

    # When two events have the same time, the one is not start will be in the front
    evts.sort()

    for _, isStart, value in evts:
      if isStart:
        ans = max(ans, value + maxValue)
      else:
        maxValue = max(maxValue, value)

    return ans
```

---

## 🧠 Dry Run
### Input
```
events = [[1,3,2],[4,5,2],[2,4,3]]
```
### Steps
```
Create time points:
  (1, 1, 2), (4, 0, 2)   ← event [1,3,2]
  (4, 1, 2), (6, 0, 2)   ← event [4,5,2]
  (2, 1, 3), (5, 0, 3)   ← event [2,4,3]

After sort: (1,1,2), (2,1,3), (4,0,2), (4,1,2), (5,0,3), (6,0,2)

(1,1,2): start → ans = max(0, 2+0) = 2
(2,1,3): start → ans = max(2, 3+0) = 3
(4,0,2): end   → maxValue = max(0, 2) = 2
(4,1,2): start → ans = max(3, 2+2) = 4
(5,0,3): end   → maxValue = max(2, 3) = 3
(6,0,2): end   → maxValue = max(3, 2) = 3

return 4
```

---

## ⏱️ Time Complexity
```
O(n log n), where n is the number of events
```

## 💾 Space Complexity
```
O(n) for the time point array
```

---

## ⚠️ Edge Cases
- All events overlap → pick the single highest value event
- All events are disjoint → pick the two highest values
- Two events share an endpoint (end of one = start of another) → they overlap, handled by `e + 1`
- Only one event worth picking (second event adds no value)

---

## 🎯 Interview Takeaways
- Line sweep with start/end markers is a powerful technique for interval problems.
- Processing ends before starts at the same time point ensures non-overlap correctness.
- Tracking a running maximum avoids the need for binary search.

---

## 📌 Key Pattern
👉 **"Line sweep with end-before-start ordering to combine at most two non-overlapping intervals"**

---

## 🔁 Related Problems
- 1235. Maximum Profit in Job Scheduling
- 435. Non-overlapping Intervals
- 253. Meeting Rooms II
- 1751. Maximum Number of Events That Can Be Attended II

---

## 🚀 Final Thoughts
The line sweep approach elegantly reduces a 2D interval problem to a 1D scan. The key trick is using `e + 1` for end times and sorting ends before starts at the same timestamp, which naturally enforces the non-overlap constraint.

---

✨ **Rule to remember:**
> In line sweep for non-overlapping intervals, process endings before beginnings at the same time.
