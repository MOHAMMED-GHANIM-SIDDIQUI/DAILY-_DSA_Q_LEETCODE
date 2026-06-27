# 3700. Number of ZigZag Arrays II

## 🔗 Problem Link
https://leetcode.com/problems/number-of-zigzag-arrays-ii/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Dynamic Programming, Math, Matrix Exponentiation

---

## 🧩 Problem Summary

Same zigzag-array counting as version I: count length-`n` arrays where every element lies in `[l, r]`, adjacent elements differ, and the comparison direction strictly alternates (up, down, up, ... or down, up, down, ...). Return the count modulo `1e9 + 7`.

The twist: **`n` can be astronomically large**, so an `O(n * m)` layer-by-layer DP is far too slow. We instead express one DP step as a **linear transformation** on a fixed-size state vector and apply it `n - 2` times using **binary matrix exponentiation** in `O(log n)` matrix multiplications.

### 📌 Constraints
- `n` can be very large (e.g. up to `10^9`), forcing a `log n` approach.
- `1 <= l <= r`, with `m = r - l + 1` distinct values (small, so the `2m × 2m` matrix is affordable).
- Answer taken modulo `1e9 + 7`.

---

## 💭 Intuition

👉 The DP state for a position is "the last value `x`, and whether the last move was **up** or **down**". That's `2 * m` states total, and the recurrence from one position to the next is **linear and identical at every step** (it does not depend on the position). Any such fixed linear recurrence applied many times is exactly what a **matrix power** computes: build the `2m × 2m` transition matrix `T` once, raise it to `n - 2`, and you have folded all the intermediate steps together.

---

## ⚡ Approach — Matrix Exponentiation over a 2m-state DP

### 🧠 Idea
- Encode the state as a vector of size `sz = 2 * m`:
  - index `x` (for `0 <= x < m`) = arrays ending at value `x` whose **last move was up**,
  - index `m + x` = arrays ending at value `x` whose **last move was down**.
- Build transition matrix `T` (`sz × sz`):
  - **up → down**: an "up" state at value `a` can extend to a "down" move landing on any `b < a`. So `T[m + b][a] = 1` for all `b < a`.
  - **down → up**: a "down" state at value `a` can extend to an "up" move landing on any `b > a`. So `T[b][m + a] = 1` for all `b > a`.
- `mat_mul` multiplies two matrices mod `p` (with a zero-skip optimization); `mat_pow` does fast exponentiation via repeated squaring.
- Build the **length-2 initialization vector** `vec`: for every ordered pair of distinct values `(a, b)`, the second element `b` is reached by an up move (if `a < b`) or a down move (if `a > b`); accumulate into `vec[b]` or `vec[m + b]`.
- If `n == 2`, the answer is just `sum(vec)`. Otherwise compute `P = T^(n-2)` and the answer is the sum over all entries of `P · vec`.

---

## 💻 Code

```python
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7

        m = r - l + 1

        # State:
        # up[x]   = arrays ending at value x, last move was up
        # down[x] = arrays ending at value x, last move was down
        #
        # Total states = 2 * m

        sz = 2 * m

        T = [[0] * sz for _ in range(sz)]

        # up -> down
        for a in range(m):
            for b in range(a):
                T[m + b][a] = 1

        # down -> up
        for a in range(m):
            for b in range(a + 1, m):
                T[b][m + a] = 1

        def mat_mul(A, B):
            n = len(A)
            C = [[0] * n for _ in range(n)]

            for i in range(n):
                for k in range(n):
                    if A[i][k] == 0:
                        continue
                    aik = A[i][k]
                    for j in range(n):
                        if B[k][j]:
                            C[i][j] = (C[i][j] + aik * B[k][j]) % MOD
            return C

        def mat_pow(M, p):
            n = len(M)
            R = [[0] * n for _ in range(n)]
            for i in range(n):
                R[i][i] = 1

            while p:
                if p & 1:
                    R = mat_mul(R, M)
                M = mat_mul(M, M)
                p >>= 1

            return R

        # length = 2 initialization
        vec = [0] * sz

        for a in range(m):
            for b in range(m):
                if a == b:
                    continue
                if a < b:
                    vec[b] += 1      # last move up
                else:
                    vec[m + b] += 1  # last move down

        if n == 2:
            return sum(vec) % MOD

        P = mat_pow(T, n - 2)

        ans = 0
        for i in range(sz):
            cur = 0
            for j in range(sz):
                cur = (cur + P[i][j] * vec[j]) % MOD
            ans = (ans + cur) % MOD

        return ans
```

