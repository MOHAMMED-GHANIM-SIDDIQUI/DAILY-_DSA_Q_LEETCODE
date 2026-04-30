# 2615. Sum of Distances

## 🔗 Problem Link
https://leetcode.com/problems/sum-of-distances/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Hash Table, Prefix Sum

---

## 🧩 Problem Summary
Given a 0-indexed array `nums`, for each index `i`, compute the sum of `|i - j|` for all `j != i` where `nums[i] == nums[j]`. Return the result array.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`

---

## 💭 Intuition
👉 Group indices by their value. For each group of indices, use prefix sums to compute the sum of absolute differences efficiently. For index at position `k` in a sorted group, the left contribution is `k * idx - prefixSum` and the right contribution is `(totalSum - prefixSum - idx) - (groupSize - k - 1) * idx`.

---

## ⚡ Approach — Group by Value + Prefix Sum

### 🧠 Idea
- Group all indices by their value using a dictionary.
- For each group, compute total sum of indices.
- Iterate through the group, maintaining a running prefix sum.
- For each index, split the distance sum into left and right contributions using arithmetic formulas.

---

## 💻 Code

```python
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        freq = defaultdict(list)

        # Step 1: Store indices
        for idx, val in enumerate(nums):
            freq[val].append(idx)

        ans = [0] * len(nums)

        # Step 2: Process each group
        for val, indices in freq.items():
            total_sum = sum(indices)
            prefix_sum = 0
            n = len(indices)

            for i, idx in enumerate(indices):
                # Left side
                left = idx * i - prefix_sum

                # Right side
                right = (total_sum - prefix_sum - idx) - (n - i - 1) * idx

                ans[idx] = left + right

                # Update prefix sum
                prefix_sum += idx

        return ans
```

---

## 🧠 Dry Run
### Input
```
nums = [1, 3, 1, 1, 2]
```
### Steps
```
Groups: {1: [0,2,3], 3: [1], 2: [4]}

Group 1 → indices=[0,2,3], total_sum=5
  i=0, idx=0: left=0*0-0=0, right=(5-0-0)-(2)*0=5 → ans[0]=5
              Wait: right = (5-0-0) - 2*0 = 5. ans[0]=0+5=5
              prefix_sum=0
  i=1, idx=2: prefix_sum=0, left=2*1-0=2, right=(5-0-2)-1*2=1 → ans[2]=3
              prefix_sum=2
  i=2, idx=3: prefix_sum=2, left=3*2-2=4, right=(5-2-3)-0*3=0 → ans[3]=4
              prefix_sum=5

Group 3: single element → ans[1]=0
Group 2: single element → ans[4]=0

Result: [5, 0, 3, 4, 0]
```

---

## ⏱️ Time Complexity
```
O(n) — each index is processed exactly once across all groups.
```

## 💾 Space Complexity
```
O(n) — for the grouping dictionary and result array.
```

---

## ⚠️ Edge Cases
- All elements unique: every answer is 0.
- All elements the same: one large group, prefix sum handles it.
- Single element: returns [0].

---

## 🎯 Interview Takeaways
- Prefix sum over sorted groups is the go-to technique for sum-of-absolute-differences.
- Splitting into left and right contributions avoids O(n^2) brute force.
- Grouping by value first simplifies the problem to 1D distance sums.

---

## 📌 Key Pattern
👉 **"Group by value, then use prefix sums for sum-of-absolute-differences."**

---

## 🔁 Related Problems
- 2121. Intervals Between Identical Elements
- 1685. Sum of Absolute Differences in a Sorted Array
- 2602. Minimum Operations to Make All Array Elements Equal

---

## 🚀 Final Thoughts
This problem is a clean application of the prefix-sum-based technique for computing pairwise distance sums. The key is recognizing that absolute differences can be decomposed into left and right contributions relative to a running prefix sum.

---

✨ **Rule to remember:**
> "For sum of absolute differences, group + prefix sum = O(n) magic."
