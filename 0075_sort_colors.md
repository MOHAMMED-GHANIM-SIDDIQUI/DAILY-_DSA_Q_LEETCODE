# 75. Sort Colors

## 🔗 Problem Link
https://leetcode.com/problems/sort-colors/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Two Pointers, Sorting

---

## 🧩 Problem Summary
Given an array with n objects colored red (0), white (1), or blue (2), sort them in-place so that objects of the same color are adjacent, in the order red, white, and blue. Do not use the library sort function.

### 📌 Constraints
- `n == nums.length`
- `1 <= n <= 300`
- `nums[i]` is `0`, `1`, or `2`

---

## 💭 Intuition
👉 Maintain three boundary pointers for 0s, 1s, and 2s. As we scan, we overwrite positions from the back, pushing each value type into its correct region.

---

## ⚡ Approach — Boundary Pointers (Overwrite)

### 🧠 Idea
- Maintain three pointers (`zero`, `one`, `two`) all starting at -1, representing the end of each color's region.
- For each number:
  - If 0: extend all three regions — write 2, then 1, then 0.
  - If 1: extend `two` and `one` regions — write 2, then 1.
  - If 2: extend only `two` region — write 2.
- This cascading overwrite ensures correct ordering.

---

## 💻 Code

```cpp
class Solution {
 public:
  void sortColors(vector<int>& nums) {
    int zero = -1;
    int one = -1;
    int two = -1;

    for (const int num : nums)
      if (num == 0) {
        nums[++two] = 2;
        nums[++one] = 1;
        nums[++zero] = 0;
      } else if (num == 1) {
        nums[++two] = 2;
        nums[++one] = 1;
      } else {
        nums[++two] = 2;
      }
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [2, 0, 2, 1, 1, 0]
```
### Steps
```
num=2: two=0 -> [2,0,2,1,1,0]
num=0: two=1,one=0,zero=0 -> [0,2,2,1,1,0] -> write 2@1, 1@0, 0@0 => [0,2,2,1,1,0]
num=2: two=2 -> [0,2,2,1,1,0]
num=1: two=3,one=1 -> [0,1,2,2,1,0]
num=1: two=4,one=2 -> [0,1,1,2,2,0]
num=0: two=5,one=3,zero=1 -> [0,0,1,1,2,2]
Result: [0,0,1,1,2,2]
```

---

## ⏱️ Time Complexity
```
O(n) — single pass through the array
```

## 💾 Space Complexity
```
O(1) — in-place with only three integer variables
```

---

## ⚠️ Edge Cases
- All same color — e.g., [0,0,0] or [2,2,2].
- Already sorted array.
- Single element array.
- Only two colors present.

---

## 🎯 Interview Takeaways
- This is an alternative to the classic Dutch National Flag algorithm.
- The cascading overwrite technique is elegant and avoids explicit swaps.
- Understanding that writing from the back of each region maintains invariants is key.

---

## 📌 Key Pattern
👉 **"Cascading overwrite with boundary pointers for fixed-category sorting"**

---

## 🔁 Related Problems
- 148. Sort List
- 280. Wiggle Sort
- 324. Wiggle Sort II

---

## 🚀 Final Thoughts
This approach offers a unique perspective on the Dutch National Flag problem. Instead of swapping elements, it overwrites from back to front within each color region, which is both clean and efficient.

---

✨ **Rule to remember:**
> "Three boundaries, one pass — push each color into place by cascading writes."
