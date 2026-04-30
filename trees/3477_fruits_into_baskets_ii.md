# 3477. Fruits Into Baskets II

## 🔗 Problem Link
https://leetcode.com/problems/fruits-into-baskets-ii/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Segment Tree, Array, Greedy

---

## 🧩 Problem Summary
You are given two arrays `fruits` and `baskets`. For each fruit, find the first basket with capacity >= the fruit's size, place the fruit there (making the basket unavailable), and count how many fruits remain unplaced.

### 📌 Constraints
- `1 <= fruits.length, baskets.length <= 10^5`
- `1 <= fruits[i], baskets[i] <= 10^9`

---

## 💭 Intuition
👉 We need to efficiently find the **first** basket whose capacity is at least the fruit's size. A Segment Tree storing maximum values allows us to query for the leftmost valid basket in O(log n) time and mark it as used.

---

## ⚡ Approach — Segment Tree with First Query

### 🧠 Idea
- Build a Segment Tree over the `baskets` array, storing maximum values.
- For each fruit, query the segment tree for the first index where `baskets[i] >= fruit`.
- When a basket is used, update its value to -1 so it won't be selected again.
- Count fruits for which no valid basket is found (query returns -1).

---

## 💻 Code

```cpp
class SegmentTree {
 public:
  explicit SegmentTree(const vector<int>& nums) : n(nums.size()), tree(n * 4) {
    build(nums, 0, 0, n - 1);
  }

  // Updates nums[i] to val.
  void update(int i, int val) {
    update(0, 0, n - 1, i, val);
  }

  // Returns the first index i where baskets[i] >= target, or -1 if not found.
  int queryFirst(int target) {
    return queryFirst(0, 0, n - 1, target);
  }

 private:
  const int n;       // the size of the input array
  vector<int> tree;  // the segment tree

  void build(const vector<int>& nums, int treeIndex, int lo, int hi) {
    if (lo == hi) {
      tree[treeIndex] = nums[lo];
      return;
    }
    const int mid = (lo + hi) / 2;
    build(nums, 2 * treeIndex + 1, lo, mid);
    build(nums, 2 * treeIndex + 2, mid + 1, hi);
    tree[treeIndex] = merge(tree[2 * treeIndex + 1], tree[2 * treeIndex + 2]);
  }

  void update(int treeIndex, int lo, int hi, int i, int val) {
    if (lo == hi) {
      tree[treeIndex] = val;
      return;
    }
    const int mid = (lo + hi) / 2;
    if (i <= mid)
      update(2 * treeIndex + 1, lo, mid, i, val);
    else
      update(2 * treeIndex + 2, mid + 1, hi, i, val);
    tree[treeIndex] = merge(tree[2 * treeIndex + 1], tree[2 * treeIndex + 2]);
  }

  int queryFirst(int treeIndex, int lo, int hi, int target) {
    if (tree[treeIndex] < target)
      return -1;
    if (lo == hi) {
      // Found a valid position, mark it as used by setting to -1.
      update(lo, -1);
      return lo;
    }
    const int mid = (lo + hi) / 2;
    const int leftChild = tree[2 * treeIndex + 1];
    return leftChild >= target
               ? queryFirst(2 * treeIndex + 1, lo, mid, target)
               : queryFirst(2 * treeIndex + 2, mid + 1, hi, target);
  }

  int merge(int left, int right) const {
    return max(left, right);
  }
};

class Solution {
 public:
  int numOfUnplacedFruits(vector<int>& fruits, vector<int>& baskets) {
    int ans = 0;
    SegmentTree tree(baskets);

    for (const int fruit : fruits)
      if (tree.queryFirst(fruit) == -1)
        ++ans;

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
fruits = [4, 2, 5], baskets = [3, 5, 4]
```
### Steps
```
Build segment tree from baskets = [3, 5, 4]
Tree max = 5

Fruit 4: queryFirst(4) -> check left max(3) < 4, go right -> index 1 (val 5 >= 4), mark used. Return 1.
Fruit 2: queryFirst(2) -> check left max(3) >= 2, go left -> index 0 (val 3 >= 2), mark used. Return 0.
Fruit 5: queryFirst(5) -> check left max(-1) < 5, go right -> index 2 (val 4 < 5), return -1. ans++.

Result: 1
```

---

## ⏱️ Time Complexity
```
O(n log n) — each fruit requires O(log n) segment tree query and update
```

## 💾 Space Complexity
```
O(n) — for the segment tree storage
```

---

## ⚠️ Edge Cases
- All fruits larger than all baskets → answer = len(fruits)
- All baskets large enough → answer = 0
- Single fruit, single basket

---

## 🎯 Interview Takeaways
- Segment trees can answer "first index satisfying a condition" queries efficiently.
- Setting used elements to -1 (or INT_MIN) is a clean way to invalidate positions.
- This pattern appears whenever you need greedy first-fit allocation.

---

## 📌 Key Pattern
👉 **"Segment Tree for first-fit allocation — query leftmost valid position and mark as used."**

---

## 🔁 Related Problems
- 3479. Fruits Into Baskets III
- 2286. Booking Concert Tickets in Groups
- 1157. Online Majority Element In Subarray

---

## 🚀 Final Thoughts
This problem is a classic application of segment trees for greedy allocation. The key insight is transforming a "find first available" problem into a segment tree max-query with leftward preference.

---

✨ **Rule to remember:**
> When you need to find the first element meeting a threshold in an array with updates, use a Segment Tree with a "query first" operation.
