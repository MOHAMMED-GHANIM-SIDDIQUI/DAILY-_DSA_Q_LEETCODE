# 2048. Next Greater Numerically Balanced Number

## 🔗 Problem Link
https://leetcode.com/problems/next-greater-numerically-balanced-number/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Math, Enumeration, Counting

---

## 🧩 Problem Summary
An integer `x` is numerically balanced if for every digit `d` in `x`, the digit `d` occurs exactly `d` times. Given an integer `n`, return the smallest numerically balanced number strictly greater than `n`.

### 📌 Constraints
- `0 <= n <= 10^6`

---

## 💭 Intuition
👉 Since n <= 10^6, the answer is at most 7 digits. We can simply increment from n+1 and check each number until we find a balanced one.

---

## ⚡ Approach — Brute Force Check

### 🧠 Idea
- Starting from `n + 1`, check each number.
- A number is balanced if every digit `d` that appears does so exactly `d` times, and `0` never appears.
- Return the first balanced number found.

---

## 💻 Code

```cpp
class Solution {
 public:
  int nextBeautifulNumber(int n) {
    while (!isBalance(++n))
      ;
    return n;
  }

 private:
  bool isBalance(int num) {
    vector<int> count(10);
    while (num > 0) {
      if (num % 10 == 0)
        return false;
      ++count[num % 10];
      num /= 10;
    }
    for (int i = 1; i < 10; ++i)
      if (count[i] && count[i] != i)
        return false;
    return true;
  }
};
```

---

## 🧠 Dry Run
### Input
```
n = 1
```
### Steps
```
Check 2: digits=[2], count[2]=1, 1!=2 -> not balanced
Check 3: digits=[3], count[3]=1, 1!=3 -> not balanced
...
Check 22: digits=[2,2], count[2]=2, 2==2 -> balanced!
Return 22
```

---

## ⏱️ Time Complexity
```
O(M * D), where M is the gap to the next balanced number and D is the number of digits (at most 7)
```

## 💾 Space Complexity
```
O(1) (fixed-size count array of size 10)
```

---

## ⚠️ Edge Cases
- n = 0: answer is 1 (digit 1 appears 1 time)
- n = 10^6: answer is 1224444
- Numbers containing 0 are never balanced

---

## 🎯 Interview Takeaways
- When the search space is small, brute force with a validity check is perfectly acceptable.
- Early return on digit 0 is a nice optimization.
- Understanding the problem definition precisely is key.

---

## 📌 Key Pattern
👉 **"Linear scan with validity check when the answer space is bounded"**

---

## 🔁 Related Problems
- 1323. Maximum 69 Number
- 2283. Check if Number Has Equal Digit Count and Digit Value
- 728. Self Dividing Numbers

---

## 🚀 Final Thoughts
The brute force approach works well here because balanced numbers are relatively sparse but bounded. The largest gap between consecutive balanced numbers in the range is manageable.

---

✨ **Rule to remember:**
> When the answer is bounded and gaps are small, just iterate and check.
