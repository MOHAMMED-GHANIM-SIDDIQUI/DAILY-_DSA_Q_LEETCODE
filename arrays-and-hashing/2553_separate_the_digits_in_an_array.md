# 2553. Separate the Digits in an Array

## 🔗 Problem Link
https://leetcode.com/problems/separate-the-digits-in-an-array/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Simulation

---

## 🧩 Problem Summary
You are given a positive integer array `nums`. Separate every element into its individual digits, **preserving** both the array order and the digit order inside each number, and return the resulting flat array.

### 📌 Constraints
- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 10^5`

---

## 💭 Intuition
Each number is already written most-significant-digit first when you cast it to a string, so "separate the digits" reduces to: walk the array, walk the digits of each number, push each digit into the output. No math required — string conversion is the cheapest, most readable way to get digits **in order**.

The only thing to *not* do is build the digits arithmetically (`n % 10`, `n //= 10`) — that gives them **reversed**, and you'd have to reverse them back. String conversion sidesteps that entirely.

---

## ⚡ Approach — Stringify and Flatten

### 🧠 Idea
1. Initialize an empty result list `ans`.
2. For each `num` in `nums`, convert it to a string and append `int(c)` for every character `c`.
3. Return `ans`.

That's it — one pass over the inputs, one append per digit.

---

## 💻 Code

```python
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            for c in str(num):
                ans.append(int(c))
        return ans
```

---

## 🧠 Dry Run
### Input
```
nums = [13, 25, 83, 77]
```

### Steps
```
num = 13  → "13" → append 1, append 3   → ans = [1, 3]
num = 25  → "25" → append 2, append 5   → ans = [1, 3, 2, 5]
num = 83  → "83" → append 8, append 3   → ans = [1, 3, 2, 5, 8, 3]
num = 77  → "77" → append 7, append 7   → ans = [1, 3, 2, 5, 8, 3, 7, 7]
```

Return `[1, 3, 2, 5, 8, 3, 7, 7]`. Order of original numbers preserved, digits in natural reading order. ✅

---

## ⏱️ Time Complexity
```
O(N · D)   where N = len(nums) and D = max number of digits per element (≤ 6 here).
         ≈ O(total digits written to output).
```

## 💾 Space Complexity
```
O(N · D)   for the output list. O(1) extra working space beyond that
           (the per-number string is bounded by D characters).
```

---

## ⚠️ Edge Cases
- **Single-digit elements**: `str(num)` has length 1 → one append per number. Works naturally.
- **Max values (`10^5 = 100000`)**: six digits is the upper bound — well within constraints.
- **No leading zeros to worry about**: problem guarantees `nums[i] >= 1`, so `str(num)` has no padding zeros.
- **Order matters**: build digits via `str(num)` (left-to-right), not via `% 10` / `// 10` (right-to-left). Reversing afterwards is a wasted pass.

---

## 🎯 Interview Takeaways
- When digit **order** matters (most-significant first), `str(n)` is the cleanest extractor — beats arithmetic in both clarity and correctness.
- Flatten-while-you-walk is a standard pattern: a single `for` loop with `extend`/`append` instead of building per-number sublists and concatenating at the end.
- Equivalent one-liner if you like comprehensions: `[int(c) for num in nums for c in str(num)]` — same complexity, same readability tradeoff.

---

## 📌 Key Pattern
👉 **"Digit-order matters → use `str(n)`. Build, don't post-process."**

---

## 🔁 Related Problems
- 1281. Subtract the Product and Sum of Digits of an Integer
- 1295. Find Numbers with Even Number of Digits
- 2094. Finding 3-Digit Even Numbers
- 9. Palindrome Number
- 7. Reverse Integer

---

## 🚀 Final Thoughts
A warm-up problem. The only thing worth internalizing is the **order** distinction: `str(n)` gives MSB→LSB, arithmetic gives LSB→MSB. Pick the one that matches the output you need and skip the reverse.

---

✨ **Rule to remember:**
> When you need digits in reading order, stringify; when you need them in computation order (units first), use `%` and `//`. Choose the extractor that matches the output shape.
