# 1935. Maximum Number of Words You Can Type

## 🔗 Problem Link
https://leetcode.com/problems/maximum-number-of-words-you-can-type/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Hash Table, String

---

## 🧩 Problem Summary
Given a string `text` of words separated by spaces and a string `brokenLetters`, return the number of words in `text` that can be fully typed using a keyboard where certain letters are broken.

### 📌 Constraints
- `1 <= text.length <= 10^4`
- `0 <= brokenLetters.length <= 26`
- `text` consists of words separated by single spaces.
- Each word consists of lowercase English letters.

---

## 💭 Intuition
👉 For each word, check if any of its characters appear in the broken letters string. If none do, the word can be typed. Simple character membership testing per word.

---

## ⚡ Approach — Word-by-Word Validation

### 🧠 Idea
- Split the text into words (or iterate using start/end indices).
- For each word, check if any character is in the broken letters set.
- If the word contains no broken letters, increment the count.

---

## 💻 Code

```cpp
class Solution {
    bool is_possible(const string &word, const string &broken) {
        for (char c : broken) {
            if (word.find(c) != string::npos) {
                return false;
            }
        }
        return true;
    }

public:
    int canBeTypedWords(string text, string brokenLetters) {
        int n = text.size();
        int strt = 0, ans = 0;

        for (int i = 0; i <= n; i++) {
            if (i == n || text[i] == ' ') {
                string word = text.substr(strt, i - strt);
                if (is_possible(word, brokenLetters)) {
                    ans++;
                }
                strt = i + 1;
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
text = "hello world", brokenLetters = "ad"
```
### Steps
```
Word "hello": check 'a' -> not found, check 'd' -> not found -> typable, ans=1
Word "world": check 'a' -> not found, check 'd' -> found at index 4 -> not typable

Result: 1
```

---

## ⏱️ Time Complexity
```
O(n * b), where n is the length of text and b is the length of brokenLetters
```

## 💾 Space Complexity
```
O(w) for substring extraction, where w is the max word length
```

---

## ⚠️ Edge Cases
- No broken letters: all words can be typed, return total word count.
- All letters are broken: only words using non-broken letters count (likely 0).
- Single-character words.

---

## 🎯 Interview Takeaways
- Simple string problems can be solved with basic iteration and membership checks.
- Using a hash set for broken letters would improve from O(b) to O(1) per character check.
- Splitting by spaces manually avoids needing a library split function in C++.

---

## 📌 Key Pattern
👉 **"Per-word validation against a forbidden character set"**

---

## 🔁 Related Problems
- 2264. Largest 3-Same-Digit Number in String
- 824. Goat Latin

---

## 🚀 Final Thoughts
This is a straightforward string problem that tests basic string manipulation skills. The solution iterates through the text, extracts each word, and checks against the broken letters. Using a set for broken letters would be a minor optimization.

---

✨ **Rule to remember:**
> "Split into words, check each against the forbidden set — straightforward validation."
