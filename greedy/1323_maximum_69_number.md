# 1323. Maximum 69 Number

## 🔗 Problem Link
https://leetcode.com/problems/maximum-69-number/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Math, Greedy, String

---

## 🧩 Problem Summary
Given a positive integer consisting only of digits `6` and `9`, return the maximum number you can get by changing at most one digit (`6` becomes `9` or `9` becomes `6`).

### 📌 Constraints
- `1 <= num <= 10^4`
- `num` consists of only the digits `6` and `9`.

---

## 💭 Intuition
👉 To maximize the number, change the leftmost `6` to `9`. Since higher-order digits contribute more value, flipping the first `6` gives the largest possible increase.

---

## ⚡ Approach — Greedy First-Six Flip

### 🧠 Idea
- Convert the number to a string.
- Scan left to right; change the first `'6'` to `'9'` and break.
- Convert back to integer and return.

---

## 💻 Code

```cpp
class Solution {
 public:
  int maximum69Number(int num) {
    string ans = to_string(num);

    for (char& c : ans)
      if (c == '6') {
        c = '9';
        break;
      }

    return stoi(ans);
  }
};
```

---

## 🧠 Dry Run
### Input
```
num = 9669
```
### Steps
```
ans = "9669"
i=0: '9' → skip
i=1: '6' → change to '9' → ans = "9969" → break
return 9969
```

---

## ⏱️ Time Complexity
```
O(d) where d is the number of digits (at most 4)
```

## 💾 Space Complexity
```
O(d) for the string conversion
```

---

## ⚠️ Edge Cases
- `num = 9999` → no `6` exists, return `9999` unchanged
- `num = 6` → return `9`
- `num = 6666` → change first `6` to get `9666`

---

## 🎯 Interview Takeaways
- Greedy from the most significant digit is the optimal strategy.
- String manipulation simplifies digit-level changes.
- Only one change is needed — always pick the leftmost `6`.

---

## 📌 Key Pattern
👉 **"Greedy: flip the most significant unfavorable digit first."**

---

## 🔁 Related Problems
- 1432. Max Difference You Can Get from Changing an Integer
- 670. Maximum Swap

---

## 🚀 Final Thoughts
A classic greedy problem. The insight is simple: the leftmost `6` has the highest positional value, so flipping it yields the maximum result.

---

✨ **Rule to remember:**
> To maximize a number, always upgrade the most significant digit first.
