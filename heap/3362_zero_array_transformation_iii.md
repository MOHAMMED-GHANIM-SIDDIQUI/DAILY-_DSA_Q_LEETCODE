# 3362. Zero Array Transformation III

## 🔗 Problem Link
https://leetcode.com/problems/zero-array-transformation-iii/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Greedy, Heap (Priority Queue), Sorting, Prefix Sum

---

## 🧩 Problem Summary
Given an array `nums` and queries `[l, r]` (each decrementing the range by 1), find the maximum number of queries you can remove while still being able to make all elements zero. Return -1 if it's impossible even with all queries.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^5`
- `1 <= queries.length <= 10^5`

---

## 💭 Intuition
👉 To maximize removals, minimize the queries used. Greedily select queries with the largest `r` (latest ending) first, as they cover the most future positions. Use a max-heap of available `r` values and a min-heap of running `r` values.

---

## ⚡ Approach — Greedy with Two Heaps

### 🧠 Idea
- Sort queries by start `l`.
- For each position `i`, add all queries starting at or before `i` to an `available` max-heap.
- Remove expired queries from the `running` min-heap.
- While `nums[i] > running.size()`, pick the query with the largest `r` from `available`.
- If no valid query is available, return -1.
- Answer = remaining queries in `available`.

---

## 💻 Code

```cpp
class Solution {
 public:
  int maxRemoval(vector<int>& nums, vector<vector<int>>& queries) {
    int queryIndex = 0;
    priority_queue<int> available;                        // available `r`s
    priority_queue<int, vector<int>, greater<>> running;  // running `r`s

    ranges::sort(queries);

    for (int i = 0; i < nums.size(); ++i) {
      while (queryIndex < queries.size() && queries[queryIndex][0] <= i)
        available.push(queries[queryIndex++][1]);
      while (!running.empty() && running.top() < i)
        running.pop();
      while (nums[i] > running.size()) {
        if (available.empty() || available.top() < i)
          return -1;
        running.push(available.top()), available.pop();
      }
    }

    return available.size();
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [2, 0, 2], queries = [[0, 2], [0, 2], [1, 1]]
```
### Steps
```
Sorted queries: [[0,2],[0,2],[1,1]]
i=0: available={2,2}, running={}
  nums[0]=2 > 0 → pick r=2, running={2}
  nums[0]=2 > 1 → pick r=2, running={2,2}
  OK
i=1: available={1} (added query [1,1])
  running: remove expired (none, both >= 1)
  nums[1]=0 <= 2 → OK
i=2: running: remove expired (none, both >= 2)
  nums[2]=2 <= 2 → OK
Result: available.size() = 1
```

---

## ⏱️ Time Complexity
```
O(n log n + q log q) — sorting queries and heap operations
```

## 💾 Space Complexity
```
O(q) — for the heaps
```

---

## ⚠️ Edge Cases
- All `nums[i] = 0` → all queries can be removed
- Insufficient queries → return -1
- Queries with single-element ranges → less flexibility

---

## 🎯 Interview Takeaways
- Greedy with max-heap for "best available" and min-heap for "expiry tracking" is a classic pattern.
- Always prefer queries that cover the most future positions.

---

## 📌 Key Pattern
👉 **"Greedy selection with max-heap for coverage and min-heap for expiry"**

---

## 🔁 Related Problems
- 3355. Zero Array Transformation I
- 3356. Zero Array Transformation II
- 1094. Car Pooling
- 253. Meeting Rooms II

---

## 🚀 Final Thoughts
This inverts the question from "minimum queries needed" to "maximum queries removable." The greedy strategy of always picking the query with the farthest reach ensures minimum usage, maximizing removals.

---

✨ **Rule to remember:**
> "To maximize removals, greedily use queries with the longest reach first."
