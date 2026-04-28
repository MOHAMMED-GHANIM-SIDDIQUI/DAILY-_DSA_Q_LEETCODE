# 3337. Total Characters in String After Transformations II

## 🔗 Problem Link
https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Math, Matrix Exponentiation, String, Modular Arithmetic

---

## 🧩 Problem Summary
Given a string `s`, an integer `t` (number of transformations), and an array `nums` of size 26, each character `c` in the string transforms into the next `nums[c - 'a']` characters in the alphabet (wrapping around). After `t` transformations, return the total length of the resulting string modulo 10^9 + 7.

### 📌 Constraints
- `1 <= s.length <= 10^5`
- `1 <= t <= 10^9`
- `nums.length == 26`
- `1 <= nums[i] <= 25`

---

## 💭 Intuition
👉 Each transformation is a linear operation on character counts, representable as a 26x26 matrix. Applying `t` transformations is equivalent to matrix exponentiation. Compute `T^t` and multiply by the initial character count vector.

---

## ⚡ Approach — Matrix Exponentiation

### 🧠 Idea
- Build a 26x26 transformation matrix `T` where `T[i][(i + step) % 26] += 1` for `step` from 1 to `nums[i]`.
- Compute `T^t` using fast matrix exponentiation (binary exponentiation).
- Count the frequency of each character in `s`.
- Multiply the frequency vector by `T^t` to get the final character counts.
- Sum all final counts modulo 10^9 + 7.

---

## 💻 Code

```cpp
class Solution {
 public:
  // Similar to 3335. Total Characters in String After Transformations I
  int lengthAfterTransformations(string s, int t, vector<int>& nums) {
    // T[i][j] := the number of ways to transform ('a' + i) to ('a' + j)
    const vector<vector<int>> T = getTransformationMatrix(nums);
    const vector poweredT = matrixPow(T, t);
    vector<int> count(26);
    // lengths[i] := the total length of ('a' + i) after t transformations
    vector<long> lengths(26);

    for (const char c : s)
      ++count[c - 'a'];

    for (int i = 0; i < 26; ++i)
      for (int j = 0; j < 26; ++j) {
        lengths[j] += static_cast<long>(count[i]) * poweredT[i][j];
        lengths[j] %= kMod;
      }

    return accumulate(lengths.begin(), lengths.end(), 0L) % kMod;
  }

 private:
  static constexpr int kMod = 1'000'000'007;

  vector<vector<int>> getTransformationMatrix(const vector<int>& nums) {
    vector<vector<int>> T(26, vector<int>(26));
    for (int i = 0; i < nums.size(); ++i)
      for (int step = 1; step <= nums[i]; ++step)
        ++T[i][(i + step) % 26];
    return T;
  }

  vector<vector<int>> getIdentityMatrix(int sz) {
    vector<vector<int>> I(sz, vector<int>(sz));
    for (int i = 0; i < sz; ++i)
      I[i][i] = 1;
    return I;
  }

  // Returns A * B.
  vector<vector<int>> matrixMult(const vector<vector<int>>& A,
                                 const vector<vector<int>>& B) {
    const int sz = A.size();
    vector<vector<int>> C(sz, vector<int>(sz));
    for (int i = 0; i < sz; ++i)
      for (int j = 0; j < sz; ++j)
        for (int k = 0; k < sz; ++k)
          C[i][j] = (C[i][j] + static_cast<long>(A[i][k]) * B[k][j]) % kMod;
    return C;
  }

  // Returns M^n.
  vector<vector<int>> matrixPow(const vector<vector<int>>& M, int n) {
    if (n == 0)
      return getIdentityMatrix(M.size());
    if (n % 2 == 1)
      return matrixMult(M, matrixPow(M, n - 1));
    return matrixPow(matrixMult(M, M), n / 2);
  }
};
```

---

## 🧠 Dry Run
### Input
```
s = "ab", t = 2, nums = [1,1,1,...,1] (all 1s)
```
### Steps
```
1. T is a 26x26 shift matrix: T[i][(i+1)%26] = 1
2. T^2: T[i][(i+2)%26] = 1 (double shift)
3. count = [1, 1, 0, ..., 0] (one 'a', one 'b')
4. After T^2: 'a' -> 'c', 'b' -> 'd'
5. lengths = [0, 0, 1, 1, 0, ..., 0]
6. Total length = 2
```

---

## ⏱️ Time Complexity
```
O(26^3 * log(t) + n) — matrix exponentiation with 26x26 matrices, plus counting characters.
```

## 💾 Space Complexity
```
O(26^2) = O(1) for the matrices.
```

---

## ⚠️ Edge Cases
- `t = 0`: return the length of `s` unchanged.
- All characters are the same: only one row of the matrix matters.
- `nums[i] = 25` for all i: maximum spread per transformation.

---

## 🎯 Interview Takeaways
- Recognizing linear recurrences as matrix operations is a key competitive programming technique.
- Matrix exponentiation reduces O(t) iterations to O(log t) matrix multiplications.
- The 26-letter alphabet keeps the matrix size constant and the approach highly efficient.

---

## 📌 Key Pattern
👉 **"Matrix exponentiation for linear character transformations over large iteration counts"**

---

## 🔁 Related Problems
- 3335. Total Characters in String After Transformations I
- 70. Climbing Stairs (matrix exponentiation variant)
- 509. Fibonacci Number (matrix exponentiation variant)

---

## 🚀 Final Thoughts
This is a classic matrix exponentiation problem disguised as a string transformation. The 26x26 transformation matrix captures how each character spawns new characters, and raising it to the t-th power efficiently handles the potentially billions of transformations.

---

✨ **Rule to remember:**
> When a transformation is linear and repeated many times, encode it as a matrix and use fast exponentiation to compute the result in O(log t).
