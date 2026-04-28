# 3354. Make Array Elements Equal to Zero

## 🔗 Problem Link
https://leetcode.com/problems/make-array-elements-equal-to-zero/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Prefix Sum, Simulation

---

## 🧩 Problem Summary
Given an array `nums`, count positions `i` where `nums[i] == 0` such that starting at position `i` and moving in either direction, you can reduce all elements to zero by subtracting 1 from each non-zero element you pass. A valid selection requires the prefix sum to the left and suffix sum to the right to satisfy balance conditions.

### 📌 Constraints
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 100`

---

## 💭 Intuition
👉 For a zero position, going left reduces the prefix sum and going right reduces the suffix sum. If prefix equals suffix, both directions work (2 options). If they differ by 1, exactly one direction works (1 option).

---

## ⚡ Approach — Prefix and Suffix Sum Comparison

### 🧠 Idea
- Compute prefix sums (sum of elements to the left) and suffix sums (sum of elements to the right).
- For each zero position: if prefix == suffix, add 2; if |prefix - suffix| == 1, add 1.

---

## 💻 Code

```cpp
class Solution {
 public:
  int countValidSelections(vector<int>& nums) {
    const int n = nums.size();
    int ans = 0;
    vector<int> prefix(n);  // sum(nums[0..i - 1])
    vector<int> suffix(n);  // sum(nums[i + 1..n - 1])

    for (int i = 1; i < n; ++i)
      prefix[i] = prefix[i - 1] + nums[i - 1];

    for (int i = n - 2; i >= 0; --i)
      suffix[i] = suffix[i + 1] + nums[i + 1];

    for (int i = 0; i < n; ++i) {
      if (nums[i] > 0)
        continue;
      if (prefix[i] == suffix[i])
        ans += 2;  // Go to either direction.
      if (abs(prefix[i] - suffix[i]) == 1)
        ans += 1;  // Go to the direction with the larger sum.
    }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [1, 0, 2, 0, 3]
```
### Steps
```
prefix = [0, 1, 1, 3, 3]
suffix = [5, 5, 3, 3, 0]
i=1: nums[1]=0, prefix=1, suffix=5, diff=4 → skip
i=3: nums[3]=0, prefix=3, suffix=3, equal → ans += 2
Result: 2
```

---

## ⏱️ Time Complexity
```
O(n) — two passes for prefix/suffix, one pass for counting
```

## 💾 Space Complexity
```
O(n) — for prefix and suffix arrays
```

---

## ⚠️ Edge Cases
- No zeros in array → answer is 0
- All zeros → each position contributes 2 (prefix == suffix == 0)
- Zero at the boundary → only one direction possible if sums differ by 1

---

## 🎯 Interview Takeaways
- Prefix and suffix sums are a fundamental tool for balance-checking problems.
- When choices depend on left-right symmetry, compare prefix and suffix sums.

---

## 📌 Key Pattern
👉 **"Prefix-suffix sum comparison for directional balance problems"**

---

## 🔁 Related Problems
- 724. Find Pivot Index
- 1991. Find the Middle Index in Array

---

## 🚀 Final Thoughts
A clean application of prefix and suffix sums. The key observation is that balance (equal sums) allows both directions, while a difference of 1 allows exactly one.

---

✨ **Rule to remember:**
> "Equal prefix and suffix sums mean two choices; a difference of one means exactly one choice."
