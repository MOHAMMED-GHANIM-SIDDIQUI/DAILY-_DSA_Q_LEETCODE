# 3721. Count Non-Decreasing Subarrays After K Operations

## 🔗 Problem Link
https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Segment Tree, Lazy Propagation, Prefix Sum, Hash Map, Deque

---

## 🧩 Problem Summary
Given an array `nums`, find the length of the longest subarray where the number of distinct even values equals the number of distinct odd values. This optimized solution uses a segment tree with lazy propagation to efficiently track prefix sums and find the farthest valid endpoint for each starting position.

### 📌 Constraints
- `1 <= len(nums) <= 10^5`
- `1 <= nums[i] <= 10^9`

---

## 💭 Intuition
👉 Assign `+1` to even numbers and `-1` to odd numbers. A balanced subarray `[i..j]` has prefix_sum[j] - prefix_sum[i-1] == 0. Use a segment tree to find the farthest index with a target prefix sum, and update lazily as the starting position slides forward.

---

## ⚡ Approach — Segment Tree with Lazy Propagation

### 🧠 Idea
- Convert parity into signs: even → `+1`, odd → `-1`.
- Build prefix sums over these sign values.
- Use a segment tree that supports range add (lazy propagation) and can find the last occurrence of a given value in a range.
- For each starting index `i`, use `find_last` to locate the farthest index where the prefix sum equals 0 (indicating balanced even/odd distinct counts).
- When removing element `nums[i]` from consideration, adjust the prefix sums via range update from `i+1` up to the next occurrence of `nums[i]`.
- Track occurrences of each value using deques for efficient front-removal.

---

## 💻 Code

```python
class LazyTag:
    def __init__(self):
        self.to_add = 0

    def add(self, other):
        self.to_add += other.to_add
        return self

    def has_tag(self):
        return self.to_add != 0

    def clear(self):
        self.to_add = 0


class SegmentTreeNode:
    def __init__(self):
        self.min_value = 0
        self.max_value = 0
        self.lazy_tag = LazyTag()


class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [SegmentTreeNode() for _ in range(self.n * 4 + 1)]
        self._build(data, 1, self.n, 1)

    def add(self, l, r, val):
        tag = LazyTag()
        tag.to_add = val
        self._update(l, r, tag, 1, self.n, 1)

    def find_last(self, start, val):
        if start > self.n:
            return -1
        return self._find(start, self.n, val, 1, self.n, 1)

    def _apply_tag(self, i, tag):
        self.tree[i].min_value += tag.to_add
        self.tree[i].max_value += tag.to_add
        self.tree[i].lazy_tag.add(tag)

    def _pushdown(self, i):
        if self.tree[i].lazy_tag.has_tag():
            tag = LazyTag()
            tag.to_add = self.tree[i].lazy_tag.to_add
            self._apply_tag(i << 1, tag)
            self._apply_tag((i << 1) | 1, tag)
            self.tree[i].lazy_tag.clear()

    def _pushup(self, i):
        self.tree[i].min_value = min(
            self.tree[i << 1].min_value, self.tree[(i << 1) | 1].min_value
        )
        self.tree[i].max_value = max(
            self.tree[i << 1].max_value, self.tree[(i << 1) | 1].max_value
        )

    def _build(self, data, l, r, i):
        if l == r:
            self.tree[i].min_value = data[l - 1]
            self.tree[i].max_value = data[l - 1]
            return

        mid = l + ((r - l) >> 1)
        self._build(data, l, mid, i << 1)
        self._build(data, mid + 1, r, (i << 1) | 1)
        self._pushup(i)

    def _update(self, target_l, target_r, tag, l, r, i):
        if target_l <= l and r <= target_r:
            self._apply_tag(i, tag)
            return

        self._pushdown(i)
        mid = l + ((r - l) >> 1)
        if target_l <= mid:
            self._update(target_l, target_r, tag, l, mid, i << 1)
        if target_r > mid:
            self._update(target_l, target_r, tag, mid + 1, r, (i << 1) | 1)
        self._pushup(i)

    def _find(self, target_l, target_r, val, l, r, i):
        if self.tree[i].min_value > val or self.tree[i].max_value < val:
            return -1

        if l == r:
            return l

        self._pushdown(i)
        mid = l + ((r - l) >> 1)

        if target_r >= mid + 1:
            res = self._find(target_l, target_r, val, mid + 1, r, (i << 1) | 1)
            if res != -1:
                return res

        if l <= target_r and mid >= target_l:
            return self._find(target_l, target_r, val, l, mid, i << 1)

        return -1


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        occurrences = defaultdict(deque)

        def sgn(x):
            return 1 if x % 2 == 0 else -1

        length = 0
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = sgn(nums[0])
        occurrences[nums[0]].append(1)

        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i - 1]
            occ = occurrences[nums[i]]
            if not occ:
                prefix_sum[i] += sgn(nums[i])
            occ.append(i + 1)

        seg = SegmentTree(prefix_sum)
        for i in range(len(nums)):
            length = max(length, seg.find_last(i + length, 0) - i)
            next_pos = len(nums) + 1
            occurrences[nums[i]].popleft()
            if occurrences[nums[i]]:
                next_pos = occurrences[nums[i]][0]

            seg.add(i + 1, next_pos - 1, -sgn(nums[i]))

        return length
```

