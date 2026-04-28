# 744. Find Smallest Letter Greater Than Target

## 🔗 Problem Link
https://leetcode.com/problems/find-smallest-letter-greater-than-target/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Binary Search

---

## 🧩 Problem Summary

Given a sorted array of characters `letters` (in non-decreasing order) and a character `target`, return the smallest character in the array that is strictly greater than `target`. The letters wrap around, so if no such character exists, return the first character.

### 📌 Constraints
- `2 <= letters.length <= 10^4`
- `letters[i]` is a lowercase English letter
- `letters` is sorted in non-decreasing order
- `target` is a lowercase English letter

---

## 💭 Intuition

Since the array is sorted, binary search is the natural approach. 👉 We need to find the leftmost character that is strictly greater than `target`. If no such character exists (target >= all elements), we wrap around to the first element using modulo.

---

## ⚡ Approach — Binary Search (Upper Bound)

### 🧠 Idea

- Use binary search with `l = 0` and `r = len(letters)`.
- Find the first position where `letters[m] > target`.
- If `l` equals `len(letters)`, wrap around using `l % len(letters)`.

---

## 💻 Code

```python
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters)

        while l < r:
            m = (l + r) // 2
            if letters[m] > target:
                r = m
            else:
                l = m + 1

        return letters[l % len(letters)]
```

---

## 🧠 Dry Run

### Input
```
letters = ["c", "f", "j"], target = "d"
```

### Steps
```
l = 0, r = 3
m = 1, letters[1] = 'f' > 'd' → r = 1
l = 0, r = 1
m = 0, letters[0] = 'c' <= 'd' → l = 1
l = 1, r = 1 → loop ends
Return letters[1 % 3] = letters[1] = 'f'
```

---

## ⏱️ Time Complexity

```
O(log n)
```

Standard binary search over the sorted array.

---

## 💾 Space Complexity

```
O(1)
```

Only a few pointer variables are used.

---

## ⚠️ Edge Cases

- **Target greater than all letters:** `letters = ["a","b"], target = "z"` → wraps to `"a"`
- **Target equals largest letter:** `letters = ["a","b","c"], target = "c"` → wraps to `"a"`
- **All letters the same:** `letters = ["a","a"], target = "a"` → wraps to `"a"`

---

## 🎯 Interview Takeaways

- This is essentially finding the upper bound in a sorted array.
- The modulo trick `l % len(letters)` elegantly handles the wrap-around case.
- Binary search boundary conditions (using `len` as right bound, not `len-1`) are critical.

---

## 📌 Key Pattern

👉 **"Upper bound binary search with modular wrap-around"**

---

## 🔁 Related Problems

- 35. Search Insert Position
- 278. First Bad Version
- 702. Search in a Sorted Array of Unknown Size

---

## 🚀 Final Thoughts

A classic binary search problem with a small twist — the wrap-around requirement. Using `l % len(letters)` at the end is a clean way to handle the circular nature.

---

✨ **Rule to remember:**
> When searching for the next greater element in a sorted circular array, binary search + modulo does the trick.
