# 3170. Lexicographically Minimum String After Removing Stars

## 🔗 Problem Link
https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/

## ⚡ Difficulty
Medium

## 🏷️ Topics
String, Stack, Greedy, Hash Table

---

## 🧩 Problem Summary
Given a string `s` containing lowercase letters and stars ('*'), each star removes the smallest character to its left (choosing the rightmost occurrence if there are ties). Return the resulting string after all stars are processed.

### 📌 Constraints
- 1 <= s.length <= 10^5
- s consists of lowercase English letters and '*'
- The input is guaranteed to be valid (enough characters to remove)

---

## 💭 Intuition
👉 Use 26 buckets (one per letter) storing indices. When encountering a star, pop from the smallest non-empty bucket to remove the lexicographically smallest character closest to the star.

---

## ⚡ Approach — Bucket Stacks

### 🧠 Idea
- Maintain 26 stacks (vectors), one for each letter, storing character indices
- For each character: push its index to the corresponding bucket
- For each star: find the smallest non-empty bucket, pop its last index, mark both positions for removal
- Finally, erase all marked positions

---

## 💻 Code

```cpp
class Solution {
 public:
  string clearStars(string s) {
    string ans = s;
    vector<vector<int>> buckets(26);

    for (int i = 0; i < s.length(); ++i)
      if (s[i] == '*') {
        ans[i] = ' ';
        int j = 0;
        while (buckets[j].empty())
          ++j;
        ans[buckets[j].back()] = ' ', buckets[j].pop_back();
      } else {
        buckets[s[i] - 'a'].push_back(i);
      }

    std::erase(ans, ' ');
    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
s = "aaba*"
```
### Steps
```
i=0 'a': buckets[0]=[0]
i=1 'a': buckets[0]=[0,1]
i=2 'b': buckets[1]=[2]
i=3 'a': buckets[0]=[0,1,3]
i=4 '*': mark ans[4]=' ', smallest bucket=0 -> pop 3, ans[3]=' '
ans = "aab  " -> erase spaces -> "aab"
```

---

## ⏱️ Time Complexity
```
O(n * 26) = O(n) — for each star, scan at most 26 buckets
```

## 💾 Space Complexity
```
O(n) — bucket storage for all character indices
```

---

## ⚠️ Edge Cases
- All characters are the same — stars remove the rightmost one
- Stars at the beginning — no valid characters to remove (guaranteed not to happen)
- String with no stars — return as-is

---

## 🎯 Interview Takeaways
- 26 buckets for character indices is an efficient "priority queue" for fixed alphabet
- Marking and erasing in a second pass avoids index shifting issues
- Using `std::erase` (C++20) for clean removal of marked characters

---

## 📌 Key Pattern
👉 **"Bucket stacks indexed by character for greedy lexicographic removal"**

---

## 🔁 Related Problems
- 1544. Make The String Great
- 316. Remove Duplicate Letters
- 402. Remove K Digits

---

## 🚀 Final Thoughts
The 26-bucket approach elegantly handles the "remove smallest, rightmost tie-break" requirement. It avoids the overhead of a full priority queue while maintaining O(n) time complexity.

---

✨ **Rule to remember:**
> Use 26 letter-indexed stacks to greedily remove the smallest character on each star.
