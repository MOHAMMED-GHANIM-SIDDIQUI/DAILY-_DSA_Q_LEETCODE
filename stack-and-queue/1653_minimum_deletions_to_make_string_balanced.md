# 1653. Minimum Deletions to Make String Balanced

## 🔗 Problem Link
https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

## ⚡ Difficulty
Medium

## 🏷️ Topics
String, Dynamic Programming, Stack

---

## 🧩 Problem Summary
Given a string `s` consisting only of characters `'a'` and `'b'`, return the minimum number of deletions needed to make `s` balanced. A string is balanced if no `'b'` appears before an `'a'`.

### 📌 Constraints
- `1 <= s.length <= 10^5`
- `s[i]` is `'a'` or `'b'`

---

## 💭 Intuition
👉 Every "ba" pair (a `'b'` followed later by an `'a'`) is a conflict. Using a stack, whenever we see an `'a'` and the top of the stack is `'b'`, we remove the `'b'` and skip the `'a'` — each such removal costs one deletion.

---

## ⚡ Approach — Stack-Based Greedy

### 🧠 Idea
- Iterate through the string, maintaining a stack.
- If the current character is `'a'` and the stack's top is `'b'`, pop the `'b'` and increment the deletion counter (we "delete" one of the pair).
- Otherwise, push the current character onto the stack.
- The final count is the minimum deletions.

---

## 💻 Code

```python
class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack = []
        ans = 0

        for c in s:
            if stack and stack[-1] == 'b' and c == 'a':
                ans += 1
                stack.pop()   # delete the 'b'
                # skip pushing 'a'
            else:
                stack.append(c)

        return ans
```

---

## 🧠 Dry Run
### Input
```
s = "aababbab"
```
### Steps
```
i=0, c='a': stack=['a']
i=1, c='a': stack=['a','a']
i=2, c='b': stack=['a','a','b']
i=3, c='a': top='b', c='a' → pop 'b', ans=1, stack=['a','a']
i=4, c='b': stack=['a','a','b']
i=5, c='b': stack=['a','a','b','b']
i=6, c='a': top='b', c='a' → pop 'b', ans=2, stack=['a','a','b']
i=7, c='b': stack=['a','a','b','b']

Result: 2
```

---

## ⏱️ Time Complexity
```
O(n) — single pass through the string
```

## 💾 Space Complexity
```
O(n) — stack can hold up to n characters in the worst case
```

---

## ⚠️ Edge Cases
- String is already balanced (e.g., "aaabbb") → 0 deletions.
- All `'b'`s come before all `'a'`s (e.g., "bbaa") → maximum conflicts.
- Single character string → always balanced.

---

## 🎯 Interview Takeaways
- Stack-based approaches are powerful for problems involving matching or cancelling pairs.
- This is analogous to matching parentheses — `'b'` before `'a'` is like an unmatched bracket.
- The greedy choice of removing the earliest `'b'` conflict is optimal.

---

## 📌 Key Pattern
👉 **"Use a stack to greedily cancel conflicting 'ba' pairs"**

---

## 🔁 Related Problems
- 20. Valid Parentheses
- 1249. Minimum Remove to Make Valid Parentheses
- 2124. Check if All A's Appears Before All B's

---

## 🚀 Final Thoughts
An elegant stack solution that treats "ba" pairs as conflicts to resolve. Each conflict costs exactly one deletion, and greedily resolving them left-to-right yields the optimal answer.

---

✨ **Rule to remember:**
> Every time a `'b'` on the stack meets an incoming `'a'`, one deletion resolves the conflict — cancel them greedily.
