# 868. Binary Gap

## 🔗 Problem Link
https://leetcode.com/problems/binary-gap/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Bit Manipulation

---

## 🧩 Problem Summary

Given a positive integer `n`, find and return the longest distance between any two adjacent `1`s in the binary representation of `n`. If there are no two adjacent `1`s, return 0.

### 📌 Constraints
- `1 <= n <= 10^9`

---

## 💭 Intuition

We need to find the maximum gap between consecutive 1-bits. 👉 Iterate through bits from right to left, tracking the index of the previous `1` bit. Whenever we find a new `1`, compute the distance from the previous one and update the maximum.

---

## ⚡ Approach — Bit Traversal with Previous Index Tracking

### 🧠 Idea

- Use a variable `prev` to store the index of the last seen `1` bit (initialized to -1).
- Use `idx` to track the current bit position.
- Right-shift `n` one bit at a time, checking the least significant bit.
- When a `1` is found and `prev != -1`, update the answer with `idx - prev`.

---

## 💻 Code

```python
class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        prev = -1
        idx=0
        while n:
            if n&1==1 :
                if prev!=-1:
                    ans=max(ans,idx-prev)
                prev=idx
            n>>=1
            idx+=1

        return ans
```

---

## 🧠 Dry Run

### Input
```
n = 22  (binary: 10110)
```

### Steps
```
idx=0: bit=0, skip
idx=1: bit=1, prev=-1 → prev=1
idx=2: bit=1, prev=1 → ans=max(0, 2-1)=1, prev=2
idx=3: bit=0, skip
idx=4: bit=1, prev=2 → ans=max(1, 4-2)=2, prev=4
n=0, loop ends
Return 2
```

---

## ⏱️ Time Complexity

```
O(log n)
```

We process each bit of n exactly once.

---

## 💾 Space Complexity

```
O(1)
```

Only a few integer variables used.

---

## ⚠️ Edge Cases

- **Power of 2:** `n = 8` (1000) → only one `1` bit → 0
- **All bits set:** `n = 7` (111) → gap is 1
- **n = 1:** Single bit → 0

---

## 🎯 Interview Takeaways

- Tracking the previous occurrence of a condition while iterating is a common pattern.
- Bit-by-bit traversal using `n & 1` and `n >>= 1` is the standard way to inspect binary digits.
- Initialize `prev = -1` to handle the "no previous 1 seen" case cleanly.

---

## 📌 Key Pattern

👉 **"Track previous 1-bit position while scanning bits right to left"**

---

## 🔁 Related Problems

- 191. Number of 1 Bits
- 693. Binary Number with Alternating Bits
- 762. Prime Number of Set Bits in Binary Representation

---

## 🚀 Final Thoughts

A straightforward bit manipulation problem. The key is maintaining the index of the last seen set bit and computing distances on the fly.

---

✨ **Rule to remember:**
> To find the longest gap between 1-bits, track the last seen 1's position and take the max distance.
