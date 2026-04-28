# 3583. Count Special Triplets

## 🔗 Problem Link
https://leetcode.com/problems/count-special-triplets/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Hash Map, Counting, Two-Pass

---

## 🧩 Problem Summary
Given an array `nums`, count the number of triplets (i, j, k) with i < j < k such that `nums[i] == 2 * nums[j]` and `nums[k] == 2 * nums[j]`. In other words, the first and third elements are double the middle element. Return the count modulo 10^9 + 7.

### 📌 Constraints
- `3 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^6`

---

## 💭 Intuition
👉 Fix the middle element and count how many valid left elements (equal to 2 * middle) and right elements (equal to 2 * middle) exist. Use two counters to track elements seen on the left and remaining on the right.

---

## ⚡ Approach — Left/Right Counter Sweep

### 🧠 Idea
- Initialize `right` counter with all elements, `left` counter empty.
- For each element x (as middle candidate), remove x from `right`.
- Count pairs: `left[2*x] * right[2*x]`.
- Add x to `left`.
- This ensures i < j < k ordering.

---

## 💻 Code

```python
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        left = Counter()
        right = Counter(nums)
        result = 0

        for x in nums:
            # move x from right to current position
            right[x] -= 1

            target = x * 2
            # count how many times target appears on left and right
            result = (result + left[target] * right[target]) % MOD

            # now x becomes part of left
            left[x] += 1

        return result
```

---

## 🧠 Dry Run
### Input
```
nums = [1, 2, 1, 4, 2]
```
### Steps
```
left={}, right={1:2, 2:2, 4:1}

x=1: right={1:1,2:2,4:1}. target=2. left[2]*right[2]=0*2=0. left={1:1}
x=2: right={1:1,2:1,4:1}. target=4. left[4]*right[4]=0*1=0. left={1:1,2:1}
x=1: right={1:0,2:1,4:1}. target=2. left[2]*right[2]=1*1=1. result=1. left={1:2,2:1}
x=4: right={1:0,2:1,4:0}. target=8. left[8]*right[8]=0*0=0. left={1:2,2:1,4:1}
x=2: right={1:0,2:0,4:0}. target=4. left[4]*right[4]=1*0=0. left={1:2,2:2,4:1}

Result: 1
```

---

## ⏱️ Time Complexity
```
O(n) — single pass through the array with O(1) counter lookups
```

## 💾 Space Complexity
```
O(n) — for the left and right counters
```

---

## ⚠️ Edge Cases
- No valid triplets → return 0
- All elements the same → only valid if the value equals 2 * value (impossible for positive integers)
- Large counts → modular arithmetic prevents overflow

---

## 🎯 Interview Takeaways
- The "fix middle, count left/right" pattern is powerful for three-element problems.
- Moving elements from right to left while scanning ensures correct ordering.
- Counter (hash map) lookups make this O(1) per element.

---

## 📌 Key Pattern
👉 **"Fix the middle element, count matching pairs on left and right using running counters."**

---

## 🔁 Related Problems
- 923. 3Sum With Multiplicity
- 1442. Count Triplets That Can Form Two Arrays of Equal XOR
- 2367. Number of Arithmetic Triplets

---

## 🚀 Final Thoughts
An elegant O(n) solution using the left/right counter technique. The key is recognizing that for each middle element, the contributions from left and right are independent and can be multiplied.

---

✨ **Rule to remember:**
> For triplet counting with ordering constraints, sweep through fixing the middle element and maintain left/right frequency maps.
