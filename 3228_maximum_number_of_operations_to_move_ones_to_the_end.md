# 3228. Maximum Number of Operations to Move Ones to the End

## 🔗 Problem Link
https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/

## ⚡ Difficulty
Medium

## 🏷️ Topics
String, Greedy, Counting

---

## 🧩 Problem Summary
Given a binary string, you can perform operations where you move a '1' that is immediately followed by a '0' to the right end of a consecutive block of '0's. Count the maximum number of such operations possible.

### 📌 Constraints
- 1 <= s.length <= 10^5
- s consists only of '0' and '1'

---

## 💭 Intuition
👉 Each block of 0s preceded by 1s triggers one operation per 1 accumulated so far. Count 1s as you scan, and add the count whenever a 0-block ends (transition from 0 to 1, or end of string while in a 0-block).

---

## ⚡ Approach — Greedy Count

### 🧠 Idea
- Track the number of 1s seen so far
- When a transition from a 0-block to a 1-block occurs, all accumulated 1s contribute one operation each
- Sum up operations at each such transition

---

## 💻 Code

```cpp
class Solution {
 public:
  int maxOperations(string s) {
    int ans = 0;
    int ones = 0;

    for (int i = 0; i < s.length(); ++i)
      if (s[i] == '1')
        ++ones;
elseif(i+1==s.length()||s[i+1]=='1')ans+=ones;returnans; }
};
```

---

## 🧠 Dry Run
### Input
```
s = "1001101"
```
### Steps
```
i=0: '1' -> ones=1
i=1: '0', next='0' -> continue
i=2: '0', next='1' -> ans+=1=1
i=3: '1' -> ones=2
i=4: '1' -> ones=3
i=5: '0', next='1' -> ans+=3=4
i=6: '1' -> ones=4
Result: 4
```

---

## ⏱️ Time Complexity
```
O(n) — single pass through the string
```

## 💾 Space Complexity
```
O(1) — only two tracking variables
```

---

## ⚠️ Edge Cases
- All 1s — no operations possible (no 0s to move across)
- All 0s — no operations possible (no 1s to move)
- Alternating 1s and 0s — each 0-block triggers accumulated 1s

---

## 🎯 Interview Takeaways
- The key is recognizing that each 0-block boundary triggers operations proportional to 1s seen
- Don't simulate individual moves — count contributions greedily
- Watch for compressed/minified code — always understand the logic behind it

---

## 📌 Key Pattern
👉 **"Count contributions at block boundaries using accumulated prefix counts"**

---

## 🔁 Related Problems
- 1529. Minimum Suffix Flips
- 2027. Minimum Moves to Convert String
- 2380. Time Needed to Rearrange a Binary String

---

## 🚀 Final Thoughts
Instead of simulating each operation, this greedy approach recognizes that all 1s to the left of a 0-block will each contribute one operation when they pass through that block. Counting at block boundaries gives the answer in O(n).

---

✨ **Rule to remember:**
> At each 0-block boundary, all preceding 1s contribute one operation each.
