# 2197. Replace Non-Coprime Numbers in Array

## 🔗 Problem Link
https://leetcode.com/problems/replace-non-coprime-numbers-in-array/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Math, Stack, Number Theory

---

## 🧩 Problem Summary
Given an array of integers, repeatedly replace adjacent non-coprime numbers (GCD > 1) with their LCM until no adjacent pair is non-coprime. Return the final array.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`

---

## 💭 Intuition
👉 Use a stack-like approach: push each number onto the result, and while the top of the stack and the current number are not coprime, merge them into their LCM.

---

## ⚡ Approach — Stack with GCD/LCM Merging

### 🧠 Idea
- Iterate through the array, treating the result as a stack.
- For each new number, check if it shares a common factor with the stack's top.
- If GCD > 1, replace both with their LCM and continue checking backwards.
- Push the final merged value onto the stack.

---

## 💻 Code

```cpp
class Solution {
public:
    vector<int> replaceNonCoprimes(vector<int>& nums) {
        vector<int> ans;

        for (int num : nums) {
            // Merge with previous numbers while they are not coprime
            while (!ans.empty() && gcd(ans.back(), num) > 1) {
                num = lcm(ans.back(), num);
                ans.pop_back();
            }
            ans.push_back(num);
        }

        return ans;
    }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [6, 4, 3, 2, 7, 6, 2]
```
### Steps
```
Push 6 → [6]
Push 4: gcd(6,4)=2 → lcm=12, pop 6 → []; push 12 → [12]
Push 3: gcd(12,3)=3 → lcm=12, pop 12 → []; push 12 → [12]
Push 2: gcd(12,2)=2 → lcm=12, pop 12 → []; push 12 → [12]
Push 7: gcd(12,7)=1 → push 7 → [12, 7]
Push 6: gcd(7,6)=1 → push 6 → [12, 7, 6]
Push 2: gcd(6,2)=2 → lcm=6, pop 6 → [12, 7]; gcd(7,6)=1 → push 6 → [12, 7, 6]
Result: [12, 7, 6]
```

---

## ⏱️ Time Complexity
```
O(n log M) — each element is pushed/popped at most once; GCD is O(log M) where M is max value
```

## 💾 Space Complexity
```
O(n) — for the result stack
```

---

## ⚠️ Edge Cases
- All elements are coprime → no merges, return original array
- All elements share a common factor → entire array reduces to one LCM
- Single element → return as-is

---

## 🎯 Interview Takeaways
- Stack-based merging is ideal when adjacent elements can combine and the merge can cascade backwards.
- GCD and LCM are fundamental number theory tools; `lcm(a,b) = a * b / gcd(a,b)`.
- Each element is pushed and popped at most once, ensuring amortized linear time.

---

## 📌 Key Pattern
👉 **"Stack-based greedy merging of adjacent elements using GCD/LCM"**

---

## 🔁 Related Problems
- 735. Asteroid Collision
- 1209. Remove All Adjacent Duplicates in String II
- 2001. Number of Pairs of Interchangeable Rectangles

---

## 🚀 Final Thoughts
An elegant stack problem disguised as number theory. The key insight is that merging is greedy and order-independent for adjacent non-coprime pairs, so a single left-to-right pass with backward merging suffices.

---

✨ **Rule to remember:**
> "Use a stack to greedily merge adjacent non-coprime numbers into their LCM — each element enters and leaves at most once."
