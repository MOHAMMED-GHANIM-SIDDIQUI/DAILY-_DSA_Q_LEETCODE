# 2452. Words Within Two Edits of Dictionary

## 🔗 Problem Link
https://leetcode.com/problems/words-within-two-edits-of-dictionary/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, String, Brute Force

---

## 🧩 Problem Summary
Given a list of `queries` words and a `dictionary`, return all words from queries that can be transformed into some dictionary word by changing at most 2 characters. All words have the same length.

### 📌 Constraints
- `1 <= queries.length, dictionary.length <= 100`
- `n == queries[i].length == dictionary[j].length`
- `1 <= n <= 100`
- All strings consist of lowercase English letters.

---

## 💭 Intuition
👉 Since constraints are small (at most 100 words of length 100), a brute-force approach comparing every query against every dictionary word and counting character differences works efficiently.

---

## ⚡ Approach — Brute Force Character Comparison

### 🧠 Idea
- For each query word, compare it character-by-character against each dictionary word.
- Count mismatches; if the count is at most 2, add the query to the result and move on.
- Early termination: if mismatch count exceeds 2, stop comparing that pair.

---

## 💻 Code

```python
class Solution:
    def is_two_diff(self, word1 , word2):
      if len(word1)!=len(word2):
        return False
      n = len(word1)
      cnt = 0
      for i in range(n):
        if word1[i]!=word2[i]:
          cnt+=1
        if cnt>2:
          return False
      return True

    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
      ans = []
      for word1 in queries:
        for word2 in dictionary:
          if self.is_two_diff(word1,word2):
            ans.append(word1)
            break
      return ans
```

---

## 🧠 Dry Run
### Input
```
queries = ["word","note","ants","wood"], dictionary = ["wood","joke","moat"]
```
### Steps
```
"word" vs "wood": w=w, o=o, r≠o (cnt=1), d=d → cnt=1 ≤ 2 → add "word"
"note" vs "wood": n≠w (1), o=o, t≠o (2), e≠d (3) → cnt>2 fail
"note" vs "joke": n≠j (1), o=o, t≠k (2), e=e → cnt=2 ≤ 2 → add "note"
"ants" vs "wood": a≠w (1), n≠o (2), t≠o (3) → fail
"ants" vs "joke": a≠j (1), n≠o (2), t≠k (3) → fail
"ants" vs "moat": a≠m (1), n≠o (2), t≠a (3) → fail → skip "ants"
"wood" vs "wood": exact match → cnt=0 ≤ 2 → add "wood"

Result: ["word", "note", "wood"]
```

---

## ⏱️ Time Complexity
```
O(q * d * n) where q = len(queries), d = len(dictionary), n = word length.
```

## 💾 Space Complexity
```
O(q) — for the result list.
```

---

## ⚠️ Edge Cases
- Exact match: 0 edits, which is ≤ 2.
- All characters different but word length ≤ 2: still valid.
- No query matches any dictionary word: return empty list.

---

## 🎯 Interview Takeaways
- Always check constraints before optimizing — brute force is fine when inputs are small.
- Early termination (break when cnt > 2) is a simple but effective optimization.
- Hamming distance comparison is a fundamental string operation.

---

## 📌 Key Pattern
👉 **"Hamming distance check with early termination for bounded edit distance."**

---

## 🔁 Related Problems
- 72. Edit Distance
- 161. One Edit Distance
- 676. Implement Magic Dictionary

---

## 🚀 Final Thoughts
With small constraints, the brute force approach is both correct and efficient. The early termination when mismatches exceed 2 ensures we don't do unnecessary work. For larger inputs, a trie-based approach could be considered.

---

✨ **Rule to remember:**
> "When constraints are small, brute force with early termination is often the best approach."
