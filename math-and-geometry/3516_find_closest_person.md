# 3516. Find Closest Person

## 🔗 Problem Link
https://leetcode.com/problems/find-closest-person/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Math, Absolute Difference

---

## 🧩 Problem Summary
Given three integers x, y, and z on a number line, determine which of x or y is closer to z. Return 1 if x is closer, 2 if y is closer, or 0 if equidistant.

### 📌 Constraints
- `1 <= x, y, z <= 100`

---

## 💭 Intuition
👉 Simply compare the absolute distances `|z - x|` and `|z - y|` and return the result accordingly.

---

## ⚡ Approach — Direct Comparison

### 🧠 Idea
- Compute `|z - x|` and `|z - y|`.
- If `|z - x| < |z - y|`, return 1 (x is closer).
- If `|z - x| > |z - y|`, return 2 (y is closer).
- Otherwise, return 0 (tie).

---

## 💻 Code

```cpp
class Solution {
public:
    int findClosest(int x, int y, int z) {
        if(abs(z-x)>abs(z-y))
        return 2;
        else if(abs(z-x)<abs(z-y))
        return 1;
        return 0;
    }
};
```

---

## 🧠 Dry Run
### Input
```
x = 2, y = 7, z = 4
```
### Steps
```
|z - x| = |4 - 2| = 2
|z - y| = |4 - 7| = 3
2 < 3 → return 1 (x is closer)
```

---

## ⏱️ Time Complexity
```
O(1) — constant time comparison
```

## 💾 Space Complexity
```
O(1) — no extra space
```

---

## ⚠️ Edge Cases
- x == y → always return 0
- z == x → return 1 (distance 0)
- z == y → return 2 (distance 0)
- x == y == z → return 0

---

## 🎯 Interview Takeaways
- Simple problems still require careful handling of tie conditions.
- Use `abs()` for distance on a number line.
- Read the return value specification carefully (1, 2, or 0).

---

## 📌 Key Pattern
👉 **"Compare absolute distances to determine closest point."**

---

## 🔁 Related Problems
- 2399. Check Distances Between Same Letters
- 1. Two Sum (distance-based thinking)

---

## 🚀 Final Thoughts
A straightforward comparison problem. The main pitfall is getting the return values correct — 1 for x closer, 2 for y closer, 0 for tie.

---

✨ **Rule to remember:**
> When comparing distances on a number line, use absolute differences and handle the equality case explicitly.
