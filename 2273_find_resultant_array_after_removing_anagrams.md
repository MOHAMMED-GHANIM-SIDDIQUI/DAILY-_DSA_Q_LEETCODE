# 2273. Find Resultant Array After Removing Anagrams

## 🔗 Problem Link
https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, String, Sorting, Hash Table

---

## 🧩 Problem Summary
Given an array of strings `words`, repeatedly remove any word that is an anagram of its left neighbor. Return the resulting array after no more removals can be made. Words are compared only with their immediate left neighbor in the current array.

### 📌 Constraints
- `1 <= words.length <= 100`
- `1 <= words[i].length <= 10`
- `words[i]` consists of lowercase English letters

---

## 💭 Intuition
👉 Group consecutive anagrams together and keep only the first word from each group — similar to removing consecutive duplicates.

---

## ⚡ Approach — Skip Consecutive Anagrams

### 🧠 Idea
- Start from the first word and add it to the result.
- Skip all following words that are anagrams of the current group leader.
- When a non-anagram is found, it becomes the new group leader.

---

## 💻 Code

```cpp
class Solution {
 public:
  vector<string> removeAnagrams(vector<string>& words) {
    vector<string> ans;

    for (int i = 0; i < words.size();) {
      int j = i + 1;
      while (j < words.size() && isAnagram(words[i], words[j]))
        ++j;
      ans.push_back(words[i]);
      i = j;
    }

    return ans;
  }

 private:
  bool isAnagram(const string& a, const string& b) {
    if (a.length() != b.length())
      return false;

    vector<int> count(26);

    for (const char c : a)
      ++count[c - 'a'];

    for (const char c : b)
      --count[c - 'a'];

    return ranges::all_of(count, [](const int c) { return c == 0; });
  }
};
```

---

## 🧠 Dry Run
### Input
```
words = ["abba", "baba", "bbaa", "cd", "cd"]
```
### Steps
```
i=0: "abba" → j=1 "baba" is anagram, j=2 "bbaa" is anagram, j=3 "cd" not anagram
     Add "abba", i=3
i=3: "cd" → j=4 "cd" is anagram, j=5 end
     Add "cd", i=5
Result: ["abba", "cd"]
```

---

## ⏱️ Time Complexity
```
O(n * m) — n words, each up to length m for anagram checking
```

## 💾 Space Complexity
```
O(1) — excluding output; the count array is fixed size 26
```

---

## ⚠️ Edge Cases
- No consecutive anagrams → return original array
- All words are anagrams of each other → return only the first word
- Single word → return it as-is

---

## 🎯 Interview Takeaways
- Anagram detection via character frequency counting is O(m) per pair.
- The "skip consecutive duplicates" pattern applies to anagrams too.
- Sorting each word also works for anagram comparison but modifies data.

---

## 📌 Key Pattern
👉 **"Remove consecutive duplicates (generalized to anagrams) — keep first of each group"**

---

## 🔁 Related Problems
- 49. Group Anagrams
- 242. Valid Anagram
- 26. Remove Duplicates from Sorted Array

---

## 🚀 Final Thoughts
This is essentially the "remove consecutive duplicates" pattern but with anagram equivalence instead of exact equality. The frequency-count approach for anagram checking is clean and efficient.

---

✨ **Rule to remember:**
> "Treat consecutive anagrams like consecutive duplicates — keep the first, skip the rest."
