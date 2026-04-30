# 3541. Find Most Frequent Vowel and Consonant

## 🔗 Problem Link
https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/

## ⚡ Difficulty
Easy

## 🏷️ Topics
String, Hash Map, Counting

---

## 🧩 Problem Summary
Given a string `s`, find the maximum frequency among vowels and the maximum frequency among consonants, then return their sum.

### 📌 Constraints
- `1 <= s.length <= 100`
- `s` consists of lowercase English letters

---

## 💭 Intuition
👉 Count the frequency of each character, then separately find the maximum frequency for vowels and consonants. Return their sum.

---

## ⚡ Approach — Frequency Map with Category Split

### 🧠 Idea
- Build a frequency map of all characters.
- Iterate through the map, classifying each character as vowel or consonant.
- Track the maximum frequency in each category.
- Return the sum of the two maxima.

---

## 💻 Code

```cpp
class Solution {
    bool is_vowel(char c)
    {
        string vowels="aeiou";
        if (vowels.find(c) != string::npos)
        {
            return true;
        }
        return false;
    }
public:
    int maxFreqSum(string s) {
        unordered_map<char,int>mpp;
        for(char c:s)
        {
            mpp[c]++;
        }
        int vow_max_freq=0,con_max_freq=0;
        for(auto it:mpp)
        {
            if(is_vowel(it.first))
            {
                vow_max_freq=max(vow_max_freq,it.second);
            }
            else
            {
                con_max_freq=max(con_max_freq,it.second);
            }
        }
        return vow_max_freq+con_max_freq;
    }
};
```

---

## 🧠 Dry Run
### Input
```
s = "successes"
```
### Steps
```
Frequency map: {s:4, u:1, c:2, e:2}

Vowels: u(1), e(2) -> max = 2
Consonants: s(4), c(2) -> max = 4

Result: 2 + 4 = 6
```

---

## ⏱️ Time Complexity
```
O(n) — single pass to count, constant pass over map (at most 26 entries)
```

## 💾 Space Complexity
```
O(1) — map has at most 26 entries (constant)
```

---

## ⚠️ Edge Cases
- String with only vowels → consonant max is 0
- String with only consonants → vowel max is 0
- All same character → one category has that frequency, other is 0

---

## 🎯 Interview Takeaways
- Separate counting by category is cleaner than interleaving logic.
- Helper functions like `is_vowel` improve readability.
- Hash map for frequency counting is a fundamental pattern.

---

## 📌 Key Pattern
👉 **"Frequency counting with category classification — find max per category."**

---

## 🔁 Related Problems
- 451. Sort Characters By Frequency
- 2278. Percentage of Letter in String
- 1456. Maximum Number of Vowels in a Substring of Given Length

---

## 🚀 Final Thoughts
A basic counting problem that tests the ability to classify characters and track separate maxima. Clean code organization with a helper function makes the solution readable.

---

✨ **Rule to remember:**
> When tracking separate maxima by category, build a single frequency map and split during the scan.
