# 717. 1-bit and 2-bit Characters

## 🔗 Problem Link
https://leetcode.com/problems/1-bit-and-2-bit-characters/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Greedy

---

## 🧩 Problem Summary
Given a binary array bits where the last element is always 0, determine if the last character must be a one-bit character (0). Characters are either one-bit (0) or two-bit (10 or 11). Decode greedily from left to right.

### 📌 Constraints
- `1 <= bits.length <= 1000`
- `bits[i]` is `0` or `1`
- `bits[bits.length - 1] == 0`

---

## 💭 Intuition
👉 Greedily decode from left to right: if the current bit is 0, it's a one-bit character (skip 1); if it's 1, it's a two-bit character (skip 2). If we land exactly on the last index, the last character is a one-bit character.

---

## ⚡ Approach — Greedy Linear Scan

### 🧠 Idea
- Start from index 0.
- If `bits[i] == 0`, advance by 1 (one-bit character).
- If `bits[i] == 1`, advance by 2 (two-bit character).
- Continue until we reach or pass the last index.
- If we land exactly on `n - 1`, the last character is one-bit; return true.

---

## 💻 Code

```cpp
class Solution {
 public:
  bool isOneBitCharacter(vector<int>& bits) {
    const int n = bits.size();

    int i = 0;
    while (i < n - 1)
      if (bits[i] == 0)
        i += 1;
      else
        i += 2;

    return i == n - 1;
  }
};
```

---

## 🧠 Dry Run
### Input
```
bits = [1, 0, 0]
```
### Steps
```
i=0: bits[0]=1 -> i+=2 -> i=2
i=2: 2 < 2? No (n-1=2), exit loop
i == n-1? 2 == 2 -> true
Result: true (decoded as [10, 0])
```

---

## ⏱️ Time Complexity
```
O(n) — single pass through the array
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- `bits = [0]` — single element, always true.
- `bits = [1, 1, 0]` — two-bit [11] then one-bit [0], returns true.
- `bits = [1, 0]` — two-bit [10], i jumps to 2 which is past n-1=1, returns false.
- Long sequence of 1s followed by 0 — depends on parity of 1s.

---

## 🎯 Interview Takeaways
- Greedy decoding from left to right is the natural approach.
- The key observation is that 1 always starts a two-bit character.
- The answer depends on whether the greedy scan lands on or skips the last position.

---

## 📌 Key Pattern
👉 **"Greedy decoding — 0 means skip 1, 1 means skip 2, check if you land on the last index"**

---

## 🔁 Related Problems
- 91. Decode Ways
- 338. Counting Bits

---

## 🚀 Final Thoughts
This is a simple greedy problem that tests understanding of variable-length encoding. The solution is elegant in its simplicity — just scan and skip, then check the landing position.

---

✨ **Rule to remember:**
> "Greedily decode left to right: if you land exactly on the last bit, it's a one-bit character."
