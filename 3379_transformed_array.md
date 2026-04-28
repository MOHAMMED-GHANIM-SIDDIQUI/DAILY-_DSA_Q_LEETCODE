# 3379. Transformed Array

## 🔗 Problem Link
https://leetcode.com/problems/transformed-array/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Simulation

---

## 🧩 Problem Summary
Given a circular array `nums`, construct a result array where each element `result[i] = nums[(i + nums[i]) % n]`. The array is circular, so indices wrap around using modulo arithmetic.

### 📌 Constraints
- `1 <= nums.length <= 100`
- `-100 <= nums[i] <= 100`

---

## 💭 Intuition
👉 For each index `i`, compute the target index `(i + nums[i]) % n` using modulo for circular wrapping, then look up the value at that position.

---

## ⚡ Approach — Direct Simulation

### 🧠 Idea
- Iterate through each index `i`.
- Compute the target index as `(i + nums[i]) % n` (Python's modulo handles negative values correctly).
- Append `nums[target]` to the result.

---

## 💻 Code

```python
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)

        for i in range(n):
            target = (i + nums[i]) % n
            res.append(nums[target])

        return res
```

---

## 🧠 Dry Run
### Input
```
nums = [3, -2, 1, 1]
```
### Steps
```
1. i=0: target = (0+3) % 4 = 3, res.append(nums[3]) = 1
2. i=1: target = (1+(-2)) % 4 = -1 % 4 = 3, res.append(nums[3]) = 1
3. i=2: target = (2+1) % 4 = 3, res.append(nums[3]) = 1
4. i=3: target = (3+1) % 4 = 0, res.append(nums[0]) = 3
Result: [1, 1, 1, 3]
```

---

## ⏱️ Time Complexity
```
O(n) — single pass through the array.
```

## 💾 Space Complexity
```
O(n) for the result array.
```

---

## ⚠️ Edge Cases
- Negative values in `nums`: Python's `%` operator handles negative modulo correctly.
- `nums[i] = 0`: target is `i` itself, so `result[i] = nums[i]`.
- Single element array: always maps to itself.

---

## 🎯 Interview Takeaways
- Python's modulo operator naturally handles negative numbers, making circular array problems cleaner.
- In languages like C++/Java, negative modulo may need manual adjustment: `((i + nums[i]) % n + n) % n`.
- Circular array indexing with modulo is a fundamental technique.

---

## 📌 Key Pattern
👉 **"Circular array indexing with modulo arithmetic"**

---

## 🔁 Related Problems
- 1652. Defuse the Bomb
- 503. Next Greater Element II
- 918. Maximum Sum Circular Subarray

---

## 🚀 Final Thoughts
A simple simulation problem that tests understanding of circular array indexing. The key is correctly handling the modulo operation, especially with negative offsets. Python makes this particularly clean.

---

✨ **Rule to remember:**
> For circular array access, use `(i + offset) % n` — in Python, this correctly handles negative offsets too.
