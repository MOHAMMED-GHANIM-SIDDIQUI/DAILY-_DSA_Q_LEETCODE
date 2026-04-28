# 3507. Minimum Pair Removal to Sort Array I

## 🔗 Problem Link
https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Greedy, Simulation

---

## 🧩 Problem Summary
Given an array `nums`, repeatedly find the pair of adjacent elements with the smallest sum, replace them with their sum, and remove the second element. Return the number of operations needed to make the array non-decreasing.

### 📌 Constraints
- `1 <= nums.length <= 50`
- `-1000 <= nums[i] <= 1000`

---

## 💭 Intuition
👉 Since the array is small, simulate the process directly: at each step, find the minimum adjacent pair sum, merge them, and check if the array is sorted.

---

## ⚡ Approach — Direct Simulation

### 🧠 Idea
- While the array has any inversion (decreasing adjacent pair), find the pair with the minimum sum.
- Replace the pair with their sum and remove the second element.
- Count each operation until the array is non-decreasing.

---

## 💻 Code

```python
class Solution:
  def minimumPairRemoval(self, nums: list[int]) -> int:
    ans = 0

    while any(x > y for x, y in itertools.pairwise(nums)):
      pairSums = [x + y for x, y in itertools.pairwise(nums)]
      minPairSum = min(pairSums)
      minPairIndex = pairSums.index(minPairSum)
      nums[minPairIndex] = minPairSum
      nums.pop(minPairIndex + 1)
      ans += 1

    return ans
```

---

## 🧠 Dry Run
### Input
```
nums = [5, 2, 3, 1]
```
### Steps
```
Step 0: [5, 2, 3, 1] — has inversions (5>2, 3>1)
  pairSums = [7, 5, 4], min=4 at index 2
  Merge index 2,3: [5, 2, 4]
  ans = 1

Step 1: [5, 2, 4] — has inversion (5>2)
  pairSums = [7, 6], min=6 at index 1
  Merge index 1,2: [5, 6]
  ans = 2

Step 2: [5, 6] — no inversions → done

Result: 2
```

---

## ⏱️ Time Complexity
```
O(n^3) — up to n-1 operations, each scanning O(n) pairs, with O(n) inversion check
```

## 💾 Space Complexity
```
O(n) — for the pairSums list
```

---

## ⚠️ Edge Cases
- Already sorted array → return 0
- Single element → return 0
- All elements equal → return 0
- All negative numbers

---

## 🎯 Interview Takeaways
- `itertools.pairwise` is a clean way to iterate adjacent pairs in Python.
- Brute-force simulation is acceptable for small constraints.
- Always check the stopping condition carefully (non-decreasing, not strictly increasing).

---

## 📌 Key Pattern
👉 **"Simulate the greedy merge process — always pick the smallest adjacent sum."**

---

## 🔁 Related Problems
- 3510. Minimum Pair Removal to Sort Array II
- 2165. Smallest Value of the Rearranged Number
- 2231. Largest Number After Digit Swaps by Parity

---

## 🚀 Final Thoughts
This is a straightforward simulation problem. The small constraints allow brute force. The harder version (3510) requires efficient data structures to scale this approach.

---

✨ **Rule to remember:**
> "For small arrays, simulate greedily — merge the smallest adjacent pair until sorted."
