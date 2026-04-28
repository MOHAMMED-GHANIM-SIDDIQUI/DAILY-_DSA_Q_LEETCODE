# 3013. Divide an Array Into Subarrays With Minimum Cost II

## 🔗 Problem Link
https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Sliding Window, Sorted Container, Heap

---

## 🧩 Problem Summary
Given an array `nums`, integers `k` and `dist`, divide `nums` into `k` contiguous subarrays such that the cost (sum of first elements of each subarray) is minimized. The constraint is that any two adjacent split points must be within distance `dist` of each other. Specifically, the i-th subarray must start within index range constrained by `dist`.

### 📌 Constraints
- `3 <= n <= 10^5`
- `1 <= nums[i] <= 10^9`
- `3 <= k <= n`
- `k - 2 <= dist <= n - 2`

---

## 💭 Intuition
👉 The first subarray always starts at index 0. We need to choose (k-1) split points from a sliding window of size (dist+1). Using a SortedList, we maintain the (k-1) smallest elements in the window and track their sum efficiently.

---

## ⚡ Approach — Sliding Window with SortedList

### 🧠 Idea
- Fix `nums[0]` as the first subarray cost.
- Use a sliding window of size `dist + 1` starting from index 1.
- Maintain a SortedList of the window elements.
- Track the sum of the smallest `(k-1)` elements in the window.
- As the window slides, remove the outgoing element and add the incoming element, adjusting the running sum based on their positions relative to the (k-1) boundary.

---

## 💻 Code

```python
class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        if k == 1:
            return nums[0]

        need = k - 1
        window = SortedList(nums[1: dist + 2])

        current_sum = sum(window[:need])
        min_cost = current_sum

        for i in range(1, len(nums) - dist - 1):
            outgoing = nums[i]
            incoming = nums[i + dist + 1]

            # Remove outgoing
            idx_out = window.bisect_left(outgoing)
            window.remove(outgoing)

            if idx_out < need:
                current_sum -= outgoing
                if len(window) >= need:
                    current_sum += window[need - 1]

            # Add incoming
            window.add(incoming)
            idx_in = window.bisect_left(incoming)

            if idx_in < need:
                current_sum += incoming
                if len(window) > need:
                    current_sum -= window[need]

            min_cost = min(min_cost, current_sum)

        return min_cost + nums[0]
```

---

## 🧠 Dry Run
### Input
```
nums = [1, 3, 5, 6, 1], k = 3, dist = 2
```
### Steps
```
1. need = 2, window = SortedList([3, 5, 6]) from nums[1:4]
2. current_sum = 3 + 5 = 8, min_cost = 8
3. i=1: outgoing=3, incoming=1
   - Remove 3 (idx_out=0 < 2): current_sum -= 3 => 5, add window[1]=6 => 11
   - Add 1 (idx_in=0 < 2): current_sum += 1 => 12, subtract window[2]=6 => 6
   - min_cost = min(8, 6) = 6
4. Return 6 + 1 = 7
```

---

## ⏱️ Time Complexity
```
O(n log n) — each insertion and removal in SortedList is O(log n).
```

## 💾 Space Complexity
```
O(dist) for the SortedList window.
```

---

## ⚠️ Edge Cases
- `k == 1`: return `nums[0]` directly.
- `dist` spans the entire array: pick the (k-1) smallest elements from `nums[1:]`.
- All elements are equal: any split gives the same cost.

---

## 🎯 Interview Takeaways
- SortedList (or balanced BST) enables efficient sliding window with order statistics.
- Maintaining a running sum of the top-k smallest in a window avoids recomputation.
- Carefully handle the boundary when removing/adding elements that cross the k-th position.

---

## 📌 Key Pattern
👉 **"Sliding window with SortedList for maintaining top-k smallest elements"**

---

## 🔁 Related Problems
- 3010. Divide an Array Into Subarrays With Minimum Cost I
- 480. Sliding Window Median
- 295. Find Median from Data Stream

---

## 🚀 Final Thoughts
This hard variant adds a distance constraint that turns the problem into a sliding window challenge. The SortedList data structure is the workhorse, enabling efficient order-statistic queries and updates as the window slides.

---

✨ **Rule to remember:**
> When you need the k smallest elements in a sliding window, use a SortedList and track the running sum with careful add/remove boundary management.
