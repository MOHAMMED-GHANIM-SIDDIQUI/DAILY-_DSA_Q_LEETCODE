# 3307. Find the K-th Character in String Game II

## 🔗 Problem Link
https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Bit Manipulation, Math, Recursion

---

## 🧩 Problem Summary
Alice starts with `"a"` and performs operations that double the string. Each operation either copies the string as-is (operation 0) or increments each character by 1 with wrap-around (operation 1). Given `k` and the operations array, find the k-th character.

### 📌 Constraints
- `1 <= k <= 10^14`
- `1 <= operations.length <= 100`
- `operations[i]` is 0 or 1

---

## 💭 Intuition
👉 Work backwards: at each step, determine if `k` is in the left half (original) or right half (transformed). If it's in the right half, shift it to the left half and accumulate the operation's increment.

---

## ⚡ Approach — Reverse Simulation with Binary Decomposition

### 🧠 Idea
- Determine how many operations are needed: `ceil(log2(k))`.
- Iterate from the last relevant operation backwards.
- At each level, the string length is `2^i`. If `k > halfSize`, it came from the right half — subtract `halfSize` and add the operation value.
- The final answer is `'a' + (total increments % 26)`.

---

## 💻 Code

```cpp
class Solution {
 public:
  char kthCharacter(long long k, vector<int>& operations) {
    const int operationsCount = ceil(log2(k));
    int increases = 0;

    for (int i = operationsCount - 1; i >= 0; --i) {
      const long halfSize = 1L << i;
      if (k > halfSize) {
        k -= halfSize;  // Move k from the right half to the left half.
        increases += operations[i];
      }
    }

    return 'a' + increases % 26;
  }
};
```

---

## 🧠 Dry Run
### Input
```
k = 5, operations = [0, 0, 1]
```
### Steps
```
operationsCount = ceil(log2(5)) = 3
i=2: halfSize=4, k=5 > 4 → k=1, increases += operations[2]=1 → increases=1
i=1: halfSize=2, k=1 <= 2 → skip
i=0: halfSize=1, k=1 <= 1 → skip
result = 'a' + 1 = 'b'
```

---

## ⏱️ Time Complexity
```
O(log k) — iterating through at most log2(k) operations
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- `k = 1` → always `'a'` (no operations affect position 1)
- All operations are 0 → answer is always `'a'`
- Wrap-around: increases can exceed 26, so `% 26` is essential

---

## 🎯 Interview Takeaways
- Working backwards through doubling operations avoids building the exponentially large string.
- The structure mirrors binary decomposition of the index.

---

## 📌 Key Pattern
👉 **"Reverse simulation through doubling steps using binary decomposition"**

---

## 🔁 Related Problems
- 3304. Find the K-th Character in String Game I
- 1545. Find Kth Bit in Nth Binary String

---

## 🚀 Final Thoughts
This extends the Game I version by supporting different operations per step. The reverse traversal elegantly handles the exponential string without materializing it.

---

✨ **Rule to remember:**
> "For doubling-string problems, trace backwards — right half means the operation was applied."
