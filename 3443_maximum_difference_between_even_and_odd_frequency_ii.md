# 3443. Maximum Difference Between Even and Odd Frequency II

## 🔗 Problem Link
https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/

## ⚡ Difficulty
Hard

## 🏷️ Topics
String, Prefix Sum, Sliding Window, Enumeration

---

## 🧩 Problem Summary
Given a string s of digits (0-4) and an integer k, find a substring of length >= k that maximizes (freq of char a) - (freq of char b), where char a has odd frequency and char b has even (nonzero) frequency in that substring. Return this maximum difference.

### 📌 Constraints
- 3 <= s.length <= 10^5
- s consists of digits '0' to '4'
- 1 <= k <= s.length

---

## 💭 Intuition
👉 Enumerate all pairs (a, b) of distinct digits. For each pair, use prefix sums and a sliding window. The key insight is tracking parities: we want prefixA[r] - prefixA[l] to be odd (so freq of a is odd) and prefixB[r] - prefixB[l] to be even nonzero. We maintain minimum (prefixA - prefixB) grouped by parity states.

---

## ⚡ Approach — Prefix Sum + Parity-Based Sliding Window

### 🧠 Idea
- For each pair (a, b), build prefix counts prefixA and prefixB.
- Use a sliding window where the left pointer advances when the window is large enough and both characters appear.
- Track `minDiff[parityA][parityB]` = minimum value of (prefixA - prefixB) seen at the left boundary.
- For current right boundary, the answer contribution is (prefixA[r] - prefixB[r]) - minDiff[1 - parityA[r] % 2][parityB[r] % 2].
- This ensures the substring has odd count of a (parity flipped) and even count of b (same parity).

---

## 💻 Code

```cpp
class Solution {
 public:
  int maxDifference(string s, int k) {
    int ans = INT_MIN;

    for (const auto& [a, b] : getPermutations()) {
      // minDiff[parityA][parityB] := min(a - b) of all valid windows with
      // parityA and parityB
      vector<vector<int>> minDiff(2, vector<int>(2, INT_MAX / 2));
      vector<int> prefixA{0};  // prefixA[i] := the number of 'a's in s[0..i)
      vector<int> prefixB{0};  // prefixB[i] := the number of 'b's in s[0..i)
      for (int l = 0, r = 0; r < s.length(); ++r) {
        prefixA.push_back(prefixA.back() + (s[r] == a ? 1 : 0));
        prefixB.push_back(prefixB.back() + (s[r] == b ? 1 : 0));
        while (r - l + 1 >= k &&               // the window size >= k
               prefixA[l] < prefixA.back() &&  // the number of 'a's > 0
               prefixB[l] < prefixB.back()) {  // the number of 'b's > 0
          minDiff[prefixA[l] % 2][prefixB[l] % 2] = min(
              minDiff[prefixA[l] % 2][prefixB[l] % 2], prefixA[l] - prefixB[l]);
          ++l;
        }
        ans = max(ans, (prefixA.back() - prefixB.back()) -
                           minDiff[1 - prefixA.back() % 2][prefixB.back() % 2]);
      }
    }

    return ans;
  }

 private:
  vector<pair<char, char>> getPermutations() {
    vector<pair<char, char>> permutations;
    for (const char a : "01234")
      for (const char b : "01234")
        if (a != b)
          permutations.emplace_back(a, b);
    return permutations;
  }
};
```

---

## 🧠 Dry Run
### Input
```
s = "12233", k = 4
```
### Steps
```
Consider pair (a='2', b='3'):
prefixA: [0, 0, 0, 1, 2, 2]
prefixB: [0, 0, 0, 0, 0, 1]

r=3 (window "1223", size=4):
  l=0: prefixA[0]=0 < 2, prefixB[0]=0 < 0? No → don't advance
  ans candidate: (2-0) - minDiff[1-0%2][0%2] = 2 - minDiff[1][0] = 2 - INF → skip

r=4 (window "12233", size=5):
  l=0: prefixA[0]=0 < 2, prefixB[0]=0 < 1 → yes
  minDiff[0][0] = min(INF, 0-0) = 0, l=1
  ans candidate: (2-1) - minDiff[1-0%2][1%2] = 1 - minDiff[1][1] → INF → skip

Best found for pair (2,1): freq(2)=odd=1, freq(1)=even → ...
(Full enumeration yields the answer across all 20 pairs)
```

---

## ⏱️ Time Complexity
```
O(25 * n) = O(n) — 20 digit pairs, each with O(n) sliding window
```

## 💾 Space Complexity
```
O(n) — prefix arrays
```

---

## ⚠️ Edge Cases
- All characters are the same → no valid pair with even frequency char
- k equals string length → only one substring to check
- Characters with zero count must be excluded from consideration

---

## 🎯 Interview Takeaways
- Enumerating over a small alphabet (5 digits) allows checking all character pairs.
- Parity-based prefix sum tracking enables finding odd/even frequency constraints in O(1).
- The sliding window with minimum tracking by parity state is a powerful technique.

---

## 📌 Key Pattern
👉 **"Enumerate character pairs + parity-grouped prefix-sum minimization"**

---

## 🔁 Related Problems
- 3442. Maximum Difference Between Even and Odd Frequency I
- 992. Subarrays with K Different Integers
- 1918. Kth Smallest Subarray Sum

---

## 🚀 Final Thoughts
This hard problem combines multiple advanced techniques: enumeration over a small alphabet, prefix sums, sliding windows, and parity-based state tracking. The constant factor of 20 pairs keeps it efficient despite the complex logic.

---

✨ **Rule to remember:**
> With a small alphabet, enumerate all character pairs and use parity-grouped prefix minimums to find optimal substrings.
