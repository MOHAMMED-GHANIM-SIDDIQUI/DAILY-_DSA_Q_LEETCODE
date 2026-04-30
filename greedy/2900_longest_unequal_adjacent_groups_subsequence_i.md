# 2900. Longest Unequal Adjacent Groups Subsequence I

## 🔗 Problem Link
https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, String, Greedy

---

## 🧩 Problem Summary
Given an array of strings `words` and a binary array `groups`, select the longest subsequence of `words` such that no two adjacent selected words have the same group value. Return the words in that subsequence.

### 📌 Constraints
- 1 <= n == words.length == groups.length <= 100
- 1 <= words[i].length <= 10
- groups[i] is 0 or 1

---

## 💭 Intuition
👉 Greedily pick every word whose group differs from the last picked word's group. This is optimal because skipping a valid word never helps — it can only reduce the subsequence length.

---

## ⚡ Approach — Greedy Selection

### 🧠 Idea
- Track the current group ID (initialize to -1 so the first word is always picked).
- Iterate through words: if the current group differs from the last picked group, add the word and update the group.
- This greedy approach guarantees the longest alternating subsequence.

---

## 💻 Code

```cpp
class Solution {
public:
    vector<string> getLongestSubsequence(vector<string>& words, vector<int>& groups) {
        int n=words.size();
         vector<string> ans;
        int groupId = -1;

        for (int i = 0; i < n; ++i) {
            if (groups[i] != groupId) {
                groupId = groups[i];
                ans.push_back(words[i]);
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
words = ["e","a","b"], groups = [0,0,1]
```
### Steps
```
Initial: groupId = -1, ans = []

i=0: groups[0]=0 != -1 → groupId=0, ans=["e"]
i=1: groups[1]=0 == 0  → skip
i=2: groups[2]=1 != 0  → groupId=1, ans=["e","b"]

Output: ["e","b"]
```

---

## ⏱️ Time Complexity
```
O(n) — single pass through the arrays
```

## 💾 Space Complexity
```
O(n) — for storing the result
```

---

## ⚠️ Edge Cases
- All groups are the same: only the first word is selected.
- Groups alternate perfectly: all words are selected.
- Single word: always returned.

---

## 🎯 Interview Takeaways
- Greedy is optimal for longest alternating subsequence problems.
- Initializing the tracking variable to an impossible value (-1) handles the first element cleanly.
- No dynamic programming needed when the greedy choice is provably optimal.

---

## 📌 Key Pattern
👉 **"Greedy alternating selection — pick whenever the group changes"**

---

## 🔁 Related Problems
- 2901. Longest Unequal Adjacent Groups Subsequence II
- 376. Wiggle Subsequence
- 1578. Minimum Time to Make Rope Colorful

---

## 🚀 Final Thoughts
This is a classic greedy problem where picking greedily at every opportunity is optimal. The simplicity of the approach makes it a great warm-up problem and a foundation for the harder variant (Problem 2901).

---

✨ **Rule to remember:**
> For longest alternating subsequence, greedily pick every element that differs from the last — skipping never helps.
