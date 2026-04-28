# 761. Special Binary String

## 🔗 Problem Link
https://leetcode.com/problems/special-binary-string/

## ⚡ Difficulty
Hard

## 🏷️ Topics
String, Recursion, Sorting

---

## 🧩 Problem Summary

A special binary string is a binary string with two properties: the number of 0s equals the number of 1s, and every prefix has at least as many 1s as 0s (like balanced parentheses with `1` = `(` and `0` = `)`). Given a special binary string `s`, make any number of swaps of consecutive special substrings and return the lexicographically largest result.

### 📌 Constraints
- `1 <= s.length <= 50`
- `s[i]` is either `'0'` or `'1'`
- `s` is a special binary string

---

## 💭 Intuition

Think of `1` as `(` and `0` as `)`. A special binary string is like a valid parentheses expression. 👉 We can decompose it into top-level special substrings (analogous to top-level balanced parentheses groups), recursively optimize each group's interior, and then sort the groups in descending order for the lexicographically largest result.

---

## ⚡ Approach — Recursive Decomposition + Sorting

### 🧠 Idea

- Traverse the string tracking a counter (increment for `1`, decrement for `0`).
- When the counter hits 0, we found a complete special substring from index `i` to `j`.
- Recursively optimize the inner portion `s[i+1:j]` (strip the outer `1` and `0`).
- Collect all top-level special substrings, sort them in descending order, and concatenate.

---

## 💻 Code

```python
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        res = []
        i = 0  # start index of current special substring

        for j, char in enumerate(s):
            if char == '1':
                count += 1
            else:
                count -= 1

            # When count == 0, we found a special substring
            if count == 0:
                # Recursively optimize the middle part
                middle_optimized = self.makeLargestSpecial(s[i + 1:j])
                # Add the optimized special substring
                res.append('1' + middle_optimized + '0')
                i = j + 1

        # Sort substrings in descending order to get lexicographically largest
        res.sort(reverse=True)

        return "".join(res)
```

---

## 🧠 Dry Run

### Input
```
s = "11011000"
```

### Steps
```
j=0: char='1', count=1
j=1: char='1', count=2
j=2: char='0', count=1
j=3: char='1', count=2
j=4: char='1', count=3
j=5: char='0', count=2
j=6: char='0', count=1
j=7: char='0', count=0 → special substring s[0:8]
  Recurse on "101100":
    j=0:'1' count=1, j=1:'0' count=0 → "10", recurse on "" → "1"+""+"0" = "10"
    j=2:'1' count=1, j=3:'1' count=2, j=4:'0' count=1, j=5:'0' count=0 → "1100"
      Recurse on "10" → "10"
      → "1" + "10" + "0" = "1100"
    res = ["10", "1100"] → sort desc → ["1100", "10"]
    → "110010"
  → "1" + "110010" + "0" = "11100100"
Result: "11100100"
```

---

## ⏱️ Time Complexity

```
O(n^2)
```

In the worst case, each recursive call processes a portion of the string and sorting is done at each level.

---

## 💾 Space Complexity

```
O(n^2)
```

Due to recursive calls and substring creation at each level.

---

## ⚠️ Edge Cases

- **Already optimal:** `"10"` → `"10"` (single minimal special string)
- **Deeply nested:** `"11110000"` → `"11110000"` (only one top-level group, recursion simplifies the interior)
- **Multiple top-level groups:** `"1010"` → `"1010"` (already in descending order)

---

## 🎯 Interview Takeaways

- Mapping `1` to `(` and `0` to `)` reveals the parentheses structure.
- Recursive decomposition is a powerful technique for structured string problems.
- Sorting substrings in descending order produces the lexicographically largest result.
- Understanding the connection between special binary strings and balanced parentheses is the key insight.

---

## 📌 Key Pattern

👉 **"Recursive decomposition of balanced parentheses-like structures with greedy sorting"**

---

## 🔁 Related Problems

- 22. Generate Parentheses
- 856. Score of Parentheses
- 1190. Reverse Substrings Between Each Pair of Parentheses

---

## 🚀 Final Thoughts

This is an elegant recursion problem disguised as a string manipulation task. Recognizing the parentheses analogy and applying divide-and-conquer with sorting makes the solution both concise and powerful.

---

✨ **Rule to remember:**
> Special binary strings are balanced parentheses in disguise — decompose, recurse, sort descending.
