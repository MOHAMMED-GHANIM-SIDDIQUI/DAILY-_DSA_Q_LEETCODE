# 3355. Zero Array Transformation I

## 🔗 Problem Link
https://leetcode.com/problems/zero-array-transformation-i/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Prefix Sum, Line Sweep

---

## 🧩 Problem Summary
Given an array `nums` and queries where each query `[l, r]` decrements all elements in `nums[l..r]` by 1, determine if all elements can be reduced to zero or below after applying all queries.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^5`
- `1 <= queries.length <= 10^5`
- `queries[i] = [l, r]`

---

## 💭 Intuition
👉 Use a difference array (line sweep) to compute the total decrement at each position from all queries. Then check if each position's decrement is at least `nums[i]`.

---

## ⚡ Approach — Difference Array (Line Sweep)

### 🧠 Idea
- Build a difference array `line` where `line[l]++` and `line[r+1]--` for each query.
- Compute the prefix sum of `line` to get actual decrements at each index.
- If `decrement >= nums[i]` for all `i`, return true.

---

## 💻 Code

```cpp
class Solution {
 public:
  bool isZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
    vector<int> line(nums.size() + 1);
    int decrement = 0;

    for (const vector<int>& query : queries) {
      const int l = query[0];
      const int r = query[1];
      ++line[l];
      --line[r + 1];
    }

    for (int i = 0; i < nums.size(); ++i) {
      decrement += line[i];
      if (decrement < nums[i])
        return false;
    }

    return true;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [1, 0, 1], queries = [[0, 2]]
```
### Steps
```
line = [1, 0, 0, -1]
i=0: decrement=1, nums[0]=1 → 1 >= 1 ✓
i=1: decrement=1, nums[1]=0 → 1 >= 0 ✓
i=2: decrement=1, nums[2]=1 → 1 >= 1 ✓
Result: true
```

---

## ⏱️ Time Complexity
```
O(n + q) — where n is array length and q is number of queries
```

## 💾 Space Complexity
```
O(n) — for the difference array
```

---

## ⚠️ Edge Cases
- Empty queries → only works if all `nums[i] == 0`
- Overlapping queries → difference array correctly sums overlapping ranges
- `nums[i] = 0` → always satisfies the condition

---

## 🎯 Interview Takeaways
- Difference arrays turn range updates into O(1) operations.
- Always think "difference array" when you see range increment/decrement problems.

---

## 📌 Key Pattern
👉 **"Difference array for efficient range update and point query"**

---

## 🔁 Related Problems
- 3356. Zero Array Transformation II
- 370. Range Addition
- 1109. Corporate Flight Bookings

---

## 🚀 Final Thoughts
A textbook application of the difference array technique. The line sweep approach processes all queries in O(q) and validates in O(n), making it highly efficient.

---

✨ **Rule to remember:**
> "For range updates, use a difference array: increment at start, decrement after end."
