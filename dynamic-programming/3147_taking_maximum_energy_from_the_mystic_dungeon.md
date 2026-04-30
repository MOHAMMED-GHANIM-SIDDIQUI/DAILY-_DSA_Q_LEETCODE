# 3147. Taking Maximum Energy From the Mystic Dungeon

## 🔗 Problem Link
https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Dynamic Programming, Prefix Sum

---

## 🧩 Problem Summary
Given an array `energy` and integer `k`, you start at any index and can jump forward by exactly `k` steps each time, collecting energy at each position. Find the maximum total energy you can collect.

### 📌 Constraints
- 1 <= energy.length <= 10^5
- -1000 <= energy[i] <= 1000
- 1 <= k <= energy.length

---

## 💭 Intuition
👉 Process from right to left: each position's best total is its own value plus the best from position i+k. Then take the global maximum.

---

## ⚡ Approach — Suffix DP

### 🧠 Idea
- Copy energy into dp array
- From index n-1-k down to 0, accumulate dp[i] += dp[i+k]
- The answer is the maximum value in dp

---

## 💻 Code

```cpp
class Solution {
 public:
  int maximumEnergy(vector<int>& energy, int k) {
    vector<int> dp(energy);
    for (int i = energy.size() - 1 - k; i >= 0; --i)
      dp[i] += dp[i + k];
    return ranges::max(dp);
  }
};
```

---

## 🧠 Dry Run
### Input
```
energy = [5, 2, -10, -5, 1], k = 3
```
### Steps
```
dp = [5, 2, -10, -5, 1]
i=1: dp[1] += dp[4] = 2+1 = 3
i=0: dp[0] += dp[3] = 5+(-5) = 0
dp = [0, 3, -10, -5, 1]
max(dp) = 3
```

---

## ⏱️ Time Complexity
```
O(n) — single pass through the array
```

## 💾 Space Complexity
```
O(n) — dp array (could be done in-place for O(1))
```

---

## ⚠️ Edge Cases
- All negative energies — must still pick the least negative path
- k equals array length — each starting point has only itself
- Single element array

---

## 🎯 Interview Takeaways
- Suffix DP is a natural fit for "jump forward by k" problems
- Processing right-to-left avoids the need for recursive calls
- The problem has k independent chains — process them all with one loop

---

## 📌 Key Pattern
👉 **"Suffix DP with fixed step size"**

---

## 🔁 Related Problems
- 198. House Robber
- 740. Delete and Earn
- 1696. Jump Game VI

---

## 🚀 Final Thoughts
This is a clean suffix DP problem. The array naturally decomposes into k independent subsequences (by starting index mod k), and the right-to-left accumulation handles all of them elegantly in a single pass.

---

✨ **Rule to remember:**
> For fixed-step jumping, suffix DP from right to left accumulates optimal paths in O(n).
