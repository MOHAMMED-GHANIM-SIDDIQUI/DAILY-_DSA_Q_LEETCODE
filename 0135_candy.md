# 135. Candy

## 🔗 Problem Link
https://leetcode.com/problems/candy/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Greedy

---

## 🧩 Problem Summary

There are `n` children standing in a line, each with a rating value. You need to distribute candies such that: (1) each child gets at least one candy, and (2) children with a higher rating than their neighbor must get more candies than that neighbor. Return the minimum total number of candies needed.

### 📌 Constraints
- `n == ratings.length`
- `1 <= n <= 2 * 10^4`
- `0 <= ratings[i] <= 2 * 10^4`

---

## 💭 Intuition

👉 A single left-to-right pass handles the constraint with the left neighbor, and a single right-to-left pass handles the right neighbor. Taking the max of both passes at each position satisfies both constraints simultaneously with minimum candies.

---

## ⚡ Approach — Two-Pass Greedy

### 🧠 Idea

- Initialize two arrays `l` and `r`, both filled with 1 (minimum one candy each).
- **Left pass:** For `i = 1` to `n-1`, if `ratings[i] > ratings[i-1]`, set `l[i] = l[i-1] + 1`.
- **Right pass:** For `i = n-2` down to `0`, if `ratings[i] > ratings[i+1]`, set `r[i] = r[i+1] + 1`.
- The answer is the sum of `max(l[i], r[i])` for all `i`.

---

## 💻 Code

```cpp
class Solution {
 public:
  int candy(vector<int>& ratings) {
    const int n = ratings.size();
    int ans = 0;
    vector<int> l(n, 1);
    vector<int> r(n, 1);

    for (int i = 1; i < n; ++i)
      if (ratings[i] > ratings[i - 1])
        l[i] = l[i - 1] + 1;

    for (int i = n - 2; i >= 0; --i)
      if (ratings[i] > ratings[i + 1])
        r[i] = r[i + 1] + 1;

    for (int i = 0; i < n; ++i)
      ans += max(l[i], r[i]);

    return ans;
  }
};
```

---

## 🧠 Dry Run

### Input
```
ratings = [1, 0, 2]
```

### Steps
```
Initialize: l = [1,1,1], r = [1,1,1]

Left pass:
  i=1: ratings[1]=0 > ratings[0]=1? No
  i=2: ratings[2]=2 > ratings[1]=0? Yes → l[2] = l[1]+1 = 2
  l = [1,1,2]

Right pass:
  i=1: ratings[1]=0 > ratings[2]=2? No
  i=0: ratings[0]=1 > ratings[1]=0? Yes → r[0] = r[1]+1 = 2
  r = [2,1,1]

Result: max(1,2) + max(1,1) + max(2,1) = 2+1+2 = 5
```

---

## ⏱️ Time Complexity

```
O(n)
```

Three linear passes through the array.

---

## 💾 Space Complexity

```
O(n)
```

Two auxiliary arrays of size n.

---

## ⚠️ Edge Cases

- **Single child:** `ratings = [5]` → return 1
- **All equal:** `ratings = [3,3,3]` → each gets 1 → return 3
- **Strictly increasing:** `ratings = [1,2,3]` → candies = [1,2,3] → return 6

---

## 🎯 Interview Takeaways

- Two-pass greedy is a powerful technique for bidirectional constraints.
- Taking the `max` of both passes ensures both neighbor constraints are satisfied.
- This problem demonstrates that greedy can solve complex constraint satisfaction with O(n) time.
- A follow-up challenge is to solve it with O(1) space using a single-pass approach.

---

## 📌 Key Pattern

👉 **"Two-pass greedy: left-to-right for left constraints, right-to-left for right constraints, take the max."**

---

## 🔁 Related Problems

- 42. Trapping Rain Water (also uses two-pass technique)
- 238. Product of Array Except Self
- 1013. Partition Array Into Three Parts With Equal Sum
- 2135. Count Words Obtained After Adding a Letter

---

## 🚀 Final Thoughts

Candy is an excellent example of how bidirectional constraints can be decomposed into two independent unidirectional passes. The two-pass greedy pattern appears in many array problems.

---

✨ **Rule to remember:**
> "When neighbors impose constraints from both sides, scan left-to-right and right-to-left, then merge with max."
