# 2574. Left and Right Sum Differences

## 🔗 Problem Link
https://leetcode.com/problems/left-and-right-sum-differences/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Prefix Sum

---

## 🧩 Problem Summary

Given a 0-indexed array `nums`, build an array `answer` where `answer[i] = |leftSum[i] - rightSum[i]|`. Here `leftSum[i]` is the sum of all elements to the left of index `i` and `rightSum[i]` is the sum of all elements to the right of index `i`. Elements at index `i` itself are excluded from both sums.

### 📌 Constraints
- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 10^5`

---

## 💭 Intuition

👉 Start with `right_sum` equal to the total of all elements. As you scan left to right, remove the current element from `right_sum` first (so it excludes index `i`), record the absolute difference, then add the current element to `left_sum` for the next index.

---

## ⚡ Approach — Two Running Sums

### 🧠 Idea
- Set `left_sum = 0` and `right_sum = sum(nums)`.
- For each `num` at index `i`:
  - Subtract `num` from `right_sum` → now `right_sum` is the sum strictly to the right of `i`.
  - Append `abs(left_sum - right_sum)` to the result.
  - Add `num` to `left_sum` → prepares `left_sum` for index `i+1`.
- Return the result array.

---

## 💻 Code

```python
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        result = []
        left_sum = 0
        right_sum = sum(nums)

        for num in nums:
            right_sum -= num
            result.append(abs(left_sum - right_sum))
            left_sum += num

        return result
```

---

## 🧠 Dry Run

### Input
```
nums = [10, 4, 8, 3]
```

### Steps
```
left_sum=0, right_sum=25
i=0 num=10: right_sum=15, append |0-15|=15, left_sum=10
i=1 num=4 : right_sum=11, append |10-11|=1, left_sum=14
i=2 num=8 : right_sum=3,  append |14-3|=11, left_sum=22
i=3 num=3 : right_sum=0,  append |22-0|=22, left_sum=25
result = [15, 1, 11, 22]
```

---

## ⏱️ Time Complexity
```
O(n)
```
One pass to compute the total plus one pass to fill the answer.

---

## 💾 Space Complexity
```
O(1)
```
Excluding the required output array, only two running sums are used.

---

## ⚠️ Edge Cases
- Single element → leftSum and rightSum are both 0, answer is `[0]`.
- All equal elements still produce correct decreasing/increasing differences.
- Large values fit comfortably in Python integers (no overflow concern).

---

## 🎯 Interview Takeaways
- Order matters: subtract from `right_sum` before recording, then add to `left_sum` after, so index `i` is never double-counted.
- This avoids precomputing a full prefix array; two scalars suffice.
- Equivalent to `prefix[i-1]` vs `total - prefix[i]`, just streamed.

---

## 📌 Key Pattern
👉 **"Sweep with left and right running sums"**

---

## 🔁 Related Problems
- 0724 - Find Pivot Index
- 1480 - Running Sum of 1d Array
- 0238 - Product of Array Except Self

---

## 🚀 Final Thoughts
A direct application of prefix/suffix sums collapsed into a single sweep. The careful subtract-then-add ordering keeps the current element out of both sides.

---

✨ **Rule to remember:**
> "Maintain left and right running totals and update them around the current element to exclude it from both."
