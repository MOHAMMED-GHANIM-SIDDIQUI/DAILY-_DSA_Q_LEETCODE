# 2843. Count Symmetric Integers

## 🔗 Problem Link
https://leetcode.com/problems/count-symmetric-integers/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Math, Enumeration

---

## 🧩 Problem Summary
An integer is symmetric if it has an even number of digits and the sum of the first half of digits equals the sum of the second half. Given `low` and `high`, count how many symmetric integers are in the range `[low, high]`.

### 📌 Constraints
- `1 <= low <= high <= 10^4`

---

## 💭 Intuition
👉 Since the range is small (up to 10^4), we can check every number individually. For each number with an even digit count, compare the digit sum of the first half with the second half.

---

## ⚡ Approach — Brute Force Enumeration

### 🧠 Idea
- Iterate from `low` to `high`.
- For each number, convert to string. If odd number of digits, skip.
- Compute sum of first half and second half of digits.
- If they are equal, increment the count.

---

## 💻 Code

```cpp
class Solution {
    bool isSymmetric(int num) {
        string s = to_string(num);
        int n = s.size();
        if (n % 2 != 0) return false;

        int half = n / 2;
        int sum1 = 0, sum2 = 0;
        for (int i = 0; i < half; i++) {
            sum1 += s[i] - '0';
        }
        for (int i = half; i < n; i++) {
            sum2 += s[i] - '0';
        }

        return sum1 == sum2;
    }

public:
    int countSymmetricIntegers(int low, int high) {
        int count = 0;
        for (int i = low; i <= high; i++) {
            if (isSymmetric(i)) {
                count++;
            }
        }
        return count;
    }
};
```

---

## 🧠 Dry Run
### Input
```
low = 1, high = 100
```
### Steps
```
1-digit numbers (1-9): odd digit count, skip all
2-digit numbers (10-99):
  11: sum1=1, sum2=1 ✓
  22: sum1=2, sum2=2 ✓
  33: sum1=3, sum2=3 ✓
  ...
  99: sum1=9, sum2=9 ✓
  Also: 10 (1 vs 0), 12 (1 vs 2), etc. — not symmetric
3-digit number 100: odd digit count, skip

Symmetric 2-digit numbers: 11,22,33,44,55,66,77,88,99 = 9
Answer: 9
```

---

## ⏱️ Time Complexity
```
O((high - low) * d) where d is the number of digits (at most 5)
```

## 💾 Space Complexity
```
O(d) for the string conversion
```

---

## ⚠️ Edge Cases
- Numbers with odd digit count (1, 3, 5 digits) are never symmetric
- Single digit range like `[5, 5]` — answer is 0
- `low == high` and the number is symmetric

---

## 🎯 Interview Takeaways
- When constraints are small, brute force is perfectly acceptable.
- Converting to string makes digit manipulation straightforward.

---

## 📌 Key Pattern
👉 **"Brute force enumeration with digit-sum comparison"**

---

## 🔁 Related Problems
- 1837. Sum of Digits in Base K
- 258. Add Digits
- 2520. Count the Digits That Divide a Number

---

## 🚀 Final Thoughts
A simple enumeration problem well-suited for the small constraint range. The string conversion approach is clean and avoids error-prone digit extraction via division and modulo.

---

✨ **Rule to remember:**
> For small ranges, brute force enumeration with a clear helper function is often the cleanest approach.
