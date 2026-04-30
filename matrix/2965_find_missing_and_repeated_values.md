# 2965. Find Missing and Repeated Values

## 🔗 Problem Link
https://leetcode.com/problems/find-missing-and-repeated-values/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Hash Table, Matrix

---

## 🧩 Problem Summary
Given an `n x n` grid containing each integer from 1 to n^2, where exactly one value is repeated and one is missing, find and return `[repeated, missing]`.

### 📌 Constraints
- 2 <= n <= 50
- 1 <= grid[i][j] <= n * n
- Exactly one number is repeated and one is missing.

---

## 💭 Intuition
👉 Use a frequency array to count occurrences of each number from 1 to n^2. The number with count 2 is the repeated value, and the number with count 0 is the missing value.

---

## ⚡ Approach — Frequency Counting

### 🧠 Idea
- Create a hash array of size n*n + 1 initialized to 0.
- Traverse the grid and count occurrences of each value.
- Scan the hash array: find the value with count 2 (repeated) and count 0 (missing).

---

## 💻 Code

```cpp
class Solution {
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<int> hash(n * n + 1, 0);
        // Use n*n+1 to ensure proper indexing
        // Fill the hash array by counting occurrences of each number
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                hash[grid[i][j]]++;
            }
        }

        int twice = 0, zero = 0;
        // Find the repeated and missing numbers
        for (int i = 1; i <= n * n; i++) {
            if (hash[i] == 2) {
                twice = i;
            } else if (hash[i] == 0) {
                zero = i;
            }
        }

        return {twice, zero};
    }
};
```

---

## 🧠 Dry Run
### Input
```
grid = [[1,3],[2,2]]
```
### Steps
```
n = 2, hash size = 5 (indices 0..4)

Traverse grid:
  hash[1]++ → hash = [0,1,0,0,0]
  hash[3]++ → hash = [0,1,0,1,0]
  hash[2]++ → hash = [0,1,1,1,0]
  hash[2]++ → hash = [0,1,2,1,0]

Scan hash[1..4]:
  hash[1]=1, hash[2]=2 → twice=2
  hash[3]=1, hash[4]=0 → zero=4

Output: [2, 4]
```

---

## ⏱️ Time Complexity
```
O(n^2) — traverse the n x n grid and the frequency array
```

## 💾 Space Complexity
```
O(n^2) — for the frequency array
```

---

## ⚠️ Edge Cases
- Repeated value is 1 or n^2 (boundary values).
- Missing value is 1 or n^2.
- 2x2 grid (smallest possible).

---

## 🎯 Interview Takeaways
- Frequency counting is the simplest approach for finding duplicates and missing values.
- Alternative approaches exist (math-based using sum and sum-of-squares), but frequency counting is most intuitive.
- Using 1-indexed array (size n*n + 1) avoids off-by-one errors.

---

## 📌 Key Pattern
👉 **"Frequency array to find duplicate and missing values"**

---

## 🔁 Related Problems
- 287. Find the Duplicate Number
- 268. Missing Number
- 442. Find All Duplicates in an Array

---

## 🚀 Final Thoughts
A classic problem solvable with a simple frequency array. While mathematical approaches using sum formulas exist, the frequency counting method is straightforward and easy to implement correctly in an interview setting.

---

✨ **Rule to remember:**
> For finding repeated/missing values in a bounded range, a frequency array gives O(n) time with clear logic.
