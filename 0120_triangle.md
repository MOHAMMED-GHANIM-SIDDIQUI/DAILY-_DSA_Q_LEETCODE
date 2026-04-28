# 120. Triangle

## 🔗 Problem Link
https://leetcode.com/problems/triangle/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Dynamic Programming

---

## 🧩 Problem Summary

Given a triangle array, return the minimum path sum from top to bottom. For each step, you may move to an adjacent number on the row below (i.e., from position `i` in the current row, you can move to position `i` or `i+1` in the next row).

### 📌 Constraints
- `1 <= triangle.length <= 200`
- `triangle[0].length == 1`
- `triangle[i].length == triangle[i - 1].length + 1`
- `-10^4 <= triangle[i][j] <= 10^4`

---

## 💭 Intuition

👉 Instead of going top-down (which requires tracking multiple paths), work bottom-up. Start from the second-to-last row and replace each element with itself plus the minimum of its two children below. After processing all rows, `triangle[0][0]` holds the answer.

---

## ⚡ Approach — Bottom-Up In-Place DP

### 🧠 Idea

- Start from the second-to-last row and iterate upward.
- For each element `triangle[row][col]`, add the minimum of `triangle[row+1][col]` and `triangle[row+1][col+1]`.
- This collapses the triangle upward until only the top element remains with the minimum path sum.
- Modifies the input array in-place, so no extra space is needed.

---

## 💻 Code

```cpp
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        // Start from second last row
        for(int row = triangle.size() - 2; row >= 0; row--) {
            for(int col = 0; col < triangle[row].size(); col++) {
                triangle[row][col] += min(triangle[row+1][col], triangle[row+1][col+1]);
            }
        }
        return triangle[0][0];
    }
};
```

---

## 🧠 Dry Run

### Input
```
triangle = [
  [2],
  [3, 4],
  [6, 5, 7],
  [4, 1, 8, 3]
]
```

### Steps
```
Row 2: col=0: 6+min(4,1)=7, col=1: 5+min(1,8)=6, col=2: 7+min(8,3)=10
  → triangle = [[2],[3,4],[7,6,10],[4,1,8,3]]

Row 1: col=0: 3+min(7,6)=9, col=1: 4+min(6,10)=10
  → triangle = [[2],[9,10],[7,6,10],[4,1,8,3]]

Row 0: col=0: 2+min(9,10)=11
  → triangle = [[11],[9,10],[7,6,10],[4,1,8,3]]

Return 11
Path: 2 → 3 → 5 → 1
```

---

## ⏱️ Time Complexity

```
O(n²)
```

Where n is the number of rows. We visit each element once.

---

## 💾 Space Complexity

```
O(1)
```

The triangle is modified in-place; no extra space is used.

---

## ⚠️ Edge Cases

- **Single row:** `triangle = [[5]]` → return 5
- **Two rows:** `triangle = [[-1],[2,3]]` → -1 + min(2,3) = 1
- **All negative:** `triangle = [[-1],[-2,-3]]` → -1 + min(-2,-3) = -4

---

## 🎯 Interview Takeaways

- Bottom-up DP avoids the complexity of tracking multiple top-down paths.
- In-place modification eliminates extra space — but clarify with the interviewer if mutation is acceptable.
- The "adjacent" constraint (can only move to `i` or `i+1`) is what makes this DP, not greedy.
- This is a textbook example of optimal substructure in DP.

---

## 📌 Key Pattern

👉 **"Bottom-up DP: collapse the triangle upward by choosing the minimum child at each step."**

---

## 🔁 Related Problems

- 64. Minimum Path Sum
- 931. Minimum Falling Path Sum
- 1289. Minimum Falling Path Sum II
- 62. Unique Paths

---

## 🚀 Final Thoughts

Triangle is a clean bottom-up DP problem. The in-place approach with O(1) extra space makes it especially elegant. This pattern of "collapsing from the bottom" appears in many path-sum problems.

---

✨ **Rule to remember:**
> "When paths fan out going down, work bottom-up — each cell only needs to know the best of its two children."
