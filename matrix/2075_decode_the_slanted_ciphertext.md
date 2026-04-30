# 2075. Decode the Slanted Ciphertext

## 🔗 Problem Link
https://leetcode.com/problems/decode-the-slanted-ciphertext/

## ⚡ Difficulty
Medium

## 🏷️ Topics
String, Simulation, Matrix

---

## 🧩 Problem Summary
A string `originalText` is encoded into a matrix of `rows` rows by writing it diagonally from top-left to bottom-right, filling remaining cells with spaces. Given the `encodedText` (the matrix read row by row) and the number of `rows`, decode and return the original text with trailing spaces removed.

### 📌 Constraints
- `0 <= encodedText.length <= 10^6`
- `encodedText` consists of lowercase English letters and spaces `' '`
- `encodedText` is a valid encoding of some `originalText`
- `1 <= rows <= 1000`

---

## 💭 Intuition
👉 The text was placed diagonally in a matrix, so reading it back means starting at each column of the first row and jumping diagonally (row+1, col+1) through the matrix. Since the matrix is flattened into a string, a diagonal step corresponds to jumping `cols + 1` positions in the encoded string.

---

## ⚡ Approach — Diagonal Traversal Simulation

### 🧠 Idea
- Compute the number of columns as `len(encodedText) // rows`.
- For each starting column `i` (0 to cols-1), traverse diagonally by stepping `cols + 1` in the flat string.
- Collect all characters in order and strip trailing spaces.

---

## 💻 Code

```python
class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
      n = len(encodedText)
      cols = n // rows
      ans = ''
      for i in range(cols):
        j=i
        while j<n:
          ans+=encodedText[j]
          j+=(cols+1)
      return ans.rstrip()
```

---

## 🧠 Dry Run
### Input
```
encodedText = "ch   ie   pr", rows = 3
```
### Steps
```
cols = 12 // 3 = 4
Matrix:
  c h _ _
  i e _ _
  p r _ _

i=0: j=0 ('c'), j=5 ('e'), j=10 ('_') → "ce "
i=1: j=1 ('h'), j=6 (' '), j=11 ('r') → "h r"
i=2: j=2 (' '), j=7 ('i') → " i"
i=3: j=3 (' '), j=8 ('p') → " p"

ans = "ce h r i p" → rstrip → "cipher"
```

---

## ⏱️ Time Complexity
```
O(n) — each character in encodedText is visited exactly once.
```

## 💾 Space Complexity
```
O(n) — for the result string.
```

---

## ⚠️ Edge Cases
- `rows = 1`: the encoded text is the original text itself.
- `encodedText` is empty: return empty string.
- All spaces: return empty string after rstrip.

---

## 🎯 Interview Takeaways
- Flattening a 2D diagonal traversal into 1D index arithmetic is a common pattern.
- Understanding how row-major order indices map to (row, col) coordinates is essential.
- Always consider trailing space removal as part of decoding.

---

## 📌 Key Pattern
👉 **"Diagonal traversal in a flattened matrix using index arithmetic (step = cols + 1)"**

---

## 🔁 Related Problems
- 498. Diagonal Traverse
- 1260. Shift 2D Grid
- 2075. Decode the Slanted Ciphertext

---

## 🚀 Final Thoughts
This problem is a simulation exercise. The key insight is recognizing that a diagonal move in a matrix translates to a fixed offset in the flattened string. Once you derive that offset (`cols + 1`), the rest is straightforward iteration.

---

✨ **Rule to remember:**
> "Diagonal in a matrix = step by (cols + 1) in the flat array."
