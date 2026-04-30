# 1304. Find N Unique Integers Sum up to Zero

## 🔗 Problem Link
https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Math

---

## 🧩 Problem Summary
Given an integer `n`, return any array containing `n` unique integers such that they add up to zero. The solution should contain `n` distinct values whose sum equals zero.

### 📌 Constraints
- `1 <= n <= 1000`

---

## 💭 Intuition
👉 For every positive integer `i`, we can pair it with `-i` to get a sum of zero. If `n` is odd, we include `0` as well. This symmetric pairing guarantees uniqueness and a total sum of zero.

---

## ⚡ Approach — Symmetric Pair Construction

### 🧠 Idea
- If `n` is odd, push `0` into the result first.
- Then push pairs `(i, -i)` for `i = 1` to `n/2`.
- Each pair sums to zero, and all values are unique.

---

## 💻 Code

```cpp
class Solution {
public:
    vector<int> sumZero(int n) {
        vector<int>ans;
        if( n%2==1)
        {

            ans.push_back(0);
            for(int i=1;i<=n/2;i++)
            {
                ans.push_back(i);
                ans.push_back(-i);

            }
            return ans;
        }

         for(int i=1;i<=n/2;i++)
            {
                ans.push_back(i);
                ans.push_back(-i);

            }
            return ans;
    }
};
```

---

## 🧠 Dry Run
### Input
```
n = 5
```
### Steps
```
n is odd → push 0 → ans = [0]
i=1 → push 1, -1 → ans = [0, 1, -1]
i=2 → push 2, -2 → ans = [0, 1, -1, 2, -2]
Sum = 0 + 1 + (-1) + 2 + (-2) = 0 ✓
```

---

## ⏱️ Time Complexity
```
O(n)
```

## 💾 Space Complexity
```
O(n) — for the result array
```

---

## ⚠️ Edge Cases
- `n = 1` → return `[0]`
- `n = 2` → return `[1, -1]`
- Large `n` (1000) → still works efficiently with linear construction

---

## 🎯 Interview Takeaways
- Symmetric pairing is a classic trick for zero-sum construction.
- Handling odd/even cases separately keeps logic clean.
- Multiple valid answers exist; any correct one is accepted.

---

## 📌 Key Pattern
👉 **"Pair positive and negative counterparts to guarantee a zero sum."**

---

## 🔁 Related Problems
- 2099. Find Subsequence of Length K With the Largest Sum
- 1588. Sum of All Odd Length Subarrays

---

## 🚀 Final Thoughts
A straightforward math-based construction problem. The symmetry insight makes it trivial — just pair `i` with `-i` and optionally include `0`.

---

✨ **Rule to remember:**
> Pair `+i` with `-i` for zero-sum arrays; add `0` when `n` is odd.
