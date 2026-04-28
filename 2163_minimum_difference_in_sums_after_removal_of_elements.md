# 2163. Minimum Difference in Sums After Removal of Elements

## 🔗 Problem Link
https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Heap (Priority Queue), Prefix Sum

---

## 🧩 Problem Summary
Given a `3n`-length array, remove exactly `n` elements, then split the remaining `2n` elements into two halves (first `n` and last `n`). Minimize the difference: sum of the first half minus sum of the second half.

### 📌 Constraints
- `nums.length == 3 * n`
- `1 <= n <= 10^5`
- `1 <= nums[i] <= 10^5`

---

## 💭 Intuition
👉 To minimize (left_sum - right_sum), make the left sum as small as possible and the right sum as large as possible. Use a max-heap from the left and a min-heap from the right to track optimal sums at every split point.

---

## ⚡ Approach — Two Heaps with Prefix/Suffix Optimization

### 🧠 Idea
- Sweep left-to-right with a max-heap to compute `minLeftSum[i]` — the minimum sum of choosing `n` elements from `nums[0..i]`.
- Sweep right-to-left with a min-heap to compute the maximum sum of choosing `n` elements from `nums[i..end]`.
- Try every valid split point and find the minimum difference.

---

## 💻 Code

```cpp
class Solution {
 public:
  long long minimumDifference(vector<int>& nums) {
    const int n = nums.size() / 3;
    long ans = LONG_MAX;
    long leftSum = 0;
    long rightSum = 0;
    // The left part should be as small as possible.
    priority_queue<int> maxHeap;
    // The right part should be as big as possible.
    priority_queue<int, vector<int>, greater<>> minHeap;
    // minLeftSum[i] := the minimum of the sum of n nums in nums[0..i)
    vector<long> minLeftSum(nums.size());

    for (int i = 0; i < 2 * n; ++i) {
      maxHeap.push(nums[i]);
      leftSum += nums[i];
      if (maxHeap.size() == n + 1)
        leftSum -= maxHeap.top(), maxHeap.pop();
      if (maxHeap.size() == n)
        minLeftSum[i] = leftSum;
    }

    for (int i = nums.size() - 1; i >= n; --i) {
      minHeap.push(nums[i]);
      rightSum += nums[i];
      if (minHeap.size() == n + 1)
        rightSum -= minHeap.top(), minHeap.pop();
      if (minHeap.size() == n)
        ans = min(ans, minLeftSum[i - 1] - rightSum);
    }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [3, 1, 2] → n = 1
```
### Steps
```
Left sweep (max-heap, keep smallest 1):
  i=0: push 3, leftSum=3, heap size=1, minLeftSum[0]=3
  i=1: push 1, leftSum=4, heap size=2, pop 3, leftSum=1, minLeftSum[1]=1

Right sweep (min-heap, keep largest 1):
  i=2: push 2, rightSum=2, heap size=1, ans = min(LONG_MAX, minLeftSum[1]-2) = min(MAX, 1-2) = -1
  i=1: push 1, rightSum=3, heap size=2, pop 1, rightSum=2, ans = min(-1, minLeftSum[0]-2) = min(-1, 1) = -1

ans = -1
```

---

## ⏱️ Time Complexity
```
O(n log n) — heap operations across the array
```

## 💾 Space Complexity
```
O(n) — for the heaps and the minLeftSum array
```

---

## ⚠️ Edge Cases
- All elements are equal → difference is 0
- Array is already sorted ascending → split naturally minimizes difference
- n = 1 → smallest single element minus largest single element

---

## 🎯 Interview Takeaways
- Two-directional heap sweeps are a powerful pattern for optimization problems with split points.
- Prefix/suffix precomputation avoids recomputing from scratch at each split.
- Using max-heap for "keep smallest n" and min-heap for "keep largest n" is a classic trick.

---

## 📌 Key Pattern
👉 **"Two-directional heap sweep to optimize over all split points"**

---

## 🔁 Related Problems
- 295. Find Median from Data Stream
- 480. Sliding Window Median
- 2098. Subsequence of Size K With the Largest Even Sum

---

## 🚀 Final Thoughts
This is an advanced problem that combines heap-based selection with prefix optimization. The key insight is decoupling left minimization and right maximization, then combining them at every valid split.

---

✨ **Rule to remember:**
> "Use max-heap to track the smallest n elements from the left, min-heap for the largest n from the right, and sweep for the best split."
