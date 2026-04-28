# 3375. Minimum Operations to Make Array Values Equal to K

## 🔗 Problem Link
https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Hash Table, Greedy

---

## 🧩 Problem Summary
Given an array of integers and a target value k, determine the minimum number of operations to make all values equal to k. In each operation, you can select a value strictly greater than k and reduce all occurrences of a chosen value. Return -1 if it is impossible.

### 📌 Constraints
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
- 1 <= k <= 100

---

## 💭 Intuition
👉 If any element is less than k, it is impossible (return -1). Otherwise, each distinct value greater than k requires exactly one operation to reduce. If k itself is present, it does not need an operation.

---

## ⚡ Approach — Set-Based Counting

### 🧠 Idea
- Find the minimum value in the array.
- If min < k, return -1 (cannot increase values).
- Count unique values using a set.
- If min > k, every unique value needs one operation → return set size.
- If min == k, the value k is already present → return set size - 1.

---

## 💻 Code

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        // Step 1: Convert the vector to a set to get only unique elements
        const unordered_set<int> numsSet{nums.begin(), nums.end()};

        // Step 2: Find the minimum value in the array
        const int mn = ranges::min(nums);

        // Step 3: Check conditions based on the minimum value (mn) and k
        if (mn < k)
            return -1;  // If the minimum value is less than k, return -1

        if (mn > k)
            return numsSet.size();  // If the minimum value is greater than k, return the number of unique elements

        return numsSet.size() - 1;  // If the minimum value is equal to k, return one less than the number of unique elements
    }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [5, 2, 5, 4, 5], k = 2
```
### Steps
```
numsSet = {5, 2, 4} → size = 3
mn = 2
mn == k → return 3 - 1 = 2
Operations: reduce 4→2, reduce 5→2
```

---

## ⏱️ Time Complexity
```
O(n) — one pass to build set and find min
```

## 💾 Space Complexity
```
O(n) — for the unordered set
```

---

## ⚠️ Edge Cases
- All elements already equal to k → 0 operations
- Any element less than k → impossible (-1)
- All elements are the same and greater than k → 1 operation

---

## 🎯 Interview Takeaways
- Using a set to count distinct values simplifies the logic.
- Always check impossibility conditions first.
- The answer depends only on how many distinct values exceed k.

---

## 📌 Key Pattern
👉 **"Count distinct values + greedy reduction"**

---

## 🔁 Related Problems
- 2357. Make Array Zero by Subtracting Equal Amounts
- 1558. Minimum Number of Function Calls to Make Target Array

---

## 🚀 Final Thoughts
A straightforward problem where recognizing that each distinct value > k needs exactly one operation leads to an elegant set-based solution.

---

✨ **Rule to remember:**
> Count distinct values above the target — each one costs exactly one operation.
