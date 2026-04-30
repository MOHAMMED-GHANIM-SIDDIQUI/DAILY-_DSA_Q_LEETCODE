# 3025. Find the Number of Ways to Place People I

## 🔗 Problem Link
https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Sorting, Geometry, Enumeration

---

## 🧩 Problem Summary
Given `n` points on a 2D plane, count the number of pairs `(i, j)` such that you can place a rectangle (axis-aligned) with its upper-left corner at point `i` and lower-right corner at point `j`, and no other point lies inside or on the boundary of that rectangle.

### 📌 Constraints
- 2 <= n <= 50
- 0 <= points[i][0], points[i][1] <= 50

---

## 💭 Intuition
👉 Sort points by x ascending, then y descending. For each pair (i, j) where `points[i]` is upper-left and `points[j]` is lower-right (meaning `x_i <= x_j` and `y_i >= y_j`), check that no other point with x in between has a y value between `y_j` and `y_i`. Track the maximum y seen to efficiently detect blocking points.

---

## ⚡ Approach — Sort + Pairwise Check with Max Tracking

### 🧠 Idea
- Sort by x ascending, breaking ties by y descending.
- For each point `i`, scan all points `j > i`.
- Only consider pairs where `y_i >= y_j` (point j is lower or equal).
- Track `maxY` of intermediate points. If `y_j > maxY`, no point blocks the rectangle — count it and update `maxY`.

---

## 💻 Code

```cpp
class Solution {
 public:
  int numberOfPairs(vector<vector<int>>& points) {
    int ans = 0;

    ranges::sort(points, ranges::less{}, [](const vector<int>& point) {
      const int x = point[0];
      const int y = point[1];
      return pair<int, int>{x, -y};
    });

    for (int i = 0; i < points.size(); ++i) {
      int maxY = INT_MIN;
      for (int j = i + 1; j < points.size(); ++j)
        if (points[i][1] >= points[j][1] && points[j][1] > maxY) {
          ++ans;
          maxY = points[j][1];
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
points = [[1,1],[2,2],[3,3]]
```
### Steps
```
After sort (x asc, y desc): [[1,1],[2,2],[3,3]]

i=0 (1,1): maxY = INT_MIN
  j=1 (2,2): y_i=1 < y_j=2 → skip (not valid rectangle)
  j=2 (3,3): y_i=1 < y_j=3 → skip

i=1 (2,2): maxY = INT_MIN
  j=2 (3,3): y_i=2 < y_j=3 → skip

Output: 0
```

---

## ⏱️ Time Complexity
```
O(n^2) — check all pairs after sorting
```

## 💾 Space Complexity
```
O(1) — constant extra space (excluding sort)
```

---

## ⚠️ Edge Cases
- All points on a horizontal line: many valid pairs if no blocking points.
- All points on a vertical line: pairs valid if y values allow upper-left/lower-right placement.
- Two points: always 0 or 1 valid pair.
- Overlapping points: handled by the sorting order.

---

## 🎯 Interview Takeaways
- Sorting by x then by -y ensures we process potential upper-left corners before lower-right ones.
- The `maxY` tracking eliminates the need for a third loop to check blocking points.
- Axis-aligned rectangle problems benefit from coordinate-based sorting.

---

## 📌 Key Pattern
👉 **"Sort by coordinates + pairwise enumeration with greedy blocking check"**

---

## 🔁 Related Problems
- 3027. Find the Number of Ways to Place People II
- 223. Rectangle Area
- 939. Minimum Area Rectangle

---

## 🚀 Final Thoughts
The clever sorting strategy and `maxY` tracking reduce what could be an O(n^3) brute force to O(n^2). The key insight is that after sorting, we only need to track the highest y among intermediate points to determine if a rectangle is blocked.

---

✨ **Rule to remember:**
> For axis-aligned rectangle placement problems, sort by x (then -y) and track the max y of intermediate points to detect blocking.
