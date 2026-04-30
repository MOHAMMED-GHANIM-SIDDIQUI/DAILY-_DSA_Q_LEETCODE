# 3085. Minimum Deletions to Make String K-Special

## 🔗 Problem Link
https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/

## ⚡ Difficulty
Medium

## 🏷️ Topics
String, Greedy, Sorting, Counting, Hash Table

---

## 🧩 Problem Summary
Given a string `word` and an integer `k`, find the minimum number of character deletions needed so that the difference between the maximum and minimum frequency of any two characters in the string is at most k. Characters with zero frequency after deletion are ignored.

### 📌 Constraints
- 1 <= word.length <= 10^5
- 0 <= k <= 10^5
- word consists of only lowercase English letters

---

## 💭 Intuition
👉 Try each character's frequency as the minimum allowed frequency. For each candidate, either delete all characters with lower frequency or trim characters exceeding minFreq + k.

---

## ⚡ Approach — Enumerate Minimum Frequency

### 🧠 Idea
- Count frequency of each character
- For each possible minimum frequency (from the existing counts), calculate deletions needed
- Characters below the minimum: delete all of them
- Characters above minimum + k: delete the excess
- Return the minimum deletions across all choices

---

## 💻 Code

```cpp
class Solution {
 public:
  int minimumDeletions(string word, int k) {
    int ans = INT_MAX;
    vector<int> count(26);

    for (const char c : word)
      ++count[c - 'a'];

    for (const int minFreq : count) {
      int deletions = 0;
      for (const int freq : count)
        if (freq < minFreq)  // Delete all the letters with smaller frequency.
          deletions += freq;
        else  // Delete letters with exceeding frequency.
          deletions += max(0, freq - (minFreq + k));
      ans = min(ans, deletions);
    }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
word = "aabcaba", k = 1
```
### Steps
```
count: a=4, b=2, c=1, rest=0
Try minFreq=4: delete b(2)+c(1)=3, trim a: max(0,4-5)=0 -> 3
Try minFreq=2: delete c(1), trim a: max(0,4-3)=1 -> 2
Try minFreq=1: trim a: max(0,4-2)=2, trim b: max(0,2-2)=0 -> 2
Try minFreq=0: trim a: max(0,4-1)=3, trim b: max(0,2-1)=1, trim c: max(0,1-1)=0 -> 4
ans = 2
```

---

## ⏱️ Time Complexity
```
O(n + 26^2) = O(n) — count frequencies in O(n), enumerate 26 candidates x 26 checks
```

## 💾 Space Complexity
```
O(1) — fixed-size frequency array of 26
```

---

## ⚠️ Edge Cases
- All characters have the same frequency — 0 deletions needed
- k = 0 — all remaining characters must have the same frequency
- String with only one distinct character — always 0 deletions

---

## 🎯 Interview Takeaways
- Enumerating over each existing frequency as the "floor" is a clean greedy approach
- Only 26 possible candidate floors makes this efficient despite the enumeration
- No sorting needed — just iterate through all 26 possibilities

---

## 📌 Key Pattern
👉 **"Enumerate the minimum allowed frequency and compute cost for each"**

---

## 🔁 Related Problems
- 1647. Minimum Deletions to Make Character Frequencies Unique
- 2516. Take K of Each Character From Left and Right
- 1838. Frequency of the Most Frequent Element

---

## 🚀 Final Thoughts
The problem reduces to choosing the right "floor" frequency. Since there are only 26 letters, trying each frequency value from the count array and computing the deletion cost is both simple and optimal.

---

✨ **Rule to remember:**
> Try each existing frequency as the minimum; delete below, trim above — pick the cheapest.
