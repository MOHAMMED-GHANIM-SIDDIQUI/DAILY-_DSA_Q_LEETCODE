# 1513. Number of Substrings With Only 1s

## 🔗 Problem Link
https://leetcode.com/problems/number-of-substrings-with-only-1s/

## ⚡ Difficulty
Medium

## 🏷️ Topics
String, Math

---

## 🧩 Problem Summary
Given a binary string `s`, return the number of substrings that contain only the character `'1'`. Return the answer modulo `10^9 + 7`.

### 📌 Constraints
- `1 <= s.length <= 10^5`
- `s[i]` is either `'0'` or `'1'`.

---

## 💭 Intuition
👉 For each position `i` with `s[i] == '1'`, the number of all-ones substrings ending at `i` equals the distance from `i` to the last `'0'` (or the start of the string). We track the position of the last `'0'` and accumulate `i - lastZeroIndex` for each character.

---

## ⚡ Approach — Linear Scan with Last Zero Tracking

### 🧠 Idea
- Initialize `l = -1` as the position of the last `'0'` (before the string starts).
- For each index `i`, if `s[i] == '0'`, update `l = i`.
- Add `i - l` to the answer (this is 0 when `s[i] == '0'` since `l` just became `i`).
- Take modulo at each step.

---

## 💻 Code

```cpp
class Solution {
 public:
  int numSub(string s) {
    constexpr int kMod = 1'000'000'007;

    int ans = 0;
    int l = -1;

    for (int i = 0; i < s.length(); ++i) {
      if (s[i] == '0')
        l = i;  // Handle the reset value.
      ans = (ans + i - l) % kMod;
    }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
s = "0110111"
```
### Steps
```
l = -1
i=0: s[0]='0', l=0, ans += 0-0 = 0, ans=0
i=1: s[1]='1', ans += 1-0 = 1, ans=1
i=2: s[2]='1', ans += 2-0 = 2, ans=3
i=3: s[3]='0', l=3, ans += 3-3 = 0, ans=3
i=4: s[4]='1', ans += 4-3 = 1, ans=4
i=5: s[5]='1', ans += 5-3 = 2, ans=6
i=6: s[6]='1', ans += 6-3 = 3, ans=9
Answer: 9
Substrings: "1","1","11","1","1","11","1","11","111" = 9
```

---

## ⏱️ Time Complexity
```
O(n), single pass through the string
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- All zeros — answer is 0.
- All ones of length `n` — answer is `n*(n+1)/2 mod 10^9+7`.
- Single character — answer is 0 or 1.

---

## 🎯 Interview Takeaways
- Tracking the last boundary (last zero) avoids nested loops.
- The formula `i - l` elegantly counts all-ones substrings ending at position `i`.
- This pattern applies to any "count substrings/subarrays with a contiguous property" problem.

---

## 📌 Key Pattern
👉 **"Track the last boundary reset position to count contiguous substrings ending at each index"**

---

## 🔁 Related Problems
- 696 — Count Binary Substrings
- 1004 — Max Consecutive Ones III
- 485 — Max Consecutive Ones

---

## 🚀 Final Thoughts
This is a clean O(n) solution that demonstrates how tracking a single boundary variable can replace the need for explicit segment detection. The key observation is that each '1' at position `i` contributes `i - lastZero` new all-ones substrings.

---

✨ **Rule to remember:**
> "For counting all-ones substrings, each '1' at index i contributes (i - lastZeroIndex) substrings."
