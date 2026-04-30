# 1784. Check if Binary String Has at Most One Segment of Ones

## 🔗 Problem Link
https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

## ⚡ Difficulty
Easy

## 🏷️ Topics
String

---

## 🧩 Problem Summary
Given a binary string `s` (without leading zeros), return `true` if the string contains at most one contiguous segment of ones. In other words, once the ones stop and zeros begin, no more ones should appear later.

### 📌 Constraints
- `1 <= s.length <= 100`
- `s[i]` is either `'0'` or `'1'`
- `s[0]` is `'1'`

---

## 💭 Intuition
👉 Once we encounter a `'0'` after seeing `'1'`s, any subsequent `'1'` means there are two separate segments of ones — so we immediately return `false`.

---

## ⚡ Approach — Linear Scan with Flag

### 🧠 Idea
- Use a boolean flag initialized to `True` (meaning we are still in the ones segment).
- When we see a `'0'` and the flag is `True`, set the flag to `False` (we've left the ones segment).
- If we see a `'1'` while the flag is `False`, a second segment of ones exists — return `False`.
- If we finish the loop without returning, return `True`.

---

## 💻 Code

```python
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # 11110001000 ----> valid
        # 0000011111--->not valid
        flag = True
        for i in s:
            if i != '1' and flag:
                flag=False # zero is here
                continue
            if i =='1' and flag==False: # getting 1 after zero
                return flag
        return True
```

---

## 🧠 Dry Run
### Input
```
s = "110"
```
### Steps
```
i='1', flag=True  → skip (it's '1' and flag is True)
i='1', flag=True  → skip
i='0', flag=True  → set flag=False
Loop ends → return True
```

---

## ⏱️ Time Complexity
```
O(n), where n is the length of the string
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- `s = "1"` → only one character, return `True`
- `s = "10"` → one segment, return `True`
- `s = "101"` → two segments, return `False`

---

## 🎯 Interview Takeaways
- A simple flag-based approach can detect pattern breaks in a single pass.
- Checking for `"01"` as a substring (`return "01" not in s`) is an even simpler alternative.

---

## 📌 Key Pattern
👉 **"Flag-based linear scan to detect a pattern break in a string"**

---

## 🔁 Related Problems
- 485. Max Consecutive Ones
- 1446. Consecutive Characters
- 696. Count Binary Substrings

---

## 🚀 Final Thoughts
This is a straightforward string traversal problem. The key insight is that a binary string without leading zeros can have at most one segment of ones only if no `'1'` appears after any `'0'`.

---

✨ **Rule to remember:**
> If a `'1'` appears after a `'0'` in a binary string starting with `'1'`, there are multiple segments.
