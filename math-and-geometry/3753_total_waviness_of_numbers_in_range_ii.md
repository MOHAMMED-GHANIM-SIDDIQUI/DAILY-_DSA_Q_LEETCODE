# 3753. Total Waviness of Numbers in Range II

## 🔗 Problem Link
https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Math, Dynamic Programming, Digit DP

---

## 🧩 Problem Summary

The **waviness** of a number is the count of its digit **peaks** and **valleys**:
- A *middle* digit (not the first, not the last) that is strictly greater than **both** neighbors is a **peak**.
- A middle digit that is strictly less than **both** neighbors is a **valley**.
- The first and last digits never count.
- Numbers with fewer than 3 digits have waviness `0`.

Return the **sum of waviness** over every integer in the inclusive range `[num1, num2]`.

### 📌 Constraints
- `1 <= num1 <= num2 <= 10^18` (large range — must use digit DP, not enumeration)

---

## 💭 Intuition

👉 The range can be astronomically large, so we cannot iterate. Instead we compute `f(n) =` total waviness of all integers in `[1, n]`, and use the prefix-difference `solve(num2) - solve(num1 - 1)`. To accumulate waviness while building numbers digit by digit, we carry the **last two placed digits** in the DP state. The moment we place a new digit, the previously-placed digit becomes a confirmed *middle* digit with both neighbors known, so we can decide right then whether it was a peak or valley and add it to the running total — multiplied by how many full numbers extend from that prefix.

---

## ⚡ Approach — Digit DP returning (count, total_waviness)

### 🧠 Idea
- `solve(n)` runs a digit DP over the decimal string `s = str(n)`.
- State `dfs(pos, tight, started, prev1, prev2)`:
  - `pos`: current digit index.
  - `tight`: whether the prefix equals `n`'s prefix (limits the digit choice).
  - `started`: whether a non-zero digit has appeared (handles leading zeros).
  - `prev1`: the **last** placed digit (`10` = sentinel "none").
  - `prev2`: the **second-to-last** placed digit (`10` = sentinel "none").
- Each call returns a pair `(count_of_numbers, total_waviness)`.
- When placing digit `d` and both `prev1` and `prev2` are real digits, `prev1` is now a confirmed middle digit between `prev2` (left) and `d` (right). It contributes `1` of waviness if `prev1 > prev2 and prev1 > d` (peak) **or** `prev1 < prev2 and prev1 < d` (valley). That `add` is multiplied by the `count` of numbers that complete this prefix.
- Leading zeros keep `started = False` and reset both prevs to the sentinel, so they never form spurious peaks/valleys.
- Final answer: `solve(num2) - solve(num1 - 1)`.

---

## 💻 Code

```python
from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(n: int) -> int:
            if n <= 0:
                return 0

            s = str(n)

            @lru_cache(None)
            def dfs(pos, tight, started, prev1, prev2):
                # returns (count_numbers, total_waviness)
                if pos == len(s):
                    return (1, 0)

                limit = int(s[pos]) if tight else 9
                total_cnt = 0
                total_wav = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if not started and d == 0:
                        cnt, wav = dfs(pos + 1, ntight, False, 10, 10)
                        total_cnt += cnt
                        total_wav += wav
                    else:
                        if not started:
                            cnt, wav = dfs(pos + 1, ntight, True, d, 10)
                            total_cnt += cnt
                            total_wav += wav
                        elif prev2 == 10:
                            cnt, wav = dfs(pos + 1, ntight, True, d, prev1)
                            total_cnt += cnt
                            total_wav += wav
                        else:
                            add = int(
                                (prev1 > prev2 and prev1 > d) or
                                (prev1 < prev2 and prev1 < d)
                            )

                            cnt, wav = dfs(pos + 1, ntight, True, d, prev1)

                            total_cnt += cnt
                            total_wav += wav + add * cnt

                return total_cnt, total_wav

            # subtract the "all-leading-zero" number
            return dfs(0, True, False, 10, 10)[1]

        return solve(num2) - solve(num1 - 1)
```

---

## 🧠 Dry Run

### Input
```
num1 = 120, num2 = 121
```
We only walk through the single number `121` to show how a peak is detected (the actual answer is `solve(121) - solve(119)`).

### Steps
```
Build "121" digit by digit (tight branch):

pos=0, started=False, prev1=10, prev2=10
  place d=1 (started becomes True) -> dfs(pos=1, started=True, prev1=1, prev2=10)

pos=1, prev1=1, prev2=10  (prev2 is sentinel -> no waviness yet)
  place d=2 -> dfs(pos=2, started=True, prev1=2, prev2=1)

pos=2, prev1=2, prev2=1  (both real digits now)
  place d=1:
    check prev1=2 vs prev2=1 (left) and d=1 (right)
    prev1 > prev2 (2 > 1) and prev1 > d (2 > 1) -> PEAK -> add = 1
    cnt from completing = 1
    total_wav += add * cnt = 1

So 121 contributes waviness 1 (the middle '2' is a peak).
```

The digit `2` sits between `1` and `1` and is strictly greater than both — exactly one peak, waviness `1`, matching the definition.

---

## ⏱️ Time Complexity
```
O(L * 2 * 2 * 11 * 11 * 10)
```
Where `L` is the number of digits (about 19 for `10^18`). The memoized state space is `pos x tight x started x prev1 x prev2`, and each state loops over 10 digit choices — effectively constant per call, so overall `O(L)` up to constant factors. Called twice (for `num2` and `num1 - 1`).

---

## 💾 Space Complexity
```
O(L * 11 * 11)
```
Dominated by the `lru_cache` memo table over the DP states, plus `O(L)` recursion depth.

---

## ⚠️ Edge Cases
- `num1 = 1`: `solve(num1 - 1) = solve(0)` returns `0`, so single-digit and two-digit numbers correctly contribute `0` waviness.
- Leading zeros never create fake peaks/valleys because they keep `started = False` and reset the prev sentinels.
- A digit equal (not strictly greater/less) to a neighbor is neither peak nor valley — the strict comparisons handle plateaus correctly.
- Numbers with fewer than 3 digits: at most one real `prev1` is ever set before the end, so the `prev2 == 10` branch fires and nothing is added.

---

## 🎯 Interview Takeaways
- Range-sum problems over `[a, b]` collapse to `f(b) - f(a - 1)` with a `[1, n]` counting function.
- Carrying the **two previous digits** is the standard trick to evaluate a local 3-digit shape (peak/valley) during digit DP.
- Returning `(count, accumulated_metric)` together lets you weight each local contribution by how many numbers share that prefix.
- Handle leading zeros explicitly so they don't pollute the adjacency window.

---

## 📌 Key Pattern
👉 **"Digit DP carrying the last two digits, returning (count, total), and crediting waviness the moment a middle digit's right neighbor is fixed."**

---

## 🔁 Related Problems
- 233. Number of Digit One
- 902. Numbers At Most N Given Digit Set
- 1397. Find All Good Strings
- 600. Non-negative Integers without Consecutive Ones

---

## 🚀 Final Thoughts
The elegance here is recognizing that a peak/valley is a purely *local* 3-digit pattern, so it can be scored the instant the third digit lands — no need to inspect the finished number. By pairing the count of completing numbers with the running waviness total in a single DP return, every prefix's contribution scales correctly across all its extensions. The leading-zero bookkeeping and the strict-inequality checks are the subtle pieces that make the count exact.

---

✨ **Rule to remember:**
> "To sum a local digit property over a huge range, carry just enough recent digits in the DP state and credit the property the moment its window is complete, weighted by the count of numbers finishing that prefix."
