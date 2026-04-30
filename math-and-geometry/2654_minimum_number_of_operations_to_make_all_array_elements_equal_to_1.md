# 2654. Minimum Number of Operations to Make All Array Elements Equal to 1

## 🔗 Problem Link
https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Math, Number Theory, GCD

---

## 🧩 Problem Summary
Given an array of positive integers, in one operation you can replace any element with the GCD of it and an adjacent element. Return the minimum number of operations to make all elements equal to 1, or -1 if impossible.

### 📌 Constraints
- `2 <= nums.length <= 50`
- `1 <= nums[i] <= 10^6`

---

## 💭 Intuition
👉 If the array already contains 1s, each non-1 element needs one operation (GCD with a 1 neighbor). If no 1 exists, we need to first create a 1 by finding the shortest subarray whose GCD is 1 — that takes `(subarray length - 1)` operations — then spread the 1 to all other elements.

---

## ⚡ Approach — Shortest Subarray with GCD 1

### 🧠 Idea
- Count existing 1s. If any exist, answer is `n - count_of_ones`.
- Otherwise, find the shortest subarray `[i..j]` with GCD = 1. The operations to create a 1 from this subarray is `j - i`.
- Then `n - 1` additional operations spread the 1 to all other elements.
- If no subarray has GCD 1, return -1 (the overall GCD > 1).

---

## 💻 Code

```cpp
class Solution {
 public:
  int minOperations(vector<int>& nums) {
    const int n = nums.size();
    const int ones = ranges::count(nums, 1);
    if (ones > 0)
      return n - ones;

    // the minimum operations to make the shortest subarray with a gcd == 1
    int minOps = INT_MAX;

    for (int i = 0; i < n; ++i) {
      int g = nums[i];
      for (int j = i + 1; j < n; ++j) {
        g = __gcd(g, nums[j]);
        if (g == 1) {  // gcd(nums[i..j]) == 1
          minOps = min(minOps, j - i);
          break;
        }
      }
    }

    // After making the shortest subarray with `minOps`, need additional n - 1
    // operations to make the other numbers to 1.
    return minOps == INT_MAX ? -1 : minOps + n - 1;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [2, 6, 3, 4]
```
### Steps
```
No 1s in array. ones = 0.

i=0: g=2
  j=1: g=gcd(2,6)=2
  j=2: g=gcd(2,3)=1 → minOps=min(INF,2)=2, break

i=1: g=6
  j=2: g=gcd(6,3)=3
  j=3: g=gcd(3,4)=1 → minOps=min(2,2)=2, break

i=2: g=3
  j=3: g=gcd(3,4)=1 → minOps=min(2,1)=1, break

minOps=1, answer = 1 + 4 - 1 = 4
```

---

## ⏱️ Time Complexity
```
O(n^2 * log(max_val)) — nested loop with GCD computation.
```

## 💾 Space Complexity
```
O(1) — constant extra space.
```

---

## ⚠️ Edge Cases
- Array already all 1s: return 0.
- Overall GCD > 1: impossible, return -1.
- Array has some 1s: just count non-1 elements.

---

## 🎯 Interview Takeaways
- If the GCD of the entire array is not 1, it is impossible to produce a 1.
- Finding the shortest subarray with GCD 1 is the core subproblem.
- Once a 1 exists, spreading it to all n elements takes n-1 operations.

---

## 📌 Key Pattern
👉 **"Shortest subarray with target GCD + propagation cost."**

---

## 🔁 Related Problems
- 1250. Check If It Is a Good Array
- 2447. Number of Subarrays With GCD Equal to K
- 1819. Number of Different Subsequences GCDs

---

## 🚀 Final Thoughts
The problem elegantly combines number theory (GCD properties) with subarray search. The two-phase approach — first create a 1, then propagate it — is a clean decomposition. The early break when GCD reaches 1 is an important optimization.

---

✨ **Rule to remember:**
> "To make all elements 1: find the shortest subarray with GCD 1, then propagate."
