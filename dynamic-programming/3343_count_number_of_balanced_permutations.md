# 3343. Count Number of Balanced Permutations

## 🔗 Problem Link
https://leetcode.com/problems/count-number-of-balanced-permutations/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Math, Dynamic Programming, Combinatorics, Modular Inverse

---

## 🧩 Problem Summary
Given a string `num` of digits, count the number of permutations where the sum of digits at even indices equals the sum of digits at odd indices. Return the result modulo 10^9 + 7.

### 📌 Constraints
- `1 <= num.length <= 80`
- `num` consists of digits '0' to '9'

---

## 💭 Intuition
👉 Sort digits in descending order and use memoized recursion to assign each digit to an even or odd index. Track remaining even/odd slots and the remaining target sum for even indices. Divide by repeated digit permutations using modular inverse.

---

## ⚡ Approach — DP with Combinatorics and Modular Inverse

### 🧠 Idea
- If the total sum is odd, return 0 (impossible to split equally).
- Sort digits descending for pruning.
- Use `dp(even, odd, evenBalance)` to count ways to place remaining digits.
- Multiply by available slot count at each step.
- Divide by permutations of duplicate digits using modular inverse.

---

## 💻 Code

```cpp
class Solution {
 public:
  int countBalancedPermutations(string num) {
    vector<int> nums = getNums(num);
    const int sum = accumulate(nums.begin(), nums.end(), 0);
    if (sum % 2 == 1)
      return 0;

    ranges::sort(nums, greater<>());

    const int even = (nums.size() + 1) / 2;
    const int odd = nums.size() / 2;
    const int evenBalance = sum / 2;
    vector<vector<vector<long>>> mem(
        even + 1,
        vector<vector<long>>(odd + 1, vector<long>(evenBalance + 1, -1)));
    const long perm = getPerm(nums);
    return countBalancedPermutations(nums, even, odd, evenBalance, mem) *
           modInverse(perm) % kMod;
  }

 private:
  static constexpr int kMod = 1'000'000'007;

  // Returns the number of permutations where there are `even` even indices
  // left, `odd` odd indices left, and `evenBalance` is the target sum of the
  // remaining numbers to be placed in even indices.
  long countBalancedPermutations(const vector<int>& nums, int even, int odd,
                                 int evenBalance,
                                 vector<vector<vector<long>>>& mem) {
    if (evenBalance < 0)
      return 0;
    if (even == 0)
      return evenBalance == 0 ? factorial(odd) : 0;
    const int index = nums.size() - (even + odd);
    if (odd == 0) {
      long remainingSum = 0;
      for (int i = index; i < nums.size(); ++i)
        remainingSum += nums[i];
      return (remainingSum == evenBalance) ? factorial(even) : 0;
    }
    if (mem[even][odd][evenBalance] != -1)
      return mem[even][odd][evenBalance];
    const long placeEven =
        countBalancedPermutations(nums, even - 1, odd,
                                  evenBalance - nums[index], mem) *
        even % kMod;
    const long placeOdd =
        countBalancedPermutations(nums, even, odd - 1, evenBalance, mem) * odd %
        kMod;
    return mem[even][odd][evenBalance] = (placeEven + placeOdd) % kMod;
  }

  vector<int> getNums(const string& num) {
    vector<int> nums;
    for (const char c : num)
      nums.push_back(c - '0');
    return nums;
  }

  long getPerm(const vector<int>& nums) {
    long res = 1;
    vector<int> count(10);
    for (const int num : nums)
      ++count[num];
    for (const int freq : count)
      res = res * factorial(freq) % kMod;
    return res;
  }

  long factorial(int n) {
    long res = 1;
    for (int i = 2; i <= n; ++i)
      res = res * i % kMod;
    return res;
  }

  long modInverse(long a) {
    long m = kMod;
    long y = 0;
    long x = 1;
    while (a > 1) {
      const long q = a / m;
      long t = m;
      m = a % m;
      a = t;
      t = y;
      y = x - q * y;
      x = t;
    }
    return x < 0 ? x + kMod : x;
  }
};
```

---

## 🧠 Dry Run
### Input
```
num = "123"
```
### Steps
```
digits = [1, 2, 3], sum = 6, evenBalance = 3
even = 2, odd = 1
Sorted desc: [3, 2, 1]
Try placing 3 at even: evenBalance=0, even=1, odd=1
  Place 2 at even: evenBalance=-2 → invalid
  Place 2 at odd: even=1, odd=0, evenBalance=0 → remainingSum=1, 1==0? No
Try placing 3 at odd: even=2, odd=0, evenBalance=3
  remainingSum = 2+1 = 3 == 3 → factorial(2) = 2
Result = 2 * modInverse(1) % MOD = 2
```

---

## ⏱️ Time Complexity
```
O(even * odd * evenBalance) — memoized states
```

## 💾 Space Complexity
```
O(even * odd * evenBalance) — memoization table
```

---

## ⚠️ Edge Cases
- Odd total sum → return 0 immediately
- All same digits → only 1 balanced permutation if even count matches
- Single digit → always balanced (odd index sum is 0)

---

## 🎯 Interview Takeaways
- Balanced permutation problems combine DP with combinatorics.
- Modular inverse (extended GCD) is essential for dividing under modular arithmetic.
- Sorting in descending order enables early pruning of negative balances.

---

## 📌 Key Pattern
👉 **"DP over slot assignments with combinatorial counting and modular inverse"**

---

## 🔁 Related Problems
- 1569. Number of Ways to Reorder Array to Get Same BST
- 920. Number of Music Playlists
- Problems involving permutation counting with constraints

---

## 🚀 Final Thoughts
A complex problem requiring three mathematical tools: memoized DP for enumeration, factorial for permutation counting, and modular inverse for division. The descending sort is a subtle but important optimization.

---

✨ **Rule to remember:**
> "For balanced permutation counting, assign digits to even/odd slots via DP and fix duplicates with modular inverse."
