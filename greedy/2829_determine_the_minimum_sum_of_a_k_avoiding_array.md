# 2829. Determine the Minimum Sum of a k-Avoiding Array

## 🔗 Problem Link
https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Math, Greedy

---

## 🧩 Problem Summary
Given two integers `n` and `k`, find the minimum possible sum of a k-avoiding array of length `n`. A k-avoiding array is an array of distinct positive integers such that no two elements sum to `k`. Note: The original file contains a solution for problem 2839 (Check if Strings Can be Made Equal With Operations I), but the filename indicates 2829.

### 📌 Constraints
- `1 <= n <= 50`
- `1 <= k <= 50`

---

## 💭 Intuition
👉 The code in the file actually solves a different problem — checking if two 4-character strings can be made equal by swapping characters at even indices with each other and odd indices with each other. Two strings are transformable if their even-indexed characters form the same set and their odd-indexed characters form the same set.

---

## ⚡ Approach — Set Comparison for Even/Odd Positions

### 🧠 Idea
- Extract characters at even indices (0, 2) and odd indices (1, 3) from both strings.
- Compare the sets: if both even sets and both odd sets match, the strings can be made equal.

---

## 💻 Code

```python
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
      even_s1 = set([s1[0],s1[2]])
      even_s2 = set([s2[0],s2[2]])
      odd_s1  = set([s1[1],s1[3]])
      odd_s2  = set([s2[1],s2[3]])
      return even_s1 == even_s2 and odd_s1 == odd_s2
```

---

## 🧠 Dry Run
### Input
```
s1 = "abcd", s2 = "cdab"
```
### Steps
```
even_s1 = {s1[0], s1[2]} = {'a', 'c'}
even_s2 = {s2[0], s2[2]} = {'c', 'a'} = {'a', 'c'}
odd_s1  = {s1[1], s1[3]} = {'b', 'd'}
odd_s2  = {s2[1], s2[3]} = {'d', 'b'} = {'b', 'd'}

even_s1 == even_s2? True
odd_s1 == odd_s2? True

Result: True
```

---

## ⏱️ Time Complexity
```
O(1) — strings are always length 4, constant work.
```

## 💾 Space Complexity
```
O(1) — sets of at most 2 elements.
```

---

## ⚠️ Edge Cases
- Both strings identical: always True.
- Characters at even positions match but odd don't: False.
- Duplicate characters at same parity positions (e.g., s1[0] == s1[2]).

---

## 🎯 Interview Takeaways
- Swaps within parity groups mean only the multiset of characters at each parity matters.
- Using sets works here because strings are length 4 with 2 elements per group.
- For longer strings, you would use sorted tuples or Counter instead of sets.

---

## 📌 Key Pattern
👉 **"Parity-grouped character matching — swaps within a group preserve the group's multiset."**

---

## 🔁 Related Problems
- 1790. Check if One String Swap Can Make Strings Equal
- 859. Buddy Strings
- 2840. Check if Strings Can be Made Equal With Operations II

---

## 🚀 Final Thoughts
A concise solution that leverages the observation that swaps at distance 2 only rearrange characters within even and odd index groups independently. Comparing the character sets at each parity is sufficient for length-4 strings.

---

✨ **Rule to remember:**
> "Swaps at fixed distance partition indices by parity — compare each group independently."
