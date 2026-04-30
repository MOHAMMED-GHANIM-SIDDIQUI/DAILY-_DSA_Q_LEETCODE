# 118. Pascal's Triangle

## 🔗 Problem Link
https://leetcode.com/problems/pascals-triangle/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Dynamic Programming, Math

---

## 🧩 Problem Summary

Given an integer `numRows`, return the first `numRows` of Pascal's triangle. In Pascal's triangle, each number is the sum of the two numbers directly above it. The first and last elements of each row are always 1.

### 📌 Constraints
- `1 <= numRows <= 30`

---

## 💭 Intuition

👉 Each row of Pascal's triangle corresponds to binomial coefficients C(n, k) for k = 0 to n. Instead of computing each element from the previous row's two parents, this solution computes each row independently using the combinatorial formula, iteratively multiplying and dividing to get successive coefficients.

---

## ⚡ Approach — Combinatorial (nCr) Row Generation

### 🧠 Idea

- For row `n` (0-indexed), the elements are C(n,0), C(n,1), ..., C(n,n).
- Compute iteratively: start with `cur = 1` (which is C(n,0)), then `cur = cur * (n-i) / (i+1)` gives C(n, i+1).
- Generate each row independently and collect them.

---

## 💻 Code

```cpp
class Solution {
    vector<int> nrow(int n)
    {
        vector<int>row;
        row.push_back(1);
        int cur=1;
        for(int i=0;i<n;i++)
        {
            cur*=(n-i);
            cur/=(i+1);
            row.push_back(cur);
        }
        return row;
    }
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>>ans;
        for(int i=0;i<numRows;i++)
        {
            ans.push_back(nrow(i));
        }
        return ans;
    }
};
```

---

## 🧠 Dry Run

### Input
```
numRows = 5
```

### Steps
```
nrow(0): cur=1, no loop → [1]
nrow(1): cur=1, i=0: cur=1*(1-0)/(0+1)=1 → [1,1]
nrow(2): cur=1, i=0: cur=1*2/1=2, i=1: cur=2*1/2=1 → [1,2,1]
nrow(3): cur=1, i=0: cur=3, i=1: cur=3, i=2: cur=1 → [1,3,3,1]
nrow(4): cur=1, i=0: cur=4, i=1: cur=6, i=2: cur=4, i=3: cur=1 → [1,4,6,4,1]
Result: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```

---

## ⏱️ Time Complexity

```
O(numRows²)
```

Each row `i` takes O(i) to generate, and the sum 0+1+2+...+(numRows-1) is O(numRows²).

---

## 💾 Space Complexity

```
O(numRows²)
```

Storing all rows of the triangle.

---

## ⚠️ Edge Cases

- **Single row:** `numRows = 1` → `[[1]]`
- **Two rows:** `numRows = 2` → `[[1],[1,1]]`
- **Maximum:** `numRows = 30` — values fit in int (C(29,14) = 1,726,484,500)

---

## 🎯 Interview Takeaways

- The combinatorial approach avoids needing the previous row to build the current one.
- The iterative nCr formula `cur = cur * (n-i) / (i+1)` avoids factorial overflow for reasonable n.
- Pascal's triangle has deep connections to binomial theorem, probability, and combinatorics.
- This is a classic DP/math warm-up problem.

---

## 📌 Key Pattern

👉 **"Use iterative nCr computation to generate each row of Pascal's triangle independently."**

---

## 🔁 Related Problems

- 119. Pascal's Triangle II
- 70. Climbing Stairs
- 121. Best Time to Buy and Sell Stock
- 62. Unique Paths

---

## 🚀 Final Thoughts

Pascal's Triangle is a fundamental problem bridging math and dynamic programming. The combinatorial row-generation approach here is elegant and avoids inter-row dependencies.

---

✨ **Rule to remember:**
> "Each Pascal's row is just binomial coefficients — compute them iteratively to avoid overflow and redundancy."
