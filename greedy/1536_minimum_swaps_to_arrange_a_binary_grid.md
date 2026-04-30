# 1536. Minimum Swaps to Arrange a Binary Grid

## 🔗 Problem Link
https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Greedy, Matrix

---

## 🧩 Problem Summary
Given an `n x n` binary grid, you can swap any two adjacent rows. Return the minimum number of swaps needed so that all positions above the main diagonal are zeros. If impossible, return -1.

### 📌 Constraints
- `n == grid.length == grid[i].length`
- `1 <= n <= 200`
- `grid[i][j]` is `0` or `1`

---

## 💭 Intuition
👉 For row `i` to satisfy the upper-triangle-zero condition, it needs at least `n - 1 - i` trailing zeros. We greedily find the closest valid row for each position and bubble it up using adjacent swaps.

---

## ⚡ Approach — Greedy with Trailing Zero Count

### 🧠 Idea
- Precompute trailing zeros for each row.
- For each row position `i` (from top to bottom), find the first row at position `j >= i` with at least `n - 1 - i` trailing zeros.
- If no such row exists, return -1.
- Bubble that row up from position `j` to position `i` using adjacent swaps (each swap costs 1).

---

## 💻 Code

```python
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        trail_zeros = []
        for r in range(n):# 0 , 1 , 2
            zeroCnt= 0
            for e in range(n-1,-1,-1):
                if grid[r][e]==0:
                 zeroCnt+=1
                else:
                    break
            trail_zeros.append(zeroCnt)
        swap = 0
        for i in range(n):  # current row
            req_zero = n-1-i
            j = i
            while j<n and req_zero > trail_zeros[j]:
                j+=1
            if j == n:
                return -1
            else:
                for k in range(j,i,-1):
                    swap+=1
                    trail_zeros[k],trail_zeros[k-1]=trail_zeros[k-1],trail_zeros[k]
        return swap
```

---

## 🧠 Dry Run
### Input
```
grid = [[0,0,1],
        [1,1,0],
        [1,0,0]]
```
### Steps
```
Trailing zeros: [0, 1, 2]

i=0: req_zero = 2
  j=0: trail_zeros[0]=0 < 2, j=1: trail_zeros[1]=1 < 2, j=2: trail_zeros[2]=2 >= 2
  Bubble from 2 to 0: swap trail_zeros[2]↔[1], then [1]↔[0]
  trail_zeros = [2, 0, 1], swap = 2

i=1: req_zero = 1
  j=1: trail_zeros[1]=0 < 1, j=2: trail_zeros[2]=1 >= 1
  Bubble from 2 to 1: swap trail_zeros[2]↔[1]
  trail_zeros = [2, 1, 0], swap = 3

i=2: req_zero = 0 → trail_zeros[2]=0 >= 0 → no swap

Answer: 3
```

---

## ⏱️ Time Complexity
```
O(n^2) for the greedy selection and bubbling
```

## 💾 Space Complexity
```
O(n) for the trailing zeros array
```

---

## ⚠️ Edge Cases
- Already valid grid — 0 swaps needed.
- Impossible case — a row with no trailing zeros cannot be placed at position 0 (needs `n-1` trailing zeros).
- All zeros — always valid, 0 swaps.

---

## 🎯 Interview Takeaways
- Reducing the problem to trailing zero counts simplifies the 2D grid to a 1D problem.
- Greedy bubble-up is optimal because earlier rows have stricter requirements.
- This is similar to selection sort with adjacent swaps.

---

## 📌 Key Pattern
👉 **"Reduce matrix row conditions to a 1D property, then greedily bubble-sort rows into position"**

---

## 🔁 Related Problems
- 1505 — Minimum Possible Integer After at Most K Adjacent Swaps On Digits
- 765 — Couples Holding Hands
- 899 — Orderly Queue

---

## 🚀 Final Thoughts
The key insight is that the upper-triangle-zero condition translates to a trailing-zero requirement for each row, which decreases from top to bottom. Greedily assigning the closest valid row and bubble-swapping it into place gives the minimum swaps.

---

✨ **Rule to remember:**
> "For upper-triangle zeros, count trailing zeros per row and greedily bubble the closest valid row into each position."
