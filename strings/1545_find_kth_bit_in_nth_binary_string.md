# 1545. Find Kth Bit in Nth Binary String

## 🔗 Problem Link
https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

## ⚡ Difficulty
Medium

## 🏷️ Topics
String, Recursion, Simulation

---

## 🧩 Problem Summary
Given two integers `n` and `k`, construct the nth binary string using the rule: `S1 = "0"`, and `Si = Si-1 + "1" + reverse(invert(Si-1))`. Return the kth bit (1-indexed) in `Sn`.

### 📌 Constraints
- `1 <= n <= 20`
- `1 <= k <= 2^n - 1`

---

## 💭 Intuition
👉 The string `Sn` has length `2^n - 1`. The middle element is always '1'. If `k` falls in the first half, recurse on `Sn-1`. If `k` falls in the second half, it maps to a mirrored and inverted position in `Sn-1`.

---

## ⚡ Approach — Recursion (Divide and Conquer)

### 🧠 Idea
- Base case: `n == 1` returns '0'.
- Compute `total_len = 2^n - 1` and `half_len = total_len // 2 + 1` (1-indexed middle).
- If `k == half_len`, return '1' (middle is always '1').
- If `k < half_len`, recurse: `findKthBit(n-1, k)`.
- If `k > half_len`, recurse on the mirrored position and invert: the mirrored index is `half_len - (k - half_len)`.

---

## 💻 Code

```python
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # s1 = 0
        # s2 = s1 + 1 + ~ s1[::-1]
        # S3 = S2 + 1 + ~s2[::-1]
        # s4 ----> 15-----> 7 (s3) + 1 [8th idx] + 7 (~s3[::-1])
        # k- half
        if n == 1 :
            return '0'
        total_len = (1<<n) - 1
        half_len = ( total_len // 2 ) + 1
        if k == half_len:
            return '1'
        elif k < half_len:
            return self.findKthBit(n-1,k)
        else:
            k = half_len - ( k - half_len )
            d=self.findKthBit(n-1,k)
            return  '0' if d == '1' else '1'
```

---

## 🧠 Dry Run
### Input
```
n = 3, k = 5
```
### Steps
```
S1 = "0"
S2 = "0" + "1" + "1" = "011"
S3 = "011" + "1" + "001" = "0111001"

n=3, k=5: total_len=7, half_len=4
  k=5 > 4 → mirror: k = 4 - (5-4) = 3, invert result of findKthBit(2, 3)

n=2, k=3: total_len=3, half_len=2
  k=3 > 2 → mirror: k = 2 - (3-2) = 1, invert result of findKthBit(1, 1)

n=1, k=1: return '0'

Back to n=2: invert '0' → '1'
Back to n=3: invert '1' → '0'

Answer: '0' (S3[5] = "0111001"[5] = '0') ✓
```

---

## ⏱️ Time Complexity
```
O(n), one recursive call per level
```

## 💾 Space Complexity
```
O(n) for the recursion stack
```

---

## ⚠️ Edge Cases
- `n = 1` — always returns '0'.
- `k` is exactly the middle — always returns '1'.
- `k = 1` — always returns '0' (first bit is always '0').

---

## 🎯 Interview Takeaways
- No need to construct the actual string — use the recursive structure.
- The string has a mirror-and-invert symmetry around its center.
- Bit shifting `(1 << n)` efficiently computes `2^n`.

---

## 📌 Key Pattern
👉 **"Recursively locate position in a self-similar string by comparing to the midpoint"**

---

## 🔁 Related Problems
- 779 — K-th Symbol in Grammar
- 1738 — Find Kth Largest XOR Coordinate Value
- 894 — All Possible Full Binary Trees

---

## 🚀 Final Thoughts
This problem showcases how recursive string construction can be navigated without materializing the string. By recognizing the mirror-and-invert structure, we reduce each query to a single recursive call, achieving O(n) time.

---

✨ **Rule to remember:**
> "For recursively defined symmetric strings, compare k to the midpoint: left half recurses directly, right half mirrors and inverts."
