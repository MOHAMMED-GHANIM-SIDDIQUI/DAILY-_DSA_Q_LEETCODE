# 2942. Find Words Containing Character

## 🔗 Problem Link
https://leetcode.com/problems/find-words-containing-character/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, String

---

## 🧩 Problem Summary
Given an array of strings `words` and a character `x`, return a list of indices of words that contain the character `x`.

### 📌 Constraints
- 1 <= words.length <= 50
- 1 <= words[i].length <= 50
- `x` is a lowercase English letter

---

## 💭 Intuition
👉 Simply iterate through each word and check if character `x` is present using `find`. If found, add the index to the result.

---

## ⚡ Approach — Linear Scan

### 🧠 Idea
- Iterate through each word with its index.
- Use `string::find` to check if `x` exists in the word.
- If `find` returns a valid position (not `npos`), add the index to the result.

---

## 💻 Code

```cpp
class Solution {
public:
    std::vector<int> findWordsContaining(const std::vector<std::string>& words, char x) {
        std::vector<int> result;
        for (int i = 0; i < (int)words.size(); ++i) {
            if (words[i].find(x) != std::string::npos) {
                result.push_back(i);
            }
        }
        return result;
    }
};
```

---

## 🧠 Dry Run
### Input
```
words = ["leet","code","yeet","b"], x = 'e'
```
### Steps
```
i=0: "leet".find('e') = 1 (found) → result = [0]
i=1: "code".find('e') = 3 (found) → result = [0, 1]
i=2: "yeet".find('e') = 1 (found) → result = [0, 1, 2]
i=3: "b".find('e') = npos (not found) → skip

Output: [0, 1, 2]
```

---

## ⏱️ Time Complexity
```
O(n * L) — where n is the number of words and L is the average word length
```

## 💾 Space Complexity
```
O(n) — for the result array in the worst case
```

---

## ⚠️ Edge Cases
- No word contains `x`: return an empty array.
- All words contain `x`: return all indices.
- Single character words.

---

## 🎯 Interview Takeaways
- Simple linear scan problems are great warm-ups.
- Using `string::find` is cleaner than manual character-by-character search.
- Passing `words` by const reference avoids unnecessary copies.

---

## 📌 Key Pattern
👉 **"Linear scan with string search"**

---

## 🔁 Related Problems
- 1933. Check if String Is Decomposable Into Value-Equal Substrings
- 2032. Two Out of Three
- 500. Keyboard Row

---

## 🚀 Final Thoughts
A straightforward problem testing basic string and array manipulation. The key is using built-in string search functions efficiently. Good for building familiarity with standard library operations.

---

✨ **Rule to remember:**
> Use `string::find` for character/substring search — it returns `npos` when not found.
