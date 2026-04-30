# 3335. Total Characters in String After Transformations I

## 🔗 Problem Link
https://leetcode.com/problems/total-characters-in-string-after-transformations-i/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Hash Table, String, Dynamic Programming, Counting

---

## 🧩 Problem Summary
Given a string `s` and integer `t`, perform `t` transformations. In each transformation, every character is replaced: 'a'->'b', 'b'->'c', ..., 'y'->'z', and 'z' becomes "ab" (two characters). Return the total length of the string after `t` transformations, modulo 10^9 + 7.

### 📌 Constraints
- `1 <= s.length <= 10^5`
- `1 <= t <= 10^5`
- `s` consists of lowercase English letters

---

## 💭 Intuition
👉 Instead of tracking the actual string (which grows exponentially), track the count of each character. Each transformation shifts counts forward, and 'z' splits into 'a' and 'b'.

---

## ⚡ Approach — Character Frequency Simulation

### 🧠 Idea
- Maintain a frequency array `count[26]` for each letter.
- Each step: shift all counts forward by one position.
- Special case: 'z' count goes to both 'a' and 'b'.
- After `t` steps, sum all counts.

---

## 💻 Code

```cpp
class Solution {
 public:
  int lengthAfterTransformations(string s, int t) {
    constexpr int kMod = 1'000'000'007;
    vector<int> count(26);

    for (const char c : s)
      ++count[c - 'a'];

    while (t-- > 0) {
      vector<int> newCount(26);
      // 'a' -> 'b', 'b' -> 'c', ..., 'y' -> 'z'
      for (int i = 0; i < 25; ++i)
        newCount[i + 1] = count[i];
      // 'z' -> 'ab'
      newCount[0] = count[25];
      newCount[1] = (newCount[1] + count[25]) % kMod;
      count = std::move(newCount);
    }

    return accumulate(count.begin(), count.end(), 0L) % kMod;
  }
};
```

---

## 🧠 Dry Run
### Input
```
s = "abcyyz", t = 2
```
### Steps
```
Initial: count = [1,1,1,0,...,0,2,1] (a=1,b=1,c=1,y=2,z=1)
t=1: newCount: a+=z(1), b=a(1)+z(1)=2, c=b(1), d=c(1), z=y(2)
     count = [1,2,1,1,0,...,0,2,0]
t=2: newCount: a+=z(0)=0, b=a(1), c=b(2)+z(0)=2, d=c(1), e=d(1), z=0... wait, z=y's count
     sum all counts
```

---

## ⏱️ Time Complexity
```
O(26 * t + n) — 26 operations per transformation step, plus initial counting
```

## 💾 Space Complexity
```
O(26) = O(1)
```

---

## ⚠️ Edge Cases
- `t = 0` → return length of `s`
- All 'z' characters → doubles the count rapidly
- Large `t` with large `s` → modular arithmetic prevents overflow

---

## 🎯 Interview Takeaways
- When strings grow exponentially, track frequencies instead of actual characters.
- Modular arithmetic is essential for counting problems with large results.

---

## 📌 Key Pattern
👉 **"Simulate character transformations via frequency arrays to avoid exponential string growth"**

---

## 🔁 Related Problems
- 2194. Cells in a Range on an Excel Sheet
- Character transformation/shifting problems

---

## 🚀 Final Thoughts
A clean simulation approach that avoids the trap of building the actual string. The key insight is that only character frequencies matter, not positions.

---

✨ **Rule to remember:**
> "Track frequencies, not strings, when transformations cause exponential growth."
