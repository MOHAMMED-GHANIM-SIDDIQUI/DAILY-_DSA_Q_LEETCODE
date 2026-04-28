# 3315. Construct the Minimum Bitwise Array II

## 🔗 Problem Link
https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Bit Manipulation

---

## 🧩 Problem Summary
Same as Problem 3314 but with larger constraints. For each prime `nums[i]`, find the minimum `ans[i]` such that `ans[i] OR (ans[i] + 1) == nums[i]`, or -1 if impossible. This version requires a more efficient bit-manipulation approach.

### 📌 Constraints
- `1 <= nums.length <= 100`
- `2 <= nums[i] <= 10^9`
- `nums[i]` is a prime number

---

## 💭 Intuition
👉 Since `x | (x+1)` sets the lowest 0-bit of `x`, the reverse operation requires finding the first 0-bit in `num` and clearing the bit just below it. For `num = 2` (the only even prime), no valid answer exists.

---

## ⚡ Approach — Bit Manipulation (Find First Zero Bit)

### 🧠 Idea
- If `num == 2`, append -1 (special case: only even prime).
- Otherwise, find the position `i` of the first 0-bit in `num`.
- Clear bit `(i - 1)` from `num` to get the answer.
- This works because `x | (x+1)` sets the lowest 0-bit, so reversing means clearing the bit just below the first 0-bit.

---

## 💻 Code

```python
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            found = False
            if num==2:
                ans.append(-1)
                continue

            for i in range(32):
                if (num & (1 << i)) == 0:
                    if i > 0:
                        num = num & ~(1 << (i - 1))
                    ans.append(num)
                    found = True
                    break

            if not found:
                ans.append(-1)

        return ans
```

---

## 🧠 Dry Run
### Input
```
nums = [2, 3, 5, 7]
```
### Steps
```
1. num=2: even prime => append -1
2. num=3 (0b11): first 0-bit at i=2, clear bit 1 => 3 & ~2 = 1, append 1
   Verify: 1 | 2 = 3 ✓
3. num=5 (0b101): first 0-bit at i=1, clear bit 0 => 5 & ~1 = 4, append 4
   Verify: 4 | 5 = 5 ✓
4. num=7 (0b111): first 0-bit at i=3, clear bit 2 => 7 & ~4 = 3, append 3
   Verify: 3 | 4 = 7 ✓
Result: [-1, 1, 4, 3]
```

---

## ⏱️ Time Complexity
```
O(n * 32) = O(n) — constant bit-width scan per number.
```

## 💾 Space Complexity
```
O(n) for the answer array.
```

---

## ⚠️ Edge Cases
- `num = 2`: the only prime that returns -1.
- Large primes (up to 10^9): the bit scan handles them in at most 32 iterations.
- All bits set in the range (e.g., 2^k - 1): clear the highest set bit below the first zero.

---

## 🎯 Interview Takeaways
- Understanding how `x | (x+1)` modifies bit patterns is essential.
- The reverse operation (finding the answer from the result) is a bit-clearing operation.
- Always handle the even-prime edge case separately.

---

## 📌 Key Pattern
👉 **"Reverse a bit-setting operation by finding and clearing the appropriate bit"**

---

## 🔁 Related Problems
- 3314. Construct the Minimum Bitwise Array I
- 201. Bitwise AND of Numbers Range
- 137. Single Number II

---

## 🚀 Final Thoughts
This medium variant requires understanding the bit-level mechanics of `x | (x+1)`. Instead of brute-forcing all candidates, we directly compute the answer by finding the first zero bit and clearing its predecessor. This scales to large inputs efficiently.

---

✨ **Rule to remember:**
> To reverse `x | (x+1) = num`, find the lowest 0-bit in `num` and clear the bit just below it.
