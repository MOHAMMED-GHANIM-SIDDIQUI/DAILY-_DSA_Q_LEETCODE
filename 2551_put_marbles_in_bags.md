# 2551. Put Marbles in Bags

## 🔗 Problem Link
https://leetcode.com/problems/put-marbles-in-bags/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Greedy, Sorting

---

## 🧩 Problem Summary
You have `weights` of marbles and need to distribute them into `k` bags (contiguous groups). The cost of a bag is the sum of the first and last marble's weight. Return the difference between the maximum and minimum total cost across all valid distributions.

### 📌 Constraints
- `1 <= k <= weights.length <= 10^5`
- `1 <= weights[i] <= 10^9`

---

## 💭 Intuition
👉 Distributing marbles into `k` bags means making `k-1` cuts. Each cut after index `i` adds `weights[i] + weights[i+1]` to the total cost. The first and last elements are always included regardless of cuts. So the problem reduces to selecting `k-1` adjacent-pair sums that maximize or minimize the total.

---

## ⚡ Approach — Sort Adjacent Pair Sums

### 🧠 Idea
- Compute all adjacent pair sums: `arr[i] = weights[i] + weights[i+1]`.
- Sort this array.
- The minimum cost uses the smallest `k-1` pair sums; the maximum uses the largest `k-1`.
- The answer is `max_sum - min_sum`.

---

## 💻 Code

```cpp
class Solution {
 public:
  long long putMarbles(vector<int>& weights, int k) {
    // To distribute marbles into k bags, there will be k - 1 cuts. If there's a
    // cut after weights[i], then weights[i] and weights[i + 1] will be added to
    // the cost. Also, no matter how we cut, weights[0] and weights[n - 1] will
    // be counted. So, the goal is to find the max/min k - 1 weights[i] +
    // weights[i + 1].
    vector<int> arr;  // weights[i] + weights[i + 1]
    long mn = 0;
    long mx = 0;

    for (int i = 0; i + 1 < weights.size(); ++i)
      arr.push_back(weights[i] + weights[i + 1]);

    ranges::sort(arr);

    for (int i = 0; i < k - 1; ++i) {
      mn += arr[i];
    mx += arr[arr.size() - 1 - i];
    }

    return mx - mn;
  }
};
```

---

## 🧠 Dry Run
### Input
```
weights = [1,3,5,1], k = 2
```
### Steps
```
Adjacent pair sums: arr = [1+3, 3+5, 5+1] = [4, 8, 6]
Sorted arr = [4, 6, 8]
k-1 = 1 cut needed
mn = arr[0] = 4
mx = arr[2] = 8
Answer = 8 - 4 = 4
```

---

## ⏱️ Time Complexity
```
O(n log n) for sorting the adjacent pair sums
```

## 💾 Space Complexity
```
O(n)
```

---

## ⚠️ Edge Cases
- `k = 1`: no cuts needed, answer is 0 (max and min cost are the same)
- `k = n`: every marble in its own bag, only one way to partition
- All weights are equal

---

## 🎯 Interview Takeaways
- Reformulating the problem from "partition into k groups" to "choose k-1 cut points" is the key breakthrough.
- The first and last elements cancel out in the difference, so only the cut-point pair sums matter.

---

## 📌 Key Pattern
👉 **"Transform partition problems into cut-point selection — sort adjacent sums"**

---

## 🔁 Related Problems
- 1011. Capacity To Ship Packages Within D Days
- 410. Split Array Largest Sum
- 813. Largest Sum of Averages

---

## 🚀 Final Thoughts
This is a beautiful problem where the key insight is that partitioning into k bags creates k-1 boundaries, and the cost depends only on the adjacent pairs at those boundaries. Once you see that, sorting and picking extremes is straightforward.

---

✨ **Rule to remember:**
> When partitioning an array into k groups, think about the k-1 cut points and what each cut contributes to the cost.
