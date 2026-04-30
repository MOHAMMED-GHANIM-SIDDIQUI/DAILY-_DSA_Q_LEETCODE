# 3330. Find the Original Typed String I

## 🔗 Problem Link
https://leetcode.com/problems/find-the-original-typed-string-i/

## ⚡ Difficulty
Easy

## 🏷️ Topics
String, Counting

---

## 🧩 Problem Summary
Alice typed a string on a faulty keyboard that may repeat consecutive identical characters. Given the displayed string `word`, count how many possible original strings could have produced it. Each group of consecutive identical characters could have been typed as any non-zero number of that character up to the group length.

### 📌 Constraints
- `1 <= word.length <= 100`
- `word` consists of lowercase English letters

---

## 💭 Intuition
👉 Each pair of consecutive identical characters adds one extra possibility for the original string. The base count is 1 (the word itself), and each adjacent duplicate adds 1 more possibility.

---

## ⚡ Approach — Count Adjacent Duplicates

### 🧠 Idea
- Start with `ans = 1`.
- For each position where `word[i] == word[i-1]`, increment `ans` by 1.
- Each duplicate could have been an extra keystroke, so it represents an additional possible original string.

---

## 💻 Code

```cpp
class Solution {
 public:
  int possibleStringCount(string word) {
    int ans = 1;
    for (int i = 1; i < word.length(); ++i)
      if (word[i] == word[i - 1])
        ++ans;
    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
word = "aabbcc"
```
### Steps
```
i=1: 'a'=='a' → ans=2
i=2: 'b'!='a' → skip
i=3: 'b'=='b' → ans=3
i=4: 'c'!='b' → skip
i=5: 'c'=='c' → ans=4
Result: 4
```

---

## ⏱️ Time Complexity
```
O(n) — single pass through the string
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- Single character string → answer is 1
- No adjacent duplicates → answer is 1 (only the original)
- All same characters (e.g., "aaaa") → answer equals string length

---

## 🎯 Interview Takeaways
- Simple counting problems often have elegant one-pass solutions.
- Look for how each character contributes independently to the count.

---

## 📌 Key Pattern
👉 **"Count adjacent duplicates for possibilities in faulty-keyboard problems"**

---

## 🔁 Related Problems
- 443. String Compression
- 1446. Consecutive Characters

---

## 🚀 Final Thoughts
A straightforward counting problem. Each adjacent duplicate adds one more possible original string. The solution is clean and efficient.

---

✨ **Rule to remember:**
> "Adjacent duplicates in typed strings each represent one extra possibility."
