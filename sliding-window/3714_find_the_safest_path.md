# 3714. Find the Safest Path

## 🔗 Problem Link
https://leetcode.com/problems/find-the-safest-path/

## ⚡ Difficulty
Hard

## 🏷️ Topics
String, Hash Table, Prefix Sum, Sliding Window

---

## 🧩 Problem Summary
Given a string `s` consisting of characters `'a'`, `'b'`, and `'c'`, find the length of the longest balanced substring. A balanced substring is one where every distinct character in the substring appears the same number of times. The solution handles 1-character, 2-character, and 3-character balanced substrings separately.

### 📌 Constraints
- `1 <= len(s) <= 10^5`
- `s` consists only of `'a'`, `'b'`, and `'c'`

---

## 💭 Intuition
👉 Instead of brute-forcing all substrings, split the problem by how many distinct characters appear. For 1 character, count consecutive runs. For 2 characters, use prefix-sum difference maps. For 3 characters, use a 2D difference map keyed on `(countA - countB, countA - countC)`.

---

## ⚡ Approach — Case-Split with Prefix Difference Maps

### 🧠 Idea
- **Case 1 (Single character):** Find the longest run of a single character using a simple counter.
- **Case 2 (Two characters):** For each pair `(a,b)`, `(a,c)`, `(b,c)`, use a helper that tracks `count1 - count2` differences. When the same difference is seen again, the substring between those indices is balanced. Reset on encountering a third character.
- **Case 3 (Three characters):** Track prefix counts of all three characters. Store the first occurrence of each `(diffAB, diffAC)` key. When the same key reappears, the substring between those positions has equal counts of all three.

---

## 💻 Code

```python
class Solution:
    def helper(self, s: str, ch1: str, ch2: str) -> int:
        diffMap = {}
        maxL = 0
        count1 = count2 = 0

        for i, ch in enumerate(s):
            if ch != ch1 and ch != ch2:
                diffMap.clear()
                count1 = count2 = 0
                continue

            if ch == ch1:
                count1 += 1
            if ch == ch2:
                count2 += 1

            if count1 == count2:
                maxL = max(maxL, count1 + count2)

            diff = count1 - count2
            if diff in diffMap:
                maxL = max(maxL, i - diffMap[diff])
            else:
                diffMap[diff] = i

        return maxL

    def longestBalanced(self, s: str) -> int:
        n = len(s)
        maxL = 0

        # ---------- Case 1: Single character ----------
        count = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                count += 1
            else:
                maxL = max(maxL, count)
                count = 1
        maxL = max(maxL, count)

        # ---------- Case 2: Two characters ----------
        maxL = max(maxL, self.helper(s, 'a', 'b'))
        maxL = max(maxL, self.helper(s, 'a', 'c'))
        maxL = max(maxL, self.helper(s, 'b', 'c'))

        # ---------- Case 3: Three characters ----------
        countA = countB = countC = 0
        diffMap = {}

        for i, ch in enumerate(s):
            if ch == 'a':
                countA += 1
            elif ch == 'b':
                countB += 1
            else:
                countC += 1

            if countA == countB == countC:
                maxL = max(maxL, countA + countB + countC)

            diffAB = countA - countB
            diffAC = countA - countC
            key = (diffAB, diffAC)  # tuple faster than string

            if key in diffMap:
                maxL = max(maxL, i - diffMap[key])
            else:
                diffMap[key] = i

        return maxL
```

---

## 🧠 Dry Run
### Input
```
s = "aabbc"
```
### Steps
```
Case 1 (Single char): runs are "aa"=2, "bb"=2, "c"=1 → maxL=2

Case 2 (Two chars):
  helper('a','b'): "aabb" → diff sequence: 1,2,1,0 → at diff=0, count1=count2=2 → len=4 → maxL=4
  helper('a','c'): resets at 'b' chars
  helper('b','c'): resets at 'a' chars

Case 3 (Three chars):
  i=0: A=1,B=0,C=0, key=(1,1) → store
  i=1: A=2,B=0,C=0, key=(2,2) → store
  i=2: A=2,B=1,C=0, key=(1,2) → store
  i=3: A=2,B=2,C=0, key=(0,2) → store
  i=4: A=2,B=2,C=1, key=(0,1) → store

No repeated keys → no 3-char balanced substring found.

Result: 4
```

---

## ⏱️ Time Complexity
```
O(n) — single pass for each case, constant number of cases
```

## 💾 Space Complexity
```
O(n) — for the difference maps storing at most n entries
```

---

## ⚠️ Edge Cases
- String with only one unique character → entire string is balanced
- String with only two unique characters → handled by helper
- Very long alternating patterns like "abcabcabc"
- Empty or single character string

---

## 🎯 Interview Takeaways
- Splitting by number of distinct characters is a powerful technique when the alphabet is small (here, only 3).
- The prefix-sum difference trick (`count1 - count2` stored in a hash map) is the classic approach for "equal count" subarray/substring problems.
- For 3 characters, a 2D difference key `(diffAB, diffAC)` generalizes the idea elegantly.
- Resetting the helper's state when an unwanted character appears correctly isolates contiguous 2-character regions.

---

## 📌 Key Pattern
👉 **"Prefix-sum difference maps — when same difference reappears, the segment between has equal counts."**

---

## 🔁 Related Problems
- 525. Contiguous Array
- 1248. Count Number of Nice Subarrays
- 2067. Number of Equal Count Substrings
- 1371. Find the Longest Substring Containing Vowels in Even Counts

---

## 🚀 Final Thoughts
This solution demonstrates how a small alphabet (size 3) allows case-splitting into manageable sub-problems. The prefix-difference-map technique, originally for binary arrays (LeetCode 525), extends naturally to multiple characters by using tuple keys. The linear time complexity makes this approach highly efficient.

---

✨ **Rule to remember:**
> "For balanced substring problems with a small alphabet, split by distinct count and use prefix-difference maps — same difference means equal frequencies in between."
