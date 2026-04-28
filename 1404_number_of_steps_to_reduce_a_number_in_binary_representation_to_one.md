# 1404. Number of Steps to Reduce a Number in Binary Representation to One

## 🔗 Problem Link
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

## ⚡ Difficulty
Medium

## 🏷️ Topics
String, Bit Manipulation

---

## 🧩 Problem Summary
Given the binary representation of an integer as a string `s`, return the number of steps to reduce it to `1` under the following rules: if the current number is even, divide it by 2; if it is odd, add 1 to it.

### 📌 Constraints
- `1 <= s.length <= 500`
- `s[0] == '1'`
- `s` consists of characters `'0'` or `'1'`.

---

## 💭 Intuition
👉 Process bits from right to left (LSB to MSB). If the current bit plus carry is `1` (odd), we need two operations: add 1 (which sets carry) then divide. If even, just divide (one operation). Handle the final carry at the MSB.

---

## ⚡ Approach — Right-to-Left Bit Processing with Carry

### 🧠 Idea
- Traverse from the rightmost bit to the second bit (skip MSB).
- If `bit + carry == 1` (odd): 2 operations (add 1 + divide), set carry = 1.
- If `bit + carry == 0 or 2` (even): 1 operation (divide only); carry stays 0 or 1 respectively.
- After the loop, add the carry (if MSB overflows, one extra step).

---

## 💻 Code

```python
class Solution:
    def numSteps(self, s: str) -> int:
        ops = 0
        carry = 0
        # Traverse from right to left (ignore first bit)
        for i in range(len(s) - 1, 0, -1):

            if int(s[i]) + carry == 1:
                # odd → add 1 + divide
                ops += 2
                carry = 1
            else:
                # even → divide only
                ops += 1

        # if carry remains at MSB, one extra operation
        return ops + carry
```

---

## 🧠 Dry Run
### Input
```
s = "1101"
```
### Steps
```
carry=0
i=3: bit='1', 1+0=1 (odd) → ops+=2=2, carry=1
i=2: bit='0', 0+1=1 (odd) → ops+=2=4, carry=1
i=1: bit='1', 1+1=2 (even) → ops+=1=5, carry stays 1
Final: ops + carry = 5 + 1 = 6
```

---

## ⏱️ Time Complexity
```
O(n) where n is the length of the binary string
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- `s = "1"` → already 1, return 0 (loop doesn't execute, carry=0)
- `s = "10"` → one divide, return 1
- Very long binary strings (up to 500 digits) — no integer overflow since we process bit by bit

---

## 🎯 Interview Takeaways
- Processing binary from right to left avoids big-integer arithmetic.
- The carry propagation mirrors how binary addition works.
- Odd → 2 ops (add + divide), Even → 1 op (divide) is the core logic.

---

## 📌 Key Pattern
👉 **"Simulate binary operations bit-by-bit from LSB to MSB with carry tracking."**

---

## 🔁 Related Problems
- 1342. Number of Steps to Reduce a Number to Zero
- 1073. Adding Two Negabinary Numbers
- 67. Add Binary

---

## 🚀 Final Thoughts
An elegant bit-manipulation problem that avoids converting to actual integers. Processing from the LSB with a carry variable cleanly handles arbitrarily large binary numbers.

---

✨ **Rule to remember:**
> Odd bit + carry = 1 costs 2 steps (add then divide); even costs 1 step (just divide).
