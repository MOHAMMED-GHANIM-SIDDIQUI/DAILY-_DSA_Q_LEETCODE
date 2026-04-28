# 3474. Lexicographically Smallest Generated String

## 🔗 Problem Link
https://leetcode.com/problems/lexicographically-smallest-generated-string/

## ⚡ Difficulty
Hard

## 🏷️ Topics
String, Greedy, String Matching

---

## 🧩 Problem Summary
Given two strings `str1` and `str2`, generate the lexicographically smallest string `s` of length `len(str1) + len(str2) - 1` such that for each index `i` in `str1`: if `str1[i] == 'T'`, then `str2` appears as a substring starting at position `i` in `s`; if `str1[i] == 'F'`, then `str2` does NOT appear as a substring starting at position `i` in `s`. Return the result or an empty string if impossible.

### 📌 Constraints
- `1 <= len(str1), len(str2) <= 10^5`
- `str1` contains only `'T'` and `'F'`
- `str2` contains only lowercase English letters

---

## 💭 Intuition
👉 Handle 'T' positions first by fixing characters in the output string, then for 'F' positions try to break the match by changing the last possible unfixed character to 'b' — this greedy approach ensures lexicographic minimality.

---

## ⚡ Approach — Greedy with Fixed Positions

### 🧠 Idea
- Initialize the result string `s` as all `'a'`s (lexicographically smallest).
- For each 'T' in `str1`, stamp `str2` onto `s` at that position and mark those positions as fixed. If a conflict arises, return "".
- For each 'F' in `str1`, check if `s[i:i+m]` already differs from `str2`. If not, find the rightmost unfixed position in that window and change it to `'b'` to break the match.
- If no unfixed position exists to break the match, return "".

---

## 💻 Code

```python
class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        s = ['a'] * (n + m - 1) # s is the ans
        fixed = [False] * (n + m - 1)

        # Handle 'T'
        for i in range(n): #str1
            if str1[i] == 'T':
                for j in range(m):
                    pos = i + j
                    if fixed[pos] and s[pos] != str2[j]: # collison
                        return ""
                    s[pos] = str2[j]
                    fixed[pos] = True

        # Handle 'F'
        for i in range(n):
            if str1[i] == 'F':
                diff = False
                # Check if already different
                for j in range(m):
                    if s[i + j] != str2[j]:
                        diff = True
                        break

                if diff:
                    continue

                # Try to force difference
                changed = False
                for j in range(m - 1, -1, -1): # win where we need to change is s[i:i+m]
                    pos = i + j
                    if not fixed[pos]:
                        s[pos] = 'b'
                        changed = True
                        break

                if not changed:
                    return ""

        return "".join(s)
```

---

## 🧠 Dry Run
### Input
```
str1 = "TFTF", str2 = "ab"
```
### Steps
```
n=4, m=2, s = ['a','a','a','a','a'] (length 5), fixed = [F,F,F,F,F]

i=0, str1[0]='T': stamp "ab" at pos 0,1 → s=['a','b','a','a','a'], fixed=[T,T,F,F,F]
i=1, str1[1]='F': s[1:3]="ba" vs "ab" → already different → skip
i=2, str1[2]='T': stamp "ab" at pos 2,3 → s=['a','b','a','b','a'], fixed=[T,T,T,T,F]
i=3, str1[3]='F': s[3:5]="ba" vs "ab" → already different → skip

Result: "ababa"
```

---

## ⏱️ Time Complexity
```
O(n * m) — for each position in str1, we may scan str2's length
```

## 💾 Space Complexity
```
O(n + m) — for the result string and fixed array
```

---

## ⚠️ Edge Cases
- All 'T' positions conflict with each other → return ""
- All 'F' positions but every character is fixed → return ""
- `str2` is a single character
- Overlapping 'T' windows must agree on character assignments

---

## 🎯 Interview Takeaways
- Process mandatory constraints ('T') before optional/negative constraints ('F').
- Using a `fixed` array to track locked positions is a clean way to detect conflicts.
- Greedy choice of 'b' (next smallest character after 'a') preserves lexicographic order.

---

## 📌 Key Pattern
👉 **"Greedy stamping with conflict detection — fix forced characters first, then break unwanted matches at the latest possible position."**

---

## 🔁 Related Problems
- 1408. String Matching in an Array
- 1397. Find All Good Strings
- 28. Find the Index of the First Occurrence in a String

---

## 🚀 Final Thoughts
This problem elegantly combines string matching with greedy construction. The key insight is separating the 'T' phase (which locks characters) from the 'F' phase (which breaks matches), and always choosing the rightmost unfixed position to minimize lexicographic impact.

---

✨ **Rule to remember:**
> "Fix what must match first, then break what must not — always from the rightmost unfixed position for lexicographic minimality."
