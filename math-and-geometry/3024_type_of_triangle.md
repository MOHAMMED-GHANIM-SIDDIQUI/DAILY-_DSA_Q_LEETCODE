# 3024. Type of Triangle

## 🔗 Problem Link
https://leetcode.com/problems/type-of-triangle/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Math, Sorting

---

## 🧩 Problem Summary
Given an array of 3 integers representing side lengths, determine if they form a valid triangle and classify it as "equilateral", "isosceles", "scalene", or "none" (not a valid triangle).

### 📌 Constraints
- nums.length == 3
- 1 <= nums[i] <= 100

---

## 💭 Intuition
👉 Sort the sides first. A valid triangle requires `a + b > c` (where c is the largest side). Then check: all equal = equilateral, two equal = isosceles, all different = scalene.

---

## ⚡ Approach — Sort and Classify

### 🧠 Idea
- Sort the array so `nums[0] <= nums[1] <= nums[2]`.
- Check triangle inequality: `nums[0] + nums[1] > nums[2]`. If not, return "none".
- If all three are equal: "equilateral".
- If any two are equal: "isosceles".
- Otherwise: "scalene".

---

## 💻 Code

```cpp
class Solution {
public:
    string triangleType(vector<int>& nums) {
        sort(nums.begin(), nums.end()); // Ensure correct order for comparison
        if (nums[0] + nums[1] <= nums[2])
            return "none"; // Not a valid triangle

        if (nums[0] == nums[1] && nums[1] == nums[2])
            return "equilateral";
        else if (nums[0] == nums[1] || nums[1] == nums[2] || nums[0] == nums[2])
            return "isosceles";
        else
            return "scalene";
    }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [3, 3, 3]
```
### Steps
```
After sort: [3, 3, 3]
Triangle check: 3 + 3 = 6 > 3 ✓
All equal: 3 == 3 == 3 → "equilateral"

Output: "equilateral"
```

---

## ⏱️ Time Complexity
```
O(1) — sorting 3 elements is constant time
```

## 💾 Space Complexity
```
O(1) — no extra space
```

---

## ⚠️ Edge Cases
- `[1, 1, 2]`: 1 + 1 = 2, not > 2 → "none".
- `[1, 2, 3]`: 1 + 2 = 3, not > 3 → "none".
- `[5, 5, 3]`: valid isosceles triangle.

---

## 🎯 Interview Takeaways
- Always sort sides before checking the triangle inequality — only need to verify `a + b > c` for the largest side.
- Check from most specific (equilateral) to least specific (scalene).
- The triangle inequality uses strict inequality (`>`), not `>=`.

---

## 📌 Key Pattern
👉 **"Sort + Triangle Inequality + Classification"**

---

## 🔁 Related Problems
- 976. Largest Perimeter Triangle
- 611. Valid Triangle Number
- 812. Largest Triangle Area

---

## 🚀 Final Thoughts
A basic geometry problem that tests understanding of the triangle inequality theorem. Sorting first simplifies the validity check to a single comparison. Classification is straightforward once validity is confirmed.

---

✨ **Rule to remember:**
> After sorting sides as a <= b <= c, a triangle is valid if and only if a + b > c.
