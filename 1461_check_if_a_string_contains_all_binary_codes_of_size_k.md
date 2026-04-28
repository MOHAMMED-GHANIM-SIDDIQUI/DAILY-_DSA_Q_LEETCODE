# 1461. Check If a String Contains All Binary Codes of Size K

## 🔗 Problem Link
https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

## ⚡ Difficulty
Medium

## 🏷️ Topics
String, Hash Table, Bit Manipulation

---

## 🧩 Problem Summary
Given a binary string `s` and an integer `k`, return `true` if every binary code of length `k` is a substring of `s`. There are `2^k` such codes in total.

### 📌 Constraints
- `1 <= s.length <= 5 * 10^5`
- `1 <= k <= 20`

---

## 💭 Intuition
👉 We need to check whether all `2^k` binary strings of length `k` appear as substrings. The brute-force approach generates each possible binary code and checks if it exists in `s`.

---

## ⚡ Approach — Brute Force Enumeration

### 🧠 Idea
- Iterate through all integers from `0` to `2^k - 1`.
- Convert each integer to a binary string of length `k` (with leading zeros).
- Check if that binary string is a substring of `s`.
- If any code is missing, return `False`.

---

## 💻 Code

```python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        for i in range(1 << k):
            # format ensures leading zeros
            if format(i, f'0{k}b') not in s:
                return False
        return True
```

---

## 🧠 Dry Run
### Input
```
s = "00110110", k = 2
```
### Steps
```
Check i=0 → "00" in s? Yes (index 0)
Check i=1 → "01" in s? Yes (index 1)
Check i=2 → "10" in s? Yes (index 4)
Check i=3 → "11" in s? Yes (index 3)
All found → return True
```

---

## ⏱️ Time Complexity
```
O(2^k * n), where n is the length of s (substring search for each code)
```

## 💾 Space Complexity
```
O(k) for the formatted binary string
```

---

## ⚠️ Edge Cases
- `k` is larger than `s.length` — impossible to contain any code, return `False`.
- `s` is all zeros — only works if `k=1` is not required to have "1".
- `k = 1` — just need both "0" and "1" in `s`.

---

## 🎯 Interview Takeaways
- A sliding window with a HashSet collecting all k-length substrings would be more efficient: O(n) time.
- Python's `format(i, f'0{k}b')` is a clean way to generate zero-padded binary strings.
- This brute-force approach is simple but may TLE for large `k`.

---

## 📌 Key Pattern
👉 **"Enumerate all possible codes and verify each exists as a substring"**

---

## 🔁 Related Problems
- 187 — Repeated DNA Sequences
- 318 — Maximum Product of Word Lengths
- 1044 — Longest Duplicate Substring

---

## 🚀 Final Thoughts
While this brute-force solution is clear and correct, an optimized approach using a sliding window to collect all unique k-length substrings into a set and checking if the set size equals `2^k` would run in O(n) time.

---

✨ **Rule to remember:**
> "To check all binary codes of size k exist, either enumerate all 2^k codes or collect all k-length substrings into a set."
