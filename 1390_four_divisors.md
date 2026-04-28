# 1390. Four Divisors

## 🔗 Problem Link
https://leetcode.com/problems/four-divisors/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Math

---

## 🧩 Problem Summary
Given an integer array `nums`, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return `0`.

### 📌 Constraints
- `1 <= nums.length <= 10^4`
- `1 <= nums[i] <= 10^5`

---

## 💭 Intuition
👉 For each number, find all its divisors by iterating up to its square root. If it has exactly four divisors, add their sum to the result. Memoize results for repeated numbers.

---

## ⚡ Approach — Trial Division with Memoization

### 🧠 Idea
- For each number `n`, iterate from `2` to `sqrt(n)` to find divisor pairs.
- Track divisor count (starting at 2 for `1` and `n` themselves).
- If count exceeds 4, break early.
- If exactly 4 divisors, cache and add their sum.

---

## 💻 Code

```python
class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        ans = 0
        memory = {}

        for n in nums:
            if n in memory:
                ans += memory[n]
                continue

            divisior = 2  # 1 and n
            cnt = {1, n}

            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    j = n // i
                    if i == j:
                        divisior += 1
                        cnt.add(i)
                    else:
                        divisior += 2
                        cnt.add(i)
                        cnt.add(j)

                if divisior > 4:
                    break

            if divisior == 4:
                memory[n] = sum(cnt)
                ans += memory[n]

        return ans
```

---

## 🧠 Dry Run
### Input
```
nums = [21, 4, 7]
```
### Steps
```
n=21: divisors of 21 → {1, 3, 7, 21} → count=4 → sum=32 → ans=32
n=4:  divisors of 4 → {1, 2, 4} → count=3 → skip
n=7:  divisors of 7 → {1, 7} → count=2 → skip
Result = 32
```

---

## ⏱️ Time Complexity
```
O(n * sqrt(max_val)) where n is array length
```

## 💾 Space Complexity
```
O(n) — for the memoization dictionary
```

---

## ⚠️ Edge Cases
- Perfect squares like `4` have 3 divisors (1, 2, 4), not 4
- Prime numbers have exactly 2 divisors — skip them
- `nums = [1]` → only 1 divisor → return 0

---

## 🎯 Interview Takeaways
- Trial division up to sqrt is the standard approach for finding divisors.
- Early termination when count exceeds 4 is a crucial optimization.
- Memoization helps when the input has duplicate values.

---

## 📌 Key Pattern
👉 **"Trial division up to sqrt(n) with early exit for divisor counting."**

---

## 🔁 Related Problems
- 1492. The kth Factor of n
- 507. Perfect Number
- 952. Largest Component Size by Common Factor

---

## 🚀 Final Thoughts
A straightforward number theory problem. The key optimization is breaking early once the divisor count exceeds four, and caching results for repeated numbers.

---

✨ **Rule to remember:**
> To count divisors, iterate only up to sqrt(n) — each divisor `i` gives a pair `(i, n/i)`.
