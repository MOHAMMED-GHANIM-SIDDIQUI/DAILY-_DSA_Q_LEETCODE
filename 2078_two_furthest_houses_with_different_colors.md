# 2078. Two Furthest Houses With Different Colors

## 🔗 Problem Link
https://leetcode.com/problems/two-furthest-houses-with-different-colors/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Greedy

---

## 🧩 Problem Summary
Given an array `colors` where `colors[i]` represents the color of the `i`-th house, find the maximum distance between two houses with different colors. The distance between houses `i` and `j` is `|i - j|`.

### 📌 Constraints
- `2 <= colors.length <= 100`
- `0 <= colors[i] <= 100`
- At least two houses have different colors.

---

## 💭 Intuition
👉 The maximum distance must involve either the first house or the last house (or both). So we only need to check each house against the first and last house to find the furthest one with a different color.

---

## ⚡ Approach — Greedy Two-Endpoint Check

### 🧠 Idea
- For each house `i`, if its color differs from `colors[0]`, the distance is `i` (from index 0).
- If its color differs from `colors[n-1]`, the distance is `n - 1 - i` (from the last index).
- Track the maximum of all such distances.

---

## 💻 Code

```python
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        maxi = 0

        for i in range(n):
            if colors[i] != colors[0]:
                maxi = max(maxi, i)
            if colors[i] != colors[n - 1]:
                maxi = max(maxi, n - 1 - i)

        return maxi
```

---

## 🧠 Dry Run
### Input
```
colors = [1, 1, 1, 6, 1, 1, 1]
```
### Steps
```
n = 7
i=0: colors[0]==colors[0] skip; colors[0]!=colors[6]? 1!=1 no
i=1: same checks, no update
i=2: same checks, no update
i=3: colors[3]!=colors[0]? 6!=1 yes → maxi=max(0,3)=3
      colors[3]!=colors[6]? 6!=1 yes → maxi=max(3,3)=3
i=4: colors[4]!=colors[0]? no; colors[4]!=colors[6]? no
i=5: same, no update
i=6: same, no update

Result: 3
```

---

## ⏱️ Time Complexity
```
O(n) — single pass through the array.
```

## 💾 Space Complexity
```
O(1) — only a few variables used.
```

---

## ⚠️ Edge Cases
- Only two houses with different colors: returns 1.
- All houses same color except one at the boundary: returns n-1.
- First and last house have different colors: returns n-1 immediately.

---

## 🎯 Interview Takeaways
- The maximum distance in a linear array always involves an endpoint.
- Greedy reasoning can reduce an O(n^2) brute force to O(n).
- Simple observation-based optimizations are valuable in interviews.

---

## 📌 Key Pattern
👉 **"Maximum distance in a line always anchors at one of the two endpoints."**

---

## 🔁 Related Problems
- 2016. Maximum Difference Between Increasing Elements
- 121. Best Time to Buy and Sell Stock
- 2078. Two Furthest Houses With Different Colors

---

## 🚀 Final Thoughts
A clean greedy approach that leverages the observation that the optimal answer must include either the first or last element. This avoids the need for nested loops entirely.

---

✨ **Rule to remember:**
> "For max distance, always check from the endpoints first."
