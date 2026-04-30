# 3403. Find the Lexicographically Largest String From the Box I

## 🔗 Problem Link
https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/

## ⚡ Difficulty
Medium

## 🏷️ Topics
String, Two Pointers, Greedy

---

## 🧩 Problem Summary
Given a string word and an integer numFriends, the string is split into numFriends non-empty parts. You collect all parts into a box and pick the lexicographically largest one. Find the largest possible string you could pick over all possible ways of splitting.

### 📌 Constraints
- 1 <= word.length <= 5 * 10^5
- 1 <= numFriends <= word.length
- word consists of lowercase English letters

---

## 💭 Intuition
👉 The optimal pick starts at the position of the lexicographically largest suffix of word. Its maximum length is word.length - numFriends + 1 (since the other numFriends - 1 parts need at least 1 character each).

---

## ⚡ Approach — Last Substring + Length Limit

### 🧠 Idea
- Find the lexicographically largest suffix of the string (same as LeetCode 1163).
- The maximum possible length of any part is `word.length - numFriends + 1`.
- Return the first `min(suffix.length, maxLen)` characters of this suffix.
- The two-pointer algorithm for last substring runs in O(n) time.

---

## 💻 Code

```cpp
class Solution {
 public:
  string answerString(string word, int numFriends) {
    if (numFriends == 1)
      return word;
    const string s = lastSubstring(word);
    const size_t sz = word.length() - numFriends + 1;
    return s.substr(0, min(s.length(), sz));
  }

 private:
  // Same as 1163. Last Substring in Lexicographical Order
  string lastSubstring(string s) {
    int i = 0;
    int j = 1;
    int k = 0;

    while (j + k < s.length())
      if (s[i + k] == s[j + k]) {
        ++k;
      } else if (s[i + k] > s[j + k]) {
        // Skip s[j..j + k) and advance to s[j + k + 1] to find a possible
        // lexicographically larger substring since s[i..i + k) == s[j..j + k)
        // and s[i + k] > s[j + k).
        j = j + k + 1;
        k = 0;
      } else {
        // Skip s[i..i + k) and advance to s[i + k + 1] or s[j] to find a
        // possible lexicographically larger substring since
        // s[i..i + k) == s[j..j + k) and s[i + k] < s[j + k).
        // Note that it's unnecessary to explore s[i + k + 1..j) if
        // i + k + 1 < j since they are already explored by j.
        i = max(i + k + 1, j);
        j = i + 1;
        k = 0;
      }

    return s.substr(i);
  }
};
```

---

## 🧠 Dry Run
### Input
```
word = "dbca", numFriends = 2
```
### Steps
```
lastSubstring("dbca"):
  i=0, j=1, k=0: s[0]='d' > s[1]='b' → j=2, k=0
  i=0, j=2, k=0: s[0]='d' > s[2]='c' → j=3, k=0
  i=0, j=3, k=0: s[0]='d' > s[3]='a' → j=4, k=0
  j+k=4 >= len=4 → stop
  lastSubstring = "dbca"

sz = 4 - 2 + 1 = 3
Result: "dbc"
```

---

## ⏱️ Time Complexity
```
O(n) — the two-pointer last substring algorithm is linear
```

## 💾 Space Complexity
```
O(n) — for the result substring
```

---

## ⚠️ Edge Cases
- numFriends == 1 → return the entire word
- Word with all identical characters → any substring of max length works
- numFriends == word.length → each part is 1 character, return the largest character

---

## 🎯 Interview Takeaways
- Finding the last (lexicographically largest) substring is a classic two-pointer problem.
- The maximum part length is constrained by needing at least 1 character for each other friend.
- Combining a known algorithm (last substring) with a problem constraint (max length) is a common pattern.

---

## 📌 Key Pattern
👉 **"Last substring in lexicographical order + length constraint"**

---

## 🔁 Related Problems
- 1163. Last Substring in Lexicographical Order
- 761. Special Binary String

---

## 🚀 Final Thoughts
This problem cleverly combines the last-substring algorithm with a length bound derived from the splitting constraint. The two-pointer approach avoids the naive O(n^2) comparison.

---

✨ **Rule to remember:**
> The lexicographically largest part in any split always starts at the position of the largest suffix — just cap its length.
