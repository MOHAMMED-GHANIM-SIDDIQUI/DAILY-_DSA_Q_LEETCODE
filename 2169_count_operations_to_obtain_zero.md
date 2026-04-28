# 2169. Count Operations to Obtain Zero

## 🔗 Problem Link
https://leetcode.com/problems/count-operations-to-obtain-zero/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Math, Simulation

---

## 🧩 Problem Summary
Given two non-negative integers `num1` and `num2`, repeatedly subtract the smaller from the larger (or either if equal) and count the operations until one becomes zero. Return the operation count.

### 📌 Constraints
- `0 <= num1, num2 <= 10^5`

---

## 💭 Intuition
👉 This is essentially a simulation of the subtraction-based GCD algorithm. Each step subtracts the smaller from the larger, counting operations along the way.

---

## ⚡ Approach — Direct Simulation

### 🧠 Idea
- While both numbers are non-zero, subtract the smaller from the larger and increment the counter.
- Return the counter when one reaches zero.

---

## 💻 Code

```cpp
class Solution {
public:
    int countOperations(int num1, int num2) {
        int ans=0;
        while(num1 && num2)
        {
            ans+=1;
            if(num1>num2)
            num1-=num2;
            else
            num2-=num1;
        }
        return ans;

    }
};
```

---

## 🧠 Dry Run
### Input
```
num1 = 10, num2 = 10
```
### Steps
```
Step 1: num1=10 > num2=10? No → num2 = 10-10 = 0, ans=1
num2 = 0, loop ends → return 1
```

---

## ⏱️ Time Complexity
```
O(max(num1, num2)) — worst case when one number is 1
```

## 💾 Space Complexity
```
O(1) — constant extra space
```

---

## ⚠️ Edge Cases
- One of the numbers is 0 initially → return 0 immediately
- Both numbers are equal → one operation
- One number is 1 → operations equal the other number

---

## 🎯 Interview Takeaways
- This mirrors the Euclidean algorithm using subtraction instead of modulo.
- Could be optimized with modulo to reduce to O(log(min)) steps, but simulation is fine for the constraints.
- Always check for zero inputs before entering the loop.

---

## 📌 Key Pattern
👉 **"Subtraction-based GCD simulation"**

---

## 🔁 Related Problems
- 1071. Greatest Common Divisor of Strings
- 2543. Check if Point Is Reachable
- 365. Water and Jug Problem

---

## 🚀 Final Thoughts
A simple simulation problem that mimics the subtraction variant of Euclid's algorithm. Understanding this helps build intuition for the modulo-based GCD approach.

---

✨ **Rule to remember:**
> "Repeated subtraction of the smaller from the larger is just the slow version of GCD — count the steps."
