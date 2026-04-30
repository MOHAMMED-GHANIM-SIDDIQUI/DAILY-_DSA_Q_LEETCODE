# 2200. Find All K-Distant Indices in an Array

## 🔗 Problem Link
https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Two Pointers

---

## 🧩 Problem Summary
Given an array `nums`, a target `key`, and a distance `k`, find all indices `i` such that there exists some index `j` where `nums[j] == key` and `|i - j| <= k`. Return the indices in increasing order.

### 📌 Constraints
- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 1000`
- `key` is an integer
- `1 <= k <= nums.length`

---

## 💭 Intuition
👉 Use two pointers: for each index `i`, find the first key-index `j` that is within range `[i-k, i+k]` and check if the distance condition holds.

---

## ⚡ Approach — Two Pointers

### 🧠 Idea
- Maintain a pointer `j` to the current candidate key-index.
- For each `i`, advance `j` until `nums[j] == key` and `j >= i - k`.
- If `|i - j| <= k`, include `i` in the result.

---

## 💻 Code

```cpp
class Solution {
 public:
  vector<int> findKDistantIndices(vector<int>& nums, int key, int k) {
    const int n = nums.size();
    vector<int> ans;

    for (int i = 0, j = 0; i < n; ++i) {
      // the first index j s.t. nums[j] == key and j >= i - k
      while (j < n && (nums[j] != key || j < i - k))
        ++j;
      if (j == n)
        break;
      if (abs(i - j) <= k)
        ans.push_back(i);
    }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [3, 4, 9, 1, 3, 9, 5], key = 9, k = 1
```
### Steps
```
i=0: j advances to 2 (nums[2]=9), |0-2|=2 > 1 → skip
i=1: j=2, |1-2|=1 <= 1 → add 1
i=2: j=2, |2-2|=0 <= 1 → add 2
i=3: j=2, |3-2|=1 <= 1 → add 3
i=4: j advances to 5 (nums[5]=9), |4-5|=1 <= 1 → add 4
i=5: j=5, |5-5|=0 <= 1 → add 5
i=6: j=5, |6-5|=1 <= 1 → add 6
Result: [1, 2, 3, 4, 5, 6]
```

---

## ⏱️ Time Complexity
```
O(n) — each pointer advances at most n times
```

## 💾 Space Complexity
```
O(1) — excluding the output array
```

---

## ⚠️ Edge Cases
- `key` not present in `nums` → return empty array
- `k >= n` → all indices are within range of any key-index
- All elements equal to `key` → all indices included

---

## 🎯 Interview Takeaways
- Two-pointer technique avoids brute-force O(n^2) pair checking.
- The `j` pointer only moves forward, ensuring linear time.
- Careful handling of the `j < i - k` condition is crucial for correctness.

---

## 📌 Key Pattern
👉 **"Two pointers to find nearest key-index within distance k"**

---

## 🔁 Related Problems
- 2180. Count Integers With Even Digit Sum
- 1. Two Sum
- 713. Subarray Product Less Than K

---

## 🚀 Final Thoughts
A clean two-pointer problem where the key insight is that the pointer to key-indices only needs to move forward. This avoids redundant scans and keeps the solution linear.

---

✨ **Rule to remember:**
> "Use a forward-only pointer to track the nearest key-index and check distance for each position."
