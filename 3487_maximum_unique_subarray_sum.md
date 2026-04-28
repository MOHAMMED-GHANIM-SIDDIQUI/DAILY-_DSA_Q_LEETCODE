# 3487. Maximum Unique Subarray Sum

## 🔗 Problem Link
https://leetcode.com/problems/maximum-unique-subarray-sum/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Hash Set, Greedy

---

## 🧩 Problem Summary
Given an array of integers, find the maximum sum of a subarray where all elements are unique. If all elements are non-positive, return the maximum element. Otherwise, sum all unique positive elements.

### 📌 Constraints
- `1 <= nums.length <= 100`
- `-100 <= nums[i] <= 100`

---

## 💭 Intuition
👉 Since we want maximum sum with unique elements, we should include each **positive** number exactly once. If no positive number exists, just return the maximum element.

---

## ⚡ Approach — Greedy with HashSet

### 🧠 Idea
- Find the maximum element — if it's <= 0, return it directly (best we can do is a single element).
- Otherwise, put all elements in a set (deduplication) and sum only the positive ones.

---

## 💻 Code

```cpp
class Solution {
 public:
  int maxSum(vector<int>& nums) {
    const int mx = ranges::max(nums);
    if (mx <= 0)
      return mx;
    unordered_set<int> numsSet(nums.begin(), nums.end());
    return accumulate(numsSet.begin(), numsSet.end(), 0,
                      [](int acc, int num) { return acc + max(0, num); });
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [1, 2, 3, 4, 5]
```
### Steps
```
mx = 5 > 0
numsSet = {1, 2, 3, 4, 5}
Sum positive: 1+2+3+4+5 = 15

Result: 15
```

---

## ⏱️ Time Complexity
```
O(n) — single pass to build set and accumulate
```

## 💾 Space Complexity
```
O(n) — for the hash set
```

---

## ⚠️ Edge Cases
- All elements negative → return the largest (least negative)
- All elements the same positive value → return that value once
- Mix of positive and negative → only sum positive unique values

---

## 🎯 Interview Takeaways
- Greedy insight: including negative numbers never helps when maximizing a sum.
- Deduplication via hash set is the simplest way to ensure uniqueness.
- Handle the all-negative case separately as a special boundary.

---

## 📌 Key Pattern
👉 **"Deduplicate with a set, sum only positive values — handle the all-negative edge case separately."**

---

## 🔁 Related Problems
- 1695. Maximum Erasure Value
- 2 Sum variants
- 128. Longest Consecutive Sequence

---

## 🚀 Final Thoughts
A straightforward greedy problem. The key insight is that for maximizing sum with unique elements, you always want all distinct positive numbers. The edge case where all numbers are non-positive requires returning just the maximum.

---

✨ **Rule to remember:**
> To maximize a unique-element sum, take every distinct positive number — negatives only hurt you.
