# 1689. Partitioning Into Minimum Number of Deci-Binary Numbers

## 🔗 Problem Link
https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

## ⚡ Difficulty
Medium

## 🏷️ Topics
String, Greedy

---

## 🧩 Problem Summary
A deci-binary number is one where each digit is either 0 or 1 (no leading zeros except for "0"). Given a string `n` representing a positive decimal integer, return the minimum number of deci-binary numbers needed to sum up to `n`.

### 📌 Constraints
- `1 <= n.length <= 10^5`
- `n` consists of only digits `0-9`
- `n` does not contain leading zeros and represents a positive integer.

---

## 💭 Intuition
👉 Each deci-binary number contributes at most 1 to each digit position. So the digit with the maximum value determines how many deci-binary numbers we need — that digit needs that many "1"s contributed to it.

---

## ⚡ Approach — Maximum Digit

### 🧠 Idea
- The answer is simply the maximum digit in the string.
- If the largest digit is `d`, we need exactly `d` deci-binary numbers.

---

## 💻 Code

```python
class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))
```

---

## 🧠 Dry Run
### Input
```
n = "32"
```
### Steps
```
Digits: '3', '2'
max digit = '3'
Answer: 3

Verify: 32 = 11 + 11 + 10 (three deci-binary numbers) ✓
```

---

## ⏱️ Time Complexity
```
O(n) — scan through all digits to find the maximum
```

## 💾 Space Complexity
```
O(1) — no extra space used
```

---

## ⚠️ Edge Cases
- `n = "10"` → max digit is 1, answer is 1.
- `n = "9999...9"` → answer is 9.
- Single digit `n = "5"` → answer is 5.

---

## 🎯 Interview Takeaways
- Sometimes the simplest observation yields the most elegant solution.
- Think about what each "unit" (deci-binary number) can contribute per digit position.
- This is a great example of a problem that looks complex but has a one-liner solution.

---

## 📌 Key Pattern
👉 **"The bottleneck digit determines the count — each unit contributes at most 1 per position"**

---

## 🔁 Related Problems
- 343. Integer Break
- 1217. Minimum Cost to Move Chips to The Same Position

---

## 🚀 Final Thoughts
A deceptively simple problem. The insight that each deci-binary number contributes at most 1 to each digit immediately gives the answer as the maximum digit. One of the most elegant one-liners on LeetCode.

---

✨ **Rule to remember:**
> The minimum number of deci-binary numbers equals the maximum digit — each contributes at most 1 per position.
