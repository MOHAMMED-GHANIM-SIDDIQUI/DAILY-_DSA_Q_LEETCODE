# 3227. Vowels Game in a String

## 🔗 Problem Link
https://leetcode.com/problems/vowels-game-in-a-string/

## ⚡ Difficulty
Medium

## 🏷️ Topics
String, Math, Game Theory, Brainteaser

---

## 🧩 Problem Summary
Alice and Bob play a game on a string. Alice goes first and must remove a substring with an odd number of vowels. Bob must remove a substring with an even number of vowels. The player who cannot make a move loses. Determine if Alice wins given both play optimally.

### 📌 Constraints
- 1 <= s.length <= 10^5
- s consists of lowercase English letters

---

## 💭 Intuition
👉 Alice wins if and only if there is at least one vowel in the string. If there are any vowels, Alice can always make a move. If there are zero vowels, Alice cannot move at all.

---

## ⚡ Approach — Count Vowels

### 🧠 Idea
- Count the total number of vowels in the string
- If count > 0, Alice wins (return true)
- If count == 0, Alice cannot make any move (return false)

---

## 💻 Code

```cpp
class Solution {
public:
    bool doesAliceWin(string s) {
        string vowels = "aeiou";
        int count = 0;
        for (char c : s) {
            if (vowels.find(c) != string::npos) {
                count++;
            }
        }
        return count > 0;
    }
};
```

---

## 🧠 Dry Run
### Input
```
s = "leetcoder"
```
### Steps
```
Vowels found: e, e, o, e -> count = 4
count > 0 -> return true (Alice wins)
```

---

## ⏱️ Time Complexity
```
O(n) — single pass through the string
```

## 💾 Space Complexity
```
O(1) — constant extra space
```

---

## ⚠️ Edge Cases
- No vowels in the string — Alice loses immediately
- Exactly one vowel — Alice removes it, Bob faces no vowels
- All vowels — Alice always has a valid move

---

## 🎯 Interview Takeaways
- Game theory problems often have surprisingly simple solutions
- The key insight is that Alice can always take the entire string if vowel count is odd, or leave one vowel for a future turn
- Don't overthink — check if the problem reduces to a simple condition

---

## 📌 Key Pattern
👉 **"Game theory brainteaser — reduce to a simple condition"**

---

## 🔁 Related Problems
- 292. Nim Game
- 1025. Divisor Game
- 1561. Maximum Number of Coins You Can Get

---

## 🚀 Final Thoughts
This is a classic brainteaser disguised as a game theory problem. The answer is simply whether the string contains any vowels. Alice can always construct a winning strategy if at least one vowel exists.

---

✨ **Rule to remember:**
> Alice wins if and only if the string has at least one vowel — it's that simple.
