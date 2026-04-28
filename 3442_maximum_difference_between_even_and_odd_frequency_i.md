# 3442. Maximum Difference Between Even and Odd Frequency I

## 🔗 Problem Link
https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/

## ⚡ Difficulty
Easy

## 🏷️ Topics
String, Hash Table, Counting

---

## 🧩 Problem Summary
Given a string of lowercase letters, find the maximum difference between the frequency of any character with odd frequency and the frequency of any character with even frequency. Return maxOddFreq - minEvenFreq.

### 📌 Constraints
- 3 <= s.length <= 100
- s consists of lowercase English letters
- At least one character has odd frequency and one has even frequency

---

## 💭 Intuition
👉 Count character frequencies, then find the maximum frequency among characters with odd count and the minimum frequency among characters with even (nonzero) count. The answer is their difference.

---

## ⚡ Approach — Frequency Counting

### 🧠 Idea
- Count frequency of each character.
- Track maxOdd = max frequency with odd count.
- Track minEven = min frequency with even nonzero count.
- Return maxOdd - minEven.

---

## 💻 Code

```cpp
class Solution {
 public:
  int maxDifference(string s) {
    vector<int> count(26);
    int maxOdd = 0;
    int minEven = s.length();

    for (const char c : s)
      ++count[c - 'a'];

    for (const int freq : count) {
      if (freq == 0)
        continue;
      if (freq % 2 == 0)
        minEven = min(minEven, freq);
      else
        maxOdd = max(maxOdd, freq);
    }

    return maxOdd - minEven;
  }
};
```

---

## 🧠 Dry Run
### Input
```
s = "aaaaabbc"
```
### Steps
```
count: a=5, b=2, c=1
Odd frequencies: a=5, c=1 → maxOdd = 5
Even frequencies: b=2 → minEven = 2

Result: 5 - 2 = 3
```

---

## ⏱️ Time Complexity
```
O(n) — one pass to count, one pass over 26 characters
```

## 💾 Space Complexity
```
O(1) — fixed-size frequency array of 26
```

---

## ⚠️ Edge Cases
- Only one character has even frequency → minEven is that frequency
- Multiple characters tied for maxOdd → any one works
- Frequency of 1 (odd) and 2 (even) → difference = -1

---

## 🎯 Interview Takeaways
- Separating frequencies by parity and finding extremes is straightforward.
- Always skip zero-frequency characters to avoid false results.
- The problem guarantees both odd and even frequency characters exist.

---

## 📌 Key Pattern
👉 **"Frequency counting with parity-based extremes"**

---

## 🔁 Related Problems
- 3443. Maximum Difference Between Even and Odd Frequency II
- 451. Sort Characters By Frequency

---

## 🚀 Final Thoughts
A simple counting problem that tests basic frequency analysis. The key is correctly categorizing frequencies by parity and finding the right extremes.

---

✨ **Rule to remember:**
> Separate character frequencies into odd and even groups, then maximize the difference between the best odd and worst even.
