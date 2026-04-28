# 1625. Lexicographically Smallest String After Applying Operations

## 🔗 Problem Link
https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/

## ⚡ Difficulty
Medium

## 🏷️ Topics
String, Breadth-First Search, Depth-First Search

---

## 🧩 Problem Summary
Given a string `s` of even length consisting of digits, and two integers `a` and `b`, you can apply two operations any number of times: (1) add `a` to all odd-indexed digits (mod 10), or (2) rotate the string right by `b` positions. Return the lexicographically smallest string achievable.

### 📌 Constraints
- `2 <= s.length <= 100`
- `s.length` is even
- `s` consists of digits `0-9`
- `1 <= a <= 9`
- `1 <= b <= s.length - 1`

---

## 💭 Intuition
👉 Since the string length is at most 100, the total number of distinct strings reachable is bounded. We can explore all reachable states using DFS/BFS and track the lexicographic minimum.

---

## ⚡ Approach — DFS with Memoization

### 🧠 Idea
- Use DFS to explore all reachable strings from the initial state.
- At each state, try both operations: add `a` to odd-indexed digits, or rotate by `b`.
- Use a set to avoid revisiting the same string.
- Track the global minimum string encountered.

---

## 💻 Code

```cpp
class Solution {
 public:
  string findLexSmallestString(string s, int a, int b) {
    string ans = s;

    dfs(s, a, b, {}, ans);

    return ans;
  }

 private:
  void dfs(string s, int a, int b, unordered_set<string>&& seen, string& ans) {
    if (seen.contains(s))
      return;

    seen.insert(s);
    ans = min(ans, s);

    dfs(add(s, a), a, b, std::move(seen), ans);
    dfs(rotate(s, b), a, b, std::move(seen), ans);
  }

  string add(string& s, int a) {
    for (int i = 1; i < s.length(); i += 2)
      s[i] = '0' + (s[i] - '0' + a) % 10;
    return s;
  }

  string rotate(const string& s, int b) {
    const int n = s.length();
    return s.substr(n - b, n) + s.substr(0, n - b);
  }
};
```

---

## 🧠 Dry Run
### Input
```
s = "5525", a = 9, b = 2
```
### Steps
```
Start: "5525"
Add 9 to odd indices: "5425" → "5325" → ... → "5025"
Rotate by 2: "2550", "5025" → ...
DFS explores all combinations.
Minimum found: "2050"
```

---

## ⏱️ Time Complexity
```
O(N * 10 * N) where N = s.length — bounded number of unique states (at most N rotations × 10 add cycles)
```

## 💾 Space Complexity
```
O(N * 10 * N) — for storing all visited strings in the set
```

---

## ⚠️ Edge Cases
- `a = 0` → add operation has no effect; only rotations matter.
- `b = s.length` → rotation has no effect; only add operations matter.
- String is already the smallest possible.

---

## 🎯 Interview Takeaways
- When the state space is small and bounded, brute-force DFS/BFS is perfectly valid.
- The key insight is recognising the finite cycle: adding `a` mod 10 cycles through at most 10 values, and rotating cycles through at most `n` positions.
- Using a set for deduplication keeps the search efficient.

---

## 📌 Key Pattern
👉 **"Explore all reachable states via DFS/BFS when the state space is provably bounded"**

---

## 🔁 Related Problems
- 752. Open the Lock
- 854. K-Similar Strings
- 1040. Moving Stones Until Consecutive II

---

## 🚀 Final Thoughts
This problem rewards recognising that the state space is small enough for exhaustive search. The combination of rotation and digit addition creates a finite group of strings, and DFS with memoization efficiently finds the minimum.

---

✨ **Rule to remember:**
> When operations cycle through a finite set of states, just explore them all and pick the best.
