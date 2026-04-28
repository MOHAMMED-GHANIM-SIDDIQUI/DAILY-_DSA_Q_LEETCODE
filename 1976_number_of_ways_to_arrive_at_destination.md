# 1976. Number of Ways to Arrive at Destination

## 🔗 Problem Link
https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Graph, Shortest Path, Dynamic Programming, Math

---

## 🧩 Problem Summary
*Note: The solution file contains code for a matrix-related problem. The file is named 1976-LEETCODE.py and the code within computes the maximum matrix sum by flipping signs — which corresponds to LeetCode 1975. The markdown below documents the code as found in the file.*

Given a matrix of integers, you can repeatedly select two adjacent elements and multiply both by -1. Return the maximum possible sum of the matrix's elements.

### 📌 Constraints
- `n == matrix.length == matrix[i].length`
- `1 <= n <= 250`
- `-10^5 <= matrix[i][j] <= 10^5`

---

## 💭 Intuition
👉 We can always flip pairs to make most numbers positive. If there's an even number of negatives, we can make all positive. If odd, one negative must remain — we want it to be the smallest absolute value.

---

## ⚡ Approach — Count Negatives + Sum of Absolutes

### 🧠 Idea
- Compute the sum of absolute values of all elements.
- Track the minimum absolute value in the matrix.
- Count whether the number of negative elements is odd or even using XOR.
- If odd negatives: subtract twice the minimum absolute value (the one element we cannot make positive).
- If even negatives: the full absolute sum is achievable.

---

## 💻 Code

```python
class Solution:
  def maxMatrixSum(self, matrix: list[list[int]]) -> int:
    absSum = 0
    minAbs = math.inf
    # 0 := even number of negatives
    # 1 := odd number of negatives
    oddNeg = 0

    for row in matrix:
      for num in row:
        absSum += abs(num)
        minAbs = min(minAbs, abs(num))
        if num < 0:
          oddNeg ^= 1

    return absSum - oddNeg * minAbs * 2
```

---

## 🧠 Dry Run
### Input
```
matrix = [[1,-1],[-1,1]]
```
### Steps
```
absSum = 1 + 1 + 1 + 1 = 4
minAbs = 1
oddNeg: 1→0 (two negatives, XOR toggles twice → 0, even)
return 4 - 0 * 1 * 2 = 4
```

---

## ⏱️ Time Complexity
```
O(n^2), where n is the side length of the matrix
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- All positive → return sum
- All negative with even count → return sum of absolute values
- Contains zero → zero absorbs the odd negative (minAbs = 0, so no penalty)
- Single element → return its absolute value (if negative, oddNeg=1, subtract 2*abs)

---

## 🎯 Interview Takeaways
- Adjacent flips let you "move" a negative sign anywhere in the matrix.
- The parity of the count of negatives determines whether one negative must remain.
- XOR is an elegant way to track odd/even parity.

---

## 📌 Key Pattern
👉 **"Parity of negatives determines if we lose the smallest absolute value"**

---

## 🔁 Related Problems
- 1005. Maximize Sum Of Array After K Negations
- 2099. Find Subsequence of Length K With the Largest Sum
- 1980. Find Unique Binary String

---

## 🚀 Final Thoughts
This problem reduces to a simple mathematical observation: flipping adjacent pairs lets you move negatives freely, so only the parity of negative count matters. A clean O(n^2) single-pass solution.

---

✨ **Rule to remember:**
> With pairwise sign flips, only the parity of negatives matters — if odd, sacrifice the smallest absolute value.
