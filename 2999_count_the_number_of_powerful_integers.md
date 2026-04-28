# 2999. Count the Number of Powerful Integers

## 🔗 Problem Link
https://leetcode.com/problems/count-the-number-of-powerful-integers/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Math, String, Dynamic Programming, Digit DP

---

## 🧩 Problem Summary
Given integers `start`, `finish`, `limit`, and a string `suffix`, count the numbers in `[start, finish]` that end with `suffix` and have every digit at most `limit`. These are called "powerful" integers.

### 📌 Constraints
- 1 <= start <= finish <= 10^15
- 1 <= limit <= 9
- 1 <= suffix.length <= floor(log10(finish)) + 1

---

## 💭 Intuition
👉 This is a classic Digit DP problem. We count valid numbers in a range by tracking tight constraints on both the lower and upper bounds. At each digit position (before the suffix), we try all digits from 0 to `limit`, respecting bounds. When we reach the suffix region, we check if the fixed suffix falls within bounds.

---

## ⚡ Approach — Digit DP with Tight Bounds

### 🧠 Idea
- Pad `start` with leading zeros to match the length of `finish`.
- Use 3D memoization: `(position, tightStart, tightFinish)`.
- At each position in the prefix region, try digits 0 to min(limit, upper_bound_digit).
- At the suffix region, check if the given suffix value falls within the allowed range.
- Tight flags track whether we're still constrained by start/finish boundaries.

---

## 💻 Code

```cpp
class Solution {
public:
    long long numberOfPowerfulInt(long long start, long long finish, int limit, string suffix) {
        string startStr = to_string(start);
        string finishStr = to_string(finish);

        // Pad the start number with leading zeros to match the length of finish
        string paddedStart = string(finishStr.length() - startStr.length(), '0') + startStr;

        // Pad the suffix with leading zeros if needed
        string paddedSuffix = string(finishStr.length() - suffix.length(), '0') + suffix;

        // 3D memoization table: position, tightStart, tightFinish
        vector<vector<vector<long>>> dp(
            finishStr.length(), vector<vector<long>>(2, vector<long>(2, -1))
        );

        return countValidNumbers(paddedStart, finishStr, 0, limit, suffix, true, true, dp);
    }

private:
    long countValidNumbers(const string& startStr, const string& finishStr, int pos, int limit,
                           const string& suffix, bool isTightStart, bool isTightFinish,
                           vector<vector<vector<long>>>& dp) {
        int totalLength = finishStr.length();
        int suffixLength = suffix.length();

        // Base case: if we're at the position where the suffix starts
        if (pos + suffixLength == totalLength) {
            string minSuffix = isTightStart
                                   ? string(startStr.end() - suffixLength, startStr.end())
                                   : string(suffixLength, '0');

            string maxSuffix = isTightFinish
                                   ? string(finishStr.end() - suffixLength, finishStr.end())
                                   : string(suffixLength, '9');

            long suffixValue = stoll(suffix);
            return (stoll(minSuffix) <= suffixValue && suffixValue <= stoll(maxSuffix)) ? 1 : 0;
        }

        // Memoization check
        if (dp[pos][isTightStart][isTightFinish] != -1) {
            return dp[pos][isTightStart][isTightFinish];
        }

        long count = 0;
        int minDigit = isTightStart ? startStr[pos] - '0' : 0;
        int maxDigit = isTightFinish ? finishStr[pos] - '0' : 9;

        // Try all possible digits at current position
        for (int digit = minDigit; digit <= maxDigit; ++digit) {
            if (digit > limit) continue;

            bool nextTightStart = isTightStart && (digit == minDigit);
            bool nextTightFinish = isTightFinish && (digit == maxDigit);

            count += countValidNumbers(
                startStr, finishStr, pos + 1, limit, suffix,
                nextTightStart, nextTightFinish, dp
            );
        }

        return dp[pos][isTightStart][isTightFinish] = count;
    }
};
```

---

## 🧠 Dry Run
### Input
```
start = 1, finish = 6000, limit = 4, suffix = "124"
```
### Steps
```
startStr = "0001", finishStr = "6000"
Prefix positions: only position 0 (digits 0-6, limited to 0-4)

pos=0:
  digit=0: tight on both → check suffix region
    suffix "124", min="001", max="000" → 124 > 000? No → 0
    Actually: tightStart && digit==0 → nextTightStart=true
    tightFinish && digit==0? 0!=6 → nextTightFinish=false
    → suffix check: min="001", max="999" → 001<=124<=999 → 1
  digit=1: nextTightStart=false, nextTightFinish=false
    → suffix check: min="000", max="999" → 124 in range → 1
  ... digits 2,3,4 similarly → 1 each

Total: 5 (numbers: 0124, 1124, 2124, 3124, 4124)
But 0124=124 >= 1, all <= 6000 ✓

Output: 5
```

---

## ⏱️ Time Complexity
```
O(D * 2 * 2 * 10) = O(D) — where D is the number of digits in finish
```

## 💾 Space Complexity
```
O(D) — for the memoization table and recursion stack
```

---

## ⚠️ Edge Cases
- `suffix` longer than some numbers in range: those numbers can't be powerful.
- `limit = 9`: No digit restriction (except the suffix constraint).
- `start = finish`: Check if that single number is powerful.
- Suffix contains digits greater than `limit`: needs careful handling in the suffix check.

---

## 🎯 Interview Takeaways
- Digit DP is the standard approach for counting numbers with digit constraints in a range.
- Using two tight flags (for lower and upper bounds) handles range queries directly.
- Padding with leading zeros normalizes the string lengths for easier comparison.

---

## 📌 Key Pattern
👉 **"Digit DP with dual tight constraints for range counting with digit restrictions"**

---

## 🔁 Related Problems
- 233. Number of Digit One
- 1012. Numbers With Repeated Digits
- 902. Numbers At Most N Given Digit Set

---

## 🚀 Final Thoughts
This is a sophisticated Digit DP problem combining suffix matching with per-digit limits. The dual tight constraint approach elegantly handles the range `[start, finish]` in a single pass rather than computing `f(finish) - f(start-1)`. The memoization ensures each state is computed only once.

---

✨ **Rule to remember:**
> For counting numbers with digit constraints in a range, use Digit DP with tight flags to track boundary constraints.
