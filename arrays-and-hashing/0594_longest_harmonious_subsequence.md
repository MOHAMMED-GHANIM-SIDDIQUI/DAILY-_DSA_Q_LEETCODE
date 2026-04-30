# 594. Longest Harmonious Subsequence

## 🔗 Problem Link
https://leetcode.com/problems/longest-harmonious-subsequence/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Hash Table, Sorting, Counting

---

## 🧩 Problem Summary
A harmonious array is one where the difference between its maximum and minimum values is exactly 1. Given an integer array nums, find the longest harmonious subsequence (not necessarily contiguous) among all its possible subsequences.

### 📌 Constraints
- `1 <= nums.length <= 2 * 10^4`
- `-10^9 <= nums[i] <= 10^9`

---

## 💭 Intuition
👉 A harmonious subsequence consists of exactly two distinct values differing by 1. Count frequencies and for each value, check if value + 1 exists; the subsequence length is the sum of their frequencies.

---

## ⚡ Approach — Hash Map Frequency Counting

### 🧠 Idea
- Count the frequency of each number using a hash map.
- For each number in the map, check if `num + 1` also exists.
- If so, the harmonious subsequence length is `freq(num) + freq(num + 1)`.
- Track the maximum across all such pairs.

---

## 💻 Code

```cpp
class Solution {
 public:
  int findLHS(vector<int>& nums) {
    int ans = 0;
    unordered_map<int, int> count;

    for (const int num : nums)
      ++count[num];

    for (const auto& [num, freq] : count)
      if (const auto it = count.find(num + 1); it != count.cend())
        ans = max(ans, freq + it->second);

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [1, 3, 2, 2, 5, 2, 3, 7]
```
### Steps
```
Frequencies: {1:1, 3:2, 2:3, 5:1, 7:1}
num=1: check 2 exists? yes -> 1+3=4
num=3: check 4 exists? no
num=2: check 3 exists? yes -> 3+2=5
num=5: check 6 exists? no
num=7: check 8 exists? no
Max = 5 (subsequence: [2,2,2,3,3])
```

---

## ⏱️ Time Complexity
```
O(n) — one pass to count, one pass to check pairs
```

## 💾 Space Complexity
```
O(n) — hash map for frequencies
```

---

## ⚠️ Edge Cases
- All elements are the same — no harmonious subsequence (return 0).
- Only two distinct values differing by 1 — entire array is harmonious.
- No adjacent values exist — return 0.
- Negative numbers — handled naturally by hash map.

---

## 🎯 Interview Takeaways
- The key insight is that harmonious = exactly two values differing by 1.
- Frequency counting with hash maps is a standard technique.
- Only checking `num + 1` (not `num - 1`) avoids double counting.

---

## 📌 Key Pattern
👉 **"Count frequencies and check adjacent values — harmonious means diff of exactly 1"**

---

## 🔁 Related Problems
- 128. Longest Consecutive Sequence
- 532. K-diff Pairs in an Array

---

## 🚀 Final Thoughts
This problem is a straightforward application of frequency counting. The main insight is that a harmonious subsequence must contain exactly two distinct values with a difference of 1, reducing the problem to finding the best pair.

---

✨ **Rule to remember:**
> "Harmonious = two values, diff of 1 — count frequencies and maximize the pair sum."
