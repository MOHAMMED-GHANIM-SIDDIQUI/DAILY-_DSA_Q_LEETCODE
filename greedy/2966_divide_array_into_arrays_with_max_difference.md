# 2966. Divide Array Into Arrays With Max Difference

## 🔗 Problem Link
https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Greedy, Sorting

---

## 🧩 Problem Summary
Given an integer array `nums` of size `n` (divisible by 3) and an integer `k`, divide the array into `n/3` groups of 3 elements each such that the difference between the max and min in each group is at most `k`. Return the groups, or an empty array if impossible.

### 📌 Constraints
- 1 <= n <= 10^5
- n is divisible by 3
- 1 <= nums[i] <= 10^5
- 0 <= k <= 10^5

---

## 💭 Intuition
👉 Sort the array first. Then greedily group every 3 consecutive elements. After sorting, consecutive elements have the smallest possible differences, so if any consecutive triple fails the condition, no valid grouping exists.

---

## ⚡ Approach — Sort and Group

### 🧠 Idea
- Sort `nums` in non-decreasing order.
- Group elements in consecutive triples: `[nums[i-2], nums[i-1], nums[i]]` for `i = 2, 5, 8, ...`.
- For each group, check if `nums[i] - nums[i-2] > k`. If so, return empty.
- Otherwise, add the group to the answer.

---

## 💻 Code

```cpp
class Solution {
 public:
  vector<vector<int>> divideArray(vector<int>& nums, int k) {
    vector<vector<int>> ans;

    ranges::sort(nums);

    for (int i = 2; i < nums.size(); i += 3) {
      if (nums[i] - nums[i - 2] > k)
        return {};
      ans.push_back({nums[i - 2], nums[i - 1], nums[i]});
    }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [1,3,4,8,7,9,3,5,1], k = 2
```
### Steps
```
After sorting: [1, 1, 3, 3, 4, 5, 7, 8, 9]

i=2: group [1,1,3], diff = 3-1 = 2 <= 2 ✓
i=5: group [3,4,5], diff = 5-3 = 2 <= 2 ✓
i=8: group [7,8,9], diff = 9-7 = 2 <= 2 ✓

Output: [[1,1,3],[3,4,5],[7,8,9]]
```

---

## ⏱️ Time Complexity
```
O(n log n) — dominated by sorting
```

## 💾 Space Complexity
```
O(n) — for the result array (O(1) extra if not counting output)
```

---

## ⚠️ Edge Cases
- `k = 0`: Only works if every consecutive triple has identical elements.
- Array already sorted: grouping is straightforward.
- Impossible case: returns empty array immediately upon first failing triple.

---

## 🎯 Interview Takeaways
- Sorting + greedy consecutive grouping is optimal for minimizing within-group differences.
- After sorting, the max difference in a group of consecutive elements is just `last - first`.
- Early termination on failure avoids unnecessary work.

---

## 📌 Key Pattern
👉 **"Sort and greedily group consecutive elements for minimum-difference partitioning"**

---

## 🔁 Related Problems
- 846. Hand of Straights
- 1296. Divide Array in Sets of K Consecutive Numbers
- 2294. Partition Array Such That Maximum Difference Is K

---

## 🚀 Final Thoughts
Sorting reduces this problem to a simple linear scan. The greedy choice of grouping consecutive elements is optimal because any other grouping would only increase the within-group difference. Clean and efficient.

---

✨ **Rule to remember:**
> To minimize max-min difference in fixed-size groups, sort first and group consecutive elements.
