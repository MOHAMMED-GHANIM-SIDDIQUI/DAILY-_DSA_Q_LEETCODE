# 3208. Alternating Groups II

## 🔗 Problem Link
https://leetcode.com/problems/alternating-groups-ii/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Sliding Window

---

## 🧩 Problem Summary
Given a circular array of colors (0s and 1s) and an integer k, count the number of alternating groups of size k. An alternating group is a contiguous subarray of length k where every pair of adjacent elements has different colors, considering the array as circular.

### 📌 Constraints
- 3 <= colors.length <= 10^5
- 0 <= colors[i] <= 1
- 3 <= k <= colors.length

---

## 💭 Intuition
👉 Track the length of the current alternating run. When the run reaches k or more, each new position adds a valid group. Handle circularity by iterating n + k - 2 times using modular indexing.

---

## ⚡ Approach — Sliding Window on Circular Array

### 🧠 Idea
- Maintain a counter `alternating` that tracks the current run of alternating elements
- If current color equals previous, reset to 1; otherwise increment
- When alternating >= k, a valid group ends at the current position
- Iterate n + k - 2 positions to handle wrap-around

---

## 💻 Code

```cpp
class Solution {
 public:
  int numberOfAlternatingGroups(vector<int>& colors, int k) {
    const int n = colors.size();
    int ans = 0;
    int alternating = 1;

    for (int i = 0; i < n + k - 2; ++i) {
      alternating =
          colors[i % n] == colors[(i - 1 + n) % n] ? 1 : alternating + 1;
      if (alternating >= k)
        ++ans;
    }

    return ans;
  }

};
```

---

## 🧠 Dry Run
### Input
```
colors = [0, 1, 0, 1, 0], k = 3
```
### Steps
```
n=5, iterate i=0..5 (n+k-2=6 iterations)
i=0: colors[0]=0, colors[4]=0 -> same, alt=1
i=1: colors[1]=1, colors[0]=0 -> diff, alt=2
i=2: colors[2]=0, colors[1]=1 -> diff, alt=3 >=3 -> ans=1
i=3: colors[3]=1, colors[2]=0 -> diff, alt=4 >=3 -> ans=2
i=4: colors[4]=0, colors[3]=1 -> diff, alt=5 >=3 -> ans=3
i=5: colors[0]=0, colors[4]=0 -> same, alt=1
Result: 3
```

---

## ⏱️ Time Complexity
```
O(n) — single pass with wrap-around
```

## 💾 Space Complexity
```
O(1) — only tracking variables
```

---

## ⚠️ Edge Cases
- Entire array is alternating — every starting position is valid
- No alternating group of length k exists — return 0
- k equals array length — at most one valid group (the entire array)

---

## 🎯 Interview Takeaways
- Circular arrays can be handled by extending iteration to n + k - 2 with modular indexing
- Tracking the alternating run length avoids explicit window management
- The "n + k - 2" bound ensures each possible starting position is covered exactly once

---

## 📌 Key Pattern
👉 **"Run-length tracking on a circular array with extended iteration"**

---

## 🔁 Related Problems
- 3207. Alternating Groups I
- 1004. Max Consecutive Ones III
- 567. Permutation in String

---

## 🚀 Final Thoughts
The run-length approach combined with circular iteration (n + k - 2 steps) is both elegant and efficient. It avoids duplicating the array or using complex window management for the circular case.

---

✨ **Rule to remember:**
> For circular alternating groups, iterate n + k - 2 times and count when the alternating run reaches k.
