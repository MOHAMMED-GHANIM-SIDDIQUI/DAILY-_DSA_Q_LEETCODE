# 2044. Count Number of Maximum Bitwise-OR Subsets

## 🔗 Problem Link
https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Backtracking, Bit Manipulation, Enumeration

---

## 🧩 Problem Summary
Given an integer array `nums`, find the maximum possible bitwise OR of a subset of `nums` and return the number of different non-empty subsets with this maximum OR value.

### 📌 Constraints
- `1 <= nums.length <= 16`
- `1 <= nums[i] <= 10^5`

---

## 💭 Intuition
👉 The maximum OR is simply the OR of all elements. With n <= 16, we can enumerate all 2^n subsets via DFS/backtracking and count those whose OR equals the maximum.

---

## ⚡ Approach — DFS/Backtracking over All Subsets

### 🧠 Idea
- Compute the overall OR of all elements.
- Use DFS to enumerate all subsets: at each index, either include or exclude the element.
- At the end of each branch, check if the accumulated OR equals the maximum OR.
- Count matching subsets.

---

## 💻 Code

```cpp
class Solution {
 public:
  int countMaxOrSubsets(vector<int>& nums) {
    const int ors = accumulate(nums.begin(), nums.end(), 0, bit_or<>());
    int ans = 0;
    dfs(nums, 0, 0, ors, ans);
    return ans;
  }

 private:
  void dfs(const vector<int>& nums, int i, int path, const int& ors, int& ans) {
    if (i == nums.size()) {
      if (path == ors)
        ++ans;
      return;
    }

    dfs(nums, i + 1, path, ors, ans);
    dfs(nums, i + 1, path | nums[i], ors, ans);
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [3, 1]
```
### Steps
```
ors = 3 | 1 = 3
DFS tree:
  i=0, path=0
    exclude 3: i=1, path=0
      exclude 1: path=0 != 3
      include 1: path=1 != 3
    include 3: i=1, path=3
      exclude 1: path=3 == 3 -> ans++  (ans=1)
      include 1: path=3|1=3 == 3 -> ans++  (ans=2)
Return 2
```

---

## ⏱️ Time Complexity
```
O(2^n), where n is the length of nums
```

## 💾 Space Complexity
```
O(n) for the recursion stack
```

---

## ⚠️ Edge Cases
- Single element: always 1 subset (the element itself)
- All elements the same: 2^n - 1 subsets (all non-empty subsets)
- n = 16: 2^16 = 65536 subsets, still feasible

---

## 🎯 Interview Takeaways
- The maximum OR is always the OR of all elements (OR is monotonically non-decreasing).
- With n <= 16, brute-force enumeration of all subsets is perfectly fine.
- DFS with include/exclude branching is the standard subset enumeration pattern.

---

## 📌 Key Pattern
👉 **"Enumerate all subsets via DFS when n is small (n <= 20)"**

---

## 🔁 Related Problems
- 78. Subsets
- 1178. Number of Valid Words for Each Puzzle
- 2275. Largest Combination With Bitwise AND Greater Than Zero

---

## 🚀 Final Thoughts
This problem is a textbook application of subset enumeration with bitwise operations. The constraint n <= 16 is the clear signal that brute-force over all 2^n subsets is intended.

---

✨ **Rule to remember:**
> When n <= 20, enumerate all subsets; the max OR is always the OR of the entire array.
