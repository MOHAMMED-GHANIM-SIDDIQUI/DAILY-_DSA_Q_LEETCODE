# 3405. Count the Number of Arrays with K Matching Adjacent Elements

## 🔗 Problem Link
https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Math, Combinatorics, Modular Arithmetic

---

## 🧩 Problem Summary
Count the number of arrays of length n where each element is in [1, m], and exactly k pairs of adjacent elements are equal. Return the answer modulo 10^9 + 7.

### 📌 Constraints
- 1 <= n <= 10^5
- 1 <= m <= 10^5
- 0 <= k <= n - 1

---

## 💭 Intuition
👉 Among n-1 adjacent pairs, choose k pairs to be equal. The remaining n-1-k transitions must be different. The first element has m choices, each "different" transition has (m-1) choices, and equal transitions have 1 choice. So the answer is m * C(n-1, k) * (m-1)^(n-1-k).

---

## ⚡ Approach — Combinatorics with Modular Exponentiation

### 🧠 Idea
- Choose which k of the n-1 adjacent pairs are equal: C(n-1, k).
- First element: m choices.
- Each of the n-1-k "different" transitions: (m-1) choices.
- Answer: m * C(n-1, k) * (m-1)^(n-1-k) mod 10^9+7.
- Precompute factorials and inverse factorials for nCk.

---

## 💻 Code

```cpp
class Solution {
 public:
  int countGoodArrays(int n, int m, int k) {
    const auto [fact, invFact] = getFactAndInvFact(n);
    return m * modPow(m - 1, n - k - 1) % kMod * nCk(n - 1, k, fact, invFact) %
           kMod;
  }

 private:
  static constexpr int kMod = 1'000'000'007;

  long modPow(long x, long n) {
    if (n == 0)
      return 1;
    if (n % 2 == 1)
      return x * modPow(x % kMod, (n - 1)) % kMod;
    return modPow(x * x % kMod, (n / 2)) % kMod;
  }

  pair<vector<long>, vector<long>> getFactAndInvFact(int n) {
    vector<long> fact(n + 1);
    vector<long> invFact(n + 1);
    vector<long> inv(n + 1);
    fact[0] = invFact[0] = 1;
    inv[0] = inv[1] = 1;
    for (int i = 1; i <= n; ++i) {
      if (i >= 2)
        inv[i] = kMod - kMod / i * inv[kMod % i] % kMod;
      fact[i] = fact[i - 1] * i % kMod;
      invFact[i] = invFact[i - 1] * inv[i] % kMod;
    }
    return {fact, invFact};
  }

  int nCk(int n, int k, const vector<long>& fact, const vector<long>& invFact) {
    return fact[n] * invFact[k] % kMod * invFact[n - k] % kMod;
  }
};
```

---

## 🧠 Dry Run
### Input
```
n = 3, m = 2, k = 1
```
### Steps
```
Choose 1 of 2 pairs to be equal: C(2,1) = 2
First element: 2 choices
Different transitions: (2-1)^(2-1) = 1^1 = 1

Answer = 2 * 1 * 2 = 4

Arrays: [1,1,2], [1,2,2], [2,2,1], [2,1,1]
```

---

## ⏱️ Time Complexity
```
O(n) — for precomputing factorials
```

## 💾 Space Complexity
```
O(n) — factorial and inverse factorial arrays
```

---

## ⚠️ Edge Cases
- k = 0 → no adjacent pairs equal, answer = m * (m-1)^(n-1)
- k = n-1 → all adjacent pairs equal, answer = m (constant array)
- m = 1 → only possible if k = n-1, otherwise 0

---

## 🎯 Interview Takeaways
- Breaking down a counting problem into independent choices is key.
- Modular inverse via the formula inv[i] = mod - (mod/i) * inv[mod%i] % mod is efficient.
- Combinatorial problems often reduce to "choose positions" * "count per configuration."

---

## 📌 Key Pattern
👉 **"Combinatorial counting: choose equal-pair positions, multiply independent choices"**

---

## 🔁 Related Problems
- 1916. Count Ways to Build Rooms in an Ant Colony
- 62. Unique Paths (combinatorial counting)

---

## 🚀 Final Thoughts
This is a pure combinatorics problem. The formula m * C(n-1, k) * (m-1)^(n-1-k) elegantly captures the structure: choose where equalities occur, then fill in the rest.

---

✨ **Rule to remember:**
> For arrays with exactly k matching adjacent pairs: choose k positions from n-1 pairs, first element has m choices, each non-matching transition has m-1 choices.
