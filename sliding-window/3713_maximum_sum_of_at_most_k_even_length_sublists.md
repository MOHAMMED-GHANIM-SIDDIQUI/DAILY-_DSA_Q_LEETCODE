# 3713. Maximum Sum of At Most K Even-Length Sublists

## 🔗 Problem Link
https://leetcode.com/problems/maximum-sum-of-at-most-k-even-length-sublists/

## ⚡ Difficulty
Medium

## 🏷️ Topics
String, Hash Table, Sliding Window, Frequency Count

---

## 🧩 Problem Summary
Given a string `s`, find the length of the longest "balanced" substring. A substring is balanced if every distinct character in it appears the same number of times — i.e., `max_frequency * distinct_count == length`.

### 📌 Constraints
- `1 <= len(s) <= 10^5`
- `s` consists of lowercase English letters

---

## 💭 Intuition
👉 A substring is balanced when all distinct characters share the same frequency. This means `max_freq * distinct == length` — a simple algebraic check that avoids scanning all frequencies each time.

---

## ⚡ Approach — Brute Force with Frequency Tracking

### 🧠 Idea
- Enumerate all substrings using two nested loops (`i`, `j`).
- Maintain a frequency array of size 26 for characters.
- Track `distinct` (number of unique characters) and `max_freq` (highest frequency of any character).
- At each extension, check if `max_freq * distinct == length`. If so, update the answer.

---

## 💻 Code

```python
class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            freq = [0] * 26
            distinct = 0
            max_freq = 0

            for j in range(i, n):
                idx = ord(s[j]) - ord('a')
                if freq[idx] == 0:
                    distinct += 1
                freq[idx] += 1
                max_freq = max(max_freq, freq[idx])

                length = j - i + 1

                # Check if balanced
                if max_freq * distinct == length:
                    ans = max(ans, length)

        return ans
```

---

## 🧠 Dry Run
### Input
```
s = "aabb"
```
### Steps
```
i=0:
  j=0: freq[a]=1, distinct=1, max_freq=1, len=1, 1*1==1 ✓ → ans=1
  j=1: freq[a]=2, distinct=1, max_freq=2, len=2, 2*1==2 ✓ → ans=2
  j=2: freq[a]=2,freq[b]=1, distinct=2, max_freq=2, len=3, 2*2!=3 ✗
  j=3: freq[a]=2,freq[b]=2, distinct=2, max_freq=2, len=4, 2*2==4 ✓ → ans=4

i=1:
  j=1: freq[a]=1, 1*1==1 ✓ → ans=4
  j=2: freq[a]=1,freq[b]=1, 1*2==2 ✓ → ans=4
  j=3: freq[a]=1,freq[b]=2, 2*2!=3 ✗

Result: 4
```

---

## ⏱️ Time Complexity
```
O(n^2) — two nested loops over the string
```

## 💾 Space Complexity
```
O(1) — fixed-size frequency array of 26
```

---

## ⚠️ Edge Cases
- Single character string → answer is 1
- All same characters → entire string is balanced
- All distinct characters with frequency 1 → entire string is balanced
- No balanced substring longer than 1

---

## 🎯 Interview Takeaways
- The condition `max_freq * distinct == length` is an elegant shortcut: if every character appeared `max_freq` times, the total would be exactly `length`.
- Maintaining running `distinct` and `max_freq` avoids rescanning the frequency array each iteration.
- This brute force is acceptable for small constraints but needs optimization (e.g., fixing distinct count) for larger inputs.

---

## 📌 Key Pattern
👉 **"Balanced substring check via algebraic invariant: max_freq * distinct == length."**

---

## 🔁 Related Problems
- 395. Longest Substring with At Least K Repeating Characters
- 1759. Count Number of Homogeneous Substrings
- 2067. Number of Equal Count Substrings

---

## 🚀 Final Thoughts
The brute force approach is clean and easy to understand. The key mathematical insight — that a balanced substring satisfies `max_freq * distinct == length` — eliminates the need for expensive per-step frequency validation. For larger inputs, consider fixing the number of distinct characters and using sliding window techniques.

---

✨ **Rule to remember:**
> "A substring is balanced when max_freq times distinct count equals the substring length — no need to check every frequency individually."
