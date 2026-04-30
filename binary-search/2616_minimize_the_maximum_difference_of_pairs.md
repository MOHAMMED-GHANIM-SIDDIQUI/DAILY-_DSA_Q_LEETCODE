# 2616. Minimize the Maximum Difference of Pairs

## 🔗 Problem Link
https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Binary Search, Greedy, Sorting

---

## 🧩 Problem Summary
Given a 0-indexed integer array `nums` and an integer `p`, find `p` pairs of indices such that the maximum difference among all pairs is minimized. Return the minimum possible maximum difference.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`
- `0 <= p <= nums.length / 2`

---

## 💭 Intuition
👉 Binary search on the maximum allowed difference. After sorting, greedily pair adjacent elements (smallest differences) and check if we can form at least `p` pairs where each pair's difference <= the candidate maximum.

---

## ⚡ Approach — Binary Search + Greedy Pairing

### 🧠 Idea
- Sort the array.
- Binary search on `maxDiff` in range `[0, max - min]`.
- For each candidate, greedily scan sorted array: if `nums[i] - nums[i-1] <= maxDiff`, pair them and skip both.
- If we can form >= `p` pairs, try a smaller `maxDiff`.

---

## 💻 Code

```cpp
class Solution {
 public:
  int minimizeMax(vector<int>& nums, int p) {
    ranges::sort(nums);

    int l = 0;
    int r = nums.back() - nums.front();

    while (l < r) {
      const int m = (l + r) / 2;
      if (numPairs(nums, m) >= p)
        r = m;
      else
        l = m + 1;
    }

    return l;
  }

 private:
  // Returns the number of pairs that can be obtained if the difference between
  // each pair <= `maxDiff`.
  int numPairs(const vector<int>& nums, int maxDiff) {
    int pairs = 0;
    for (int i = 1; i < nums.size(); ++i)
      // Greedily pair nums[i] with nums[i - 1].
      if (nums[i] - nums[i - 1] <= maxDiff) {
        ++pairs;
        ++i;
      }
    return pairs;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [10,1,2,7,1,3], p = 2
```
### Steps
```
Sorted: [1,1,2,3,7,10]
l=0, r=9

m=4: pairs: (1,1)=0<=4 pair, skip, (2,3)=1<=4 pair => 2 >= 2, r=4
m=2: pairs: (1,1)=0<=2 pair, skip, (2,3)=1<=2 pair => 2 >= 2, r=2
m=1: pairs: (1,1)=0<=1 pair, skip, (2,3)=1<=1 pair => 2 >= 2, r=1
m=0: pairs: (1,1)=0<=0 pair, skip, (2,3)=1>0 skip, (7,3)=4>0 skip, (10,7)=3>0 skip => 1 < 2, l=1
l==r==1 => return 1
```

---

## ⏱️ Time Complexity
```
O(n log n + n log(max - min))
```

## 💾 Space Complexity
```
O(1) (ignoring sort space)
```

---

## ⚠️ Edge Cases
- `p = 0`: no pairs needed, answer is 0
- All elements are equal: answer is 0
- `p = n/2`: must pair all elements

---

## 🎯 Interview Takeaways
- "Minimize the maximum" is a strong signal for binary search on the answer.
- Greedy adjacent pairing on sorted arrays is optimal because adjacent elements have the smallest differences.

---

## 📌 Key Pattern
👉 **"Binary search on the answer + greedy adjacent pairing on sorted array"**

---

## 🔁 Related Problems
- 2560. House Robber IV
- 875. Koko Eating Bananas
- 1552. Magnetic Force Between Two Balls

---

## 🚀 Final Thoughts
A textbook example of binary search on the answer. The greedy validation is elegant: in a sorted array, pairing adjacent elements minimizes pair differences, and the skip-one-after-pairing strategy ensures non-overlapping pairs.

---

✨ **Rule to remember:**
> "Minimize the maximum" problems almost always call for binary search on the answer with a greedy feasibility check.
