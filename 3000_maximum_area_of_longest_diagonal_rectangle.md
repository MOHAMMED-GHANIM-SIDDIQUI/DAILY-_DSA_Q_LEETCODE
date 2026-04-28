# 3000. Maximum Area of Longest Diagonal Rectangle

## 🔗 Problem Link
https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Math

---

## 🧩 Problem Summary
Given a list of rectangle dimensions `[length, width]`, find the rectangle with the longest diagonal. If multiple rectangles have the same longest diagonal, return the one with the maximum area.

### 📌 Constraints
- 1 <= dimensions.length <= 100
- 1 <= dimensions[i][0], dimensions[i][1] <= 100

---

## 💭 Intuition
👉 The diagonal squared is `l^2 + w^2`. Compare rectangles by diagonal squared first (to avoid floating point), then by area as a tiebreaker. Use `max_element` with a custom comparator.

---

## ⚡ Approach — Custom Comparator with Max Element

### 🧠 Idea
- Use `ranges::max_element` with a comparator that:
  - First compares by `l^2 + w^2` (diagonal squared).
  - On ties, compares by `l * w` (area).
- Return the area of the winning rectangle.

---

## 💻 Code

```cpp
class Solution {
 public:
  int areaOfMaxDiagonal(vector<vector<int>>& dimensions) {
    const vector<int> maxDimension = *ranges::max_element(
        dimensions, [](const vector<int>& a, const vector<int>& b) {
      return (a[0] * a[0] + a[1] * a[1] == b[0] * b[0] + b[1] * b[1])
                 ? (a[0] * a[1] < b[0] * b[1])
                 : (a[0] * a[0] + a[1] * a[1] < b[0] * b[0] + b[1] * b[1]);
    });
    return maxDimension[0] * maxDimension[1];
  }
};
```

---

## 🧠 Dry Run
### Input
```
dimensions = [[9,3],[8,6]]
```
### Steps
```
Rectangle [9,3]: diagonal^2 = 81+9 = 90, area = 27
Rectangle [8,6]: diagonal^2 = 64+36 = 100, area = 48

Compare: 90 < 100 → [8,6] wins
Output: 48
```

---

## ⏱️ Time Complexity
```
O(n) — single pass through the dimensions array
```

## 💾 Space Complexity
```
O(1) — constant extra space
```

---

## ⚠️ Edge Cases
- All rectangles are squares: diagonal is proportional to side length.
- Multiple rectangles with same diagonal: choose the one with larger area.
- Single rectangle: return its area.

---

## 🎯 Interview Takeaways
- Compare diagonal squared to avoid floating point precision issues.
- Custom comparators with tiebreakers are a clean way to handle multi-criteria selection.
- `ranges::max_element` with lambdas provides concise, readable code.

---

## 📌 Key Pattern
👉 **"Multi-criteria max selection using custom comparator"**

---

## 🔁 Related Problems
- 1725. Number Of Rectangles That Can Form The Largest Square
- 2200. Find All K-Distant Indices in an Array
- 1030. Matrix Cells in Distance Order

---

## 🚀 Final Thoughts
A simple problem that tests the ability to write clean custom comparators. The key optimization is comparing diagonal squared instead of the actual diagonal to avoid unnecessary square root computations and floating point issues.

---

✨ **Rule to remember:**
> Compare squared diagonals (l^2 + w^2) instead of actual diagonals to avoid floating point errors.
