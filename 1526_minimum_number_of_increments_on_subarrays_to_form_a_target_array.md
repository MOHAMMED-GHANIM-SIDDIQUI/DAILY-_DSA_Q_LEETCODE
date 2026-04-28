# 1526. Minimum Number of Increments on Subarrays to Form a Target Array

## 🔗 Problem Link
https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Dynamic Programming, Stack, Greedy

---

## 🧩 Problem Summary
Given an integer array `target`, starting from an array of all zeros of the same length, in each operation you can choose a subarray and increment each element by 1. Return the minimum number of operations needed to form `target` from the initial array.

### 📌 Constraints
- `1 <= target.length <= 10^5`
- `1 <= target[i] <= 10^5`

---

## 💭 Intuition
👉 Each time the target value increases compared to the previous element, we need additional operations to "raise" the subarray to that height. The total number of operations equals the first element plus the sum of all positive differences between consecutive elements.

---

## ⚡ Approach — Greedy (Count Positive Increments)

### 🧠 Idea
- Start with `ans = target[0]` (we need that many operations to build the first element from 0).
- For each subsequent element, if `target[i] > target[i-1]`, we need `target[i] - target[i-1]` additional operations.
- If `target[i] <= target[i-1]`, the existing operations from previous subarrays can cover it (they just extend shorter).

---

## 💻 Code

```cpp
class Solution {
 public:
  int minNumberOperations(vector<int>& target) {
    int ans = target.front();

    for (int i = 1; i < target.size(); ++i)
      if (target[i] > target[i - 1])
        ans += target[i] - target[i - 1];

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
target = [1, 2, 3, 2, 1]
```
### Steps
```
ans = target[0] = 1
i=1: target[1]=2 > target[0]=1 → ans += 2-1 = 1, ans=2
i=2: target[2]=3 > target[1]=2 → ans += 3-2 = 1, ans=3
i=3: target[3]=2 < target[2]=3 → no change
i=4: target[4]=1 < target[3]=2 → no change
Answer: 3
(Operations: [1,1,1,1,1], [0,1,1,1,0], [0,0,1,0,0])
```

---

## ⏱️ Time Complexity
```
O(n), single pass through the array
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- Single element — answer is `target[0]`.
- Strictly increasing array — answer is `target[n-1]` (the maximum).
- Strictly decreasing array — answer is `target[0]`.
- All elements equal — answer is `target[0]`.

---

## 🎯 Interview Takeaways
- This problem looks complex but has an elegant O(n) greedy solution.
- Think of it like painting horizontal stripes: each new "rise" requires a new stripe.
- This is equivalent to counting the "staircase" pattern from the left.

---

## 📌 Key Pattern
👉 **"Count only the positive increments between consecutive elements — decreases are free"**

---

## 🔁 Related Problems
- 42 — Trapping Rain Water
- 84 — Largest Rectangle in Histogram
- 135 — Candy

---

## 🚀 Final Thoughts
This problem has a beautifully simple solution once you realize that each operation covers a contiguous subarray. When the target drops, existing operations naturally end. When it rises, new operations must begin. The answer is simply the sum of all upward steps.

---

✨ **Rule to remember:**
> "Minimum subarray increments = first element + sum of all positive consecutive differences."
