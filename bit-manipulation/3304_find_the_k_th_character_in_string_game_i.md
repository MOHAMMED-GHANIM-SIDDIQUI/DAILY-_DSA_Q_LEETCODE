# 3304. Find the K-th Character in String Game I

## 🔗 Problem Link
https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Bit Manipulation, Math, Simulation

---

## 🧩 Problem Summary
Alice starts with the string `"a"` and repeatedly appends a transformed copy of the current string by incrementing each character by one. Given an integer `k`, return the k-th character (1-indexed) of the resulting string after enough operations.

### 📌 Constraints
- `1 <= k <= 500`
- The string grows exponentially (doubles each step)

---

## 💭 Intuition
👉 The k-th character's value depends on how many times it was "incremented" during the doubling process. Each time `k` falls in the right half of a doubling step, it gets +1. The number of times this happens equals the number of set bits (popcount) of `k - 1`.

---

## ⚡ Approach — Bit Counting (Popcount)

### 🧠 Idea
- Convert the problem to counting how many times the character at position `k` was derived from an increment operation.
- Each doubling step either keeps the character (left half) or increments it (right half).
- The number of increments equals `popcount(k - 1)`.

---

## 💻 Code

```cpp
class Solution {
 public:
  char kthCharacter(unsigned k) {
    return 'a' + popcount(k - 1);
  }
};
```

---

## 🧠 Dry Run
### Input
```
k = 5
```
### Steps
```
k - 1 = 4 = 0b100
popcount(4) = 1
result = 'a' + 1 = 'b'
```

---

## ⏱️ Time Complexity
```
O(log k) — for popcount computation
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- `k = 1` → always `'a'` (popcount(0) = 0)
- Large `k` near 500 → popcount handles it correctly

---

## 🎯 Interview Takeaways
- Recognizing the binary structure of doubling processes is key.
- `popcount` is a powerful tool for problems involving repeated halving/doubling.

---

## 📌 Key Pattern
👉 **"Bit manipulation to track transformations across doubling steps"**

---

## 🔁 Related Problems
- 3307. Find the K-th Character in String Game II
- 1545. Find Kth Bit in Nth Binary String

---

## 🚀 Final Thoughts
An elegant one-liner leveraging the insight that each bit in `k-1` represents a doubling step where the character was incremented. The popcount directly gives the shift from `'a'`.

---

✨ **Rule to remember:**
> "In doubling-string games, the answer hides in the binary representation of the index."
