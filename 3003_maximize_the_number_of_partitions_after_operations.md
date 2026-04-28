# 3003. Maximize the Number of Partitions After Operations

## 🔗 Problem Link
https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/

## ⚡ Difficulty
Hard

## 🏷️ Topics
String, Dynamic Programming, Bitmask, Memoization

---

## 🧩 Problem Summary
Given a string `s` and integer `k`, you can change at most one character in `s`. Then partition `s` into parts where each part has at most `k` distinct characters (greedily from left). Maximize the number of partitions.

### 📌 Constraints
- 1 <= s.length <= 10^4
- 1 <= k <= 26

---

## 💭 Intuition
👉 Use bitmask DP to track which characters have been seen in the current partition. At each position, we can either keep the character or (if we haven't used our change yet) try changing it to any of 26 letters to potentially force more partition splits.

---

## ⚡ Approach — Bitmask DP with Memoization

### 🧠 Idea
- State: `(position, canChange, mask)` where mask tracks distinct characters in current partition.
- At each position, try keeping the character. If `canChange` is true, also try all 26 replacements.
- When adding a character causes distinct count to exceed `k`, start a fresh partition (count +1).
- Use a hash map with a compressed key for memoization.

---

## 💻 Code

```cpp
class Solution {
 public:
  int maxPartitionsAfterOperations(string s, int k) {
    unordered_map<long, int> mem;
    return maxPartitionsAfterOperations(s, 0, true, 0, k, mem) + 1;
  }

 private:
  // Returns the maximum number of partitions of s[i..n), where `canChange` is
  // true if we can still change a letter, and `mask` is the bitmask of the
  // letters we've seen.
  int maxPartitionsAfterOperations(const string& s, int i, bool canChange,
                                   int mask, int k,
                                   unordered_map<long, int>& mem) {
    if (i == s.length())
      return 0;

    long key = static_cast<long>(i) << 27 | (canChange ? 1 : 0) << 26 | mask;
    if (const auto it = mem.find(key); it != mem.end())
      return it->second;

    // Initialize the result based on the current letter.
    int res = getRes(s, i, canChange, mask, 1 << (s[i] - 'a'), k, mem);

    // If allowed, explore the option to change the current letter.
    if (canChange)
      for (int j = 0; j < 26; ++j)
        res = max(res, getRes(s, i, false, mask, 1 << j, k, mem));

    return mem[key] = res;
  }

  int getRes(const string& s, int i, bool nextCanChange, unsigned mask,
             int newBit, int k, unordered_map<long, int>& mem) {
    const unsigned newMask = mask | newBit;
    if (popcount(newMask) > k)  // fresh start
      return 1 + maxPartitionsAfterOperations(s, i + 1, nextCanChange, newBit,
                                              k, mem);
    return maxPartitionsAfterOperations(s, i + 1, nextCanChange, newMask, k,
                                        mem);
  }
};
```

---

## 🧠 Dry Run
### Input
```
s = "accca", k = 2
```
### Steps
```
Without change: partitions are "accc" (2 distinct) | "a" → 2 partitions

With change at index 3 (c→b): "accba"
  "ac" (2 distinct) | "cb" (2 distinct) | "a" → 3 partitions

The DP explores all change options and returns max = 3

Output: 3
```

---

## ⏱️ Time Complexity
```
O(n * 2^26 * 2 * 26) — but memoization prunes heavily; practical runtime is much smaller
```

## 💾 Space Complexity
```
O(n * 2^26 * 2) — memoization table (in practice much smaller due to reachable states)
```

---

## ⚠️ Edge Cases
- `k = 26`: Only one partition possible regardless of changes.
- `k = 1`: Every different character forces a new partition.
- String with all same characters: changing one character at a boundary can maximize splits.
- Already optimal: no change helps.

---

## 🎯 Interview Takeaways
- Bitmask DP is powerful for tracking character sets (up to 26 lowercase letters = 26 bits).
- The key compression `(i << 27 | canChange << 26 | mask)` fits the state into a single long.
- `popcount` efficiently counts set bits (distinct characters).
- Exploring all 26 change options at each position is feasible when combined with memoization.

---

## 📌 Key Pattern
👉 **"Bitmask DP with optional single modification for partition maximization"**

---

## 🔁 Related Problems
- 2405. Optimal Partition of String
- 763. Partition Labels
- 1239. Maximum Length of a Concatenated String with Unique Characters

---

## 🚀 Final Thoughts
This Hard problem combines greedy partitioning with DP exploration of a single character change. The bitmask representation of character sets is elegant and enables efficient state tracking. The key insight is that changing one character strategically can force additional partition boundaries.

---

✨ **Rule to remember:**
> Use bitmask DP to track character sets in partitioning problems — popcount gives distinct character count in O(1).
