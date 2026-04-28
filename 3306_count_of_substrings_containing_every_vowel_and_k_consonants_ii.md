# 3306. Count of Substrings Containing Every Vowel and K Consonants II

## 🔗 Problem Link
https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Hash Table, String, Sliding Window

---

## 🧩 Problem Summary
Given a string `word` and an integer `k`, count the number of substrings that contain every vowel ('a', 'e', 'i', 'o', 'u') at least once and exactly `k` consonants.

### 📌 Constraints
- `5 <= word.length <= 2 * 10^5`
- `word` consists of lowercase English letters
- `0 <= k <= word.length - 5`

---

## 💭 Intuition
👉 Counting substrings with exactly `k` consonants is hard directly. Use the classic trick: `exactly(k) = atMost(k) - atMost(k - 1)`. Within each "at most" call, use a sliding window tracking unique vowels and consonant counts.

---

## ⚡ Approach — Sliding Window with At-Most Decomposition

### 🧠 Idea
- Decompose `exactly(k)` into `atMost(k) - atMost(k - 1)`.
- In `substringsWithAtMost`, maintain a sliding window `[l, r]` ensuring at most `k` consonants.
- Track unique vowels and their last-seen positions.
- When all 5 vowels are present, count valid starting positions using the minimum last-seen vowel position.

---

## 💻 Code

```cpp
class Solution {
public:
    // Count the number of substrings containing every vowel and at most k consonants
    long long countOfSubstrings(string word, int k) {
        // Substrings with at most k consonants minus those with at most (k-1) consonants
        return substringsWithAtMost(word, k) - substringsWithAtMost(word, k - 1);
    }

private:
    // Return the number of substrings containing every vowel with at most k consonants
    long substringsWithAtMost(const string& word, int k) {
        // If k is -1, no valid substring exists with a negative number of consonants
        if (k == -1) return 0;

        long res = 0;            // Result to store the number of valid substrings
        int vowels = 0;          // Count of vowels in the current window
        int uniqueVowels = 0;    // Count of unique vowels in the current window
        unordered_map<char, int> vowelLastSeen; // Track last seen positions of vowels

        // Sliding window technique (using two pointers l and r)
        for (int l = 0, r = 0; r < word.length(); ++r) {
            // If the current character is a vowel
            if (isVowel(word[r])) {
                ++vowels; // Increase the count of vowels in the window
                // If it's a new vowel or it's seen after the left pointer 'l', increase unique vowel count
                if (const auto it = vowelLastSeen.find(word[r]); it == vowelLastSeen.end() || it->second < l) {
                    ++uniqueVowels;
                }
                // Update the last seen position of the vowel
                vowelLastSeen[word[r]] = r;
            }

            // Shrink the window from the left until we have at most k consonants
            while (r - l + 1 - vowels > k) {
                if (isVowel(word[l])) {
                    --vowels; // Decrease the vowel count if we're removing a vowel
                    // If we removed the last occurrence of the vowel, decrease unique vowel count
                    if (vowelLastSeen[word[l]] == l) {
                        --uniqueVowels;
                    }
                }
                ++l; // Move the left pointer to the right
            }

            // If all 5 vowels are present in the current window
            if (uniqueVowels == 5) {
                // Add the number of valid substrings starting from l to r
                // Valid substrings are from word[l..r] to word[min(vowelLastSeen[vowel])..r]
                res += min({vowelLastSeen['a'], vowelLastSeen['e'], vowelLastSeen['i'],
                            vowelLastSeen['o'], vowelLastSeen['u']}) - l + 1;
            }
        }

        return res;
    }

    // Helper function to check if a character is a vowel
    bool isVowel(char c) {
        static constexpr string_view kVowels = "aeiou";
        return kVowels.find(c) != string_view::npos;
    }
};
```

---

## 🧠 Dry Run
### Input
```
word = "aeioubk", k = 1
```
### Steps
```
atMost(1):
  Window expands r=0..6
  At r=5 ('b'), consonants=1, all 5 vowels present → count substrings
  At r=6 ('k'), consonants=2 → shrink window from left
atMost(0):
  Similar but no consonant allowed
Result = atMost(1) - atMost(0)
```

---

## ⏱️ Time Complexity
```
O(n) — each character is visited at most twice by left and right pointers
```

## 💾 Space Complexity
```
O(1) — constant extra space (vowel map has at most 5 entries)
```

---

## ⚠️ Edge Cases
- `k = 0` → substrings must have zero consonants but all 5 vowels
- All characters are vowels → many valid substrings when k = 0
- String has fewer than 5 distinct vowels → result is 0

---

## 🎯 Interview Takeaways
- The `exactly(k) = atMost(k) - atMost(k-1)` decomposition is a classic sliding window trick.
- Tracking last-seen positions of vowels enables efficient counting of valid start positions.

---

## 📌 Key Pattern
👉 **"At-most decomposition + sliding window for exact count substring problems"**

---

## 🔁 Related Problems
- 992. Subarrays with K Different Integers
- 1358. Number of Substrings Containing All Three Characters
- 2062. Count Vowel Substrings of a String

---

## 🚀 Final Thoughts
A well-structured approach that breaks a hard counting problem into manageable sliding window passes. The key insight is using last-seen vowel positions to avoid recounting.

---

✨ **Rule to remember:**
> "When you need exactly k, think atMost(k) minus atMost(k-1)."
