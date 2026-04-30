# 2179. Count Good Triplets in an Array

## 🔗 Problem Link
https://leetcode.com/problems/count-good-triplets-in-an-array/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Binary Indexed Tree (Fenwick Tree), Merge Sort, Ordered Set

---

## 🧩 Problem Summary
Given two permutations `nums1` and `nums2` of `[0, n-1]`, count the number of triplets `(x, y, z)` such that the relative order of `x`, `y`, `z` is the same in both arrays (i.e., `pos1(x) < pos1(y) < pos1(z)` and `pos2(x) < pos2(y) < pos2(z)`).

### 📌 Constraints
- `n == nums1.length == nums2.length`
- `3 <= n <= 10^5`
- `0 <= nums1[i], nums2[i] < n`
- Both arrays are permutations of `[0, n-1]`

---

## 💭 Intuition
👉 Remap `nums2` using the index positions from `nums1`. The problem reduces to counting increasing triplets in the remapped array, which can be done with two Fenwick trees.

---

## ⚡ Approach — Fenwick Tree (BIT) for Increasing Triplets

### 🧠 Idea
- Build a mapping from value to index in `nums1`.
- Remap `nums2` to get array `arr` where `arr[i] = index of nums2[i] in nums1`.
- For each position `i`, compute `leftSmaller[i]` (elements before `i` that are smaller) and `rightLarger[i]` (elements after `i` that are larger) using two Fenwick trees.
- Sum `leftSmaller[i] * rightLarger[i]` for all `i`.

---

## 💻 Code

```cpp
class FenwickTree {
 public:
  FenwickTree(int n) : sums(n + 1) {}

  void add(int i, int delta) {
    while (i < sums.size()) {
      sums[i] += delta;
      i += lowbit(i);
    }
  }

  int get(int i) const {
    int sum = 0;
    while (i > 0) {
      sum += sums[i];
      i -= lowbit(i);
    }
    return sum;
  }

 private:
  vector<int> sums;

  static inline int lowbit(int i) {
    return i & -i;
  }
};

class Solution {
 public:
  long long goodTriplets(vector<int>& nums1, vector<int>& nums2) {
    const int n = nums1.size();
    long ans = 0;
    unordered_map<int, int> numToIndex;
    vector<int> arr;
    // leftSmaller[i] := the number of arr[j] < arr[i], where 0 <= j < i
    vector<int> leftSmaller(n);
    // rightLarger[i] := the number of arr[j] > arr[i], where i < j < n
    vector<int> rightLarger(n);
    FenwickTree tree1(n);  // Calculates `leftSmaller`.
    FenwickTree tree2(n);  // Calculates `rightLarger`.

    for (int i = 0; i < n; ++i)
      numToIndex[nums1[i]] = i;

    // Remap each number in `nums2` to the according index in `nums1` as `arr`.
    // So the problem is to find the number of increasing tripets in `arr`.
    for (const int num : nums2)
      arr.push_back(numToIndex[num]);

    for (int i = 0; i < n; ++i) {
      leftSmaller[i] = tree1.get(arr[i]);
      tree1.add(arr[i] + 1, 1);
    }

    for (int i = n - 1; i >= 0; --i) {
      rightLarger[i] = tree2.get(n) - tree2.get(arr[i]);
      tree2.add(arr[i] + 1, 1);
    }

    for (int i = 0; i < n; ++i)
      ans += static_cast<long>(leftSmaller[i]) * rightLarger[i];

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums1 = [2, 0, 1, 3], nums2 = [0, 1, 2, 3]
```
### Steps
```
numToIndex: {2:0, 0:1, 1:2, 3:3}
arr (remap nums2): [1, 2, 0, 3]

leftSmaller: [0, 1, 0, 3]
rightLarger: [2, 1, 1, 0]

ans = 0*2 + 1*1 + 0*1 + 3*0 = 1
```

---

## ⏱️ Time Complexity
```
O(n log n) — Fenwick tree operations are O(log n) each, done n times
```

## 💾 Space Complexity
```
O(n) — for the Fenwick trees, mapping, and auxiliary arrays
```

---

## ⚠️ Edge Cases
- n = 3 → only one possible triplet to check
- Both arrays are identical → maximum number of increasing triplets
- Arrays are reverse of each other → zero good triplets

---

## 🎯 Interview Takeaways
- Remapping one permutation using another reduces the problem to counting increasing subsequences.
- Fenwick trees efficiently compute prefix counts for "how many smaller elements before" queries.
- The triplet count decomposes as: for each middle element, multiply left-smaller count by right-larger count.

---

## 📌 Key Pattern
👉 **"Remap + Fenwick tree to count increasing triplets across two permutations"**

---

## 🔁 Related Problems
- 315. Count of Smaller Numbers After Self
- 493. Reverse Pairs
- 2426. Number of Pairs Satisfying Inequality

---

## 🚀 Final Thoughts
A beautiful problem that combines permutation remapping with Fenwick tree counting. The decomposition of triplets into (leftSmaller * rightLarger) per middle element is a fundamental technique.

---

✨ **Rule to remember:**
> "Remap two permutations into one array, then count increasing triplets using Fenwick trees: left-smaller × right-larger for each middle."
