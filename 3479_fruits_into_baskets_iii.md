# 3479. Fruits Into Baskets III

## 🔗 Problem Link
https://leetcode.com/problems/fruits-into-baskets-iii/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Segment Tree, Array, Greedy

---

## 🧩 Problem Summary
Same as 3477 — given two arrays `fruits` and `baskets`, for each fruit find the first basket with capacity >= the fruit's size, place the fruit (making that basket unavailable), and return the count of unplaced fruits. This variant may have different constraints but uses the same segment tree approach.

### 📌 Constraints
- `1 <= fruits.length, baskets.length <= 10^5`
- `1 <= fruits[i], baskets[i] <= 10^9`

---

## 💭 Intuition
👉 Identical to 3477 — use a Segment Tree storing max values to efficiently find the **leftmost basket** with sufficient capacity, then mark it as used.

---

## ⚡ Approach — Segment Tree with First Query

### 🧠 Idea
- Build a max segment tree over baskets.
- For each fruit, find the leftmost basket with value >= fruit size.
- Mark used baskets by setting value to -1.
- Count unplaced fruits.

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
  // Same as 3477. Fruits Into Baskets II
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

Fruit 4: queryFirst(4) -> left max(3) < 4, go right -> index 1 (val 5 >= 4), mark used. Return 1.
Fruit 2: queryFirst(2) -> left max(3) >= 2, go left -> index 0 (val 3 >= 2), mark used. Return 0.
Fruit 5: queryFirst(5) -> left max(-1) < 5, go right -> index 2 (val 4 < 5), return -1. ans++.

Result: 1
```

---

## ⏱️ Time Complexity
```
O(n log n) — each fruit requires O(log n) for query + update
```

## 💾 Space Complexity
```
O(n) — segment tree storage
```

---

## ⚠️ Edge Cases
- All fruits larger than all baskets → answer = len(fruits)
- All baskets large enough → answer = 0
- Identical fruit sizes competing for same baskets

---

## 🎯 Interview Takeaways
- Recognize when a problem is a variant of a known problem — same approach applies.
- Segment trees shine for "find first satisfying element" with point updates.
- Greedy left-to-right allocation is a common pattern.

---

## 📌 Key Pattern
👉 **"Segment Tree for first-fit allocation with point invalidation."**

---

## 🔁 Related Problems
- 3477. Fruits Into Baskets II
- 2286. Booking Concert Tickets in Groups
- 1157. Online Majority Element In Subarray

---

## 🚀 Final Thoughts
This is essentially the same problem as 3477. The segment tree approach handles both variants cleanly, demonstrating the versatility of segment trees for online greedy allocation queries.

---

✨ **Rule to remember:**
> When two problems share the same structure, reuse the same data structure — segment trees generalize across similar first-fit problems.
