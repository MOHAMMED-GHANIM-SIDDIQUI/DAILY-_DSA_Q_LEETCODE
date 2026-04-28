# 2573. Find the String with LCP

## 🔗 Problem Link
https://leetcode.com/problems/find-the-string-with-lcp/

## ⚡ Difficulty
Hard

## 🏷️ Topics
String, Dynamic Programming, Greedy, Matrix

---

## 🧩 Problem Summary
Given an `n x n` matrix `lcp` where `lcp[i][j]` equals the length of the longest common prefix between `s[i:]` and `s[j:]` for some unknown string `s`, reconstruct and return `s`. If no valid string exists, return an empty string.

### 📌 Constraints
- `1 <= n <= 1000`
- `0 <= lcp[i][j] <= n - max(i, j)`
- `lcp` is symmetric: `lcp[i][j] == lcp[j][i]`

---

## 💭 Intuition
👉 Build the string greedily: assign the smallest possible character to each position. Two positions must share the same character if `lcp[i][j] > 0`. After constructing a candidate string, verify it by recomputing the LCP matrix and checking equality.

---

## ⚡ Approach — Greedy Construction + Verification

### 🧠 Idea
- Start with character 'a' at position 0. For each subsequent position, check all earlier positions: if `lcp[j][i] > 0`, they must share the same character.
- If no earlier position constrains it, assign the next unused character.
- If more than 26 characters needed, return "".
- Verify by computing the LCP matrix of the candidate string from bottom-right to top-left using DP: `lcp[i][j] = 1 + lcp[i+1][j+1]` if `s[i] == s[j]`, else 0.

---

## 💻 Code

```python
class Solution:
    def longest_common_prefix_matrix(self, s: str):
        n = len(s)
        result = [[0] * n for _ in range(n)]

        # Fill last row and column
        for j in range(n):
            result[n - 1][j] = 1 if s[j] == s[n - 1] else 0
            result[j][n - 1] = 1 if s[j] == s[n - 1] else 0

        # Fill rest
        for i in range(n - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if s[i] == s[j]:
                    result[i][j] = 1 + result[i + 1][j + 1]
                else:
                    result[i][j] = 0

        return result

    def findTheString(self, lcp):
        n = len(lcp)
        result = ['a'] * n

        for i in range(1, n):
            not_equal = [False] * 26
            matched = False

            for j in range(i):
                if lcp[j][i] == 0:
                    not_equal[ord(result[j]) - ord('a')] = True
                else:
                    result[i] = result[j]
                    matched = True
                    break

            if matched:
                continue

            for c in range(26):
                if not not_equal[c]:
                    result[i] = chr(ord('a') + c)
                    break

        result_str = ''.join(result)

        if self.longest_common_prefix_matrix(result_str) == lcp:
            return result_str
        return ""
```

---

## 🧠 Dry Run
### Input
```
lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]
```
### Steps
```
n=4, result = ['a','a','a','a']

i=1: j=0 → lcp[0][1]=0 → not_equal['a']=True. No match.
     Find first available: 'b'. result[1]='b'

i=2: j=0 → lcp[0][2]=2>0 → result[2]='a', matched.

i=3: j=0 → lcp[0][3]=0 → not_equal['a']=True
     j=1 → lcp[1][3]=1>0 → result[3]='b', matched.

result_str = "abab"
Verify LCP matrix of "abab" == given lcp → True

Result: "abab"
```

---

## ⏱️ Time Complexity
```
O(n^2) — both construction and verification require O(n^2) operations.
```

## 💾 Space Complexity
```
O(n^2) — for the LCP verification matrix.
```

---

## ⚠️ Edge Cases
- Needs more than 26 characters: return "".
- Invalid LCP matrix (inconsistent values): detected during verification.
- Single character string (n=1): always valid.

---

## 🎯 Interview Takeaways
- Greedy character assignment with constraint propagation is powerful for string construction.
- Always verify the constructed answer against the input when the construction is heuristic.
- The LCP matrix DP recurrence (`lcp[i][j] = 1 + lcp[i+1][j+1]` if same char) is fundamental.

---

## 📌 Key Pattern
👉 **"Greedy construction + verification: build the lexicographically smallest candidate, then validate."**

---

## 🔁 Related Problems
- 1960. Maximum Product of the Length of Two Palindromic Substrings
- 718. Maximum Length of Repeated Subarray
- 1143. Longest Common Subsequence

---

## 🚀 Final Thoughts
This problem combines greedy string construction with DP-based verification. The greedy step ensures we use the smallest possible alphabet, while the verification step catches any invalid LCP matrices. The LCP matrix computation itself is a useful subroutine to know.

---

✨ **Rule to remember:**
> "Build greedily, verify exhaustively — especially when constructing from constraints."
