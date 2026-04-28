# 3347. Maximum Frequency of an Element After Performing Operations II

## 🔗 Problem Link
https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Hash Table, Sorting, Line Sweep, Ordered Set

---

## 🧩 Problem Summary
Given an array `nums`, an integer `k`, and `numOperations`, you can add any value in `[-k, k]` to at most `numOperations` elements. Find the maximum possible frequency of any single value after performing the operations.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i], k <= 10^9`
- `0 <= numOperations <= nums.length`

---

## 💭 Intuition
👉 Use a line sweep approach: for each number `num`, it can contribute to any target in `[num - k, num + k]`. Build a sweep line of these intervals, then at each candidate point, compute how many elements can be adjusted to match it.

---

## ⚡ Approach — Line Sweep with Candidate Points

### 🧠 Idea
- For each `num`, create interval `[num - k, num + k + 1)` in a sweep line.
- Collect candidate points: each `num`, `num - k`, and `num + k + 1`.
- Sweep through candidates, tracking how many elements are "adjustable" to that target.
- At each candidate, the answer is `count[candidate] + min(numOperations, adjustable - count[candidate])`.

---

## 💻 Code

```cpp
class Solution {
 public:
  // Same as 3346. Maximum Frequency of an Element After Performing Operations I
  int maxFrequency(vector<int>& nums, int k, int numOperations) {
    int ans = 1;
    int adjustable = 0;
    unordered_map<int, int> count;
    map<int, int> line;
    set<int> candidates;

    for (const int num : nums) {
      ++count[num];
      ++line[num - k];
      --line[num + k + 1];
      candidates.insert(num);
      candidates.insert(num - k);
      candidates.insert(num + k + 1);
    }

    for (const int num : candidates) {
      adjustable += line.contains(num) ? line[num] : 0;
      const int countNum = count.contains(num) ? count[num] : 0;
      const int adjusted = adjustable - countNum;
      ans = max(ans, countNum + min(numOperations, adjusted));
    }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [1, 4, 5], k = 1, numOperations = 2
```
### Steps
```
Intervals: 1→[0,2], 4→[3,5], 5→[4,6]
line: {0:+1, 2:-1, 3:+1, 4:+1, 5:-1, 6:-1}  (using num+k+1 for end)
candidates: {0, 1, 2, 3, 4, 5, 6}
Sweep:
  0: adjustable=1, count=0, ans=max(1, 0+min(2,1))=1
  1: adjustable=1, count=1, adjusted=0, ans=max(1, 1+min(2,0))=1
  2: adjustable=0, count=0 → ans=1
  3: adjustable=1, count=0 → ans=max(1, min(2,1))=1
  4: adjustable=2, count=1, adjusted=1, ans=max(1, 1+min(2,1))=2
  5: adjustable=2, count=1, adjusted=1, ans=max(2, 1+min(2,1))=2
  6: adjustable=1 → ...
Result: 2
```

---

## ⏱️ Time Complexity
```
O(n log n) — sorting candidates and sweep line operations
```

## 💾 Space Complexity
```
O(n) — for maps and sets
```

---

## ⚠️ Edge Cases
- `numOperations = 0` → answer is the max frequency in original array
- `k = 0` → same as numOperations = 0
- All elements the same → answer is `nums.length`
- `numOperations >= nums.length` → all can be adjusted

---

## 🎯 Interview Takeaways
- Line sweep converts range problems into point events for efficient processing.
- Separating "already at target" from "adjustable to target" simplifies the counting.

---

## 📌 Key Pattern
👉 **"Line sweep over adjustment intervals to find optimal target frequency"**

---

## 🔁 Related Problems
- 3346. Maximum Frequency of an Element After Performing Operations I
- 1838. Frequency of the Most Frequent Element
- 2271. Maximum White Tiles Covered by a Carpet

---

## 🚀 Final Thoughts
An elegant line sweep approach that avoids brute-force checking of all possible target values. The key insight is that only boundary points of intervals matter as candidates.

---

✨ **Rule to remember:**
> "When elements can adjust within a range, sweep through interval boundaries to find the best target."
