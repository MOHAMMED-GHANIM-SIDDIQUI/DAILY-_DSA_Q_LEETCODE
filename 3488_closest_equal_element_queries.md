# 3488. Closest Equal Element Queries

## 🔗 Problem Link
https://leetcode.com/problems/closest-equal-element-queries/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Hash Table, Binary Search

---

## 🧩 Problem Summary
Given a circular array `nums` and a list of `queries` where each query is an index, find the minimum circular distance from that index to the nearest other occurrence of the same value. Return -1 if no other occurrence exists.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`
- `1 <= queries.length <= 10^5`
- `0 <= queries[i] < nums.length`

---

## 💭 Intuition
👉 Group indices by value, then for each index precompute the minimum circular distance to its nearest neighbor in the same group — this allows O(1) query answering.

---

## ⚡ Approach — Precompute with Circular Neighbor Distance

### 🧠 Idea
- Group all indices by their value using a hash map.
- For each group with more than one element, compute the circular distance to the previous and next occurrence for every index.
- Store results in a precomputed array for O(1) lookups.
- Answer each query by simple array access.

---

## 💻 Code

```python
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        tracker = defaultdict(list)
        n = len(nums)

        # Step 1: group indices
        for i, val in enumerate(nums):
            tracker[val].append(i)

        # Step 2: precompute answers
        res = [-1] * n

        for val in tracker:
            positions = tracker[val]
            k = len(positions)

            if k == 1:
                continue  # stays -1

            for i in range(k):
                curr = positions[i]
                prev = positions[(i - 1) % k]
                next_ = positions[(i + 1) % k]

                d1 = abs(curr - prev)
                d2 = abs(curr - next_)

                d1 = min(d1, n - d1)
                d2 = min(d2, n - d2)

                res[curr] = min(d1, d2)

        # Step 3: answer queries in O(1)
        return [res[q] for q in queries]
```

---

## 🧠 Dry Run
### Input
```
nums = [1, 3, 1, 4, 1, 3, 2], queries = [0, 3, 5]
```
### Steps
```
Group indices:
  1 → [0, 2, 4]
  3 → [1, 5]
  4 → [3]
  2 → [6]

For value 1, positions=[0,2,4]:
  idx 0: prev=4 (d=min(4,3)=3), next=2 (d=2) → res[0]=2
  idx 2: prev=0 (d=2), next=4 (d=2) → res[2]=2
  idx 4: prev=2 (d=2), next=0 (d=min(4,3)=3) → res[4]=2

For value 3, positions=[1,5]:
  idx 1: prev=5 (d=min(4,3)=3), next=5 (d=min(4,3)=3) → res[1]=3
  idx 5: prev=1 (d=min(4,3)=3), next=1 (d=min(4,3)=3) → res[5]=3

res = [2, 3, 2, -1, 2, 3, -1]
Queries: [0→2, 3→-1, 5→3]
```

---

## ⏱️ Time Complexity
```
O(n + q) — O(n) to group and precompute, O(q) to answer queries
```

## 💾 Space Complexity
```
O(n) — for the tracker and result arrays
```

---

## ⚠️ Edge Cases
- Value appears only once → answer is -1
- All elements are the same → check circular distances
- Query index at boundaries of the array (first/last element)
- Array of length 1

---

## 🎯 Interview Takeaways
- Precomputing answers allows batch query processing in O(1) per query.
- Circular distance formula: `min(|a - b|, n - |a - b|)`.
- Grouping by value is a classic pattern for "nearest same element" problems.

---

## 📌 Key Pattern
👉 **"Group indices by value, precompute circular neighbor distances, answer queries in O(1)."**

---

## 🔁 Related Problems
- 2612. Minimum Reverse Operations
- 1170. Compare Strings by Frequency of the Smallest Character
- 2260. Minimum Consecutive Cards to Pick Up

---

## 🚀 Final Thoughts
The elegance of this solution lies in decoupling computation from queries. By precomputing the answer for every index, query answering becomes trivial. The circular distance formula is the key detail to get right.

---

✨ **Rule to remember:**
> "Precompute per-index answers using grouped positions and circular distance — then queries are just lookups."
