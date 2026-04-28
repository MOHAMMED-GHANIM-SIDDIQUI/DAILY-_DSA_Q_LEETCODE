# 1061. Lexicographically Smallest Equivalent String

## 🔗 Problem Link
https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

## ⚡ Difficulty
Medium

## 🏷️ Topics
String, Union-Find

---

## 🧩 Problem Summary

Given two strings `s1` and `s2` of equal length that define character equivalence relations, and a string `baseStr`, return the lexicographically smallest equivalent string of `baseStr` using the equivalence information from `s1` and `s2`.

### 📌 Constraints
- `1 <= s1.length, s2.length, baseStr.length <= 1000`
- `s1.length == s2.length`
- Strings consist of lowercase English letters.

---

## 💭 Intuition

👉 Equivalent characters form groups. Within each group, we want to map every character to the lexicographically smallest one.

👉 Union-Find is perfect here — always attach the larger character under the smaller one so the root of each group is the smallest character.

---

## ⚡ Approach — Union-Find with Smallest Root

### 🧠 Idea
- Create a Union-Find over 26 characters.
- For each pair `(s1[i], s2[i])`, union them, always making the smaller character the root.
- For each character in `baseStr`, find its root (smallest equivalent character) and use that.

---

## 💻 Code

```cpp
class UnionFind {
 public:
  UnionFind(int n) : id(n) {
    iota(id.begin(), id.end(), 0);
  }

  void union_(int u, int v) {
    const int i = find(u);
    const int j = find(v);
    if (i > j)
      id[i] = j;
    else
      id[j] = i;
  }

  int find(int u) {
    return id[u] == u ? u : id[u] = find(id[u]);
  }

 private:
  vector<int> id;
};

class Solution {
 public:
  string smallestEquivalentString(string s1, string s2, string baseStr) {
    string ans;
    UnionFind uf(26);

    for (int i = 0; i < s1.length(); ++i)
      uf.union_(s1[i] - 'a', s2[i] - 'a');

    for (const char c : baseStr)
      ans += 'a' + uf.find(c - 'a');

    return ans;
  }
};
```

---

## 🧠 Dry Run

### Input
```
s1 = "abc", s2 = "bcd", baseStr = "eed"
```

### Steps
```
Union operations:
  union(a, b) → root of {a,b} = a
  union(b, c) → root of {a,b,c} = a
  union(c, d) → root of {a,b,c,d} = a

Process baseStr "eed":
  'e' → find(e) = e → 'e'
  'e' → find(e) = e → 'e'
  'd' → find(d) = a → 'a'

Output: "eea"
```

---

## ⏱️ Time Complexity
```
O(n + m)
```
Where `n` is the length of `s1`/`s2` and `m` is the length of `baseStr`. Union-Find operations are nearly O(1) with path compression.

---

## 💾 Space Complexity
```
O(1)
```
The Union-Find uses a fixed array of size 26 (constant).

---

## ⚠️ Edge Cases
- `s1` and `s2` are identical → no new equivalences, return `baseStr` unchanged.
- All characters map to 'a' → every character in result is 'a'.
- `baseStr` contains characters not in `s1` or `s2` → they remain unchanged.

---

## 🎯 Interview Takeaways
- Union-Find with a "smaller root wins" policy naturally produces the lexicographically smallest representative.
- Path compression keeps find operations efficient.
- This is a clean application of Union-Find to equivalence classes.
- Fixed-size Union-Find (26 letters) means constant space.

---

## 📌 Key Pattern
👉 **"Union-Find with smallest-root policy to find the lexicographically smallest representative in each equivalence class."**

---

## 🔁 Related Problems
- 990 - Satisfiability of Equality Equations
- 721 - Accounts Merge
- 547 - Number of Provinces

---

## 🚀 Final Thoughts
A textbook Union-Find problem where the twist is always making the smaller element the root. This elegant invariant ensures we get the smallest equivalent character in O(1) per query.

---

✨ **Rule to remember:**
> "When you need the smallest equivalent, make Union-Find always root at the smallest element."
