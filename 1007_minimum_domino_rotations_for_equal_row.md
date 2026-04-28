# 1007. Minimum Domino Rotations For Equal Row

## 🔗 Problem Link
https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Greedy

---

## 🧩 Problem Summary

Given two rows of dominoes `tops` and `bottoms` of the same length, return the minimum number of rotations so that all values in `tops` are the same, or all values in `bottoms` are the same. If it cannot be done, return -1.

### 📌 Constraints
- `2 <= tops.length <= 2 * 10^4`
- `tops.length == bottoms.length`
- `1 <= tops[i], bottoms[i] <= 6`

---

## 💭 Intuition

👉 The target value that fills an entire row must be either `A[0]` or `B[0]` — if a valid answer exists, one of these two values must appear in every column.

👉 For a candidate value, count how many swaps are needed to fill the top row vs. the bottom row, and pick the minimum.

---

## ⚡ Approach — Greedy with Two Candidates

### 🧠 Idea
- Try both `A[0]` and `B[0]` as candidate target values.
- For each candidate, iterate through every position and count rotations needed.
- If a position has neither top nor bottom equal to the candidate, that candidate is impossible.
- Return the minimum rotations across both candidates and both rows.

---

## 💻 Code

```cpp
class Solution {
public:
    int minDominoRotations(vector<int>& A, vector<int>& B) {
        // Try to make all values in A and B equal to the values from A[0] or B[0]
        int min_rotations = min(helper(A, B, A[0]), helper(A, B, B[0]));

        // If neither A[0] nor B[0] could result in a valid solution, return -1
        return min_rotations == INT_MAX ? -1 : min_rotations;
    }

    int helper(vector<int>& A, vector<int>& B, int x) {
        int rotationsA = 0, rotationsB = 0;

        for (int i = 0; i < A.size(); ++i) {
            // If x doesn't appear in either A[i] or B[i], it's not possible
            if (A[i] != x && B[i] != x) return INT_MAX;

            // Count the number of rotations needed to make A[i] or B[i] equal to x
            if (A[i] != x) rotationsA++;
            else if (B[i] != x) rotationsB++;
        }

        return min(rotationsA, rotationsB);
    }
};
```

---

## 🧠 Dry Run

### Input
```
A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
```

### Steps
```
Candidate x = 2 (A[0]):
  i=0: A[0]=2 == x → rotationsB++ → rotationsA=0, rotationsB=1
  i=1: A[1]=1 != x, B[1]=2 == x → rotationsA++ → rotationsA=1, rotationsB=1
  i=2: A[2]=2 == x → rotationsB++ → rotationsA=1, rotationsB=2
  i=3: A[3]=4 != x, B[3]=2 == x → rotationsA++ → rotationsA=2, rotationsB=2
  i=4: A[4]=2 == x → rotationsB++ → rotationsA=2, rotationsB=3
  i=5: A[5]=2 == x, B[5]=2 == x → no change
  Return min(2, 3) = 2

Candidate x = 5 (B[0]):
  i=0: A[0]=2 != 5, B[0]=5 == 5 → rotationsA++
  i=1: A[1]=1 != 5, B[1]=2 != 5 → return INT_MAX

Answer = min(2, INT_MAX) = 2
```

---

## ⏱️ Time Complexity
```
O(n)
```
We iterate through the array at most twice (once per candidate).

---

## 💾 Space Complexity
```
O(1)
```
Only a few integer counters are used.

---

## ⚠️ Edge Cases
- All dominoes already have the same value on top → return 0.
- No valid value can fill an entire row → return -1.
- A[0] == B[0] → only one candidate needs checking.

---

## 🎯 Interview Takeaways
- The key insight is narrowing candidates to just A[0] and B[0].
- Greedy counting avoids brute-force checking all 6 possible values.
- Using a helper function keeps the code clean and DRY.
- INT_MAX serves as a sentinel for "impossible."

---

## 📌 Key Pattern
👉 **"Candidate elimination — if a value must appear everywhere, it must appear at position 0."**

---

## 🔁 Related Problems
- 1053 - Previous Permutation With One Swap
- 969 - Pancake Sorting
- 838 - Push Dominoes

---

## 🚀 Final Thoughts
A clean greedy solution that reduces a seemingly complex problem to two simple linear scans by identifying that the answer must involve A[0] or B[0].

---

✨ **Rule to remember:**
> "If every column must contain a target value, that target must appear in the very first column."
