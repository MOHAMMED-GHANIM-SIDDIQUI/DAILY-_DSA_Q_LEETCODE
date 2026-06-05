# 3121. Count the Number of Special Characters II

## 🔗 Problem Link
https://leetcode.com/problems/count-the-number-of-special-characters-ii/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Hash Table, String

---

## 🧩 Problem Summary
A letter `c` is **special** if it appears **both** in lowercase and uppercase in `word`, **and** every lowercase occurrence comes **before** every uppercase occurrence. Equivalently: the **last** index of the lowercase `c` is **smaller** than the **first** index of the uppercase `C`. Return the count of special letters.

### 📌 Constraints
- `1 <= word.length <= 2 * 10^5`
- `word` consists of only lowercase and uppercase English letters.

---

## 💭 Intuition
The only thing that matters for each letter is the boundary between its lowercase region and uppercase region:

- the **last** position where the lowercase form appears, and
- the **first** position where the uppercase form appears.

The letter is special iff `last[lowercase] < first[uppercase]` (and both forms exist). So we make a single pass recording, for every character, its **first** index and its **last** index. Then for each of the 26 letters we compare `last[low]` against `first[up]`.

---

## ⚡ Approach — First/last index tables

### 🧠 Idea
1. One pass over `word`: for each character `ch` at index `i`,
   - set `first[ch]` if not already set (first sighting),
   - always update `last[ch] = i` (latest sighting).
2. For each letter pairing `(low, up)` over `a..z` / `A..Z`:
   - if `low` has a last index and `up` has a first index, and `last[low] < first[up]` → special, `ans += 1`.
3. Return `ans`.

### 🔑 Why first/last indices
"All lowercase before all uppercase" is exactly "the latest lowercase precedes the earliest uppercase." Comparing extremes captures the whole ordering in `O(1)` per letter.

---

## 💻 Code

```python
from string import ascii_lowercase, ascii_uppercase

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        first = {}
        last = {}

        for i, ch in enumerate(word):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        ans = 0

        for low, up in zip(ascii_lowercase, ascii_uppercase):
            if low in last and up in first:
                if last[low] < first[up]:
                    ans += 1

        return ans
```

---

## 🧠 Dry Run
### Input
```
word = "AbBCab"
index: A0 b1 B2 C3 a4 b5
```

### first / last
```
first = {A:0, b:1, B:2, C:3, a:4}
last  = {A:0, b:5, B:2, C:3, a:4}
```

### Check letters
```
a/A: last['a']=4, first['A']=0 → 4 < 0? no
b/B: last['b']=5, first['B']=2 → 5 < 2? no
c/C: 'c' not in last → skip
```
Answer: `0` (every lowercase comes after its uppercase here).

### Special example
```
word = "aaAbB"
last['a']=1, first['A']=2 → 1 < 2 ✓ special
last['b']=3, first['B']=4 → 3 < 4 ✓ special
→ 2
```

---

## ⏱️ Time Complexity
```
O(n + 26)  → O(n)   — one pass to build tables, constant scan over letters.
```

## 💾 Space Complexity
```
O(1)   — at most 52 keys in each dictionary.
```

---

## ⚠️ Edge Cases
- **Lowercase exists but no uppercase** (or vice-versa) → skipped, not special.
- **Interleaved cases** (`"aAa"`) → `last['a']=2 > first['A']=1` → not special.
- **Exactly adjacent boundary** (`"aA"`) → `0 < 1` → special.
- Large input (`2·10^5`) → linear pass keeps it fast.

---

## 🎯 Interview Takeaways
- The leap from **3120** (presence only) to **3121** (ordering) is the classic "now add a positional constraint" follow-up. The fix is recording **first** and **last** indices instead of mere presence.
- `last[low] < first[up]` is the compact encoding of "all lowercase strictly before all uppercase" — extremes beat scanning every occurrence.
- `zip(ascii_lowercase, ascii_uppercase)` cleanly pairs `a↔A … z↔Z` without index math.

---

## 📌 Key Pattern
👉 **"'All of group A before all of group B' ⇔ max-index(A) < min-index(B). Track first/last positions, compare extremes."**

---

## 🔁 Related Problems
- 3120. Count the Number of Special Characters I
- 942. DI String Match
- 1657. Determine if Two Strings Are Close
- 2055. Plates Between Candles

---

## 🚀 Final Thoughts
Whenever a problem upgrades from "does X occur" to "does X occur before Y," reach for first/last index tracking. Here it turns an ordering question into two dictionary lookups and a single comparison per letter.

---

✨ **Rule to remember:**
> "Everything lowercase before everything uppercase" reduces to `last[low] < first[up]`. Record extremes in one pass; never re-scan to verify ordering.
