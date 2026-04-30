# 3567. Minimum Absolute Difference in Sliding Subarray

## 🔗 Problem Link
https://leetcode.com/problems/minimum-absolute-difference-in-sliding-subarray/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Sliding Window, Sorting

---

## 🧩 Problem Summary
Given a 2D grid and an integer `k`, for every `k x k` submatrix, find the minimum absolute difference between any two distinct elements. If all elements in the submatrix are the same, the answer is 0.

### 📌 Constraints
- `1 <= m, n <= 100`
- `1 <= k <= min(m, n)`
- `0 <= grid[i][j] <= 10^5`

---

## 💭 Intuition
👉 For each `k x k` window, collect the unique elements, sort them, and the minimum absolute difference is the smallest gap between consecutive sorted elements.

---

## ⚡ Approach — Sort Unique Elements per Window

### 🧠 Idea
- For each valid top-left corner `(i, j)` of a `k x k` submatrix, collect all elements into a set.
- Sort the unique elements and find the minimum consecutive difference.
- If fewer than 2 unique elements exist, the answer is 0.

---

## 💻 Code

```python
class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = []

        for i in range(m - k + 1):
            temp = []
            for j in range(n - k + 1):
                sub_mat = set()

                # collect elements
                for r in range(i, i + k):
                    for c in range(j, j + k):
                        sub_mat.add(grid[r][c])

                arr = sorted(sub_mat)

                # compute min difference
                if len(arr) < 2:
                    min_diff = 0
                else:
                    min_diff = float('inf')
                    for t in range(len(arr) - 1):
                        min_diff = min(min_diff, arr[t+1] - arr[t])

                temp.append(min_diff)
            ans.append(temp)

        return ans
```

---

## 🧠 Dry Run
### Input
```
grid = [[1, 8], [3, 2]], k = 2
```
### Steps
```
Only one 2x2 window: (0,0) to (1,1)
Elements: {1, 8, 3, 2}
Sorted: [1, 2, 3, 8]
Consecutive diffs: 1, 1, 5
Min diff = 1

Result: [[1]]
```

---

## ⏱️ Time Complexity
```
O((m-k+1) * (n-k+1) * k^2 * log(k^2)) — for each window: collect O(k^2), sort O(k^2 log k^2)
```

## 💾 Space Complexity
```
O(k^2) — for the set and sorted array per window
```

---

## ⚠️ Edge Cases
- k = 1 → single element, always 0
- All elements in a window are identical → 0
- Window contains only two distinct elements
- Grid where k equals full dimensions

---

## 🎯 Interview Takeaways
- Using a set removes duplicates efficiently before sorting.
- Minimum absolute difference in a sorted array is always between consecutive elements.
- Brute-force is acceptable when constraints are small (100x100).

---

## 📌 Key Pattern
👉 **"Sort unique elements, check consecutive pairs — minimum difference is always between neighbors in sorted order."**

---

## 🔁 Related Problems
- 220. Contains Duplicate III
- 532. K-diff Pairs in an Array
- 2200. Find All K-Distant Indices in an Array

---

## 🚀 Final Thoughts
A straightforward sliding window problem on a 2D grid. The key insight that minimum absolute difference occurs between consecutive elements in sorted order makes this efficient. For larger constraints, one could use more advanced data structures for the sliding window.

---

✨ **Rule to remember:**
> "Minimum absolute difference in any set equals the minimum gap between consecutive elements when sorted."
