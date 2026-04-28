# 2131. Longest Palindrome by Concatenating Two Letter Words

## 🔗 Problem Link
https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Hash Table, String, Greedy, Counting

---

## 🧩 Problem Summary
Given an array of two-letter strings `words`, find the longest palindrome that can be formed by selecting some words and concatenating them. Each word can be used at most once. Return the length of the longest palindrome.

### 📌 Constraints
- `1 <= words.length <= 10^5`
- `words[i].length == 2`
- `words[i]` consists of lowercase English letters

---

## 💭 Intuition
👉 A word and its reverse can be placed symmetrically. For palindromic words (like "aa"), one unpaired instance can go in the center.

---

## ⚡ Approach — Greedy Pairing with Count Matrix

### 🧠 Idea
- Use a 26x26 count matrix for two-letter words.
- For each word `(i, j)`, check if its reverse `(j, i)` has been seen. If yes, pair them (add 4 to answer). If no, increment `count[i][j]`.
- After processing all words, check if any palindromic word `(i, i)` remains unpaired; if so, add 2 for the center.

---

## 💻 Code

```cpp
class Solution {
 public:
  int longestPalindrome(vector<string>& words) {
    int ans = 0;
    vector<vector<int>> count(26, vector<int>(26));

    for (const string& word : words) {
      const int i = word[0] - 'a';
      const int j = word[1] - 'a';
      if (count[j][i]) {
        ans += 4;
        --count[j][i];
      } else {
        ++count[i][j];
      }
    }

    for (int i = 0; i < 26; ++i)
      if (count[i][i])
        return ans + 2;

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
words = ["lc","cl","gg"]
```
### Steps
```
Process "lc": count[11][2]=0, no reverse -> count[11][2]=1
Process "cl": count[11][2]>0 -> ans+=4=4, count[11][2]=0
Process "gg": count[6][6]=0, no reverse -> count[6][6]=1
Check palindromic: count[6][6]=1 > 0 -> return 4+2=6
```

---

## ⏱️ Time Complexity
```
O(n), where n is the number of words
```

## 💾 Space Complexity
```
O(1) -- 26x26 matrix is constant size
```

---

## ⚠️ Edge Cases
- All words are the same palindromic word (e.g., "aa"): pairs contribute 4 each, one leftover adds 2
- No pairs possible: answer may be just 2 (single palindromic word) or 0
- All words are reverses of each other: n/2 pairs, each contributing 4

---

## 🎯 Interview Takeaways
- Two-letter words simplify to a 26x26 pairing problem.
- Palindromic words (same two letters) can serve as the center of the palindrome.
- Greedy pairing in a single pass is optimal.

---

## 📌 Key Pattern
👉 **"Pair words with their reverses; use unpaired palindromic word as center"**

---

## 🔁 Related Problems
- 409. Longest Palindrome
- 336. Palindrome Pairs
- 1177. Can Make Palindrome from Substring

---

## 🚀 Final Thoughts
This problem combines palindrome construction with greedy pairing. The 26x26 matrix is a clean alternative to hash maps for two-letter words, and the center-word check is a nice detail that many miss.

---

✨ **Rule to remember:**
> Pair each word with its reverse for +4 length; one unpaired palindromic word can sit in the center for +2.
