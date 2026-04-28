# 2033. Minimum Operations to Make a Uni-Value Grid

## 🔗 Problem Link
https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Math, Sorting, Matrix

---

## 🧩 Problem Summary
Given a 2D grid of integers and an integer `x`, in one operation you can add or subtract `x` from any element. Return the minimum number of operations to make all elements equal, or `-1` if it is impossible.

### 📌 Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 10^5`
- `1 <= m * n <= 10^5`
- `1 <= x, grid[i][j] <= 10^4`

---

## 💭 Intuition
👉 All elements must share the same remainder modulo `x` for a solution to exist. The optimal target to minimize total operations is the median of the flattened array.

---

## ⚡ Approach — Median + Modular Check (C++ Implementation)

### 🧠 Idea
- Flatten the 2D grid into a 1D vector.
- Check all elements share the same `% x` remainder; if not, return -1.
- Sort the array and select the median.
- Sum `abs(num - median) / x` for every element.

---

## 💻 Code

```cpp
class Solution {
public:
    int minOperations(vector<vector<int>>& grid, int x) {
        // Step 1: Flatten the 2D grid into a 1D array
        vector<int> arr;
        for (const vector<int>& row : grid) {
            for (int num : row) {
                arr.push_back(num);
            }
        }

        // Step 2: Check if all elements can be made equal by the given x
        int base = arr[0];
        for (int num : arr) {
            if ((num - base) % x != 0) {
                return -1;  // Return -1 if it's impossible to make all elements equal
            }
        }

        // Step 3: Sort the array to find the median
        sort(arr.begin(), arr.end());

        // Step 4: Calculate the minimum number of operations
        int median = arr[arr.size() / 2];
        int operations = 0;
        for (int num : arr) {
            operations += abs(num - median) / x;
        }

        return operations;
    }
};
```

---

## 🧠 Dry Run
### Input
```
grid = [[2,4],[6,8]], x = 2
```
### Steps
```
Flatten: arr = [2, 4, 6, 8]
Check mod: (2-2)%2=0, (4-2)%2=0, (6-2)%2=0, (8-2)%2=0 -> all valid
Sort: [2, 4, 6, 8]
Median: arr[2] = 6
Operations: |2-6|/2 + |4-6|/2 + |6-6|/2 + |8-6|/2 = 2 + 1 + 0 + 1 = 4
Return 4
```

---

## ⏱️ Time Complexity
```
O(m*n * log(m*n)) due to sorting
```

## 💾 Space Complexity
```
O(m*n) for the flattened array
```

---

## ⚠️ Edge Cases
- Different remainders mod `x` -> return -1
- Single element grid -> 0 operations
- All elements already equal -> 0 operations
- `x = 1` -> always possible

---

## 🎯 Interview Takeaways
- The median minimizes total absolute deviation -- a key statistics result.
- The modular check is the feasibility gate before optimization.
- Flattening a 2D grid into 1D simplifies the problem.

---

## 📌 Key Pattern
👉 **"Median minimizes total absolute deviation; mod check ensures feasibility"**

---

## 🔁 Related Problems
- 462. Minimum Moves to Equal Array Elements II
- 2448. Minimum Cost to Make Array Equal
- 1551. Minimum Operations to Make Array Equal

---

## 🚀 Final Thoughts
This C++ implementation follows the same median-based approach as the Python version. The algorithm combines a feasibility check via modular arithmetic with the optimization insight that the median minimizes L1 distance.

---

✨ **Rule to remember:**
> To equalize elements with fixed-step operations, check mod compatibility first, then converge to the median.
