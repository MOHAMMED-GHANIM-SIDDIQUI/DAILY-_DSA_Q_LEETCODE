# 57. Insert Interval

## 🔗 Problem Link
https://leetcode.com/problems/insert-interval/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Intervals

---

## 🧩 Problem Summary

Given a set of non-overlapping intervals sorted by their start time and a new interval, insert the new interval into the list (merging if necessary) so that the intervals remain sorted and non-overlapping. Return the resulting list of intervals.

### 📌 Constraints
- `0 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^5`
- Intervals are sorted by `start_i` in ascending order
- `newInterval.length == 2`
- `0 <= start <= end <= 10^5`

---

## 💭 Intuition

👉 Since intervals are already sorted, we can process them in three phases: (1) add all intervals that come entirely before the new interval, (2) merge all overlapping intervals with the new interval, and (3) add all intervals that come entirely after. The key is recognizing overlap: two intervals overlap when one's start is <= the other's end.

---

## ⚡ Approach — Linear Scan with Three Phases

### 🧠 Idea

- **Phase 1:** Add all intervals whose end is before the new interval's start (no overlap).
- **Phase 2:** Merge all intervals that overlap with the new interval by expanding the new interval's start/end.
- **Phase 3:** Add the merged new interval, then append all remaining intervals.

---

## 💻 Code

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx = 0
        n = len(intervals)
        ans = []
        while idx<n and intervals[idx][1]<newInterval[0]:
            ans.append(intervals[idx])
            idx+=1
        while idx<n and newInterval[1]>=intervals[idx][0]:
            newInterval[0] = min(intervals[idx][0],newInterval[0])
            newInterval[1] = max(intervals[idx][1],newInterval[1])
            idx+=1
        ans.append(newInterval)
        while idx<n:
            ans.append(intervals[idx])
            idx+=1
        return ans
```

---

## 🧠 Dry Run

### Input
```
intervals = [[1,3],[6,9]], newInterval = [2,5]
```

### Steps
```
Phase 1: idx=0, intervals[0][1]=3 < newInterval[0]=2? No → skip phase 1
Phase 2: idx=0, newInterval[1]=5 >= intervals[0][0]=1? Yes
         newInterval = [min(1,2), max(3,5)] = [1,5]
         idx=1, newInterval[1]=5 >= intervals[1][0]=6? No → exit phase 2
Append newInterval [1,5] → ans = [[1,5]]
Phase 3: idx=1, append [6,9] → ans = [[1,5],[6,9]]
Return [[1,5],[6,9]]
```

---

## ⏱️ Time Complexity

```
O(n)
```

We iterate through all intervals exactly once.

---

## 💾 Space Complexity

```
O(n)
```

The result list stores all intervals.

---

## ⚠️ Edge Cases

- **Empty intervals:** `intervals = [], newInterval = [5,7]` → `[[5,7]]`
- **No overlap:** `intervals = [[1,2],[6,9]], newInterval = [3,5]` → `[[1,2],[3,5],[6,9]]`
- **New interval covers all:** `intervals = [[1,2],[3,5],[6,9]], newInterval = [0,10]` → `[[0,10]]`

---

## 🎯 Interview Takeaways

- Interval problems often benefit from a multi-phase approach: before, overlap, after.
- Merging intervals means taking `min` of starts and `max` of ends.
- Sorted input is a gift — exploit it to avoid sorting overhead.
- This is a fundamental interval manipulation pattern used in scheduling and calendar problems.

---

## 📌 Key Pattern

👉 **"Three-phase linear scan: before, merge, after."**

---

## 🔁 Related Problems

- 56. Merge Intervals
- 252. Meeting Rooms
- 253. Meeting Rooms II
- 986. Interval List Intersections

---

## 🚀 Final Thoughts

Insert Interval is a clean interval manipulation problem. The three-phase approach is elegant and runs in O(n), making it a must-know pattern for interval-related interview questions.

---

✨ **Rule to remember:**
> "For sorted intervals, split your logic into before-overlap-after — merge in the middle, copy the rest."