---

## 🧠 Dry Run
### Input
```
nums = [1, 2, 3, 4]
```
### Steps
```
sgn: 1→-1, 2→+1, 3→-1, 4→+1
occurrences: {1:[1], 2:[2], 3:[3], 4:[4]}

prefix_sum computation:
  ps[0] = sgn(1) = -1
  ps[1] = -1 + sgn(2) = -1+1 = 0
  ps[2] = 0 + sgn(3) = 0-1 = -1
  ps[3] = -1 + sgn(4) = -1+1 = 0

Build segment tree on [-1, 0, -1, 0]

i=0: find_last(start=0, val=0) → finds index 4 (ps[3]=0) → length=max(0, 4-0)=4
     remove nums[0]=1, no more 1s → seg.add(1, 4, +1) (undo the -1)

Result: 4 (subarray [1,2,3,4] has distinct evens={2,4}, distinct odds={1,3}, both size 2)
```

---

## ⏱️ Time Complexity
```
O(n log n) — each of the n iterations performs O(log n) segment tree operations
```

## 💾 Space Complexity
```
O(n) — for the segment tree (4n nodes), prefix sums, and occurrence deques
```

---

## ⚠️ Edge Cases
- All elements are the same value → no balance possible if all same parity
- Large arrays requiring efficient segment tree operations
- Duplicate values affecting when a "distinct" count changes as the window slides
- Elements appearing only once vs. multiple times

---

## 🎯 Interview Takeaways
- Segment trees with lazy propagation enable efficient range updates and queries over dynamic prefix sums.
- The `find_last` operation (finding the rightmost position with a given value) is a powerful query variant.
- Tracking occurrences with deques allows O(1) removal from the front as the sliding window advances.
- Converting a "distinct count balance" problem into a prefix-sum problem using sign assignment is a key insight.

---

## 📌 Key Pattern
👉 **"Convert parity-based distinct counting into prefix sums with signs, then use a segment tree to find the farthest balanced endpoint efficiently."**

---

## 🔁 Related Problems
- 525. Contiguous Array
- 327. Count of Range Sum
- 2407. Longest Increasing Subsequence II
- 307. Range Sum Query - Mutable

---

## 🚀 Final Thoughts
This is an advanced solution that transforms a distinct-count balance problem into a prefix-sum search problem. The segment tree with lazy propagation handles dynamic updates as elements leave the window, while the `find_last` query maximizes the subarray length. The use of occurrence deques to track when a value's contribution should shift is particularly elegant.

---

✨ **Rule to remember:**
> "When brute force is too slow, convert distinct-count balance into prefix sums and use a segment tree to find the farthest zero — turning O(n^2) into O(n log n)."
