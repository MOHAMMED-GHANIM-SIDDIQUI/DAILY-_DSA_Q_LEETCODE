# 2818. Apply Operations to Maximize Score

## 🔗 Problem Link
https://leetcode.com/problems/apply-operations-to-maximize-score/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Math, Stack, Greedy, Monotonic Stack, Number Theory, Sorting

---

## 🧩 Problem Summary
Given an array `nums` and an integer `k`, you perform `k` operations. In each operation, choose a subarray, compute its score (product of elements raised to the prime score of the subarray's element with the highest prime score), and multiply it into the total. Return the maximum total score modulo 10^9 + 7.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`
- `1 <= k <= min(n * (n + 1) / 2, 10^9)`

---

## 💭 Intuition
👉 For each element, determine how many subarrays it would be the "chosen" element (having the highest prime score). Prioritize larger elements first — greedily assign as many of their subarrays as possible to the k operations.

---

## ⚡ Approach — Monotonic Stack + Greedy + Modular Exponentiation

### 🧠 Idea
- Compute the prime score (number of distinct prime factors) for each element using a sieve.
- Use monotonic stacks to find, for each index, the nearest left/right indices with greater/equal prime scores.
- The number of subarrays where `nums[i]` is the dominant element is `(i - left[i]) * (right[i] - i)`.
- Sort elements by value (descending). Greedily assign subarrays to the largest elements first, using modular exponentiation.

---

## 💻 Code

```cpp
class Solution {
 public:
  int maximumScore(vector<int>& nums, int k) {
    const int n = nums.size();
    const int mx = ranges::max(nums);
    const vector<int> minPrimeFactors = sieveEratosthenes(mx + 1);
    const vector<int> primeScores = getPrimeScores(nums, minPrimeFactors);
    int ans = 1;
    // left[i] := the next index on the left (if any) s.t.
    // primeScores[left[i]] >= primeScores[i]
    vector<int> left(n, -1);
    // right[i] := the next index on the right (if any) s.t.
    // primeScores[right[i]] > primeScores[i]
    vector<int> right(n, n);
    stack<int> stack;

    // Find the next indices on the left where `primeScores` are greater or
    // equal.
    for (int i = n - 1; i >= 0; --i) {
      while (!stack.empty() && primeScores[stack.top()] <= primeScores[i])
        left[stack.top()] = i, stack.pop();
      stack.push(i);
    }

    stack = std::stack<int>();

    // Find the next indices on the right where `primeScores` are greater.
    for (int i = 0; i < n; ++i) {
      while (!stack.empty() && primeScores[stack.top()] < primeScores[i])
        right[stack.top()] = i, stack.pop();
      stack.push(i);
    }

    vector<pair<int, int>> numAndIndexes;

    for (int i = 0; i < n; ++i)
      numAndIndexes.emplace_back(nums[i], i);

    ranges::sort(numAndIndexes,
                 [&](const pair<int, int>& a, const pair<int, int>& b) {
      return a.first == b.first ? a.second < b.second : a.first > b.first;
    });

    for (const auto& [num, i] : numAndIndexes) {
      // nums[i] is the maximum value in the range [left[i] + 1, right[i] - 1]
      // So, there are (i - left[i]) * (right[i] - 1) ranges where nums[i] will
      // be chosen.
      const long rangeCount = static_cast<long>(i - left[i]) * (right[i] - i);
      const long actualCount = min(rangeCount, static_cast<long>(k));
      k -= actualCount;
      ans = static_cast<long>(ans) * modPow(num, actualCount) % kMod;
    }

    return ans;
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

  // Gets the minimum prime factor of i, where 1 < i <= n.
  vector<int> sieveEratosthenes(int n) {
    vector<int> minPrimeFactors(n + 1);
    iota(minPrimeFactors.begin() + 2, minPrimeFactors.end(), 2);
    for (int i = 2; i * i < n; ++i)
      if (minPrimeFactors[i] == i)  // `i` is prime.
        for (int j = i * i; j < n; j += i)
          minPrimeFactors[j] = min(minPrimeFactors[j], i);
    return minPrimeFactors;
  }

  vector<int> getPrimeScores(const vector<int>& nums,
                             const vector<int>& minPrimeFactors) {
    vector<int> primeScores;
    for (const int num : nums)
      primeScores.push_back(getPrimeScore(num, minPrimeFactors));
    return primeScores;
  }

  int getPrimeScore(int num, const vector<int>& minPrimeFactors) {
    unordered_set<int> primeFactors;
    while (num > 1) {
      const int divisor = minPrimeFactors[num];
      primeFactors.insert(divisor);
      while (num % divisor == 0)
        num /= divisor;
    }
    return primeFactors.size();
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [8,3,9,3,8], k = 2
```
### Steps
```
Prime scores: 8=1(only 2), 3=1(only 3), 9=1(only 3), 3=1, 8=1
All prime scores = 1, so left[i] and right[i] use default boundaries.

Sorted by value desc: [(9,2), (8,0), (8,4), (3,1), (3,3)]

For (9,2): rangeCount = (2-(-1))*(5-2) = 3*3 = 9, actualCount = min(9,2) = 2
ans = 1 * 9^2 % MOD = 81, k = 0

Return 81
```

---

## ⏱️ Time Complexity
```
O(n * sqrt(max) + n log n) — sieve + prime scores + sorting + stack passes
```

## 💾 Space Complexity
```
O(n + max) for the sieve and auxiliary arrays
```

---

## ⚠️ Edge Cases
- All elements have the same prime score
- `k = 1`: just pick the largest element
- Very large `k` requiring all possible subarrays

---

## 🎯 Interview Takeaways
- Monotonic stack to find the "dominance range" of each element is a powerful technique.
- Greedy assignment (largest elements first) combined with counting valid subarrays per element.
- Modular exponentiation handles large powers efficiently.

---

## 📌 Key Pattern
👉 **"Monotonic stack for dominance ranges + greedy assignment + modular exponentiation"**

---

## 🔁 Related Problems
- 907. Sum of Subarray Minimums
- 2104. Sum of Subarray Ranges
- 1856. Maximum Subarray Min-Product

---

## 🚀 Final Thoughts
This is a challenging problem combining multiple advanced techniques: prime factorization via sieve, monotonic stack for range computation, greedy strategy with sorting, and modular arithmetic. Each piece is well-known individually, but combining them cleanly is the real challenge.

---

✨ **Rule to remember:**
> To maximize scores across subarrays, compute each element's dominance range via monotonic stacks, then greedily assign the largest elements first.
