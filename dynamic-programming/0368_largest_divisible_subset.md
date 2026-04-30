# 368. Largest Divisible Subset

## 🔗 Problem Link
https://leetcode.com/problems/largest-divisible-subset/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Math, Dynamic Programming, Sorting

---

## 🧩 Problem Summary
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements satisfies either Si % Sj == 0 or Sj % Si == 0. Return any valid largest subset.

### 📌 Constraints
- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 2 * 10^9`
- All integers in nums are unique.

---

## 💭 Intuition
👉 After sorting, if a divides b and b divides c, then a divides c (transitivity). So we only need to check divisibility with the last element in the chain, making this a longest-increasing-subsequence-style DP.

---

## ⚡ Approach — Dynamic Programming with Path Reconstruction

### 🧠 Idea
- Sort the array so divisibility chains go left to right.
- Use `sizeEndsAt[i]` to track the longest chain ending at index i.
- Use `prevIndex[i]` to reconstruct the actual subset.
- For each element, check all previous elements for divisibility and extend the best chain.
- Track the global best and reconstruct the answer by following `prevIndex`.

---

## 💻 Code

```cpp
class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        const int n = nums.size();
        if (n == 0) return {};  // Return an empty result if the input is empty

        vector<int> ans;
        vector<int> sizeEndsAt(n, 1);  // Tracks the maximum subset size ending at index i
        vector<int> prevIndex(n, -1);  // Tracks the previous index for subset construction
        int maxSize = 1;  // Max size of the subset
        int bestIndex = 0;  // The index of the element that ends the largest subset

        // Sort the numbers to ensure we can form divisibility chains.
        sort(nums.begin(), nums.end());

        // Build the dynamic programming table.
        for (int i = 1; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                if (nums[i] % nums[j] == 0 && sizeEndsAt[i] < sizeEndsAt[j] + 1) {
                    sizeEndsAt[i] = sizeEndsAt[j] + 1;
                    prevIndex[i] = j;
                }
            }
            // Update the maxSize and the bestIndex when a larger subset is found.
            if (sizeEndsAt[i] > maxSize) {
                maxSize = sizeEndsAt[i];
                bestIndex = i;
            }
        }

        // Reconstruct the largest divisible subset by following prevIndex.
        while (bestIndex != -1) {
            ans.push_back(nums[bestIndex]);
            bestIndex = prevIndex[bestIndex];
        }

        // Reverse the answer to have the correct order from smallest to largest
        reverse(ans.begin(), ans.end());

        return ans;
    }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [1, 2, 4, 8]
```
### Steps
```
After sorting: [1, 2, 4, 8]
i=1: 2%1==0 -> sizeEndsAt[1]=2, prevIndex[1]=0, maxSize=2, bestIndex=1
i=2: 4%1==0 -> sizeEndsAt[2]=2, prevIndex[2]=0
     4%2==0 -> sizeEndsAt[2]=3, prevIndex[2]=1, maxSize=3, bestIndex=2
i=3: 8%1==0 -> sizeEndsAt[3]=2, prevIndex[3]=0
     8%2==0 -> sizeEndsAt[3]=3, prevIndex[3]=1
     8%4==0 -> sizeEndsAt[3]=4, prevIndex[3]=2, maxSize=4, bestIndex=3
Reconstruct: 8->4->2->1, reverse: [1,2,4,8]
```

---

## ⏱️ Time Complexity
```
O(n^2) — nested loops over all pairs
```

## 💾 Space Complexity
```
O(n) — for the DP and prevIndex arrays
```

---

## ⚠️ Edge Cases
- Single element — return that element.
- No element divides another — return any single element.
- All elements form a chain — return the entire sorted array.
- Very large numbers — divisibility check still O(1).

---

## 🎯 Interview Takeaways
- Sorting transforms the problem into a LIS-like DP.
- Transitivity of divisibility means we only check adjacent pairs in the chain.
- Path reconstruction with `prevIndex` is a common DP technique.

---

## 📌 Key Pattern
👉 **"Sort + LIS-style DP with divisibility as the chain condition"**

---

## 🔁 Related Problems
- 300. Longest Increasing Subsequence
- 1027. Longest Arithmetic Subsequence

---

## 🚀 Final Thoughts
This problem elegantly combines sorting with LIS-style dynamic programming. The key mathematical insight is that divisibility is transitive in a sorted array, so we only need to extend from the nearest divisor in the chain.

---

✨ **Rule to remember:**
> "Sort first, then build the longest divisibility chain — it's LIS with a modulo twist."
