# 1432. Max Difference You Can Get from Changing an Integer

## 🔗 Problem Link
https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Math, Greedy, String

---

## 🧩 Problem Summary
Given an integer `num`, you may pick a digit `x` and replace all occurrences of `x` with another digit `y` (you do this twice independently to create two numbers `a` and `b`). Return the maximum difference `a - b`.

### 📌 Constraints
- `1 <= num <= 10^8`

---

## 💭 Intuition
👉 To maximize `a`, replace the first non-9 digit (and all its occurrences) with 9. To minimize `b`, replace the first digit that isn't 0 or 1 — if it's the leading digit, replace with 1 (to avoid leading zeros); otherwise replace with 0.

---

## ⚡ Approach — Greedy Digit Replacement

### 🧠 Idea
- For maximum `a`: find the first digit that isn't `9`, replace all its occurrences with `9`.
- For minimum `b`: find the first digit that isn't `0` or `1`. If it's the leading digit, replace with `1`; otherwise replace with `0`.
- Return `a - b`.

---

## 💻 Code

```cpp
class Solution {
 public:
  int maxDiff(int num) {
    const string s = to_string(num);
    int firstNot9 = s.find_first_not_of('9');
    int firstNot01 = s.find_first_not_of("01");
    if (firstNot9 == string::npos)
      firstNot9 = 0;
    if (firstNot01 == string::npos)
      firstNot01 = 0;

    string a = s;
    string b = s;
    replace(a.begin(), a.end(), s[firstNot9], '9');
    replace(b.begin(), b.end(), s[firstNot01], firstNot01 == 0 ? '1' : '0');
    return stoi(a) - stoi(b);
  }
};
```

---

## 🧠 Dry Run
### Input
```
num = 555
```
### Steps
```
s = "555"
firstNot9 = 0 (digit '5' at index 0)
firstNot01 = 0 (digit '5' at index 0)

a: replace '5' with '9' → "999" → 999
b: firstNot01 == 0 (leading digit) → replace '5' with '1' → "111" → 111
Result = 999 - 111 = 888
```

---

## ⏱️ Time Complexity
```
O(d) where d is the number of digits (at most 9)
```

## 💾 Space Complexity
```
O(d) for string copies
```

---

## ⚠️ Edge Cases
- `num = 9` → a=9, b=1 → diff=8
- `num = 111` → already all 1s → firstNot01 = npos → b stays 111, a = 999, diff = 888
- `num = 10000` → careful with leading digit replacement

---

## 🎯 Interview Takeaways
- Greedy: maximize one number by replacing with 9, minimize the other smartly.
- Leading digit must be replaced with 1 (not 0) to avoid leading zeros.
- `find_first_not_of` is a handy string utility in C++.

---

## 📌 Key Pattern
👉 **"Greedy digit replacement — maximize by replacing with 9, minimize by replacing with 0 or 1."**

---

## 🔁 Related Problems
- 1323. Maximum 69 Number
- 670. Maximum Swap
- 2566. Maximum Difference by Remapping a Digit

---

## 🚀 Final Thoughts
A greedy string manipulation problem. The tricky part is handling the minimization correctly — the leading digit must become 1, not 0, while other digits can become 0.

---

✨ **Rule to remember:**
> To maximize difference: make one number as large as possible (→9) and the other as small as possible (→0 or 1).
