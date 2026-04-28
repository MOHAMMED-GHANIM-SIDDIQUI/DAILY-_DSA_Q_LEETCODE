# 2210. Count Hills and Valleys in an Array

## 🔗 Problem Link
https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array

---

## 🧩 Problem Summary
Given an array `nums`, count the number of indices that are either a hill (strictly greater than both neighbors) or a valley (strictly less than both neighbors). Equal adjacent elements are treated as the same group — use the last distinct left neighbor for comparison.

### 📌 Constraints
- `3 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

---

## 💭 Intuition
👉 Track the last distinct left neighbor instead of `nums[i-1]` to correctly handle plateaus of equal values.

---

## ⚡ Approach — Single Pass with Left Tracking

### 🧠 Idea
- Keep a variable `left` initialized to `nums[0]`.
- For each index `i` (1 to n-2), check if it forms a hill or valley compared to `left` and `nums[i+1]`.
- Only update `left` when a hill or valley is found (skip equal neighbors).

---

## 💻 Code

```cpp
class Solution {
 public:
  int countHillValley(vector<int>& nums) {
    int ans = 0;
    int left = nums[0];

    for (int i = 1; i + 1 < nums.size(); ++i)
      if (left < nums[i] && nums[i] > nums[i + 1] ||  // the hill
          left > nums[i] && nums[i] < nums[i + 1]) {  // the valley
        ++ans;
        left = nums[i];
      }

    return ans;
  }
}
```

---

## 🧠 Dry Run
### Input
```
nums = [2, 4, 1, 1, 6, 5]
```
### Steps
```
left=2
i=1: left=2 < 4 && 4 > 1 → hill ✓, ans=1, left=4
i=2: left=4 > 1 && 1 < 1? No (1 not < 1)
i=3: left=4 > 1 && 1 < 6 → valley ✓, ans=2, left=1
i=4: left=1 < 6 && 6 > 5 → hill ✓, ans=3, left=6
Result: 3
```

---

## ⏱️ Time Complexity
```
O(n) — single pass through the array
```

## 💾 Space Complexity
```
O(1) — constant extra space
```

---

## ⚠️ Edge Cases
- All elements are the same → 0 hills/valleys
- Strictly increasing or decreasing → 0 hills/valleys
- Alternating up-down pattern → maximum hills/valleys

---

## 🎯 Interview Takeaways
- Handling plateaus (equal adjacent elements) requires tracking the last distinct neighbor.
- Updating `left` only on confirmed hills/valleys avoids false positives from flat regions.
- Simple single-pass with a state variable is elegant and efficient.

---

## 📌 Key Pattern
👉 **"Track last distinct left neighbor to handle plateaus in hill/valley detection"**

---

## 🔁 Related Problems
- 896. Monotonic Array
- 941. Valid Mountain Array
- 1095. Find in Mountain Array

---

## 🚀 Final Thoughts
The twist in this problem is handling consecutive equal elements. By tracking the last distinct left neighbor, we cleanly skip plateaus and only count true inflection points.

---

✨ **Rule to remember:**
> "For hill/valley detection with equal neighbors, track the last distinct left value — don't use the immediate predecessor."
