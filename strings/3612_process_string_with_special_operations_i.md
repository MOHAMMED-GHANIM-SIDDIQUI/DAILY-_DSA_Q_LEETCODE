# 3612. Process String with Special Operations I

## 🔗 Problem Link
https://leetcode.com/problems/process-string-with-special-operations-i/

## ⚡ Difficulty
Medium

## 🏷️ Topics
String, Simulation

---

## 🧩 Problem Summary

Process the string `s` from left to right, maintaining a growing `result` string. A lowercase letter is appended to `result`; `'*'` removes the last character of `result`; `'#'` duplicates `result` (appends a copy of itself); `'%'` reverses `result`. Return the final `result` after processing every character of `s`.

### 📌 Constraints
- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters and the characters `'*'`, `'#'`, `'%'`.
- For this version the resulting string stays small enough to build directly.

---

## 💭 Intuition

👉 Each operation acts directly on the current accumulated string, so you can just simulate them in order with simple Python string operations: append, slice-off-last, repeat-twice, and reverse-slice.

---

## ⚡ Approach — Direct Simulation

### 🧠 Idea
- Start with an empty answer `ans = ""`.
- Walk each character `ch` in `s`:
  - `'*'` → drop the last char with `ans[:-1]`.
  - `'#'` → duplicate via `ans *= 2`.
  - `'%'` → reverse via `ans[::-1]`.
  - otherwise (a letter) → append with `ans += ch`.
- Return `ans` after the full pass.

---

## 💻 Code

```python
class Solution:
    def processStr(self, s: str) -> str:
        ans = ""
        for ch in s:
            if ch == '*':
                ans = ans[:-1]
            elif ch =='#':
                ans*=2
            elif ch=='%':
                ans=ans[::-1]
            else:
                ans+=ch
        return ans
```

---

## 🧠 Dry Run

### Input
```
s = "ab*c%#"
```

### Steps
```
ans = ""
ch='a' (letter)  -> ans = "a"
ch='b' (letter)  -> ans = "ab"
ch='*' (delete)  -> ans = "a"
ch='c' (letter)  -> ans = "ac"
ch='%' (reverse) -> ans = "ca"
ch='#' (double)  -> ans = "caca"

return "caca"
```

---

## ⏱️ Time Complexity
```
O(n * L)
```
For each of the `n` operations, building/copying the current string of length up to `L` costs O(L) (duplication and reversal copy the whole string).

---

## 💾 Space Complexity
```
O(L)
```
The answer string of length up to `L` is held in memory (duplication can grow it).

---

## ⚠️ Edge Cases
- `'*'` on an empty `ans` → `ans[:-1]` on `""` is safely `""` (no error).
- `'#'` on empty `ans` → stays `""`.
- `'%'` on empty or single-char `ans` → unchanged.
- Leading operations before any letter just keep `ans` empty.

---

## 🎯 Interview Takeaways
- Python slicing makes delete-last (`[:-1]`), reverse (`[::-1]`), and duplicate (`*2`) one-liners.
- Slicing the empty string never raises, so no guard is needed for `'*'`.
- This direct approach only works because version I keeps the string size manageable.

---

## 📌 Key Pattern
👉 **"Stateful left-to-right simulation: apply each command to the running accumulator."**

---

## 🔁 Related Problems
- 3614. Process String with Special Operations II
- 2390. Removing Stars From a String
- 1190. Reverse Substrings Between Each Pair of Parentheses

---

## 🚀 Final Thoughts
A straightforward simulation where the trick is mapping each special character to the right Python slice operation. Because the string can only grow to a manageable size in this version, building it explicitly is acceptable — version II removes that luxury and forces index back-tracking.

---

✨ **Rule to remember:**
> "When the final state is small enough, just simulate every operation directly on the running string."
