# 3314. Construct the Minimum Bitwise Array I

## 🔗 Problem Link
https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Bit Manipulation

---

## 🧩 Problem Summary
Given an array of prime numbers `nums`, construct an array `ans` where for each `nums[i]`, find the minimum non-negative integer `ans[i]` such that `ans[i] OR (ans[i] + 1) == nums[i]`. If no such value exists, set `ans[i] = -1`.

### 📌 Constraints
- `1 <= nums.length <= 100`
- `2 <= nums[i] <= 1000`
- `nums[i]` is a prime number

---

## 💭 Intuition
👉 Brute force: for each `num`, try all values `j` from 1 to `num - 1` and check if `j | (j + 1) == num`. Since constraints are small (up to 1000), this is efficient enough.

---

## ⚡ Approach — Brute Force Enumeration

### 🧠 Idea
- For each `num` in `nums`, iterate `j` from 1 to `num - 1`.
- Check if `j | (j + 1) == num`.
- Append the first valid `j` found, or -1 if none exists.

---

## 💻 Code

```python
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            Flag = False
            for j in range(1,num):
                if j | (j+1) == num:
                    ans.append(j)
                    Flag= True
                    break
            if Flag == False:
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
1. num=2: j=1 => 1|2=3 ≠ 2. No match => -1
2. num=3: j=1 => 1|2=3 == 3 ✓ => append 1
3. num=5: j=1 => 1|2=3≠5, j=2 => 2|3=3≠5, j=3 => 3|4=7≠5, j=4 => 4|5=5==5 ✓ => append 4
4. num=7: j=1..., j=3 => 3|4=7==7 ✓ => append 3
Result: [-1, 1, 4, 3]
```

---

## ⏱️ Time Complexity
```
O(n * max(nums)) where n is the length of nums and max(nums) <= 1000.
```

## 💾 Space Complexity
```
O(n) for the answer array.
```

---

## ⚠️ Edge Cases
- `num = 2`: the only even prime, no valid answer exists => -1.
- All odd primes have a valid answer.
- Smallest input: single element array.

---

## 🎯 Interview Takeaways
- For small constraints, brute force is perfectly acceptable.
- Understanding `x | (x+1)` sets the lowest unset bit of `x`, producing a number with a specific bit pattern.
- The only case returning -1 is `num = 2`.

---

## 📌 Key Pattern
👉 **"Brute force bit manipulation search under small constraints"**

---

## 🔁 Related Problems
- 3315. Construct the Minimum Bitwise Array II
- 201. Bitwise AND of Numbers Range

---

## 🚀 Final Thoughts
A straightforward easy problem solvable by brute force. The key observation is that `x | (x+1)` always sets the lowest 0-bit of `x`, making the search space manageable. For the optimized version, see Problem 3315.

---

✨ **Rule to remember:**
> `x | (x+1)` sets the lowest unset bit of x — to reverse this operation, find which bit to clear.
