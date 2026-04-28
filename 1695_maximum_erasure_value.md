# 1695. Maximum Erasure Value

## 🔗 Problem Link
https://leetcode.com/problems/maximum-erasure-value/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Hash Table, Sliding Window

---

## 🧩 Problem Summary
Given an array of positive integers `nums`, find the maximum sum of a contiguous subarray where all elements are unique. You "erase" (select) a subarray with all unique elements and want to maximise its sum.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^4`

---

## 💭 Intuition
👉 This is a classic sliding window problem: expand the right boundary to include new elements, and shrink the left boundary whenever a duplicate is encountered, maintaining a running sum of the current window.

---

## ⚡ Approach — Sliding Window with Hash Set

### 🧠 Idea
- Use two pointers `l` and `r` defining the current window.
- Maintain a hash set of elements in the current window and a running `score`.
- If inserting `nums[r]` causes a duplicate, remove elements from the left until the duplicate is gone.
- Track the maximum `score` seen.

---

## 💻 Code

```cpp
class Solution {
 public:
  int maximumUniqueSubarray(vector<int>& nums) {
    int ans = 0;
    int score = 0;
    unordered_set<int> seen;

    for (int l = 0, r = 0; r < nums.size(); ++r) {
      while (!seen.insert(nums[r]).second) {
        score -= nums[l];
        seen.erase(nums[l++]);
      }
      score += nums[r];
      ans = max(ans, score);
    }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [4, 2, 4, 5, 6]
```
### Steps
```
r=0: seen={4}, score=4, ans=4
r=1: seen={4,2}, score=6, ans=6
r=2: 4 duplicate → remove 4 (l=0→1), score=2, seen={2}
     insert 4, score=6, seen={2,4}, ans=6
r=3: seen={2,4,5}, score=11, ans=11
r=4: seen={2,4,5,6}, score=17, ans=17

Result: 17
```

---

## ⏱️ Time Complexity
```
O(n) — each element is added and removed from the set at most once
```

## 💾 Space Complexity
```
O(n) — hash set stores at most n unique elements
```

---

## ⚠️ Edge Cases
- All elements are the same → window size is always 1, answer is the max element.
- All elements are unique → answer is the sum of the entire array.
- Single element array → answer is that element.

---

## 🎯 Interview Takeaways
- Sliding window + hash set is the go-to pattern for "max/min subarray with unique elements."
- The `insert().second` trick in C++ simultaneously attempts insertion and checks for duplicates.
- Maintaining a running sum avoids recalculating the window sum each iteration.

---

## 📌 Key Pattern
👉 **"Sliding window with a hash set to maintain uniqueness and a running sum for efficiency"**

---

## 🔁 Related Problems
- 3. Longest Substring Without Repeating Characters
- 209. Minimum Size Subarray Sum
- 992. Subarrays with K Different Integers

---

## 🚀 Final Thoughts
A textbook sliding window problem. The key is recognising that the "unique elements" constraint maps perfectly to a set-based window, and maintaining a running sum keeps the solution efficient.

---

✨ **Rule to remember:**
> For maximum sum subarray with all unique elements, slide a window and shrink from the left whenever a duplicate appears.
