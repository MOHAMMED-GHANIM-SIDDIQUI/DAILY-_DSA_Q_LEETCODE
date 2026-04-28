# 3539. Find Sum of Array Product of Magical Sequences

## 🔗 Problem Link
https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Dynamic Programming, Combinatorics, Modular Arithmetic, Bit Manipulation

---

## 🧩 Problem Summary
Given integers m, k, and an array nums, find the sum of array products of all "magical sequences" — sequences of length m whose elements come from nums, with exactly k ones in the binary representation of the multinomial coefficient weighted sum. Results are modulo 10^9 + 7.

### 📌 Constraints
- `1 <= m <= 30`
- `0 <= k <= m`
- `1 <= nums.length <= 30`
- `1 <= nums[i] <= 10^8`

---

## 💭 Intuition
👉 This is a deep combinatorial DP problem. The key is tracking the carry from binary addition of counts, and using the popcount of the carry to determine when the binary-ones constraint is satisfied.

---

## ⚡ Approach — DP with Carry Tracking and Combinatorics

### 🧠 Idea
- Use memoized DP with states: remaining slots `m`, remaining ones `k`, current index `i`, and carry from binary addition.
- At each index, try all possible counts (0 to m), weighted by C(m, count) * nums[i]^count.
- The carry propagates through binary addition, and `k` is reduced by `newCarry % 2`.
- Base case: m == 0 and k equals `popcount(carry)`.

---

## 💻 Code

```cpp
class Solution {
 public:
  int magicalSum(int m, int k, vector<int>& nums) {
    const vector<vector<int>> comb = getComb(m, m);
    vector<vector<vector<vector<int>>>> mem(
        m + 1, vector<vector<vector<int>>>(
                   k + 1, vector<vector<int>>(nums.size() + 1,
                                              vector<int>(m + 1, -1))));
    return dp(m, k, 0, 0, nums, mem, comb);
  }

 private:
  static constexpr int kMod = 1'000'000'007;

  int dp(int m, int k, int i, unsigned carry, const vector<int>& nums,
         vector<vector<vector<vector<int>>>>& mem,
         const vector<vector<int>>& comb) {
    if (m < 0 || k < 0 || (m + popcount(carry) < k))
      return 0;
    if (m == 0)
      return k == popcount(carry) ? 1 : 0;
    if (i == nums.size())
      return 0;
    if (mem[m][k][i][carry] != -1)
      return mem[m][k][i][carry];
    int res = 0;
    for (int count = 0; count <= m; ++count) {
      const long contribution = comb[m][count] * modPow(nums[i], count) % kMod;
      const int newCarry = carry + count;
      res = (res + static_cast<long>(dp(m - count, k - (newCarry % 2), i + 1,
                                        newCarry / 2, nums, mem, comb)) *
                       contribution) %
            kMod;
    }
    return mem[m][k][i][carry] = res;
  }

  // C(n, k) = C(n - 1, k) + C(n - 1, k - 1)
  vector<vector<int>> getComb(int n, int k) {
    vector<vector<int>> comb(n + 1, vector<int>(k + 1));
    for (int i = 0; i <= n; ++i)
      comb[i][0] = 1;
    for (int i = 1; i <= n; ++i)
      for (int j = 1; j <= k; ++j)
        comb[i][j] = comb[i - 1][j] + comb[i - 1][j - 1];
    return comb;
  }

  long modPow(long x, long n) {
    if (n == 0)
      return 1;
    if (n % 2 == 1)
      return x * modPow(x % kMod, (n - 1)) % kMod;
    return modPow(x * x % kMod, (n / 2)) % kMod;
  }
};
```

---

## 🧠 Dry Run
### Input
```
m = 2, k = 1, nums = [2]
```
### Steps
```
dp(2, 1, 0, 0):
  count=0: comb[2][0]*2^0=1, dp(2, 1-(0%2)=1, 1, 0) -> i==1==nums.size() -> 0
  count=1: comb[2][1]*2^1=4, dp(1, 1-(1%2)=0, 1, 0) -> i==1 -> 0
  count=2: comb[2][2]*2^2=4, dp(0, 1-(2%2)=1, 1, 1) -> m==0, k==1==popcount(1) -> 1
  res = 0 + 0 + 4*1 = 4

Result: 4
```

---

## ⏱️ Time Complexity
```
O(m^2 * k * n * m) — DP states times loop over counts
```

## 💾 Space Complexity
```
O(m * k * n * m) — for the memoization table
```

---

## ⚠️ Edge Cases
- k = 0 → only valid if carry produces zero ones in binary
- Single element in nums → pure combinatorial counting
- m = 0 → base case, check carry's popcount

---

## 🎯 Interview Takeaways
- Carry tracking in DP connects combinatorial sums with binary representations.
- Pruning with `m + popcount(carry) < k` avoids exploring impossible states.
- Precomputing combinatorial coefficients (Pascal's triangle) is essential for efficiency.

---

## 📌 Key Pattern
👉 **"DP with carry tracking to connect multinomial coefficients with binary digit constraints."**

---

## 🔁 Related Problems
- 2338. Count the Number of Ideal Arrays
- 1799. Maximize Score After N Operations
- Digit DP problems with popcount constraints

---

## 🚀 Final Thoughts
This is a highly advanced problem combining DP, combinatorics, modular arithmetic, and bit manipulation. The carry-tracking mechanism is the novel insight that ties everything together.

---

✨ **Rule to remember:**
> When a problem constrains binary properties of combinatorial sums, track the carry through DP states.
