# 3068. Find the Maximum Sum of Node Values

## 🔗 Problem Link
https://leetcode.com/problems/find-the-maximum-sum-of-node-values/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Greedy, Bit Manipulation, Tree, Sorting

---

## 🧩 Problem Summary
Given a tree with node values and an integer k, you can pick any edge and XOR both endpoint values with k. The goal is to maximize the sum of all node values after performing any number of such operations.

### 📌 Constraints
- 1 <= n <= 2 * 10^4
- 1 <= k <= 10^9
- 0 <= nums[i] <= 10^9
- edges.length == n - 1

---

## 💭 Intuition
👉 XOR-ing an edge flips both endpoints. Since each operation affects exactly 2 nodes, the total number of "changed" nodes must be even. Greedily XOR each node if it increases value, then adjust by removing the smallest gain if the count is odd.

---

## ⚡ Approach — Greedy with Parity Check

### 🧠 Idea
- For each node, take max(num, num ^ k) to build the maximum sum
- Count how many nodes benefit from XOR
- If the count is even, return the sum directly
- If odd, subtract the minimum absolute difference |num - (num ^ k)| to make the count even

---

## 💻 Code

```cpp
class Solution {
 public:
  long long maximumValueSum(vector<int>& nums, int k,
                            vector<vector<int>>& edges) {
    long maxSum = 0;
    int changedCount = 0;
    int minChangeDiff = INT_MAX;

    for (const int num : nums) {
      maxSum += max(num, num ^ k);
      changedCount += ((num ^ k) > num) ? 1 : 0;
      minChangeDiff = min(minChangeDiff, abs(num - (num ^ k)));
    }

    if (changedCount % 2 == 0)
      return maxSum;
    return maxSum - minChangeDiff;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [1, 2, 1], k = 3, edges = [[0,1],[0,2]]
```
### Steps
```
num=1: 1^3=2, max=2, changed=1, diff=1
num=2: 2^3=1, max=2, changed=1, diff=min(1,1)=1
num=1: 1^3=2, max=2, changed=2, diff=1
maxSum=6, changedCount=2 (even) -> return 6
```

---

## ⏱️ Time Complexity
```
O(n) — single pass through all nodes
```

## 💾 Space Complexity
```
O(1) — constant extra space
```

---

## ⚠️ Edge Cases
- k = 0 means XOR has no effect, return original sum
- All nodes benefit from XOR (even count)
- Only one node benefits — must sacrifice the smallest gain

---

## 🎯 Interview Takeaways
- XOR on an edge always flips an even number of nodes — parity is the key constraint
- The tree structure is actually irrelevant; only parity matters
- Greedy approach with parity correction gives O(n) solution

---

## 📌 Key Pattern
👉 **"Greedy XOR with even-parity constraint"**

---

## 🔁 Related Problems
- 2939. Maximum Xor Product
- 1681. Minimum Incompatibility
- 1863. Sum of All Subset XOR Totals

---

## 🚀 Final Thoughts
The critical observation is that the tree structure is a red herring — any even-sized subset of nodes can be XOR'd via a series of edge operations. This transforms a tree problem into a simple greedy problem with a parity check.

---

✨ **Rule to remember:**
> XOR on tree edges always flips pairs; greedily XOR nodes and fix parity if odd.
