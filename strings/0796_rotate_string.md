# 796. Rotate String

## 🔗 Problem Link
https://leetcode.com/problems/rotate-string/

## ⚡ Difficulty
Easy

## 🏷️ Topics
String, String Matching

---

## 🧩 Problem Summary

Given two strings `s` and `goal`, return `True` if and only if `s` can become `goal` after some number of **left shifts** on `s`. A shift on `s` consists of moving the leftmost character of `s` to the rightmost position, e.g. if `s = "abcde"`, then it will be `"bcdea"` after one shift.

### 📌 Constraints
- `1 <= s.length, goal.length <= 100`
- `s` and `goal` consist of lowercase English letters.

---

## 💭 Intuition

👉 Every possible rotation of `s` is a length-`n` substring of `s + s`. So the question "is `goal` a rotation of `s`?" reduces to a single substring check on the doubled string — provided the lengths actually match.

---

## ⚡ Approach — Doubled-String Substring Check

### 🧠 Idea

- Concatenate `s` with itself: `s + s` contains every rotation of `s` as a contiguous length-`n` slice.
- Therefore `goal` is a rotation of `s` iff:
  1. `len(goal) == len(s)` (otherwise it can't be a rotation), and
  2. `goal in (s + s)` (Python's `in` does the substring scan).
- Both checks are required — without the length guard, a shorter `goal` could falsely match a substring of `s + s`.

---

## 💻 Code

```python
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
      n = len(s)
      s = s + s      
      if goal in s and len(goal) == n:
        return True
      return False
```

---

## 🧠 Dry Run

### Input
```
s = "abcde", goal = "cdeab"
```

### Steps
```
n        = 5
s + s    = "abcdeabcde"
goal in (s + s)?  →  "cdeab" appears at index 2 → True
len(goal) == n ?  →  5 == 5 → True
return True
```

### Counter-example
```
s = "abcde", goal = "abced"
s + s = "abcdeabcde"
"abced" in "abcdeabcde" → False
return False
```

---

## ⏱️ Time Complexity

```
O(n²)   in the worst case for Python's `in` on strings
        (CPython uses a tuned two-way / Boyer-Moore-Horspool variant,
         giving close to O(n) on typical inputs)
```

The string concatenation `s + s` is O(n), and the substring search is at most O(n²).

---

## 💾 Space Complexity

```
O(n)
```

For the doubled string `s + s`.

---

## ⚠️ Edge Cases

- **Different lengths:** `s = "abc"`, `goal = "abcd"` → length guard rejects immediately. Without the `len(goal) == n` check, a shorter `goal` like `"ab"` would falsely match inside `s + s = "abcabc"`.
- **Identical strings:** `s == goal` → `goal` appears at index 0 of `s + s`, returns `True` (zero rotation counts).
- **Single character:** `s = "a"`, `goal = "a"` → `"a" in "aa"` is `True`.
- **Empty edge:** constraints guarantee length ≥ 1, so empty strings are not a concern.
- **Order of checks:** placing `len(goal) == n` **before** the substring search would short-circuit on length mismatch and avoid the O(n²) scan.

---

## 🎯 Interview Takeaways

- The `s + s` trick collapses "is this a rotation?" into one substring lookup — worth memorizing.
- For O(n) worst-case, swap Python's `in` for KMP / Z-algorithm on the doubled string.
- Always pair the substring check with a length check; the trick assumes equal lengths.

---

## 📌 Key Pattern

👉 **"All rotations of a string live inside `s + s`, so rotation queries become substring queries."**

---

## 🔁 Related Problems

- 28. Find the Index of the First Occurrence in a String
- 686. Repeated String Match
- 1668. Maximum Repeating Substring
- 459. Repeated Substring Pattern

---

## 🚀 Final Thoughts

Rotate String is a classic "doubling trick" warm-up. Once you see that every rotation of `s` is a window inside `s + s`, the entire problem collapses to one `in` check plus a length guard. The same idea (`A + A` contains all rotations of `A`) shows up in cyclic-array problems and string-matching variants.

---

✨ **Rule to remember:**
> "When a problem mentions rotations of a string or array, double it — every rotation becomes a contiguous slice."
