# 3043. Find the Length of the Longest Common Prefix

## 🔗 Problem Link
https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Hash Table, String, Trie

---

## 🧩 Problem Summary
Given two integer arrays `arr1` and `arr2`, a **common prefix** of two integers `x` and `y` is an integer that is a prefix of **both** `x` and `y` (digits read left to right; e.g. `123` and `12345` share prefixes `1`, `12`, `123`). Return the **length** of the longest common prefix among **all pairs** `(x, y)` with `x ∈ arr1`, `y ∈ arr2`. If no common prefix exists, return `0`.

### 📌 Constraints
- `1 <= arr1.length, arr2.length <= 5 * 10^4`
- `1 <= arr1[i], arr2[i] <= 10^8`

---

## 💭 Intuition
A "prefix of a number" is just the number you get by chopping digits off the **right** end: `12345 → 1234 → 123 → 12 → 1`. So every integer generates `O(9)` prefixes (numbers up to `10^8` have ≤ 9 digits).

Comparing all pairs directly is `5·10⁴ × 5·10⁴ = 2.5·10⁹` — too slow. Instead, **precompute every prefix of every number in `arr1` into a hash set**. Then for each number in `arr2`, peel its digits from the right and check the set; the first (longest) prefix that's present gives a candidate answer. Take the max length over all of `arr2`.

A Trie of `arr1`'s prefixes would also work (hence the tag), but a hash set of integers is simpler and just as fast here because each number has at most 9 prefixes.

---

## ⚡ Approach — Prefix hash set

### 🧠 Idea
1. For every `x` in `arr1`, repeatedly add `x` to the set and do `x //= 10`, until `x` becomes `0`. This stores **all** prefixes of `x`.
2. For every `x` in `arr2`, peel from the right (`x //= 10`); the **first** value found in the set is the longest common prefix for that number — record `len(str(x))` and stop peeling.
3. Return the maximum length seen (0 if none).

### 🔑 Why peel right-to-left for arr2
We want the **longest** matching prefix per number. Starting from the full number and shrinking means the first hit is the longest possible, so we can `break` immediately.

---

## 💻 Code

```python
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()

        # Store every prefix from arr1
        for x in arr1:
            while x:
                prefixes.add(x)
                x //= 10

        ans = 0

        # Check prefixes of arr2 numbers
        for x in arr2:
            while x:
                if x in prefixes:
                    ans = max(ans, len(str(x)))
                    break
                x //= 10

        return ans
```

---

## 🧠 Dry Run
### Input
```
arr1 = [1, 10, 100]
arr2 = [1000]
```

### Build set from arr1
```
1   → {1}
10  → {1, 10}
100 → {1, 10, 100}
prefixes = {1, 10, 100}
```

### Query 1000
```
x=1000 in set? no
x=100  in set? yes → len("100") = 3 → break
```
Answer: `3`.

### No-match example
```
arr1=[1], arr2=[2]: peel 2 → not in {1} → 0
```

---

## ⏱️ Time Complexity
```
O((m + n) · D)   — D ≤ 9 digits per number; m, n are the array sizes.
                   Effectively linear.
```

## 💾 Space Complexity
```
O(m · D)   — every prefix of every arr1 number in the hash set.
```

---

## ⚠️ Edge Cases
- **No common prefix anywhere** → `ans` stays `0`.
- **Equal numbers** (`arr1=[123]`, `arr2=[123]`) → full number matches → length `3`.
- **One number is a prefix of another** (`12` and `12345`) → matches at `12` → length `2`.
- Single-digit overlaps still count (e.g. both contain numbers starting with `5`).

---

## 🎯 Interview Takeaways
- Turning "digit prefix" into integer division by 10 avoids string slicing entirely on the build side.
- The hash-set-of-prefixes trick is the pragmatic alternative to a Trie when the alphabet is tiny (10 digits) and depth is bounded (≤ 9).
- Right-to-left peeling on the query side gives an immediate `break` on the longest match — don't go left-to-right or you can't early-exit cleanly.

---

## 📌 Key Pattern
👉 **"Digit prefixes = repeated `// 10`. Hash every source prefix, then peel each target from the longest end and take the first hit."**

---

## 🔁 Related Problems
- 14. Longest Common Prefix
- 208. Implement Trie (Prefix Tree)
- 3093. Longest Common Suffix Queries
- 1233. Remove Sub-Folders from the Filesystem

---

## 🚀 Final Thoughts
This is "Longest Common Prefix" generalised from strings to integers and from one pair to a cross product of two arrays. The cross product looks scary until you realise prefixes are few (≤ 9 per number) and a hash set collapses the pairwise comparison into two linear sweeps.

---

✨ **Rule to remember:**
> A numeric prefix is just `n // 10` applied repeatedly. Precompute one side's prefixes into a set; the cross-product comparison melts into linear time.
