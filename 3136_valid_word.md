# 3136. Valid Word

## 🔗 Problem Link
https://leetcode.com/problems/valid-word/

## ⚡ Difficulty
Easy

## 🏷️ Topics
String, Simulation

---

## 🧩 Problem Summary
A string `word` is valid if it has at least 3 characters, contains only alphanumeric characters (digits and letters), and includes at least one vowel and at least one consonant. Return true if the word is valid.

### 📌 Constraints
- `1 <= word.length <= 20`
- `word` consists of English letters (uppercase and lowercase), digits, '@', '#', and '$'.

---

## 💭 Intuition
👉 Check three conditions: length >= 3, all characters are alphanumeric, and the word contains at least one vowel and one consonant. Use helper functions for vowel/consonant classification.

---

## ⚡ Approach — Direct Validation

### 🧠 Idea
- Check if the word length is at least 3.
- Verify all characters are alphanumeric using `isalnum()`.
- Check for at least one vowel (a, e, i, o, u in both cases).
- Check for at least one consonant (alphabetic but not a vowel).

---

## 💻 Code

```cpp
class Solution {
 public:
  bool isValid(string word) {
    return word.length() >= 3 &&
           ranges::all_of(word, [](char c) { return isalnum(c); }) &&
           ranges::any_of(word, isVowel) && ranges::any_of(word, isConsonant);
  }

 private:
  static bool isVowel(char c) {
    static constexpr string_view kVowels = "aeiouAEIOU";
    return kVowels.find(c) != string_view::npos;
  }

  static bool isConsonant(char c) {
    return isalpha(c) && !isVowel(c);
  }
};
```

---

## 🧠 Dry Run
### Input
```
word = "234Adas"
```
### Steps
```
1. Length = 7 >= 3 ✓
2. All alphanumeric: '2','3','4','A','d','a','s' — all pass isalnum ✓
3. Has vowel: 'A' and 'a' are vowels ✓
4. Has consonant: 'd' and 's' are consonants ✓
Result: true
```

---

## ⏱️ Time Complexity
```
O(n) where n is the length of the word.
```

## 💾 Space Complexity
```
O(1) — constant extra space.
```

---

## ⚠️ Edge Cases
- Word has special characters like '@', '#', '$': return false (not alphanumeric).
- Word is all digits: no vowel or consonant, return false.
- Word is only vowels: no consonant, return false.
- Word length < 3: return false.

---

## 🎯 Interview Takeaways
- Break compound conditions into clear helper functions for readability.
- C++20 `ranges::all_of` and `ranges::any_of` make validation concise and expressive.
- `string_view` for constant lookup strings avoids heap allocation.

---

## 📌 Key Pattern
👉 **"Multi-condition string validation with helper predicates"**

---

## 🔁 Related Problems
- 2042. Check if Numbers Are Ascending in a Sentence
- 1678. Goal Parser Interpretation

---

## 🚀 Final Thoughts
A simple validation problem that tests attention to detail. The C++ solution leverages modern ranges for clean, functional-style validation. Each condition is independently checked, making the code easy to understand and maintain.

---

✨ **Rule to remember:**
> For multi-condition validation, decompose into independent predicates and combine with all_of/any_of for clarity.
