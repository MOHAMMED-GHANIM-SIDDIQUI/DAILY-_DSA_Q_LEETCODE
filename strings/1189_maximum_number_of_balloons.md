# 1189. Maximum Number of Balloons

## 🔗 Problem Link
https://leetcode.com/problems/maximum-number-of-balloons/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Hash Table, String, Counting

---

## 🧩 Problem Summary

Given a string `text`, return the maximum number of times you can spell the word `"balloon"` using the characters of `text`, where each character can be used at most once. The word `"balloon"` requires `b`, `a`, `n` once each and `l`, `o` twice each. The answer is limited by whichever required letter runs out first.

### 📌 Constraints
- `1 <= text.length <= 10^4`
- `text` consists of lowercase English letters only.

---

## 💭 Intuition

👉 The number of `"balloon"` words you can build is bottlenecked by the scarcest required letter. Count every character, then divide each letter's count by how many times that letter appears in `"balloon"` (`l` and `o` need 2, the rest need 1) and take the minimum.

---

## ⚡ Approach — Frequency Count + Min Bottleneck

### 🧠 Idea
- Build a frequency map of all characters in `text` using `Counter`.
- For each letter in `"balloon"`, compute how many full words its supply allows: `b`, `a`, `n` divide by 1; `l`, `o` divide by 2 (integer division).
- The answer is the minimum across all five quantities, since you cannot exceed the limit set by the rarest letter.

---

## 💻 Code

```python
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)

        return min( c['b'], c['a'],  c['l'] // 2, c['o'] // 2, c['n'] )
```

---

## 🧠 Dry Run

### Input
```
text = "loonbalxballpoon"
```

### Steps
```
Counter(text):
  l: 4, o: 4, n: 2, b: 2, a: 2, x: 1, p: 1

Evaluate min:
  c['b']      = 2
  c['a']      = 2
  c['l'] // 2 = 4 // 2 = 2
  c['o'] // 2 = 4 // 2 = 2
  c['n']      = 2

min(2, 2, 2, 2, 2) = 2
```
Answer: `2`

---

## ⏱️ Time Complexity
```
O(n)
```
One pass to count all `n` characters; the `min` over a fixed 5 letters is constant.

---

## 💾 Space Complexity
```
O(1)
```
The `Counter` holds at most 26 distinct lowercase keys regardless of input size.

---

## ⚠️ Edge Cases
- `text` missing a required letter → that key returns count `0` via `Counter`, so the min is `0`.
- Plenty of `l`/`o` but odd counts → integer division correctly floors (e.g. 3 `l` allows only 1 use).
- No `"balloon"` letters at all → returns `0`.

---

## 🎯 Interview Takeaways
- `Counter` returns `0` for missing keys, avoiding `KeyError` and explicit defaults.
- Recognize the "build target word from a letter pool" pattern as a min-of-ratios problem.
- Account for repeated letters in the target by dividing the supply.

---

## 📌 Key Pattern
👉 **"Bottleneck by the scarcest resource: min of (supply / demand) per required item."**

---

## 🔁 Related Problems
- 383. Ransom Note
- 387. First Unique Character in a String
- 1160. Find Words That Can Be Formed by Characters

---

## 🚀 Final Thoughts
A clean counting problem: the entire solution collapses to one `min` over five precomputed ratios once you realize the target word's letter multiplicities (`l` and `o` twice). The `Counter` defaulting to zero keeps the code short and safe.

---

✨ **Rule to remember:**
> "When forming copies of a target from a pool, the answer is the minimum of each letter's supply divided by its demand."
