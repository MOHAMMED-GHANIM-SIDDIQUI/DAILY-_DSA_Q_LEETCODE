# 3027. Find the Number of Ways to Place People II

## 🔗 Problem Link
https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Math, Geometry, Sorting, Enumeration

---

## 🧩 Problem Summary
Given a 2D array of points, count the number of pairs (i, j) such that you can place Alice at point i and Bob at point j where Alice is at the upper-left and Bob at the lower-right of an axis-aligned rectangle, and no other point lies inside or on the border of that rectangle.

### 📌 Constraints
- 2 <= points.length <= 1000
- points[i].length == 2
- -10^9 <= points[i][0], points[i][1] <= 10^9
- All points are distinct

---

## 💭 Intuition
👉 Sort points by x ascending and y descending. Then for each point i, iterate through subsequent points j and track the maximum y seen so far. If points[i][1] >= points[j][1] and points[j][1] > maxY, no intermediate point blocks the rectangle.

---

## ⚡ Approach — Sorting + Greedy Enumeration

### 🧠 Idea
- Sort points by x ascending, breaking ties by y descending
- For each point i, scan all points j > i
- Keep track of the maximum y-coordinate among valid lower-right candidates seen so far
- If points[j] has a y within range and greater than maxY, it forms a valid pair

---

## 💻 Code

```cpp
class Solution {
 public:
  // Same as 3025. Find the Number of Ways to Place People I
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
points = [[1,1],[2,3],[3,2]]
```
### Steps
```
After sorting by (x, -y): [[1,1],[2,3],[3,2]]
i=0 (1,1): j=1 (2,3) -> 1>=3? No. j=2 (3,2) -> 1>=2? No.
i=1 (2,3): j=2 (3,2) -> 3>=2? Yes, 2>INT_MIN? Yes -> ans=1, maxY=2
Result: 1
```

---

## ⏱️ Time Complexity
```
O(n^2) — nested loop over all pairs of points
```

## 💾 Space Complexity
```
O(1) — only a few variables besides the sorted input
```

---

## ⚠️ Edge Cases
- All points on the same horizontal or vertical line
- Only two points — always check if valid rectangle can be formed
- Large coordinate values (up to 10^9)

---

## 🎯 Interview Takeaways
- Sorting with a custom key (x asc, y desc) simplifies the enumeration
- Tracking maxY efficiently eliminates blocked rectangles without explicit containment checks
- This is an extension of problem 3025 with larger constraints

---

## 📌 Key Pattern
👉 **"Sort + greedy sweep to count valid geometric pairs"**

---

## 🔁 Related Problems
- 3025. Find the Number of Ways to Place People I
- 223. Rectangle Area
- 836. Rectangle Overlap

---

## 🚀 Final Thoughts
The key insight is that sorting by x ascending and y descending creates an ordering where you only need to track the maximum y seen to determine if a rectangle is unblocked. This reduces a potentially complex geometry problem to a simple O(n^2) enumeration.

---

✨ **Rule to remember:**
> Sort by x ascending, y descending; then sweep with maxY to count unblocked rectangle pairs.
