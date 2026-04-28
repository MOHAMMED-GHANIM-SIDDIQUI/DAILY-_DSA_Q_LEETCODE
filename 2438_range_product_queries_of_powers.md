# 2438. Range Product Queries of Powers

## 🔗 Problem Link
https://leetcode.com/problems/range-product-queries-of-powers/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Bit Manipulation, Prefix Sum

---

## 🧩 Problem Summary
Given a positive integer `n`, decompose it into its minimal set of powers of 2 (sorted ascending). For each query `[left, right]`, compute the product of `powers[left..right]` modulo 10^9 + 7.

### 📌 Constraints
- `1 <= n <= 10^9`
- `1 <= queries.length <= 10^5`
- `0 <= queries[i][0] <= queries[i][1] < powers.length`

---

## 💭 Intuition
👉 The powers of 2 that sum to `n` are exactly the set bits in `n`'s binary representation. Extract them, then answer each range product query by multiplying the relevant powers with modular arithmetic.

---

## ⚡ Approach — Bit Decomposition + Range Product

### 🧠 Idea
- Extract powers of 2 from `n` by checking each bit position.
- For each query `[left, right]`, multiply `powers[left]` through `powers[right]` under modulo.
- Since `n` has at most 30 bits, the powers array is small.

---

## 💻 Code

```cpp
class Solution {
 public:
  vector<int> productQueries(int n, vector<vector<int>>& queries) {
    constexpr int kMod = 1'000'000'007;
    constexpr int kMaxBit = 30;
    vector<int> ans;
    vector<int> pows;

    for (int i = 0; i < kMaxBit; ++i)
      if (n >> i & 1)
        pows.push_back(1 << i);

    for (const vector<int>& query : queries) {
      const int left = query[0];
      const int right = query[1];
      long prod = 1;
      for (int i = left; i <= right; ++i) {
        prod *= pows[i];
        prod %= kMod;
      }
      ans.push_back(prod);
    }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
n = 15, queries = [[0,1],[2,2],[0,3]]
```
### Steps
```
n=15 = 1111 in binary → pows = [1, 2, 4, 8]

Query [0,1]: prod = 1*2 = 2
Query [2,2]: prod = 4
Query [0,3]: prod = 1*2*4*8 = 64

Result: [2, 4, 64]
```

---

## ⏱️ Time Complexity
```
O(30 + q * 30) = O(q) where q = number of queries. Each query iterates at most 30 powers.
```

## 💾 Space Complexity
```
O(30 + q) = O(q) — powers array (at most 30) and answer array.
```

---

## ⚠️ Edge Cases
- `n` is a power of 2: only one element in powers array.
- Query with `left == right`: product is a single power.
- `n = 1`: powers = [1], all products are 1.

---

## 🎯 Interview Takeaways
- Any positive integer can be uniquely decomposed into powers of 2 (binary representation).
- Since there are at most 30 set bits, the powers array is always small.
- Range product over a small array is efficient even without prefix products.

---

## 📌 Key Pattern
👉 **"Decompose n into set bits (powers of 2), then answer range queries over the small array."**

---

## 🔁 Related Problems
- 338. Counting Bits
- 1009. Complement of Base 10 Integer
- 477. Total Hamming Distance

---

## 🚀 Final Thoughts
The problem is straightforward once you recognize that the "minimal powers of 2" are simply the set bits in `n`. The bounded size of the powers array (at most 30) makes even naive range product queries efficient.

---

✨ **Rule to remember:**
> "Set bits of n give the powers of 2 — at most 30 elements, so range queries are cheap."