---

## 🧠 Dry Run

### Input
```
n = 3, l = 1, r = 2   ->   m = 2 values {1, 2}, sz = 4
state layout: [up@1, up@2, down@1, down@2]
```

### Steps (conceptual)
```
Build vec (all length-2 zigzag arrays):
  ordered distinct pairs (a, b):
    (0,1): a<b -> up   -> vec[1]   += 1   (array [1,2], last move up)
    (1,0): a>b -> down -> vec[2+0] += 1   (array [2,1], last move down)
  vec = [0, 1, 1, 0]

Build T (transition for one more element):
  up -> down: a=1 has b=0  -> T[2][1] = 1
  down -> up: a=0 has b=1  -> T[1][2] = 1
  (all other entries 0)

n = 3, so exponent = n - 2 = 1, P = T^1 = T.

Compute P · vec:
  row 0: T[0][*]·vec = 0
  row 1: T[1][2]*vec[2] = 1*1 = 1          -> array [2,1] extended up to [2,1,2]? 
         (down@1 -> up lands on value 2): contributes the length-3 array ending up
  row 2: T[2][1]*vec[1] = 1*1 = 1          (up@2 -> down lands on value 1)
  row 3: 0
  sum over all rows = 2

answer = 2   ->  the two length-3 zigzag arrays over {1,2}: [1,2,1] and [2,1,2]
```

For very large `n`, `mat_pow` squares `T` `O(log n)` times instead of stepping one position at a time, but the meaning of each multiply is identical to appending one element.

---

## ⏱️ Time Complexity
```
O(m^3 * log n)
```
Each matrix multiply of two `2m × 2m` matrices is `O((2m)^3) = O(m^3)`, and fast exponentiation performs `O(log n)` of them. The final matrix-vector product is `O(m^2)`, negligible by comparison.

---

## 💾 Space Complexity
```
O(m^2)
```
A constant number of `2m × 2m` matrices are stored at any time (the running result, the squared base, and one product buffer).

---

## ⚠️ Edge Cases
- `n == 2`: handled directly by returning `sum(vec)` without any matrix power (exponent would be `0`).
- `m == 1` (`l == r`): no distinct-adjacent pair exists, so `vec` stays all zeros and the answer is `0`.
- Huge `n`: `log n` keeps the work bounded; the `mod` inside every multiplication prevents overflow growth.
- The zero-skip checks (`if A[i][k] == 0` / `if B[k][j]`) speed up the sparse transition matrix considerably.

---

## 🎯 Interview Takeaways
- Any DP with a **fixed-size state** and a **position-independent linear recurrence** can be accelerated to `O(log n)` via matrix exponentiation.
- Encoding the "last move direction" into the state (doubling it to `2m`) is what makes the zigzag recurrence linear and time-invariant.
- Separate the **base case vector** (length-2 here) from the **repeated transition**, then apply the matrix `n - 2` times.

---

## 📌 Key Pattern
👉 **"Fixed linear recurrence applied n times → raise the transition matrix to the n-th power with binary exponentiation."**

---

## 🔁 Related Problems
- Number of ZigZag Arrays I
- 70. Climbing Stairs (matrix-power form)
- 509. Fibonacci Number (matrix exponentiation)
- 1137. N-th Tribonacci Number

---

## 🚀 Final Thoughts
Version I solves the same counting problem with a per-layer prefix-sum DP that is `O(n * m)`; version II keeps the identical state model but recognizes the transition is linear and unchanging, so the entire chain of `n` steps compresses into `T^(n-2)`. The art is choosing the state — "(value, last direction)" — so that the recurrence becomes a single constant matrix. Once that is set, matrix exponentiation is mechanical, and the `log n` factor lets `n` be enormous.

---

✨ **Rule to remember:**
> "When n is huge but the per-step DP transition is linear and constant, stop iterating — build the transition matrix and exponentiate it in O(log n)."
