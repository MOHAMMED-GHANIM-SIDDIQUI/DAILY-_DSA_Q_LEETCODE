# 2785. Sort Vowels in a String

## 🔗 Problem Link
https://leetcode.com/problems/sort-vowels-in-a-string/

## ⚡ Difficulty
Medium

## 🏷️ Topics
String, Sorting

---

## 🧩 Problem Summary
Given a string `s`, sort all the vowels in the string in ascending order of their ASCII values while keeping the consonants in their original positions. Return the resulting string.

### 📌 Constraints
- `1 <= s.length <= 10^5`
- `s` consists of uppercase and lowercase English letters

---

## 💭 Intuition
👉 Extract all vowels, sort them, then place them back into the vowel positions in sorted order. Consonants stay untouched.

---

## ⚡ Approach — Extract, Sort, Replace

### 🧠 Idea
- Scan the string and collect all vowels into a separate list.
- Sort the vowels list.
- Rebuild the string: for each character, if it's a vowel, take the next sorted vowel; otherwise, keep the original consonant.

---

## 💻 Code

```cpp
class Solution {
 public:
  string sortVowels(string s) {
    string ans;
    vector<char> vowels;

    for (const char c : s)
      if (isVowel(c))
        vowels.push_back(c);

    ranges::sort(vowels);

    int i = 0;  // vowels' index
    for (const char c : s)
      ans += isVowel(c) ? vowels[i++] : c;

    return ans;
  }

 private:
  bool isVowel(char c) {
    static constexpr string_view kVowels = "aeiouAEIOU";
    return kVowels.find(c) != string_view::npos;
  }
};
```

---

## 🧠 Dry Run
### Input
```
s = "lEetcOde"
```
### Steps
```
Vowels found: ['E', 'e', 'O', 'e']
Sorted vowels: ['E', 'O', 'e', 'e']

Rebuild:
l -> consonant -> 'l'
E -> vowel -> 'E'
e -> vowel -> 'O'
t -> consonant -> 't'
c -> consonant -> 'c'
O -> vowel -> 'e'
d -> consonant -> 'd'
e -> vowel -> 'e'

Result: "lEOtcede"
```

---

## ⏱️ Time Complexity
```
O(n log n) for sorting the vowels
```

## 💾 Space Complexity
```
O(n)
```

---

## ⚠️ Edge Cases
- No vowels in the string — return as-is
- All vowels — the entire string gets sorted
- Mixed case vowels — uppercase ASCII values are smaller than lowercase

---

## 🎯 Interview Takeaways
- Separating concerns (extract, sort, merge) makes the solution clean and easy to understand.
- Remember that uppercase letters have smaller ASCII values than lowercase (A=65, a=97).

---

## 📌 Key Pattern
👉 **"Extract-Sort-Replace pattern for partial sorting of specific character types"**

---

## 🔁 Related Problems
- 345. Reverse Vowels of a String
- 917. Reverse Only Letters

---

## 🚀 Final Thoughts
A straightforward problem that tests string manipulation and sorting. The three-step approach (extract, sort, replace) is clean and extensible to similar "sort only certain characters" problems.

---

✨ **Rule to remember:**
> To sort only specific characters in a string, extract them, sort separately, then place back in their original positions.
