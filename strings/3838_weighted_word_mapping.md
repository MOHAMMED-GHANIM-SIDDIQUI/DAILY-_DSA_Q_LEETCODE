# 3838. Weighted Word Mapping

## 🔗 Problem Link
https://leetcode.com/problems/weighted-word-mapping/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Hash Table, String, Counting

---

## 🧩 Problem Summary

You are given a list of `words` and a `weights` array of length 26, where `weights[i]` is the weight of the `i`-th lowercase letter (`a` = index 0). The weight of a word is the sum of its letters' weights. For each word compute `weight % 26` and map it through the reverse alphabet: `0 -> 'z'`, `1 -> 'y'`, …, `25 -> 'a'` (i.e. `chr(ord('z') - weight % 26)`). Concatenate the mapped characters of all words into the result string.

### 📌 Constraints
- `1 <= words.length`
- Each word consists of lowercase English letters.
- `weights` has length 26 with integer weights.

---

## 💭 Intuition

👉 Each word collapses to exactly one output character: sum its letter weights, take it mod 26, and read off the reverse-alphabet letter via `chr(ord('z') - r)`.

---

## ⚡ Approach — Per-Word Weight Sum + Reverse-Alphabet Map

### 🧠 Idea
- For each `word`, accumulate `total += weights[ord(ch) - ord('a')]` over its characters.
- Reduce with `total % 26` to get a value `r` in `[0, 25]`.
- Map to a character with `chr(ord('z') - r)` so that `0` maps to `'z'` and `25` maps to `'a'`.
- Append each mapped char to a list and `"".join` them at the end.

---

## 💻 Code

```python
class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []

        for word in words:
            total = 0

            for ch in word:
                total += weights[ord(ch) - ord('a')]

            ans.append(chr(ord('z') - (total % 26)))

        return "".join(ans)
```

---

## 🧠 Dry Run

### Input
```
words = ["abc", "z"]
weights = [1, 2, 3, 0, 0, ..., 0, 25]   # a=1, b=2, c=3, z=25
```

### Steps
```
word = "abc":
  total = weights['a'-'a'] + weights['b'-'a'] + weights['c'-'a']
        = 1 + 2 + 3 = 6
  6 % 26 = 6
  chr(ord('z') - 6) = chr(122 - 6) = chr(116) = 't'
  ans = ['t']

word = "z":
  total = weights['z'-'a'] = weights[25] = 25
  25 % 26 = 25
  chr(ord('z') - 25) = chr(122 - 25) = chr(97) = 'a'
  ans = ['t', 'a']

"".join(ans) = "ta"
```

---

## ⏱️ Time Complexity
```
O(N)
```
`N` is the total number of characters across all words; each character is visited once.

---

## 💾 Space Complexity
```
O(W)
```
`W` is the number of words — one mapped character per word stored in `ans` (output size).

---

## ⚠️ Edge Cases
- A word weight that is a multiple of 26 → `r = 0` → maps to `'z'`.
- Large weight sums are fine since `% 26` normalizes the range.
- Single-letter words simply map that letter's weight directly.

---

## 🎯 Interview Takeaways
- `ord(ch) - ord('a')` is the standard 0-based index for a lowercase letter.
- `chr(ord('z') - r)` cleanly encodes the reverse-alphabet mapping without a lookup table.
- Building a list and joining beats repeated string concatenation for the output.

---

## 📌 Key Pattern
👉 **"Sum-and-mod fold: reduce each group to one bounded value, then map it to a symbol."**

---

## 🔁 Related Problems
- 1880. Check if Word Equals Summation of Two Words
- 2011. Final Value of Variable After Performing Operations
- 1832. Check if the Sentence Is Pangram

---

## 🚀 Final Thoughts
A tidy mapping exercise: each word folds into a single number via weighted sum, modular arithmetic bounds it to one of 26 values, and the reverse-alphabet formula turns that into a letter. Using a list plus `join` keeps the concatenation efficient.

---

✨ **Rule to remember:**
> "Reduce each item to a bounded key with mod, then translate the key to its output symbol with simple arithmetic."
