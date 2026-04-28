# 611. Valid Triangle Number

## 🔗 Problem Link
https://leetcode.com/problems/valid-triangle-number/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Two Pointers, Binary Search, Greedy, Sorting

---

## 🧩 Problem Summary
Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths. Three sides form a valid triangle if the sum of any two sides is greater than the third.

### 📌 Constraints
- `1 <= nums.length <= 1000`
- `0 <= nums[i] <= 1000`

---

## 💭 Intuition
👉 After sorting, for a fixed largest side nums[k], we only need to check if nums[i] + nums[j] > nums[k]. Using two pointers from both ends of the subarray before k, we can count valid pairs efficiently.

---

## ⚡ Approach — Sort + Two Pointers

### 🧠 Idea
- Sort the array in ascending order.
- Fix the largest side as nums[k] (iterate k from end to start).
- Use two pointers i (left) and j (right, just before k).
- If nums[i] + nums[j] > nums[k], all elements from i to j-1 paired with j also work (count j - i pairs), then decrement j.
- Otherwise, increment i.

---

## 💻 Code

```cpp
class Solution {
 public:
  int triangleNumber(vector<int>& nums) {
    if (nums.size() < 3)
      return 0;

    int ans = 0;

    ranges::sort(nums);

    for (int k = nums.size() - 1; k > 1; --k) {
      int i = 0;
      int j = k - 1;
      while (i < j)
        if (nums[i] + nums[j] > nums[k]) {
          // (nums[i], nums[j], nums[k])
          // (nums[i + 1], nums[j], nums[k])
          // ...
          // (nums[j - 1], nums[j], nums[k])
          ans += j - i;
          --j;
        } else {
          ++i;
        }
    }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [2, 2, 3, 4]
```
### Steps
```
After sort: [2, 2, 3, 4]
k=3 (nums[k]=4): i=0, j=2
  nums[0]+nums[2]=5 > 4 -> ans += 2-0 = 2, j=1
  i=0, j=1: nums[0]+nums[1]=4 > 4? No -> i=1
  i=1, j=1: i not < j, stop
k=2 (nums[k]=3): i=0, j=1
  nums[0]+nums[1]=4 > 3 -> ans += 1-0 = 1, j=0
  i=0, j=0: stop
Result: ans = 3
```

---

## ⏱️ Time Complexity
```
O(n^2) — outer loop O(n), inner two-pointer O(n) each
```

## 💾 Space Complexity
```
O(log n) — sorting space (in-place sort)
```

---

## ⚠️ Edge Cases
- Array with fewer than 3 elements — return 0.
- Array with zeros — zeros can't form valid triangles.
- All elements equal — every triplet is valid if elements > 0.
- Array with duplicates — handled naturally by the algorithm.

---

## 🎯 Interview Takeaways
- Sorting + two pointers is a powerful combination for triplet problems.
- Fixing the largest element and scanning smaller ones simplifies the triangle inequality.
- The key insight is that if nums[i] + nums[j] > nums[k], all elements between i and j also work with j.

---

## 📌 Key Pattern
👉 **"Sort + fix largest side + two pointers to count valid triangle pairs"**

---

## 🔁 Related Problems
- 15. 3Sum
- 16. 3Sum Closest
- 259. 3Sum Smaller

---

## 🚀 Final Thoughts
This problem is a great example of the sort-and-two-pointer paradigm applied to counting valid triplets. The batch counting (`ans += j - i`) is what makes it O(n^2) instead of O(n^3).

---

✨ **Rule to remember:**
> "Fix the largest side, two-pointer the rest — if the smallest pair works, everything in between does too."
