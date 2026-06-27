# 3699. Number of ZigZag Arrays I

## 🔗 Problem Link
https://leetcode.com/problems/number-of-zigzag-arrays-i/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Dynamic Programming, Prefix Sum

---

## 🧩 Problem Summary

Count the number of arrays of length `n` where:
- every element lies in `[l, r]`,
- no two adjacent elements are equal, and
- the array **strictly alternates** up/down (zigzag) — there are never three consecutive strictly increasing or strictly decreasing elements.

Return the count modulo `1e9 + 7`.

### 📌 Constraints
- `2 <= n <= 1000` (a per-layer `O(m)` DP is fast enough here)
- `1 <= l <= r <= 1000`, with `m = r - l + 1` distinct values
- Adjacent elements differ, and the comparison direction flips at every step.

---

## 💭 Intuition

👉 Build the array left to right. The only thing the next choice depends on is **the current last value** and **which direction the next step must take** (because zigzag forces the direction to alternate). If we fix the parity of the position, the required direction is determined, so we just need, for each value `v`, how many zigzag arrays end at `v`.

The transition "next value must be strictly greater (or smaller) than the previous" is a sum over a contiguous range of values, so a **prefix sum** (for "up" steps) or **suffix sum** (for "down" steps) collapses each layer to `O(m)`.

---

## ⚡ Approach — Layered DP with prefix/suffix sums

### 🧠 Idea
- `dp[v]` = number of zigzag arrays built so far that end at value index `v` (where `v = 0` maps to `l`, `v = m-1` maps to `r`), with the direction required so far satisfied.
- Initialize `dp = [1] * m`: a single-element array can end at any of the `m` values.
- For each subsequent position `i` from `1` to `n-1`:
  - On **odd `i`** the new value must be **larger** than the previous (an "up" step). For value `v`, the count is the sum of `dp[0..v-1]` — accumulate a running **prefix sum** `pref` as `v` increases.
  - On **even `i`** the new value must be **smaller** than the previous (a "down" step). For value `v`, the count is the sum of `dp[v+1..m-1]` — accumulate a running **suffix sum** `suff` as `v` decreases.
- The code fixes the *first* step direction implicitly; multiplying the final total by `2` accounts for the two possible starting directions (first step up vs. first step down).

---

## 💻 Code

```python
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7

        m = r - l + 1

        # dp[v] = number of ways ending with value v
        dp = [1] * m

        for i in range(1, n):
            ndp = [0] * m

            if i % 2 == 1:
                # previous value must be smaller
                pref = 0
                for v in range(m):
                    ndp[v] = pref
                    pref = (pref + dp[v]) % MOD
            else:
                # previous value must be larger
                suff = 0
                for v in range(m - 1, -1, -1):
                    ndp[v] = suff
                    suff = (suff + dp[v]) % MOD

            dp = ndp

        return (2 * sum(dp)) % MOD
```

---

## 🧠 Dry Run

### Input
```
n = 3, l = 1, r = 3   ->   m = 3 values: {1, 2, 3}
```

### Steps
```
dp init (length-1 arrays): dp = [1, 1, 1]   (end at 1, 2, 3)

i = 1 (odd, "up": prev smaller -> prefix sum of dp[0..v-1]):
  v=0: ndp[0]=pref(0)=0; pref=1
  v=1: ndp[1]=pref(1)=1; pref=2
  v=2: ndp[2]=pref(2)=2
  dp = [0, 1, 2]
     (ways ending at value index v after an up step)

i = 2 (even, "down": prev larger -> suffix sum of dp[v+1..m-1]):
  v=2: ndp[2]=suff(0)=0; suff=2
  v=1: ndp[1]=suff(2)=2; suff=3
  v=0: ndp[0]=suff(3)=3
  dp = [3, 2, 0]

sum(dp) = 5
answer = 2 * 5 = 10  (mod 1e9+7)
```

The factor of 2 covers both starting directions, giving all zigzag arrays of length 3 over {1,2,3}.

---

## ⏱️ Time Complexity
```
O(n * m)
```
There are `n - 1` layers; each layer does a single linear pass over the `m` values using a running prefix/suffix sum.

---

## 💾 Space Complexity
```
O(m)
```
Only two arrays of length `m` (`dp` and `ndp`) are kept at a time.

---

## ⚠️ Edge Cases
- `l == r` (`m == 1`): no array can have distinct adjacent elements for `n >= 2`; the first "up" layer makes `dp = [0]`, so the answer is `0`.
- `n == 2`: after one transition, `sum(dp)` counts ordered pairs with one direction; the `* 2` gives all valid adjacent-distinct pairs.
- Large values: every addition is taken `mod 1e9 + 7`, including the final doubling.

---

## 🎯 Interview Takeaways
- "Next element strictly greater/less than the previous" is a **range-sum transition** — prefix/suffix sums turn an `O(m^2)` layer into `O(m)`.
- Zigzag's alternating constraint means the required direction is a pure function of position parity, so you never need to store the direction in the state.
- Doubling at the end is a clean way to handle the symmetric "starts up" vs "starts down" cases.

---

## 📌 Key Pattern
👉 **"Alternating-direction DP: parity fixes the comparison, and a prefix/suffix sum collapses the 'greater/less than previous' transition to linear time."**

---

## 🔁 Related Problems
- Number of ZigZag Arrays II
- 376. Wiggle Subsequence
- 1955. Count Number of Special Subsequences
- 1186. Maximum Subarray Sum with One Deletion

---

## 🚀 Final Thoughts
This is a model example of how a seemingly quadratic counting DP becomes linear per layer once you recognize the transition is a contiguous range sum. The prefix sum handles "must be larger", the suffix sum handles "must be smaller", and the alternation of zigzag is what lets you pick one or the other purely from the position index. Keep this prefix/suffix-sum-over-DP trick handy — it generalizes to many "monotone neighbor" counting problems.

---

✨ **Rule to remember:**
> "When a DP transition sums over all previous values below/above the current one, replace the inner loop with a running prefix/suffix sum."
