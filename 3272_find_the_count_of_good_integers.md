# 3272. Find the Count of Good Integers

## 🔗 Problem Link
https://leetcode.com/problems/find-the-count-of-good-integers/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Math, Combinatorics, Hash Table, Enumeration

---

## 🧩 Problem Summary
A "good integer" is an n-digit number (no leading zeros) that can be rearranged into a palindrome divisible by k. Count the total number of such good integers.

### 📌 Constraints
- 1 <= n <= 10
- 1 <= k <= 9

---

## 💭 Intuition
👉 Generate all n-digit palindromes by constructing the first half, check divisibility by k, then count all distinct permutations (avoiding leading zeros) of each valid palindrome's digits.

---

## ⚡ Approach — Enumerate Palindromes + Permutation Counting

### 🧠 Idea
- Generate palindromes by iterating over the first half (halfLength digits)
- Mirror the first half to form the full palindrome
- Check if the palindrome is divisible by k
- Sort the digits to avoid counting the same digit multiset twice
- For each unique digit multiset, count valid permutations (no leading zeros)
- Permutations = (n - count_of_zeros) * (n-1)! / product(freq!)

---

## 💻 Code

```cpp
class Solution {
 public:
  long long countGoodIntegers(int n, int k) {
    const int halfLength = (n + 1) / 2;
    const int minHalf = pow(10, halfLength - 1);
    const int maxHalf = pow(10, halfLength);
    long ans = 0;
    unordered_set<string> seen;

    for (int num = minHalf; num < maxHalf; ++num) {
      const string firstHalf = to_string(num);
      const string secondHalf = {firstHalf.rbegin(), firstHalf.rend()};
      const string palindrome = firstHalf + secondHalf.substr(n % 2);
      if (stol(palindrome) % k != 0)
        continue;
      string sortedDigits = palindrome;
      ranges::sort(sortedDigits);
      if (seen.contains(sortedDigits))
        continue;
      seen.insert(sortedDigits);
      vector<int> digitCount(10);
      for (const char c : palindrome)
        ++digitCount[c - '0'];
      // Leading zeros are not allowed, so the first digit is special.
      const int firstDigitChoices = n - digitCount[0];
      long permutations = firstDigitChoices * factorial(n - 1);
      // For each repeated digit, divide by the factorial of the frequency since
      // permutations that swap identical digits don't create a new number.
      for (const int freq : digitCount)
        if (freq > 1)
          permutations /= factorial(freq);
      ans += permutations;
    }

    return ans;
  }

 private:
  long factorial(int n) {
    long res = 1;
    for (int i = 2; i <= n; ++i)
      res *= i;
    return res;
  }
};
```

---

## 🧠 Dry Run
### Input
```
n = 3, k = 5
```
### Steps
```
halfLength = 2, minHalf = 10, maxHalf = 100
num=10: palindrome="100" -> 100%5=0 -> sorted="001"
  digitCount: 0->2, 1->1
  firstDigitChoices = 3-2 = 1
  permutations = 1 * 2! / 2! = 1
num=15: palindrome="151" -> 151%5=1 -> skip
num=50: palindrome="505" -> 505%5=0 -> sorted="055"
  digitCount: 0->1, 5->2
  firstDigitChoices = 3-1 = 2
  permutations = 2 * 2! / 2! = 2
... continue for all valid palindromes
```

---

## ⏱️ Time Complexity
```
O(10^(n/2) * n) — enumerate all half-palindromes and process each
```

## 💾 Space Complexity
```
O(10^(n/2)) — set of seen digit multisets
```

---

## ⚠️ Edge Cases
- n = 1: single-digit palindromes divisible by k
- k = 1: all palindromes are valid
- Large n (10): up to 10^5 half-values to enumerate
- Digit multisets with many zeros — careful permutation counting

---

## 🎯 Interview Takeaways
- Generating palindromes via half-construction is efficient
- Deduplication via sorted digit string avoids overcounting
- Permutation counting with leading-zero exclusion is a classic combinatorics technique

---

## 📌 Key Pattern
👉 **"Generate palindromes from half, deduplicate by digit multiset, count permutations"**

---

## 🔁 Related Problems
- 906. Super Palindromes
- 564. Find the Closest Palindrome
- 2967. Minimum Cost to Make Array Equalindromic

---

## 🚀 Final Thoughts
This problem combines palindrome generation, divisibility checking, and combinatorial counting. The key optimization is deduplicating by sorted digit strings so each valid digit multiset is counted exactly once with the correct number of permutations.

---

✨ **Rule to remember:**
> Build palindromes from halves, deduplicate by sorted digits, count permutations minus leading zeros.
