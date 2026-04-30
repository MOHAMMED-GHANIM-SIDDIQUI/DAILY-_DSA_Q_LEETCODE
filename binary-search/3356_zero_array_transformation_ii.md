# 3356. Zero Array Transformation II

## 🔗 Problem Link
https://leetcode.com/problems/zero-array-transformation-ii/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Prefix Sum, Line Sweep, Binary Search

---

## 🧩 Problem Summary
Given an array `nums` and queries `[l, r, val]`, each query decrements elements in `nums[l..r]` by `val`. Find the minimum number of queries needed (in order) to make all elements zero or below. Return -1 if impossible.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^5`
- `1 <= queries.length <= 10^5`
- `queries[i] = [l, r, val]`

---

## 💭 Intuition
👉 Process queries greedily from left to right. For each position, apply queries until the decrement is sufficient. Use a difference array for efficient range updates. This is an online/greedy approach rather than binary search.

---

## ⚡ Approach — Greedy with Difference Array

### 🧠 Idea
- Maintain a difference array `line` and running `decrement`.
- For each position `i`, if current decrement is insufficient, apply the next query.
- Skip queries whose range `r` is before `i`.
- Apply the query starting from `max(l, i)` to avoid double-counting past positions.
- Return total queries used, or -1 if exhausted.

---

## 💻 Code

```cpp
class Solution {
public:
    int minZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        vector<int> line(nums.size() + 1, 0); // Initialize the vector with 0s
        int decrement = 0;
        int queryIndex = 0;

        for (int i = 0; i < nums.size(); ++i) {
            // Process queries while nums[i] is greater than the current decrement value
            while (decrement + line[i] < nums[i]) {
                // If all queries have been used up, return -1
                if (queryIndex == queries.size()) {
                    return -1;
                }

                // Extract the values from the current query
                const int l = queries[queryIndex][0];
                const int r = queries[queryIndex][1];
                const int val = queries[queryIndex][2];

                // Increment the query index to move to the next query
                ++queryIndex;

                // Skip the query if it doesn't affect the current range
                if (r < i) continue;

                // Apply the value to the line using a range increment technique
                line[max(l, i)] += val;
                if (r + 1 < line.size()) {
                    line[r + 1] -= val;
                }
            }
            // Update the decrement with the current line value
            decrement += line[i];
        }

        // Return the number of queries processed
        return queryIndex;
    }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [2, 0, 2], queries = [[0, 2, 1], [0, 2, 1], [1, 1, 3]]
```
### Steps
```
i=0: decrement+line[0]=0 < 2
  query 0: [0,2,1] → line[0]+=1, line[3]-=1 → line=[1,0,0,-1]
  decrement+line[0]=1 < 2
  query 1: [0,2,1] → line[0]+=1, line[3]-=1 → line=[2,0,0,-2]
  decrement+line[0]=2 >= 2 → ok
  decrement = 0+2 = 2
i=1: decrement+line[1]=2+0=2 >= 0 → ok, decrement=2
i=2: decrement+line[2]=2+0=2 >= 2 → ok, decrement=2
Result: 2
```

---

## ⏱️ Time Complexity
```
O(n + q) — each query is processed at most once
```

## 💾 Space Complexity
```
O(n) — for the difference array
```

---

## ⚠️ Edge Cases
- All `nums[i] = 0` → return 0 queries needed
- Query range entirely before current position → skip it
- Queries insufficient → return -1
- `val = 0` → query has no effect

---

## 🎯 Interview Takeaways
- Greedy query application with a difference array is more efficient than binary search for ordered queries.
- Starting the query effect from `max(l, i)` handles partially-relevant queries correctly.

---

## 📌 Key Pattern
👉 **"Greedy online processing with difference array for minimum query count"**

---

## 🔁 Related Problems
- 3355. Zero Array Transformation I
- 370. Range Addition
- 1589. Maximum Sum Obtained of Any Permutation

---

## 🚀 Final Thoughts
Building on the difference array from 3355, this version adds the optimization question: how many queries are needed? The greedy approach processes queries in order and stops as soon as each position is satisfied.

---

✨ **Rule to remember:**
> "Apply queries greedily until each position is satisfied, using a difference array for efficiency."
