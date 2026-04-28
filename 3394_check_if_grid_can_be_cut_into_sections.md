# 3394. Check if Grid can be Cut into Sections

## 🔗 Problem Link
https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Sorting, Interval Merging, Greedy

---

## 🧩 Problem Summary
Given n x n grid and a list of axis-aligned rectangles placed on it, determine if you can make two horizontal or two vertical cuts such that the grid is divided into three sections, and every rectangle belongs to exactly one section. This is equivalent to checking if merging overlapping intervals along either axis yields at least 3 non-overlapping groups.

### 📌 Constraints
- 2 <= n <= 10^9
- 1 <= rectangles.length <= 10^5
- rectangles[i] = [startX, startY, endX, endY]

---

## 💭 Intuition
👉 If we project all rectangles onto the x-axis (or y-axis), we get intervals. Merging overlapping intervals, if the merged count is >= 3, we can cut between merged intervals. We need at least 3 groups on either axis.

---

## ⚡ Approach — Interval Merging

### 🧠 Idea
- Extract x-intervals (startX, endX) and y-intervals (startY, endY).
- For each axis, sort intervals by start, then merge overlapping ones.
- Count the number of merged intervals.
- If either axis has >= 3 merged intervals, return true.

---

## 💻 Code

```cpp
class Solution {
 public:
  bool checkValidCuts(int n, vector<vector<int>>& rectangles) {
    vector<pair<int, int>> xs;
    vector<pair<int, int>> ys;

    for (const vector<int> rectangles : rectangles) {
      const int startX = rectangles[0];
      const int startY = rectangles[1];
      const int endX = rectangles[2];
      const int endY = rectangles[3];
      xs.emplace_back(startX, endX);
      ys.emplace_back(startY, endY);
    }

    return max(countMerged(xs), countMerged(ys)) >= 3;
  }

 private:
  int countMerged(vector<pair<int, int>>& intervals) {
    int count = 0;
    int prevEnd = 0;

    ranges::sort(intervals);

    for (const auto& [start, eend] : intervals)
      if (start < prevEnd) {
        prevEnd = max(prevEnd, eend);
      } else {
        prevEnd = eend;
        ++count;
      }

    return count;
  }
};
```

---

## 🧠 Dry Run
### Input
```
n = 5, rectangles = [[0,0,2,2],[1,0,3,3],[3,0,5,5]]
```
### Steps
```
xs = [(0,2), (1,3), (3,5)]
ys = [(0,2), (0,3), (0,5)]

countMerged(xs):
  Sorted: [(0,2), (1,3), (3,5)]
  (0,2): start=0 >= prevEnd=0 → count=1, prevEnd=2
  (1,3): start=1 < prevEnd=2 → merge, prevEnd=3
  (3,5): start=3 >= prevEnd=3 → count=2, prevEnd=5
  Result: 2

countMerged(ys):
  Sorted: [(0,2), (0,3), (0,5)]
  (0,2): start=0 >= prevEnd=0 → count=1, prevEnd=2
  (0,3): start=0 < prevEnd=2 → merge, prevEnd=3
  (0,5): start=0 < prevEnd=3 → merge, prevEnd=5
  Result: 1

max(2, 1) = 2 < 3 → false
```

---

## ⏱️ Time Complexity
```
O(r log r) — where r is the number of rectangles (sorting dominates)
```

## 💾 Space Complexity
```
O(r) — storing interval projections
```

---

## ⚠️ Edge Cases
- All rectangles span the entire grid → only 1 merged interval per axis
- Rectangles are non-overlapping along one axis → may have >= 3 groups
- Touching rectangles (end of one == start of another) count as separate groups

---

## 🎯 Interview Takeaways
- Interval merging is a fundamental technique for geometric partition problems.
- Projecting 2D rectangles onto 1D intervals simplifies the problem greatly.
- The condition >= 3 merged groups directly corresponds to the ability to make 2 cuts.

---

## 📌 Key Pattern
👉 **"Project 2D geometry to 1D intervals, then merge"**

---

## 🔁 Related Problems
- 56. Merge Intervals
- 435. Non-overlapping Intervals
- 252. Meeting Rooms

---

## 🚀 Final Thoughts
This problem elegantly reduces a 2D geometric partitioning question to a classic 1D interval merging problem. The key realization is that cuts can only be placed between non-overlapping merged groups.

---

✨ **Rule to remember:**
> To cut a grid into sections, project rectangles onto each axis and count merged intervals — need at least 3 for two cuts.
