# 2014. Longest Subsequence Repeated k Times

## 🔗 Problem Link
https://leetcode.com/problems/longest-subsequence-repeated-k-times/

## ⚡ Difficulty
Hard

## 🏷️ Topics
String, Backtracking, Greedy, Counting, Enumeration

---

## 🧩 Problem Summary
Given a string `s` and an integer `k`, find the longest subsequence `seq` of `s` such that `seq` repeated `k` times is a subsequence of `s`. If multiple answers exist, return the lexicographically largest one.

### 📌 Constraints
- `n == s.length`
- `2 <= n <= 8`
- `2 <= k <= 2000`
- `s` consists of lowercase English letters

---

## 💭 Intuition
👉 Since `n` is very small (up to 8), we can use BFS to enumerate all possible subsequences level by level (by length), checking each against `s`. Characters appearing fewer than `k` times cannot be in the answer.

---

## ⚡ Approach — BFS Enumeration with Pruning

### 🧠 Idea
- Count character frequencies; only characters appearing >= `k` times are candidates.
- BFS from empty string, appending one candidate character at a time.
- For each new subsequence, verify it repeats `k` times as a subsequence of `s`.
- Since BFS explores by increasing length and we try characters in order, the last valid result found is the answer (longest, and lexicographically largest due to BFS order).

---

## 💻 Code

```cpp
class Solution {
 public:
  string longestSubsequenceRepeatedK(string s, int k) {
    string ans;
    vector<int> count(26);
    vector<char> possibleChars;
    // Stores subsequences, where the length grows by 1 each time.
    queue<string> q{{""}};

    for (const char c : s)
      ++count[c - 'a'];

    for (char c = 'a'; c <= 'z'; ++c)
      if (count[c - 'a'] >= k)
        possibleChars.push_back(c);

    while (!q.empty()) {
      const string currSubseq = q.front();
      q.pop();
      if (currSubseq.length() * k > s.length())
        return ans;
      for (const char c : possibleChars) {
        const string& newSubseq = currSubseq + c;
        if (isSubsequence(newSubseq, s, k)) {
          q.push(newSubseq);
          ans = newSubseq;
        }
      }
    }

    return ans;
  }

 private:
  bool isSubsequence(const string& subseq, string& s, int k) {
    int i = 0;  // subseq's index
    for (const char c : s)
      if (c == subseq[i])
        if (++i == subseq.length()) {
          if (--k == 0)
            return true;
          i = 0;
        }
    return false;
  }
};
```

---

## 🧠 Dry Run
### Input
```
s = "letsleetcode", k = 2
```
### Steps
```
Count: l=2, e=3, t=2, s=1, c=1, o=1, d=1
possibleChars (freq >= 2): ['e', 'l', 't']
BFS level 0: ""
  Try "e" -> is "ee" subseq of s? Yes -> push, ans="e"
  Try "l" -> is "ll" subseq of s? Yes -> push, ans="l"
  Try "t" -> is "tt" subseq of s? Yes -> push, ans="t"
BFS level 1: "e", "l", "t"
  "e" + 'e' = "ee" -> is "eeee" subseq? No
  "e" + 'l' = "el" -> is "elel" subseq? No
  "e" + 't' = "et" -> is "etet" subseq? Yes -> push, ans="et"
  ...
Result: "et"
```

---

## ⏱️ Time Complexity
```
O(26^(n/k) * n) in the worst case, but pruning makes it much faster for small n
```

## 💾 Space Complexity
```
O(26^(n/k)) for the BFS queue
```

---

## ⚠️ Edge Cases
- No character appears >= k times: return empty string
- `s` length exactly `k`: answer is at most 1 character
- All characters the same: answer is `s.length / k` copies of that character

---

## 🎯 Interview Takeaways
- BFS naturally explores subsequences by increasing length.
- Pruning via character frequency drastically reduces the search space.
- The `isSubsequence` helper checks if a pattern repeats k times as a subsequence in one pass.

---

## 📌 Key Pattern
👉 **"BFS enumeration of subsequences with frequency-based pruning"**

---

## 🔁 Related Problems
- 392. Is Subsequence
- 1143. Longest Common Subsequence
- 686. Repeated String Match

---

## 🚀 Final Thoughts
The small constraint on `n` makes brute-force BFS feasible. The key optimization is filtering to only characters with frequency >= k, and the elegant subsequence-repeat check in a single linear scan of `s`.

---

✨ **Rule to remember:**
> When n is tiny, BFS over all possible subsequences with smart pruning can solve even "hard" problems efficiently.
