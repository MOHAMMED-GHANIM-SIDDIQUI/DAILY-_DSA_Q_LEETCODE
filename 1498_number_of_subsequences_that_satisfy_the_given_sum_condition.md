# 1498. Number of Subsequences That Satisfy the Given Sum Condition

## 🔗 Problem Link
https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Two Pointers, Sorting, Binary Search

---

## 🧩 Problem Summary
Given an array of integers `nums` and an integer `target`, return the number of non-empty subsequences such that the sum of the minimum and maximum element is less than or equal to `target`. Return the answer modulo `10^9 + 7`.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^6`
- `1 <= target <= 10^6`

---

## 💭 Intuition
👉 After sorting, if `nums[l] + nums[r] <= target`, then any subsequence with `nums[l]` as the minimum and any subset of elements between `l+1` and `r` is valid. This gives `2^(r-l)` valid subsequences for that `l`. We use two pointers to efficiently enumerate all valid pairs.

---

## ⚡ Approach — Sort + Two Pointers

### 🧠 Idea
- Sort the array so we can reason about min/max of subsequences.
- Precompute powers of 2 modulo `10^9 + 7`.
- Use two pointers: if `nums[l] + nums[r] <= target`, add `2^(r-l)` subsequences (all subsets of elements between l and r that include `nums[l]`) and advance `l`.
- Otherwise, shrink `r`.

---

## 💻 Code

```cpp
class Solution {
 public:
  int numSubseq(vector<int>& nums, int target) {
    constexpr int kMod = 1'000'000'007;
    const int n = nums.size();
    int ans = 0;
    vector<int> pows(n, 1);  // pows[i] = 2^i % kMod

    for (int i = 1; i < n; ++i)
      pows[i] = pows[i - 1] * 2 % kMod;

    ranges::sort(nums);

    for (int l = 0, r = n - 1; l <= r;)
      if (nums[l] + nums[r] <= target) {
        ans += pows[r - l];
        ans %= kMod;
        ++l;
      } else {
        --r;
      }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [3, 5, 6, 7], target = 9
```
### Steps
```
Sorted: [3, 5, 6, 7]
pows = [1, 2, 4, 8]

l=0, r=3: 3+7=10 > 9 → r=2
l=0, r=2: 3+6=9 <= 9 → ans += pows[2] = 4, ans=4, l=1
l=1, r=2: 5+6=11 > 9 → r=1
l=1, r=1: 5+5=10 > 9 → r=0
l=1 > r=0 → stop

Answer: 4 (subsequences: [3], [3,5], [3,6], [3,5,6])
```

---

## ⏱️ Time Complexity
```
O(n log n) for sorting + O(n) for two pointers = O(n log n)
```

## 💾 Space Complexity
```
O(n) for the precomputed powers array
```

---

## ⚠️ Edge Cases
- Single element — if `2 * nums[0] <= target`, answer is 1.
- All elements same — if `2 * nums[0] <= target`, answer is `2^n - 1`.
- No valid subsequence — return 0.

---

## 🎯 Interview Takeaways
- Sorting allows us to fix the min element and use two pointers for the max.
- Precomputing powers of 2 avoids repeated exponentiation.
- The key insight: for a sorted array, subsequences with min at index `l` and max at most index `r` have `2^(r-l)` choices.

---

## 📌 Key Pattern
👉 **"Sort + Two Pointers with power-of-2 counting for subsequence enumeration"**

---

## 🔁 Related Problems
- 167 — Two Sum II (sorted + two pointers)
- 611 — Valid Triangle Number
- 923 — 3Sum With Multiplicity

---

## 🚀 Final Thoughts
This problem combines sorting, two pointers, and combinatorics beautifully. The insight that sorting doesn't change the set of subsequences (only their order) and that fixing min/max reduces counting to powers of 2 is elegant and powerful.

---

✨ **Rule to remember:**
> "Sort the array, fix the min with left pointer, and count 2^(r-l) valid subsequences for each valid (l, r) pair."
