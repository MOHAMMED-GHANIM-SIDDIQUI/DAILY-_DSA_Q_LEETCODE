# 966. Vowel Spellchecker

## 🔗 Problem Link
https://leetcode.com/problems/vowel-spellchecker/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Hash Table, String

---

## 🧩 Problem Summary

Implement a spellchecker that takes a wordlist and queries. For each query, it returns the correct word using these priority rules: (1) exact match, (2) case-insensitive match, (3) vowel-insensitive match (vowels can be any vowel, case-insensitive). If no match is found, return an empty string.

### 📌 Constraints
- `1 <= wordlist.length, queries.length <= 5000`
- `1 <= wordlist[i].length, queries[i].length <= 7`
- `wordlist[i]` and `queries[i]` consist only of English letters

---

## 💭 Intuition

We need three levels of matching with decreasing strictness. 👉 Build three hash maps: one for exact matches, one for case-insensitive matches (lowercase key), and one for vowel-insensitive matches (vowels replaced with a wildcard). Use `insert` (not `[]`) to keep the first match priority.

---

## ⚡ Approach — Three-Level Hash Map Lookup

### 🧠 Idea

- Build a single map with three types of keys: exact word, lowercased word (prefixed with `$`), and vowel-masked word.
- Use `insert` so only the first word for each key is stored (preserving priority).
- For each query, try exact match, then case-insensitive, then vowel-insensitive.

---

## 💻 Code

```cpp
class Solution {
 public:
  vector<string> spellchecker(vector<string>& wordlist,
                              vector<string>& queries) {
    vector<string> ans;
    unordered_map<string, string> dict;

    for (const string& word : wordlist) {
      dict.insert({word, word});
      dict.insert({lowerKey(word), word});
      dict.insert({vowelKey(word), word});
    }

    for (const string& query : queries)
      if (const auto it = dict.find(query); it != dict.cend())
        ans.push_back(it->second);
      else if (const auto it = dict.find(lowerKey(query)); it != dict.cend())
        ans.push_back(it->second);
      else if (const auto it = dict.find(vowelKey(query)); it != dict.cend())
        ans.push_back(it->second);
      else
        ans.push_back("");

    return ans;
  }

 private:
  string lowerKey(const string& word) {
    string s{"$"};
    for (const char c : word)
      s += tolower(c);
    return s;
  }

  string vowelKey(const string& word) {
    string s;
    for (const char c : word)
      s += isVowel(c) ? '*' : tolower(c);
    return s;
  }

  bool isVowel(char c) {
    static constexpr string_view kVowels = "aeiouAEIOU";
    return kVowels.find(c) != string_view::npos;
  }
};
```

---

## 🧠 Dry Run

### Input
```
wordlist = ["KiTe","kite","hare","Hare"]
queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
```

### Steps
```
Build dict:
  "KiTe" → "KiTe", "$kite" → "KiTe", "k*t*" → "KiTe"
  "kite" → "kite" (exact), "$kite" exists (skip), "k*t*" exists (skip)
  "hare" → "hare", "$hare" → "hare", "h*r*" → "hare"
  "Hare" → "Hare", "$hare" exists (skip), "h*r*" exists (skip)

Query "kite" → exact match "kite"
Query "Kite" → no exact → "$kite" → "KiTe"
Query "KiTe" → exact match "KiTe"
Query "Hare" → exact match "Hare"
Query "HARE" → no exact → "$hare" → "hare"
Query "Hear" → no exact → no "$hear" → "h**r" → "hare"
...
```

---

## ⏱️ Time Complexity

```
O(n * L + q * L)
```

Where n is the wordlist size, q is the number of queries, and L is the average word length.

---

## 💾 Space Complexity

```
O(n * L)
```

For storing up to 3 keys per word in the hash map.

---

## ⚠️ Edge Cases

- **Exact match exists:** Should return the exact match, not a case/vowel variant
- **Multiple case matches:** Return the first one in the wordlist (handled by `insert` semantics)
- **No match at all:** Return empty string

---

## 🎯 Interview Takeaways

- Using different key prefixes/transformations in a single map is a clever way to handle multi-level matching.
- The `$` prefix for lowercase keys prevents collisions with exact keys.
- `insert` (not `operator[]`) preserves the first inserted value, maintaining priority.
- The vowel wildcard pattern (`*`) normalizes vowel variations.

---

## 📌 Key Pattern

👉 **"Multi-level string matching using transformed keys in a single hash map"**

---

## 🔁 Related Problems

- 720. Longest Word in Dictionary
- 676. Implement Magic Dictionary
- 211. Design Add and Search Words Data Structure

---

## 🚀 Final Thoughts

An elegant hash map design problem. The trick of using key transformations (lowercase prefix, vowel masking) to handle different matching levels in a single map is both space-efficient and clean.

---

✨ **Rule to remember:**
> For multi-level string matching, encode each level as a different key transformation in the same hash map.
