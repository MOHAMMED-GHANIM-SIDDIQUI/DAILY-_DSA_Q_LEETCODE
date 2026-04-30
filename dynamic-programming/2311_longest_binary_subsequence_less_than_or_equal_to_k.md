# 2311. Longest Binary Subsequence Less Than or Equal to K

## 🔗 Problem Link
https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/

## ⚡ Difficulty
Medium

## 🏷️ Topics
String, Greedy, Dynamic Programming, Binary

---

## 🧩 Problem Summary
Given a binary string `s` and a positive integer `k`, find the length of the longest subsequence of `s` that represents a binary number less than or equal to `k`.

### 📌 Constraints
- `1 <= s.length <= 1000`
- `s[i]` is either `'0'` or `'1'`
- `1 <= k <= 10^9`

---

## 💭 Intuition
👉 All '0's can always be included (they don't increase the value when prepended). Then greedily take as many '1's as possible from the right (least significant positions) while staying <= k.

---

## ⚡ Approach — Greedy from Right

### 🧠 Idea
- Count all '0's — they are always included in the subsequence.
- From the rightmost position, greedily take '1's and track the binary value.
- Stop taking '1's when adding the next one would exceed `k`.
- Answer = count of '0's + count of '1's taken.

---

## 💻 Code

```cpp
class Solution {
 public:
  int longestSubsequence(string s, int k) {
    int oneCount = 0;
    int num = 0;
    int pow = 1;

    // Take as many 1s as possible from the right.
    for (int i = s.length() - 1; i >= 0 && num + pow <= k; --i) {
      if (s[i] == '1') {
        ++oneCount;
        num += pow;
      }
      pow *= 2;
    }

    return ranges::count(s, '0') + oneCount;
  }
};
```

---

## 🧠 Dry Run
### Input
```
s = "1001010", k = 5
```
### Steps
```
Scan from right:
i=6: s[6]='0', pow=1→2
i=5: s[5]='1', num=0+2=2<=5 ✓, oneCount=1, pow=2→4
i=4: s[4]='0', pow=4→8
i=3: s[3]='1', num=2+8=10 > 5? Check: num+pow=2+8=10>5 → but condition is num+pow<=k → 2+8=10>5 → STOP

Wait, let me re-trace:
i=6: '0', pow=1, num+pow=0+1<=5 ✓
i=5: '1', num+pow=0+2<=5 ✓, oneCount=1, num=2, pow=4
i=4: '0', num+pow=2+4<=5? 6>5 → STOP

zeros = 4, oneCount = 1 → answer = 5
```

---

## ⏱️ Time Complexity
```
O(n) — single pass to count zeros, partial pass from right for ones
```

## 💾 Space Complexity
```
O(1) — constant extra space
```

---

## ⚠️ Edge Cases
- All zeros → the entire string (value is 0 <= k)
- k = 1 → all zeros plus at most one '1' at the rightmost position
- String value is exactly k → entire string is the answer
- Very large string but small k → mostly zeros included

---

## 🎯 Interview Takeaways
- Zeros are always "free" in a binary subsequence — they don't increase value when prepended.
- Greedy from the right (least significant bits) ensures we maximize the count of 1s included.
- The power-of-2 tracking avoids converting the entire string to a number.

---

## 📌 Key Pattern
👉 **"Greedy bit selection from least significant position — zeros are free, ones are costly"**

---

## 🔁 Related Problems
- 1498. Number of Subsequences That Satisfy the Given Sum Condition
- 2311. Longest Binary Subsequence Less Than or Equal to K
- 600. Non-negative Integers without Consecutive Ones

---

## 🚀 Final Thoughts
The key insight is that zeros never hurt and ones at lower bit positions cost less. By greedily taking ones from the right, we maximize the subsequence length while respecting the value constraint.

---

✨ **Rule to remember:**
> "In binary subsequences, all zeros are free — greedily add ones from the right (least significant) while staying within the limit."
