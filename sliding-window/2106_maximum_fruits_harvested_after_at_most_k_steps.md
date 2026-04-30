# 2106. Maximum Fruits Harvested After at Most K Steps

## 🔗 Problem Link
https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Binary Search, Sliding Window, Prefix Sum

---

## 🧩 Problem Summary
You are at position `startPos` on an infinite number line. Fruits are placed at various positions. You can move at most `k` steps left or right. Find the maximum total number of fruits you can collect. You can change direction at most once.

### 📌 Constraints
- `1 <= fruits.length <= 10^5`
- `fruits[i].length == 2`
- `0 <= startPos, position_i <= 2 * 10^5`
- `1 <= amount_i <= 10^4`
- `0 <= k <= 2 * 10^5`

---

## 💭 Intuition
👉 If you go right `r` steps then turn left, total steps = r + 2*r (going right then back and left) or vice versa. Use prefix sums to quickly compute fruit totals in any range, and enumerate all possible split points.

---

## ⚡ Approach — Prefix Sum + Enumerate Direction Splits

### 🧠 Idea
- Build a position-indexed array of fruit amounts and compute prefix sums.
- For each possible number of right steps, compute remaining left steps (k - 2*right) and query the prefix sum.
- Similarly, for each possible number of left steps, compute remaining right steps.
- Take the maximum across all splits.

---

## 💻 Code

```cpp
class Solution {
 public:
  int maxTotalFruits(vector<vector<int>>& fruits, int startPos, int k) {
    const int maxRight = max(startPos, fruits.back()[0]);
    int ans = 0;
    vector<int> amounts(1 + maxRight);
    vector<int> prefix(2 + maxRight);

    for (const vector<int>& f : fruits)
      amounts[f[0]] = f[1];

    partial_sum(amounts.begin(), amounts.end(), prefix.begin() + 1);

    auto getFruits = [&](int leftSteps, int rightSteps) {
      const int l = max(0, startPos - leftSteps);
      const int r = min(maxRight, startPos + rightSteps);
      return prefix[r + 1] - prefix[l];
    };

    // Go right first.
    const int maxRightSteps = min(maxRight - startPos, k);
    for (int rightSteps = 0; rightSteps <= maxRightSteps; ++rightSteps) {
      const int leftSteps = max(0, k - 2 * rightSteps);  // Turn left
      ans = max(ans, getFruits(leftSteps, rightSteps));
    }

    // Go left first.
    const int maxLeftSteps = min(startPos, k);
    for (int leftSteps = 0; leftSteps <= maxLeftSteps; ++leftSteps) {
      const int rightSteps = max(0, k - 2 * leftSteps);  // Turn right
      ans = max(ans, getFruits(leftSteps, rightSteps));
    }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4
```
### Steps
```
amounts: [0,0,8,0,0,0,3,0,6]
prefix:  [0,0,0,8,8,8,8,11,11,17]
Go right first:
  rightSteps=0, leftSteps=4: range [1,5] -> prefix[6]-prefix[1]=8 -> ans=8
  rightSteps=1, leftSteps=2: range [3,6] -> prefix[7]-prefix[3]=3 -> ans=8
  rightSteps=2, leftSteps=0: range [5,7] -> prefix[8]-prefix[5]=3 -> ans=8
  rightSteps=3, leftSteps=->(0): range [5,8] -> prefix[9]-prefix[5]=9 -> ans=9
  rightSteps=4, leftSteps=->(0): range [5,9?->8] -> 9 -> ans=9
Go left first:
  leftSteps=0, rightSteps=4: range [5,9?->8] -> 9 -> ans=9
  ...
Return 9
```

---

## ⏱️ Time Complexity
```
O(max(startPos, max_position) + k), essentially O(n) where n is the position range
```

## 💾 Space Complexity
```
O(max_position) for the amounts and prefix arrays
```

---

## ⚠️ Edge Cases
- All fruits behind start position: only go left
- All fruits ahead: only go right
- k = 0: only collect fruit at startPos
- No fruits at or near startPos

---

## 🎯 Interview Takeaways
- Prefix sums enable O(1) range queries.
- When you can turn at most once, enumerate the turning point.
- The cost of going right then left is `2 * rightSteps + leftSteps` (and vice versa).

---

## 📌 Key Pattern
👉 **"Prefix sum + enumerate direction split for one-turn movement problems"**

---

## 🔁 Related Problems
- 1793. Maximum Score of a Good Subarray
- 2270. Number of Ways to Split Array
- 1423. Maximum Points You Can Obtain from Cards

---

## 🚀 Final Thoughts
This problem elegantly combines prefix sums with the geometric insight about optimal movement on a line. Enumerating all possible turning points is the key to finding the optimal path.

---

✨ **Rule to remember:**
> On a line with one allowed turn, enumerate one direction's steps and compute the other from the budget.
