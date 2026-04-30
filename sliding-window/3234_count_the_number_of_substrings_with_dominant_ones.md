# 3234. Count the Number of Substrings With Dominant Ones

## 🔗 Problem Link
https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/

## ⚡ Difficulty
Medium

## 🏷️ Topics
String, Sliding Window, Enumeration, Math

---

## 🧩 Problem Summary
Given a binary string, count the number of substrings where the number of 1s is at least the square of the number of 0s. A substring is "dominant in ones" if count(1) >= count(0)^2.

### 📌 Constraints
- 1 <= s.length <= 4 * 10^4
- s consists only of '0' and '1'

---

## 💭 Intuition
👉 Enumerate over the number of zeros. For each possible zero count, use a sliding window to find valid substrings. The constraint count(0)^2 <= count(1) limits the number of zeros to O(sqrt(n)).

---

## ⚡ Approach — Enumerate Zeros + Sliding Window

### 🧠 Idea
- For each possible zero count (0, 1, 2, ... up to sqrt(n)), use a sliding window
- Maintain counts of 0s and 1s in the window
- Shrink from the left to maintain exactly the target number of 0s
- Count valid substrings where count(1) >= zero^2

---

## 💻 Code

```cpp
class Solution {
 public:
  int numberOfSubstrings(string s) {
    int ans = 0;

    // Iterate through all possible number of 0s.
    for (int zero = 0; zero + zero * zero <= s.length(); ++zero) {
      int lastInvalidPos = -1;
      vector<int> count(2);
      for (int l = 0, r = 0; r < s.length(); ++r) {
        ++count[s[r] - '0'];
        // Try to shrink the window to maintain the "minimum" length of the
        // valid substring.
        for (; l < r; ++l)
          if (s[l] == '0' && count[0] > zero) {
            --count[0];  // Remove an extra '0'.
            lastInvalidPos = l;
          } else if (s[l] == '1' && count[1] - 1 >= zero * zero) {
            --count[1];  // Remove an extra '1'.
          } else {
            break;  // Cannot remove more characters.
          }
        if (count[0] == zero && count[1] >= zero * zero)
          // Add valid substrings ending in s[r] to the answer. They are
          // s[lastInvalidPos + 1..r], s[lastInvalidPos + 2..r], ..., s[l..r].
          ans += l - lastInvalidPos;
      }
    }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
s = "1011"
```
### Steps
```
zero=0 (need 0 zeros, >=0 ones):
  All substrings with only 1s: "1","1","1","11","11","111"
  but also "1011" has 1 zero, skip for zero=0
  Valid: positions of pure-1 substrings -> count accordingly

zero=1 (need 1 zero, >=1 one):
  Substrings with exactly 1 zero and >=1 one: "10","01","011","101","1011"

Total valid substrings counted across all zero values.
```

---

## ⏱️ Time Complexity
```
O(n * sqrt(n)) — outer loop runs O(sqrt(n)) times, inner sliding window is O(n)
```

## 💾 Space Complexity
```
O(1) — only tracking variables and a size-2 count array
```

---

## ⚠️ Edge Cases
- All 1s — every substring is valid (zero=0 covers all)
- All 0s — only single "0" substrings are valid (0 >= 0^2 = 0? No, need 1 >= 1... depends on definition)
- Very long strings — O(n*sqrt(n)) handles up to 4*10^4

---

## 🎯 Interview Takeaways
- The constraint count(0)^2 <= length limits zero count to O(sqrt(n)), enabling efficient enumeration
- Combining enumeration with sliding window is a powerful technique
- Tracking lastInvalidPos avoids recounting valid starting positions

---

## 📌 Key Pattern
👉 **"Enumerate over the constrained dimension (zeros), sliding window for the rest"**

---

## 🔁 Related Problems
- 1248. Count Number of Nice Subarrays
- 992. Subarrays with K Different Integers
- 2302. Count Subarrays With Score Less Than K

---

## 🚀 Final Thoughts
The mathematical insight that zero count is bounded by sqrt(n) transforms this from a brute-force O(n^2) problem into an elegant O(n*sqrt(n)) solution. The sliding window within each zero-count iteration handles the counting efficiently.

---

✨ **Rule to remember:**
> When one quantity is bounded by sqrt(n) due to constraints, enumerate it and use sliding window for the rest.
