# 2537. Count the Number of Good Subarrays

## 🔗 Problem Link
https://leetcode.com/problems/count-the-number-of-good-subarrays/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Hash Table, Sliding Window

---

## 🧩 Problem Summary
Given an integer array `nums` and an integer `k`, return the number of good subarrays. A subarray is good if there are at least `k` pairs of indices `(i, j)` such that `i < j` and `nums[i] == nums[j]` within the subarray.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i], k <= 10^9`

---

## 💭 Intuition
👉 When we add a new element `nums[r]` to the window, the number of new equal pairs formed equals the current count of `nums[r]` already in the window. We shrink from the left when pairs >= k, and all windows starting from indices `0` to `l-1` with right endpoint `r` are good.

---

## ⚡ Approach — Sliding Window

### 🧠 Idea
- Maintain a sliding window `[l, r]` and a hash map tracking element frequencies.
- When adding `nums[r]`, increment pairs by `count[nums[r]]` (existing occurrences form new pairs).
- While `pairs >= k`, shrink from the left by removing `nums[l]` and decrementing pairs accordingly.
- After shrinking, all subarrays `nums[0..r], nums[1..r], ..., nums[l-1..r]` are good, so add `l` to the answer.

---

## 💻 Code

```cpp

class Solution {
 public:
  long long countGood(vector<int>& nums, int k) {
    long ans = 0;
    int pairs = 0;
    unordered_map<int, int> count;

    for (int l = 0, r = 0; r < nums.size(); ++r) {
      // Since there're count[r] nums[r]s, including nums[r] to the window will
      // increase the number of good subarrays by count[r].
      pairs += count[nums[r]]++;
      while (pairs >= k)
        pairs -= --count[nums[l++]];
      // nums[0..r], nums[1..r], ..., nums[l - 1..r] are good subarrays, so add
      // l to `ans`.
      ans += l;
    }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [1,1,1,1,1], k = 10
```
### Steps
```
r=0: count={1:1}, pairs=0, ans+=0 => ans=0
r=1: count={1:2}, pairs=1, ans+=0 => ans=0
r=2: count={1:3}, pairs=3, ans+=0 => ans=0
r=3: count={1:4}, pairs=6, ans+=0 => ans=0
r=4: count={1:5}, pairs=10 >= 10
  shrink l=0: pairs=10-4=6, count={1:4}, l=1
  6 < 10, stop shrinking
  ans += 1 => ans=1
Result: 1
```

---

## ⏱️ Time Complexity
```
O(n)
```

## 💾 Space Complexity
```
O(n) for the hash map
```

---

## ⚠️ Edge Cases
- All elements are the same — many pairs form quickly
- k is very large — no good subarrays exist, answer is 0
- Array of length 1 — no pairs possible

---

## 🎯 Interview Takeaways
- When adding element `x` to a window with `c` existing copies, the number of new pairs is exactly `c`.
- The sliding window "shrink from left, count valid starting points" pattern is powerful for counting subarrays satisfying a monotonic condition.

---

## 📌 Key Pattern
👉 **"Sliding window with pair counting — shrink left, add left index to answer"**

---

## 🔁 Related Problems
- 992. Subarrays with K Different Integers
- 1248. Count Number of Nice Subarrays
- 2799. Count Complete Subarrays in an Array

---

## 🚀 Final Thoughts
The key insight is that adding an element contributes exactly `count[element]` new pairs. Combined with the sliding window technique of counting valid left endpoints, this yields an elegant O(n) solution.

---

✨ **Rule to remember:**
> When counting pairs of equal elements in a sliding window, each new duplicate adds exactly "its current frequency" new pairs.
