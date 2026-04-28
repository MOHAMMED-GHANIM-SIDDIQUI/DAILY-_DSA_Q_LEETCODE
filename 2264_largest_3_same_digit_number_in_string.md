# 2264. Largest 3-Same-Digit Number in String

## 🔗 Problem Link
https://leetcode.com/problems/largest-3-same-digit-number-in-string/

## ⚡ Difficulty
Easy

## 🏷️ Topics
String

---

## 🧩 Problem Summary
Given a string `num` of digits, find the largest substring of length 3 where all three digits are the same (e.g., "777"). If no such substring exists, return an empty string.

### 📌 Constraints
- `3 <= num.length <= 1000`
- `num` consists of only digits `'0'` through `'9'`

---

## 💭 Intuition
👉 Slide a window of size 3 across the string. When all three characters match, compare with the current best using lexicographic order.

---

## ⚡ Approach — Sliding Window

### 🧠 Idea
- Iterate through the string checking every triplet of consecutive characters.
- If all three are the same, form the 3-character string.
- Track the lexicographically largest such string found.

---

## 💻 Code

```cpp
class Solution {
public:
    string largestGoodInteger(string s) {
        string ans = "";
        for (int i = 0; i + 2 < (int)s.size(); ++i) {
            if (s[i] == s[i + 1] && s[i + 1] == s[i + 2]) {
                string t = string(3, s[i]);     // e.g., "777"
                if (ans.empty() || t > ans) ans = t;  // lex works for equal-length digit strings
            }
        }
        return ans;
    }
};
```

---

## 🧠 Dry Run
### Input
```
s = "6777133339"
```
### Steps
```
i=0: "677" → not all same
i=1: "777" → all same, ans = "777"
i=2: "771" → not all same
i=3: "713" → not all same
i=4: "133" → not all same
i=5: "333" → all same, "333" < "777", ans stays "777"
i=6: "333" → all same, "333" < "777", ans stays "777"
i=7: "339" → not all same
Result: "777"
```

---

## ⏱️ Time Complexity
```
O(n) — single pass through the string
```

## 💾 Space Complexity
```
O(1) — only storing a 3-character result
```

---

## ⚠️ Edge Cases
- No three consecutive identical digits → return ""
- "000" present → return "000" if no larger exists
- Entire string is one repeated digit → that digit repeated 3 times

---

## 🎯 Interview Takeaways
- Lexicographic comparison works correctly for equal-length digit strings.
- Simple sliding window of fixed size is efficient for pattern detection.
- "000" is a valid good integer — don't confuse with empty/false.

---

## 📌 Key Pattern
👉 **"Fixed-size sliding window to find the best matching substring"**

---

## 🔁 Related Problems
- 1876. Substrings of Size Three with Distinct Characters
- 459. Repeated Substring Pattern
- 1446. Consecutive Characters

---

## 🚀 Final Thoughts
A simple string scanning problem. The trick is using lexicographic comparison on equal-length strings of digits, which correctly identifies the numerically largest match.

---

✨ **Rule to remember:**
> "Slide a window of size 3, check for triple match, and keep the lexicographically largest."
