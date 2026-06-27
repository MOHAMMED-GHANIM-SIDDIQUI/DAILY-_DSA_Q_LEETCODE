# 3614. Process String with Special Operations II

## 🔗 Problem Link
https://leetcode.com/problems/process-string-with-special-operations-ii/

## ⚡ Difficulty
Hard

## 🏷️ Topics
String, Simulation

---

## 🧩 Problem Summary

Same operations as version I — a lowercase letter appends, `'*'` deletes the last char, `'#'` duplicates the string, `'%'` reverses it — but here repeated `'#'` operations make the final string astronomically large (doubling each time). Instead of returning the whole string, you must return only the single character at index `k`, or `'.'` if `k` is out of range, all without ever materializing the string.

### 📌 Constraints
- `1 <= s.length <= 10^5`
- `s` consists of lowercase letters and `'*'`, `'#'`, `'%'`.
- `0 <= k` can be very large; the final string may be exponentially long.
- Return the char at index `k`, or `'.'` if `k >= finalLength`.

---

## 💭 Intuition

👉 You can never build the exponential string, but you can track its *length* cheaply, then walk the operations backwards, repeatedly translating "which index am I looking for now" until you reach the exact letter that produced it.

---

## ⚡ Approach — Forward Length Pass + Reverse Index Mapping

### 🧠 Idea
- **Forward pass:** simulate only the length. A letter adds 1; `'*'` subtracts 1 (if non-empty); `'#'` doubles the length; `'%'` leaves length unchanged.
- If `k >= length` after the full forward pass, the index is out of range → return `'.'`.
- **Reverse pass:** iterate operations from last to first, undoing each one and remapping `k` to the index it corresponded to *before* that operation:
  - Letter: this op added the last char. If `k == length - 1`, that last char is exactly the answer → return `ch`. Otherwise `k` lies in the earlier part, so decrement `length`.
  - `'*'`: it had removed a char, so restore `length += 1` (k unaffected — it indexes within the still-present prefix).
  - `'#'`: the string was `half + half`. If `k >= half`, it came from the second copy → subtract `half`. Set `length = half`.
  - `'%'`: a reversal maps index `k` to `length - 1 - k`.
- If nothing returns, fall through to `'.'`.

---

## 💻 Code

```python
class Solution:
    def processStr(self, s: str, k: int) -> str:
        # Compute final length
        length = 0

        for ch in s:
            if 'a' <= ch <= 'z':
                length += 1
            elif ch == '*':
                if length:
                    length -= 1
            elif ch == '#':
                length *= 2
            else:  # %
                pass

        if k >= length:
            return '.'

        # Reverse simulation
        for ch in reversed(s):
            if 'a' <= ch <= 'z':
                if k == length - 1:
                    return ch
                length -= 1

            elif ch == '*':
                length += 1

            elif ch == '#':
                half = length // 2
                if k >= half:
                    k -= half
                length = half

            else:  # %
                k = length - 1 - k

        return '.'
```

---

## 🧠 Dry Run

### Input
```
s = "ab%#", k = 5
```

### Steps
```
Forward length pass:
  'a' letter -> length = 1
  'b' letter -> length = 2
  '%' reverse-> length = 2
  '#' double -> length = 4

k = 5, length = 4  ->  k >= length  ->  return '.'
```

Second example to show a hit:
```
Input: s = "ab%#", k = 3

Forward: length = 4 (as above).  k=3 < 4, continue.

Reverse over "ab%#" reversed = ['#','%','b','a']:
  ch='#': half = 4//2 = 2; k=3 >= 2 -> k = 3-2 = 1; length = 2
  ch='%': k = length-1-k = 2-1-1 = 0
  ch='b': k == length-1? 0 == 1? no -> length = 1
  ch='a': k == length-1? 0 == 0? yes -> return 'a'

Answer: 'a'
```

---

## ⏱️ Time Complexity
```
O(n)
```
One forward pass and one reverse pass over the `n` operations; each step is O(1) arithmetic.

---

## 💾 Space Complexity
```
O(1)
```
Only integer counters (`length`, `half`, `k`) are tracked; the giant string is never built. (Big integers from doubling are the only growth.)

---

## ⚠️ Edge Cases
- `k >= length` → returns `'.'` immediately after the forward pass.
- `'*'` on empty during forward pass is guarded by `if length`.
- `'%'` does not change length, only remaps index during reverse.
- `'#'` with odd intermediate handling is impossible since doubling always yields even halves of the current state at undo time (`length // 2` is exact for a `'#'` op).

---

## 🎯 Interview Takeaways
- For exponentially large constructed strings, track size forward and back-map the queried index in reverse.
- Each operation has a clean inverse on a single index: append→maybe-answer-or-decrement, delete→length+1, duplicate→fold into half, reverse→mirror.
- Avoid materializing data when only one element is queried — work with indices and lengths.

---

## 📌 Key Pattern
👉 **"Reverse-engineer the index: undo operations from the end, remapping k until it lands on the source character."**

---

## 🔁 Related Problems
- 3612. Process String with Special Operations I
- 880. Decoded String at Index
- 2390. Removing Stars From a String

---

## 🚀 Final Thoughts
This is the canonical "decoded string at index" trick generalized to four operations. The key realization is that doubling forbids construction, but every operation is invertible on a single position. Computing the final length first lets you reject out-of-range queries, and the reverse walk peels operations off one at a time until `k` points at the actual letter that generated it.

---

✨ **Rule to remember:**
> "When the string is too big to build, don't build it — track its length forward and map the target index backward to its origin."
