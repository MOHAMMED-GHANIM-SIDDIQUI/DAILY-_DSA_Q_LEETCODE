# 757. Set Intersection Size At Least Two

## 🔗 Problem Link
https://leetcode.com/problems/set-intersection-size-at-least-two/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Greedy, Sorting

---

## 🧩 Problem Summary
Given a list of intervals, find the minimum size of a set S such that for every interval, the intersection of S with that interval has at least 2 elements. In other words, pick the fewest integers such that every interval contains at least 2 of the picked integers.

### 📌 Constraints
- `1 <= intervals.length <= 3000`
- `intervals[i].length == 2`
- `0 <= start_i < end_i <= 10^8`

---

## 💭 Intuition
👉 Sort intervals by end point (ascending), then by start point (descending). Greedily place points at the end of each interval, reusing previously placed points whenever possible.

---

## ⚡ Approach — Greedy with Sorted Intervals

### 🧠 Idea
- Sort by end ascending, then by start descending (to process tighter intervals first among same-end intervals).
- Track the two largest points placed so far (`mx` and `secondMax`).
- For each interval:
  - If both points satisfy (both >= start), skip.
  - If only `mx` satisfies, add `end` as a new point.
  - If neither satisfies, add both `end` and `end - 1`.

---

## 💻 Code

```cpp
class Solution {
 public:
  int intersectionSizeTwo(vector<vector<int>>& intervals) {
    int ans = 0;
    int mx = -1;
    int secondMax = -1;

    ranges::sort(intervals, ranges::less{}, [](const vector<int>& interval) {
      const int start = interval[0];
      const int end = interval[1];
      return pair<int, int>{end, -start};
    });

    for (const vector<int>& interval : intervals) {
      const int start = interval[0];
      const int end = interval[1];
      // The maximum and the second maximum still satisfy.
      if (mx >= start && secondMax >= start)
        continue;
      if (mx >= start) {
        // The maximum still satisfy.
        secondMax = mx;
        mx = end;  // Add `end` to the set.
        ans += 1;
      } else {
        // The maximum and the second maximum can't satisfy.
        mx = end;             // Add `end` to the set.
        secondMax = end - 1;  // Add `end - 1` to the set.
        ans += 2;
      }
    }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
intervals = [[1,3],[1,4],[2,5],[3,5]]
```
### Steps
```
After sort by (end, -start): [[1,3],[1,4],[3,5],[2,5]]
mx=-1, secondMax=-1

[1,3]: neither satisfies -> mx=3, secondMax=2, ans=2
[1,4]: mx=3>=1, secondMax=2>=1 -> skip
[3,5]: mx=3>=3, secondMax=2<3 -> secondMax=3, mx=5, ans=3
[2,5]: mx=5>=2, secondMax=3>=2 -> skip

Result: 3 (set = {2, 3, 5})
```

---

## ⏱️ Time Complexity
```
O(n log n) — dominated by sorting
```

## 💾 Space Complexity
```
O(log n) — sorting space
```

---

## ⚠️ Edge Cases
- Single interval — always need 2 points.
- All intervals identical — need exactly 2 points.
- Non-overlapping intervals — need 2 points per interval.
- Nested intervals — outer interval is automatically satisfied by inner's points.

---

## 🎯 Interview Takeaways
- Sorting by end point enables greedy placement at the rightmost positions.
- Tracking only the two largest points is sufficient for the "at least 2" constraint.
- The secondary sort by -start ensures tighter intervals are processed first.

---

## 📌 Key Pattern
👉 **"Sort by end, greedy placement — track the two latest points to minimize set size"**

---

## 🔁 Related Problems
- 452. Minimum Number of Arrows to Burst Balloons
- 435. Non-overlapping Intervals
- 759. Employee Free Time

---

## 🚀 Final Thoughts
This problem extends the classic interval greedy pattern from "at least 1" to "at least 2" intersection. Tracking two points instead of one and the clever sorting strategy make this an elegant hard problem.

---

✨ **Rule to remember:**
> "Sort by end, place points greedily at the end — track the top two to ensure each interval gets at least two."
