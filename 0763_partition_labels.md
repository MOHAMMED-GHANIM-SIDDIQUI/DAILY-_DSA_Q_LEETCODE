# 763. Partition Labels

## 🔗 Problem Link
https://leetcode.com/problems/partition-labels/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Hash Table, Two Pointers, String, Greedy

---

## 🧩 Problem Summary
Given a string `s`, partition it into as many parts as possible so that each letter appears in at most one part. Return a list of integers representing the size of these parts.

### 📌 Constraints
- `1 <= s.length <= 500`
- `s` consists of lowercase English letters.

---

## 💭 Intuition
👉 For each character, find its last occurrence. As we iterate, we expand the current partition's end to include the last occurrence of every character we encounter. When our index reaches the partition end, we've found a valid partition.

---

## ⚡ Approach — Greedy with Last Occurrence

### 🧠 Idea
- Precompute the last index of each character in the string.
- Iterate through the string, maintaining a `start` and `end` for the current partition.
- Update `end` to be the max of the current `end` and the last occurrence of the current character.
- When `i == end`, we have found a complete partition; record its length and start a new one.

---

## 💻 Code

```cpp
class Solution {
public:
    vector<int> partitionLabels(string s) {
        vector<int> ans;
        vector<int> lastIndex(26);

        // Store the last occurrence of each character
        for (int i = 0; i < s.size(); ++i)
            lastIndex[s[i] - 'a'] = i;

        int start = 0, end = 0;

        // Iterate through the string to determine partitions
        for (int i = 0; i < s.size(); ++i) {
            end = max(end, lastIndex[s[i] - 'a']);

            // When we reach the end of a partition, store its length
            if (i == end) {
                ans.push_back(end - start + 1);
                start = i + 1;
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
s = "ababcbacadefegdehijhklij"
```
### Steps
```
lastIndex: a=8, b=5, c=7, d=14, e=15, f=11, g=13, h=19, i=22, j=23, k=20, l=21

i=0 (a): end=8
i=1 (b): end=8
i=2 (a): end=8
...
i=8 (a): end=8, i==end -> partition size = 8-0+1 = 9
i=9 (d): end=14
...
i=15 (e): end=15, i==end -> partition size = 15-9+1 = 7 (actually recalculated)
i=16 (h): end=19
...
i=23 (j): end=23, i==end -> partition size = 23-16+1 = 8

Result: [9, 7, 8]
```

---

## ⏱️ Time Complexity
```
O(n), where n is the length of the string
```

## 💾 Space Complexity
```
O(1), since the lastIndex array has a fixed size of 26
```

---

## ⚠️ Edge Cases
- Single character string: returns `[1]`.
- All same characters: returns `[n]`.
- All unique characters: returns `[1, 1, 1, ...]`.

---

## 🎯 Interview Takeaways
- Precomputing last occurrences is a common greedy trick for partition problems.
- The two-pointer greedy approach avoids the need for backtracking or DP.
- Always think about "what defines the boundary" when partitioning.

---

## 📌 Key Pattern
👉 **"Greedy interval merging using last occurrence tracking"**

---

## 🔁 Related Problems
- 56. Merge Intervals
- 435. Non-overlapping Intervals
- 768. Max Chunks To Make Sorted II

---

## 🚀 Final Thoughts
This problem elegantly demonstrates greedy partitioning. By tracking the farthest reach of each character, we can determine partition boundaries in a single pass. It is a great example of how precomputation simplifies greedy decisions.

---

✨ **Rule to remember:**
> "A partition ends when the current index catches up to the farthest last-occurrence of any character seen so far."
