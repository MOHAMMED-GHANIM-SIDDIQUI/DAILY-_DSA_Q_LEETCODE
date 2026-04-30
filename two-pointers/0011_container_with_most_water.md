# 11. Container With Most Water

## 🔗 Problem Link
https://leetcode.com/problems/container-with-most-water/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Two Pointers, Greedy

---

## 🧩 Problem Summary

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the i-th line are `(i, 0)` and `(i, height[i])`. Find two lines that together with the x-axis form a container that holds the most water. Return the maximum amount of water a container can store.

### 📌 Constraints
- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

---

## 💭 Intuition

👉 The brute force would check every pair of lines, but that's O(n²). The key insight is that we can use two pointers starting at the widest container and greedily shrink inward. We always move the pointer pointing to the shorter line, because moving the taller one can never increase the area (the height is limited by the shorter line, and the width is decreasing).

---

## ⚡ Approach — Two Pointers (Greedy)

### 🧠 Idea

- Start with two pointers at the leftmost and rightmost lines (maximum width).
- Calculate the area formed by the two lines: `min(height[l], height[r]) * (r - l)`.
- Move the pointer pointing to the shorter line inward, because keeping it won't help — the area is bounded by the shorter height.
- Continue until the two pointers meet.

---

## 💻 Code

```cpp
class Solution {
 public:
  int maxArea(vector<int>& height) {
    int ans = 0;
    int l = 0;
    int r = height.size() - 1;

    while (l < r) {
      const int minHeight = min(height[l], height[r]);
      ans = max(ans, minHeight * (r - l));
      if (height[l] < height[r])
        ++l;
      else
        --r;
    }

    return ans;
  }
};
```

---

## 🧠 Dry Run

### Input
```
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
```

### Steps
```
l=0, r=8 → min(1,7)=1, area=1*8=8,  ans=8,  height[0]<height[8] → l++
l=1, r=8 → min(8,7)=7, area=7*7=49, ans=49, height[1]>height[8] → r--
l=1, r=7 → min(8,3)=3, area=3*6=18, ans=49, height[1]>height[7] → r--
l=1, r=6 → min(8,8)=8, area=8*5=40, ans=49, height[1]==height[6] → r--
l=1, r=5 → min(8,4)=4, area=4*4=16, ans=49, height[1]>height[5] → r--
l=1, r=4 → min(8,5)=5, area=5*3=15, ans=49, height[1]>height[4] → r--
l=1, r=3 → min(8,2)=2, area=2*2=4,  ans=49, height[1]>height[3] → r--
l=1, r=2 → min(8,6)=6, area=6*1=6,  ans=49, height[1]>height[2] → r--
l=1, r=1 → loop ends
Return 49
```

---

## ⏱️ Time Complexity

```
O(n)
```

Each pointer moves at most n times total, so the loop runs at most n iterations.

---

## 💾 Space Complexity

```
O(1)
```

Only a constant number of variables are used.

---

## ⚠️ Edge Cases

- **Two elements:** `height = [1, 1]` → area = `1 * 1 = 1`
- **Decreasing heights:** `height = [5, 4, 3, 2, 1]` → best is `min(5,1)*4 = 4` vs `min(5,2)*3 = 6` → answer = 6
- **All same height:** `height = [3, 3, 3, 3]` → area = `3 * 3 = 9`

---

## 🎯 Interview Takeaways

- Two-pointer technique is ideal when you need to search pairs in a sorted or bounded structure.
- Greedy reasoning: always discard the less promising side.
- This problem demonstrates that O(n) can replace O(n²) brute force with the right insight.
- Always consider starting from the extremes and narrowing inward.

---

## 📌 Key Pattern

👉 **"Two pointers from both ends, greedily move the shorter side inward."**

---

## 🔁 Related Problems

- 42. Trapping Rain Water
- 15. 3Sum
- 16. 3Sum Closest
- 167. Two Sum II – Input Array Is Sorted

---

## 🚀 Final Thoughts

Container With Most Water is a classic two-pointer problem. The greedy reasoning behind moving the shorter pointer is the core insight that transforms an O(n²) brute force into an elegant O(n) solution.

---

✨ **Rule to remember:**
> "When bounded by two sides, always move the weaker side — you have nothing to lose and everything to gain."
