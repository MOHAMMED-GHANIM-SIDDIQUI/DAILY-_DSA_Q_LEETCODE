# 2125. Number of Laser Beams in a Bank

## 🔗 Problem Link
https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Math, String, Matrix

---

## 🧩 Problem Summary
Given a 2D bank floor plan where `'1'` represents a security device and `'0'` is empty, laser beams form between every pair of devices on two consecutive rows that contain devices (rows with no devices are skipped). Return the total number of laser beams.

### 📌 Constraints
- `m == bank.length`
- `n == bank[i].length`
- `1 <= m, n <= 500`
- `bank[i][j]` is either `'0'` or `'1'`

---

## 💭 Intuition
👉 The number of beams between two consecutive device-containing rows is simply the product of their device counts. Skip rows with no devices.

---

## ⚡ Approach — Count Devices Per Row

### 🧠 Idea
- Track the number of `'1'`s in the previous row that had devices (`prevOnes`).
- For each new row with at least one device, add `prevOnes * currentOnes` to the answer.
- Update `prevOnes` to `currentOnes`.

---

## 💻 Code

```cpp
class Solution {
 public:
  int numberOfBeams(vector<string>& bank) {
    int ans = 0;
    int prevOnes = 0;

    for (const string& row : bank) {
      const int ones = ranges::count(row, '1');
      if (ones > 0) {
        ans += prevOnes * ones;
        prevOnes = ones;
      }
    }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
bank = ["011001","000000","010100","001000"]
```
### Steps
```
Row "011001": ones=3, ans += 0*3 = 0, prevOnes=3
Row "000000": ones=0, skip
Row "010100": ones=2, ans += 3*2 = 6, prevOnes=2
Row "001000": ones=1, ans += 2*1 = 8, prevOnes=1
Return 8
```

---

## ⏱️ Time Complexity
```
O(m * n), where m = rows, n = columns
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- Only one row with devices: 0 beams
- All rows empty except one: 0 beams
- Every row has devices: sum of products of consecutive row counts
- All cells are devices: product of consecutive row lengths

---

## 🎯 Interview Takeaways
- Rows with zero devices act as "transparent" and are simply skipped.
- Beams between rows = product of device counts (combinatorial pairing).
- Single pass with O(1) space.

---

## 📌 Key Pattern
👉 **"Product of consecutive non-zero row counts"**

---

## 🔁 Related Problems
- 1572. Matrix Diagonal Sum
- 1582. Special Positions in a Binary Matrix
- 2482. Difference Between Ones and Zeros in Row and Column

---

## 🚀 Final Thoughts
A simple math problem disguised as a matrix problem. The key realization is that empty rows don't block beams, so we just need consecutive non-empty row device counts.

---

✨ **Rule to remember:**
> Laser beams between rows = product of device counts; skip empty rows entirely.
