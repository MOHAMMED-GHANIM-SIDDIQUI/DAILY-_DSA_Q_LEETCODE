# 2563. Count the Number of Fair Pairs

## 🔗 Problem Link
https://leetcode.com/problems/count-the-number-of-fair-pairs/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Two Pointers, Binary Search, Sorting

---

## 🧩 Problem Summary
Given a 0-indexed integer array `nums` and two integers `lower` and `upper`, return the number of fair pairs `(i, j)` where `0 <= i < j < n` and `lower <= nums[i] + nums[j] <= upper`.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `nums.length == n`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= lower <= upper <= 10^9`

---

## 💭 Intuition
👉 After sorting, for each element `nums[i]`, the valid partner `nums[j]` must lie in the range `[lower - nums[i], upper - nums[i]]`. We can use binary search (`lower_bound` / `upper_bound`) to find the count of valid partners in the remaining array.

---

## ⚡ Approach — Sort + Binary Search

### 🧠 Idea
- Sort the array.
- For each index `i`, compute the valid range for `nums[j]`: `[lower - nums[i], upper - nums[i]]`.
- Use `lower_bound` and `upper_bound` on `nums[i+1..n-1]` to count valid `j` indices.
- Sum up all valid pair counts.

---

## 💻 Code

```cpp
class Solution {
public:
    long long countFairPairs(vector<int>& nums, int lower, int upper) {
        sort(nums.begin(), nums.end()); // Sort for binary search
        long long count = 0;
        int n = nums.size();

        for (int i = 0; i < n; ++i) {
            int left = lower - nums[i];
            int right = upper - nums[i];

            // Use binary search to find the valid range
            int low = lower_bound(nums.begin() + i + 1, nums.end(), left) - nums.begin();
            int high = upper_bound(nums.begin() + i + 1, nums.end(), right) - nums.begin();

            count += (high - low);
        }

        return count;
    }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [0,1,7,4,4,5], lower = 3, upper = 6
```
### Steps
```
Sorted: [0, 1, 4, 4, 5, 7]
i=0 (val=0): range [3,6], search in [1,4,4,5,7] => [4,4,5] => 3 pairs
i=1 (val=1): range [2,5], search in [4,4,5,7] => [4,4,5] => 3 pairs
i=2 (val=4): range [-1,2], search in [4,5,7] => none => 0 pairs
i=3 (val=4): range [-1,2], search in [5,7] => none => 0 pairs
i=4 (val=5): range [-2,1], search in [7] => none => 0 pairs
Total = 6
```

---

## ⏱️ Time Complexity
```
O(n log n)
```

## 💾 Space Complexity
```
O(1) (ignoring sort space)
```

---

## ⚠️ Edge Cases
- Negative numbers in the array
- `lower == upper`: looking for exact sum pairs
- No valid pairs exist
- All pairs are valid

---

## 🎯 Interview Takeaways
- Sorting + binary search is a classic approach for pair-sum range counting.
- `lower_bound` finds the first element >= target; `upper_bound` finds the first element > target. Their difference gives count in range.

---

## 📌 Key Pattern
👉 **"Sort + Binary Search for counting pairs within a sum range"**

---

## 🔁 Related Problems
- 1. Two Sum
- 167. Two Sum II - Input Array Is Sorted
- 327. Count of Range Sum

---

## 🚀 Final Thoughts
This is a clean application of sorting and binary search for pair counting. The key is recognizing that sorting doesn't affect the pair count (since order doesn't matter for the sum condition) and enables efficient range queries.

---

✨ **Rule to remember:**
> To count pairs with sums in a range, sort the array and binary search for valid partners of each element.
