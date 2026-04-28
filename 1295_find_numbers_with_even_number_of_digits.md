# 1295. Find Numbers with Even Number of Digits

## 🔗 Problem Link
https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Math

---

## 🧩 Problem Summary

Given an array of integers `nums`, return how many of them contain an even number of digits.

### 📌 Constraints
- `1 <= nums.length <= 500`
- `1 <= nums[i] <= 10^5`

---

## 💭 Intuition

👉 Count the number of digits in each number using `log10(n) + 1`, then check if that count is even.

---

## ⚡ Approach — Log10 Digit Count

### 🧠 Idea
- For each number, compute the digit count using `floor(log10(n)) + 1`.
- If the digit count is even, increment the answer.

---

## 💻 Code

```cpp
class Solution {
    int numofdig(int n)
    {
       return log10(n)+1;
    }
public:
    int findNumbers(vector<int>& nums) {
        int ans=0;
        for(int i:nums)
        {
            if(numofdig(i)%2==0)
            ans++;
        }
        return ans;
    }
};
```

---

## 🧠 Dry Run

### Input
```
nums = [12, 345, 2, 6, 7896]
```

### Steps
```
12:   log10(12)+1 = 1.08+1 = 2 (even) → ans=1
345:  log10(345)+1 = 2.54+1 = 3 (odd)  → ans=1
2:    log10(2)+1 = 0.30+1 = 1 (odd)    → ans=1
6:    log10(6)+1 = 0.78+1 = 1 (odd)    → ans=1
7896: log10(7896)+1 = 3.90+1 = 4 (even) → ans=2

Output: 2
```

---

## ⏱️ Time Complexity
```
O(n)
```
Each number is processed in O(1) using log10.

---

## 💾 Space Complexity
```
O(1)
```
Only a counter variable is used.

---

## ⚠️ Edge Cases
- All single-digit numbers → all have 1 digit (odd), return 0.
- Numbers like 10, 100, 1000 → boundary cases for log10.
- `n = 0` is not in the constraints (1 <= nums[i]), so log10(0) is not an issue.

---

## 🎯 Interview Takeaways
- `log10(n) + 1` gives the digit count, but relies on floating-point which can have edge cases.
- Alternative: convert to string and check length, or repeatedly divide by 10.
- For the given constraints (1 to 10^5), log10 works reliably.
- Even-digit numbers in range: 10-99 (2 digits), 1000-9999 (4 digits), 100000 (6 digits).

---

## 📌 Key Pattern
👉 **"Digit counting — use log10(n)+1 or string conversion to determine the number of digits."**

---

## 🔁 Related Problems
- 1281 - Subtract the Product and Sum of Digits
- 2520 - Count the Digits That Divide a Number
- 258 - Add Digits

---

## 🚀 Final Thoughts
A straightforward warm-up problem. The log10 approach is concise but string conversion (`to_string(n).length()`) is arguably safer and more readable in interviews.

---

✨ **Rule to remember:**
> "Number of digits = floor(log10(n)) + 1, but watch out for floating-point edge cases."
