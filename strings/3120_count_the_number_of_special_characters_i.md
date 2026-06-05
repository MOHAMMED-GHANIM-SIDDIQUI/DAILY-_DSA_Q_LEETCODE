# 3120. Count the Number of Special Characters I

## 🔗 Problem Link
https://leetcode.com/problems/count-the-number-of-special-characters-i/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Hash Table, String

---

## 🧩 Problem Summary
A letter `c` is **special** if it appears in the string `word` **both** in lowercase and in uppercase. Return the number of special letters.

### 📌 Constraints
- `1 <= word.length <= 50`
- `word` consists of only lowercase and uppercase English letters.

---

## 💭 Intuition
A letter is special when **both** case forms are present somewhere in the string. Position doesn't matter (that's the "II" version) — only presence. So for each distinct letter we ask: is its lowercase form in `word` **and** its uppercase form in `word`?

The cleanest way: take the **set** of characters in `word` (so each letter is examined once), and for each character check whether both `c.upper()` and `c.lower()` occur in `word`. Because we iterate over distinct characters, every special letter gets counted **twice** (once when we see its lowercase, once its uppercase), so we divide the final count by 2.

---

## ⚡ Approach — Set membership, both cases

### 🧠 Idea
1. Build `set(word)` so each character is visited once.
2. For each `c`, if `c.upper() in word` **and** `c.lower() in word`, it's special → `ans += 1`.
3. Each special letter is hit from both its cases → return `ans // 2`.

---

## 💻 Code

```python
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0
        for c in set(word):
            if c.upper() in word and c.lower() in word:
                ans += 1
        return ans // 2
```

---

## 🧠 Dry Run
### Input
```
word = "aaAbcBC"
```

### Distinct chars
```
{a, A, b, c, B, C}
```

### Check
```
a: 'A' in word? yes, 'a' in word? yes → +1
A: same letter → +1
b: 'B' yes, 'b' yes → +1
B: → +1
c: 'C' yes, 'c' yes → +1
C: → +1
ans = 6 → 6 // 2 = 3
```
Special letters: `a, b, c` → `3`.

---

## ⏱️ Time Complexity
```
O(n · 26) → O(n)   — for each distinct char (≤ 52), `in word` scans the string.
```

## 💾 Space Complexity
```
O(1)   — the character set holds at most 52 entries.
```

---

## ⚠️ Edge Cases
- **No letter in both cases** (`"abc"`) → `0`.
- **Only one case present** for every letter → `0`.
- **All letters special** → counted twice each, the `// 2` corrects it.

---

## 🎯 Interview Takeaways
- The double-count + `// 2` is a tidy trick, but an arguably clearer alternative is to compare two sets: `lower = {c for c in word if c.islower()}`, `upper = {c.lower() for c in word if c.isupper()}`, then `len(lower & upper)` — no division needed. Worth mentioning both.
- Position-independence is what makes this Easy; the follow-up **3121** adds an ordering constraint that breaks the pure-set approach.

---

## 📌 Key Pattern
👉 **"'Appears in both forms' = set membership of both `lower()` and `upper()`; or intersect the lowercase-seen and uppercase-seen sets."**

---

## 🔁 Related Problems
- 3121. Count the Number of Special Characters II
- 2784. Check if Array Is Good
- 1832. Check if the Sentence Is Pangram

---

## 🚀 Final Thoughts
Tiny constraints make brute force fine, but recognising this as a **set intersection** of "letters seen lowercase" and "letters seen uppercase" is the mental model that scales and sets up the harder ordered follow-up.

---

✨ **Rule to remember:**
> "Present in both cases" is a set-intersection question. The `// 2` shortcut works only because iterating distinct characters visits each special letter from both of its case forms.
