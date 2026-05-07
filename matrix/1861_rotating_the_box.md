# 1861. Rotating the Box

## 🔗 Problem Link
https://leetcode.com/problems/rotating-the-box/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Two Pointers, Matrix

---

## 🧩 Problem Summary
You are given an `m x n` matrix `box` representing a side-view of a box. Each cell is one of:
- `'#'` → a stone
- `'*'` → a stationary obstacle
- `'.'` → empty space

The box is rotated 90° clockwise. After the rotation, gravity pulls every stone **downward** (in the rotated view) until it hits the bottom of the box, an obstacle, or another stone.

Return the matrix after the rotation, with all stones settled.

### 📌 Constraints
- `m == box.length`
- `n == box[i].length`
- `1 <= m, n <= 500`
- `box[i][j]` is `'#'`, `'*'`, or `'.'`

---

## 💭 Intuition
👉 In the **original** orientation, gravity points to the **right** (because after a 90° clockwise rotation, the right side becomes the bottom). So the cleanest order of operations is:

1. Apply **rightward gravity** on each row of the input — far simpler than reasoning about a rotated grid.
2. Then perform the 90° clockwise rotation.

For rightward gravity, walk each row from right to left tracking the next empty slot. When we see `#`, drop it into that slot and move the slot left. When we see `*`, the slot resets to just left of the obstacle.

The two steps can also be **fused into one pass**: while scanning, write each character directly into its final position in the rotated grid — this skips the second loop entirely.

---

## ⚡ Approach — Right-Gravity + Rotate (Fused)

### 🧠 Idea
- Allocate the rotated matrix `rotate[n][m]` filled with `'.'`.
- For each row `i` of `box`, scan from right to left with a pointer `bottom = n - 1`.
  - On `'*'`: place it at `rotate[j][r-1-i]` and reset `bottom = j - 1`.
  - On `'#'`: place it at `rotate[bottom][r-1-i]` and decrement `bottom`.
  - On `'.'`: skip (the rotated cell already holds `'.'`).
- The clockwise mapping `(i, j) → (j, m-1-i)` is applied directly during the scan, so no separate rotation step is needed.

---

## 💻 Code

```python
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        r, c = len(box), len(box[0])
        rotate = [['.'] * r for _ in range(c)]
        
        for i in range(r):
            bottom = c - 1
            for j in range(c - 1, -1, -1):
                if box[i][j] == '*':
                    rotate[j][r - 1 - i] = '*'
                    bottom = j - 1
                elif box[i][j] == '#':
                    rotate[bottom][r - 1 - i] = '#'
                    bottom -= 1
        
        return rotate
```

---

## 🧠 Dry Run
### Input
```
box = [["#",".","#"]]    (1 x 3)
```
### Steps
```
r = 1, c = 3, rotate = [['.'], ['.'], ['.']]   (3 x 1)

Row i = 0, bottom = 2
 j = 2: box[0][2] = '#'  → rotate[2][0] = '#', bottom = 1
 j = 1: box[0][1] = '.'  → skip
 j = 0: box[0][0] = '#'  → rotate[1][0] = '#', bottom = 0

Result:
 [['.'],
  ['#'],
  ['#']]
```
Both stones fall to the bottom of the rotated column ✅

---

## ⏱️ Time Complexity
```
O(m * n) — every cell of box is visited exactly once and a constant amount of work is done.
```

## 💾 Space Complexity
```
O(m * n) — for the output matrix `rotate`. No additional auxiliary structures.
        (The problem requires returning a new matrix shaped n x m, so this is unavoidable.)
```

---

## ⚠️ Edge Cases
- Single row (`m == 1`) → becomes a single column after rotation, gravity stacks stones at the bottom.
- Single column (`n == 1`) → becomes a single row; nothing to fall (each row of length 1 has no horizontal motion).
- Row full of obstacles → no stones move; rotation places everything as-is.
- Row full of stones with no obstacles → all stones land at the right end, then become the bottom of the rotated column.
- Empty cells only → the row contributes a column of `'.'` after rotation.

---

## 🎯 Interview Takeaways
- **Apply gravity in the easy frame first, rotate after.** Reasoning about gravity in the rotated grid is error-prone; rightward gravity per row is trivially correct.
- Use a **two-pointer right-to-left scan** with an `empty`/`bottom` index — the canonical pattern for "settle items against a wall with obstacles."
- The rotation map `(i, j) → (j, m-1-i)` for 90° clockwise is worth memorizing; it lets you fuse rotation with any per-row preprocessing.
- Fusing the two passes saves one full grid traversal but does **not** change the asymptotic complexity — choose readability vs. micro-optimization based on context.

---

## 📌 Key Pattern
👉 **"Simulate gravity in the original orientation with a right-to-left two-pointer pass, then map each cell to its rotated coordinate."**

---

## 🔁 Related Problems
- 48. Rotate Image
- 1886. Determine Whether Matrix Can Be Obtained By Rotation
- 723. Candy Crush
- 2073. Time Needed to Buy Tickets

---

## 🚀 Final Thoughts
The trap on this problem is trying to apply gravity *after* rotating — which makes "down" a column-walk and tangles the indexing. Doing gravity first, rotation second, keeps each step a clean one-liner of well-known patterns.

---

✨ **Rule to remember:**
> When a problem combines a transformation with a physics-style settle, do the settle in whichever orientation is simplest, then apply the transformation — don't fight gravity in the rotated frame.
