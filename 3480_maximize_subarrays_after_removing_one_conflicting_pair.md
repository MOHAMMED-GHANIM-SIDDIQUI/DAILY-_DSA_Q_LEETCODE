# 3480. Maximize Subarrays After Removing One Conflicting Pair

## 🔗 Problem Link
https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Greedy, Sweep Line, Prefix

---

## 🧩 Problem Summary
Given an integer `n` and a list of conflicting pairs, count the maximum number of valid subarrays of `[1..n]` if you are allowed to remove at most one conflicting pair. A subarray is invalid if it contains both elements of any conflicting pair.

### 📌 Constraints
- `1 <= n <= 10^5`
- `1 <= conflictingPairs.length <= 10^5`
- Each pair contains two distinct indices in `[1, n]`

---

## 💭 Intuition
👉 For each right endpoint, the most restrictive conflict determines where valid subarrays can start. If we track the **top two** most restrictive left endpoints, removing the most restrictive one gains us extra subarrays equal to the gap between the first and second most restrictive.

---

## ⚡ Approach — Greedy with Gain Tracking

### 🧠 Idea
- For each right endpoint `r`, maintain `maxLeft` (most restrictive) and `secondMaxLeft`.
- Valid subarrays ending at `r` start from `maxLeft + 1` to `r`.
- The "gain" from removing the restriction at `maxLeft` is `maxLeft - secondMaxLeft`.
- Accumulate gains per left endpoint, then pick the best one to remove.

---

## 💻 Code

```cpp
class Solution {
 public:
  long long maxSubarrays(int n, vector<vector<int>>& conflictingPairs) {
    long validSubarrays = 0;
    int maxLeft = 0;
    int secondMaxLeft = 0;
    // gains[i] := the number of additional valid subarrays we can gain if the
    // restriction at index `i` is removed
    vector<long> gains(n + 1);
    // conflicts[r] := left endpoints that conflict with subarrays ending in r
    vector<vector<int>> conflicts(n + 1);

    for (const vector<int>& pair : conflictingPairs) {
      const int a = pair[0];
      const int b = pair[1];
      conflicts[max(a, b)].push_back(min(a, b));
    }

    for (int right = 1; right <= n; ++right) {
      for (const int left : conflicts[right]) {
        if (left > maxLeft) {
          secondMaxLeft = maxLeft;
          maxLeft = left;
        } else if (left > secondMaxLeft) {
          secondMaxLeft = left;
        }
      }
      // Subarrays [maxLeft + 1..right],
      //           [maxLeft + 2..right],
      //           ...
      //           [right..right] are valid.
      validSubarrays += right - maxLeft;
      // If we remove `maxLeft` (the most restrictive conflict), we gain
      // `maxLeft - secondMaxLeft` new subarrays:
      // [secondMaxLeft + 1..right],
      // [secondMaxLeft + 2..right],
      // ...
      // [maxLeft..right].
      gains[maxLeft] += maxLeft - secondMaxLeft;
    }

    return validSubarrays + ranges::max(gains);
  }
};
```

---

## 🧠 Dry Run
### Input
```
n = 4, conflictingPairs = [[1,3],[2,4]]
```
### Steps
```
conflicts[3] = [1], conflicts[4] = [2]

right=1: maxLeft=0, valid += 1-0=1. Total=1
right=2: maxLeft=0, valid += 2-0=2. Total=3
right=3: conflict left=1, maxLeft=1, secondMax=0. valid += 3-1=2. Total=5. gains[1] += 1-0=1
right=4: conflict left=2, maxLeft=2, secondMax=1. valid += 4-2=2. Total=7. gains[2] += 2-1=1

max(gains) = 1
Result = 7 + 1 = 8
```

---

## ⏱️ Time Complexity
```
O(n + m) — where m is the number of conflicting pairs
```

## 💾 Space Complexity
```
O(n + m) — for conflicts and gains arrays
```

---

## ⚠️ Edge Cases
- No conflicting pairs → all n*(n+1)/2 subarrays are valid
- All pairs share the same left endpoint → removing that one element yields max gain
- Single element array

---

## 🎯 Interview Takeaways
- Tracking the top-2 most restrictive constraints lets you evaluate the impact of removing one.
- Sweep-line processing by right endpoint is a powerful technique for subarray problems.
- The "gain" concept transforms an optimization problem into a simple max selection.

---

## 📌 Key Pattern
👉 **"Track top-2 constraints per position to evaluate the benefit of removing the most restrictive one."**

---

## 🔁 Related Problems
- 2963. Count the Number of Good Partitions
- 828. Count Unique Characters of All Substrings
- 2262. Total Appeal of A String

---

## 🚀 Final Thoughts
This is a clever greedy problem where the key observation is that only the most restrictive conflict matters at each position. By precomputing gains, we avoid brute-force enumeration of which pair to remove.

---

✨ **Rule to remember:**
> When allowed to remove one constraint, track the top two constraints — the gain is the gap between them.
