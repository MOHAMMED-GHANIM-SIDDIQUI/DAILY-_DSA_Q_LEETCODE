# 1758. Minimum Changes to Make Alternating Binary String

## 🔗 Problem Link
https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

## ⚡ Difficulty
Easy

## 🏷️ Topics
String

---

## 🧩 Problem Summary
Given a string `s` consisting only of `'0'` and `'1'`, return the minimum number of character changes needed to make `s` alternating. An alternating string has no two adjacent characters that are equal (e.g., `"0101..."` or `"1010..."`).

### 📌 Constraints
- `1 <= s.length <= 10^4`
- `s[i]` is either `'0'` or `'1'`.

---

## 💭 Intuition
👉 There are only two possible alternating patterns: starting with `'0'` (`"0101..."`) or starting with `'1'` (`"1010..."`). Count mismatches against both and return the minimum.

---

## ⚡ Approach — Compare Against Both Patterns

### 🧠 Idea
- Iterate through the string.
- Count how many characters differ from the pattern `"010101..."` → `diff1`.
- Count how many characters differ from the pattern `"101010..."` → `diff2`.
- Return `min(diff1, diff2)`.

---

## 💻 Code

```python
class Solution:
    def minOperations(self, s: str) -> int:
        diff1 = diff2 = 0

        for i, ch in enumerate(s):
            if ch != ('1' if i % 2 == 0 else '0'):
                diff1 += 1
            if ch != ('0' if i % 2 == 0 else '1'):
                diff2 += 1

        return min(diff1, diff2)
```

---

## 🧠 Dry Run
### Input
```
s = "0100"
```
### Steps
```
Pattern1: "1010"  Pattern2: "0101"

i=0: ch='0', P1='1' → diff1++, P2='0' → match     → diff1=1, diff2=0
i=1: ch='1', P1='0' → diff1++, P2='1' → match     → diff1=2, diff2=0
i=2: ch='0', P1='1' → diff1++, P2='0' → match     → diff1=3, diff2=0
i=3: ch='0', P1='0' → match,   P2='1' → diff2++   → diff1=3, diff2=1

Result: min(3, 1) = 1
```

---

## ⏱️ Time Complexity
```
O(n) — single pass through the string
```

## 💾 Space Complexity
```
O(1) — only two counters
```

---

## ⚠️ Edge Cases
- String of length 1 → already alternating, answer is 0.
- String already alternating → answer is 0.
- Note: `diff1 + diff2 = n` always, so `min(diff1, diff2) = min(diff1, n - diff1)`.

---

## 🎯 Interview Takeaways
- When there are only two possible target patterns, compare against both.
- The observation that `diff1 + diff2 = n` means you only need one counter.
- This is a common pattern for problems with binary choices.

---

## 📌 Key Pattern
👉 **"Compare against both possible alternating patterns and take the minimum"**

---

## 🔁 Related Problems
- 926. Flip String to Monotone Increasing
- 1653. Minimum Deletions to Make String Balanced
- 2170. Minimum Operations to Make the Array Alternating

---

## 🚀 Final Thoughts
A straightforward problem with a clean O(n) solution. The key realisation is that there are only two valid alternating patterns, so checking both and taking the minimum gives the answer directly.

---

✨ **Rule to remember:**
> For alternating binary strings, there are only two patterns — count mismatches against both and pick the smaller.
