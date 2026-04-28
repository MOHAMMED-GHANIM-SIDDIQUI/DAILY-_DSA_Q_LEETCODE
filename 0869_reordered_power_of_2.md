# 869. Reordered Power of 2

## 🔗 Problem Link
https://leetcode.com/problems/reordered-power-of-2/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Math, Sorting, Counting, Enumeration

---

## 🧩 Problem Summary
Given a positive integer `n`, determine if its digits can be reordered to form a power of 2. Leading zeros are not allowed.

### 📌 Constraints
- `1 <= n <= 10^9`

---

## 💭 Intuition
👉 Instead of generating all permutations, compute a "digit signature" (count of each digit) and compare it against the signatures of all powers of 2 within the valid range. If any match, return true.

---

## ⚡ Approach — Digit Counting / Signature Matching

### 🧠 Idea
- Create a digit-count signature for the input number.
- Iterate through all powers of 2 (up to 2^29, since 2^30 > 10^9).
- For each power, compute its digit signature.
- If any power's signature matches the input's signature, return true.

---

## 💻 Code

```cpp
class Solution {
 public:
  bool reorderedPowerOf2(int n) {
    int count = counter(n);

    for (int i = 0; i < 30; ++i)
      if (counter(1 << i) == count)
        return true;

    return false;
  }

 private:
  int counter(int n) {
    int count = 0;

    for (; n > 0; n /= 10)
      count += pow(10, n % 10);

    return count;
  }
};
```

---

## 🧠 Dry Run
### Input
```
n = 46
```
### Steps
```
counter(46): digits are 6, 4 -> count = 10^6 + 10^4 = 1010000
Check powers of 2:
  counter(64) = 10^4 + 10^6 = 1010000 -> Match!
Return true (46 can be reordered to 64 = 2^6)
```

---

## ⏱️ Time Complexity
```
O(30 * log(n)) = O(log(n)), checking 30 powers each with digit extraction
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- `n = 1`: Already a power of 2, return true.
- `n = 10`: Cannot form a power of 2.
- Large numbers near 10^9.

---

## 🎯 Interview Takeaways
- Digit signature matching avoids expensive permutation enumeration.
- Using `10^digit` as a hash for each digit is a clever encoding trick.
- The finite range of powers of 2 (only 30 for 32-bit integers) makes brute force feasible.

---

## 📌 Key Pattern
👉 **"Digit frequency signature matching against a finite set of candidates"**

---

## 🔁 Related Problems
- 242. Valid Anagram
- 49. Group Anagrams
- 326. Power of Three

---

## 🚀 Final Thoughts
This problem showcases how reframing "can digits be rearranged" as "do digit frequencies match" turns a combinatorial problem into a simple lookup. The encoding using powers of 10 is compact and avoids sorting.

---

✨ **Rule to remember:**
> "To check if digits can form a target number, compare digit-frequency signatures instead of generating permutations."
