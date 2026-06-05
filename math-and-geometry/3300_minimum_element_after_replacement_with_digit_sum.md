# 3300. Minimum Element After Replacement With Digit Sum

## 🔗 Problem Link
https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Math

---

## 🧩 Problem Summary
You are given an integer array `nums`. Replace **every** element with the **sum of its digits**. Return the **minimum** element of the array after all replacements.

### 📌 Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 10^4`

---

## 💭 Intuition
There's no interaction between elements — each is independently mapped to its digit sum. So we just compute the digit sum of each value and track the running minimum. No need to materialise a new array.

Digit sum is the textbook `while n: total += n % 10; n //= 10` loop.

---

## ⚡ Approach — Digit sum + running min

### 🧠 Idea
1. Initialise `min_res = ∞`.
2. For each `n` in `nums`:
   - Accumulate `cur = sum of digits of n` via repeated `% 10` and `// 10`.
   - Update `min_res = min(min_res, cur)`.
3. Return `min_res`.

---

## 💻 Code

```python
class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_res = float('inf')

        for n in nums:
            cur = 0
            while n:
                cur += n % 10
                n //= 10
            min_res = min(min_res, int(cur))
        return min_res
```

---

## 🧠 Dry Run
### Input
```
nums = [10, 12, 1000, 999]
```

### Digit sums
```
10   → 1 + 0 = 1
12   → 1 + 2 = 3
1000 → 1 + 0 + 0 + 0 = 1
999  → 9 + 9 + 9 = 27
```

### Running min
```
min(∞, 1)=1, min(1,3)=1, min(1,1)=1, min(1,27)=1
```
Answer: `1`.

---

## ⏱️ Time Complexity
```
O(n · D)   — D ≤ 5 digits (values ≤ 10^4). Effectively O(n).
```

## 💾 Space Complexity
```
O(1)   — a couple of scalars.
```

---

## ⚠️ Edge Cases
- **Single element** → its own digit sum is the answer.
- **Powers of ten** (`10, 100, 1000`) → digit sum `1`, often the global minimum.
- **All same value** → all map to the same digit sum.
- The smallest possible digit sum for a positive number is `1` (a power of ten), never `0`, since `nums[i] >= 1`.

---

## 🎯 Interview Takeaways
- Recognise "replace each independently then aggregate" → no array rebuild needed, just fold a running statistic.
- The digit-sum loop (`% 10`, `// 10`) is a primitive worth having reflexively; it shows up in digit-DP, happy numbers, and divisibility tricks.

---

## 📌 Key Pattern
👉 **"Independent per-element transform + reduction → compute the transform inline and fold into the running min/max."**

---

## 🔁 Related Problems
- 1085. Sum of Digits in the Minimum Number
- 2160. Minimum Sum of Four Digit Number After Splitting Digits
- 258. Add Digits
- 1295. Find Numbers with Even Number of Digits

---

## 🚀 Final Thoughts
A warm-up problem whose only substance is the digit-sum loop. The takeaway is the habit: when each element is transformed independently and you only need an aggregate, skip building the intermediate array.

---

✨ **Rule to remember:**
> Digit sum = `while n: s += n % 10; n //= 10`. When the transform is per-element and you only need min/max, fold it inline — don't allocate the mapped array.
