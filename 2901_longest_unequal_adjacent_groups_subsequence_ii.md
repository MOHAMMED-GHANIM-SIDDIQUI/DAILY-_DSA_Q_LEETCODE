# 2901. Longest Unequal Adjacent Groups Subsequence II

## 🔗 Problem Link
https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, String, Dynamic Programming, Hamming Distance

---

## 🧩 Problem Summary
Given `words` and `groups`, find the longest subsequence such that adjacent words in the subsequence have different groups, equal lengths, and a Hamming distance of exactly 1. Return the words in the subsequence.

### 📌 Constraints
- 1 <= n == words.length == groups.length <= 1000
- 1 <= words[i].length <= 10
- groups[i] is in range [0, n-1]

---

## 💭 Intuition
👉 This is a longest increasing subsequence (LIS) variant where the transition condition checks three things: different groups, same word length, and Hamming distance of exactly 1. Use O(n^2) DP with parent tracking for path reconstruction.

---

## ⚡ Approach — Dynamic Programming with Path Reconstruction

### 🧠 Idea
- `dp[i]` = length of the longest valid subsequence ending at index `i`.
- `prev[i]` = previous index in the optimal subsequence ending at `i`.
- For each pair `(j, i)` with `j < i`, check: different groups, same word length, Hamming distance == 1.
- Find the index with maximum `dp` value and reconstruct the path backward.

---

## 💻 Code

```cpp
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<string> getWordsInLongestSubsequence(vector<string>& words, vector<int>& groups) {
        int n = words.size();
        vector<int> dp(n, 1);       // dp[i]: length of longest valid subsequence ending at i
        vector<int> prev(n, -1);    // prev[i]: previous index in the subsequence

        for (int i = 1; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                if (groups[i] == groups[j]) continue;
                if (words[i].length() != words[j].length()) continue;
                if (hammingDist(words[i], words[j]) != 1) continue;
                if (dp[i] < dp[j] + 1) {
                    dp[i] = dp[j] + 1;
                    prev[i] = j;
                }
            }
        }

        // Find the index with the maximum dp value
        int maxIndex = max_element(dp.begin(), dp.end()) - dp.begin();

        // Reconstruct the subsequence
        vector<string> result;
        while (maxIndex != -1) {
            result.push_back(words[maxIndex]);
            maxIndex = prev[maxIndex];
        }

        reverse(result.begin(), result.end());
        return result;
    }

private:
    int hammingDist(const string& s1, const string& s2) {
        int dist = 0;
        for (int i = 0; i < s1.length(); ++i) {
            if (s1[i] != s2[i]) ++dist;
        }
        return dist;
    }
};
```

---

## 🧠 Dry Run
### Input
```
words = ["bab","dab","cab"], groups = [1,2,2]
```
### Steps
```
dp = [1, 1, 1], prev = [-1, -1, -1]

i=1, j=0: groups differ (1!=2), len equal (3==3), hamming("bab","dab")=1
  dp[1] = dp[0]+1 = 2, prev[1] = 0

i=2, j=0: groups differ (1!=2), len equal, hamming("bab","cab")=1
  dp[2] = dp[0]+1 = 2, prev[2] = 0
i=2, j=1: groups same (2==2) → skip

dp = [1, 2, 2], maxIndex = 1
Reconstruct: 1 → 0 → -1 → ["bab", "dab"]

Output: ["bab","dab"]
```

---

## ⏱️ Time Complexity
```
O(n^2 * L) — where L is the maximum word length (for Hamming distance computation)
```

## 💾 Space Complexity
```
O(n) — for dp and prev arrays
```

---

## ⚠️ Edge Cases
- No valid transitions exist: return any single word.
- All words have different lengths: each word forms its own subsequence of length 1.
- Multiple subsequences of the same max length: any valid one is acceptable.

---

## 🎯 Interview Takeaways
- LIS-style DP with custom transition conditions is a versatile pattern.
- Path reconstruction using a `prev` array is essential for returning the actual subsequence.
- Early filtering (group check, length check) before expensive Hamming distance computation improves constant factors.

---

## 📌 Key Pattern
👉 **"LIS-variant DP with custom transition + path reconstruction"**

---

## 🔁 Related Problems
- 2900. Longest Unequal Adjacent Groups Subsequence I
- 300. Longest Increasing Subsequence
- 1048. Longest String Chain

---

## 🚀 Final Thoughts
This problem extends the simple greedy of Problem 2900 into a full DP problem by adding the Hamming distance constraint. The O(n^2) approach works well within the constraints (n <= 1000). The path reconstruction via `prev` array is a classic technique worth mastering.

---

✨ **Rule to remember:**
> When transition conditions are complex (multiple checks), use LIS-style DP with parent tracking and filter conditions in order of cheapness.
