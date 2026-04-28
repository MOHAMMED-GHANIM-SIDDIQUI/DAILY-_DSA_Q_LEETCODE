# 3542. Minimum Operations to Convert All Elements to Zero

## 🔗 Problem Link
https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Stack, Monotonic Stack, Greedy

---

## 🧩 Problem Summary
Given an array of non-negative integers, find the minimum number of operations to make all elements zero. In each operation, you can select a contiguous subarray of equal non-zero elements and decrement all of them by 1. The key insight is to count distinct "layers."

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`

---

## 💭 Intuition
👉 Each new distinct value encountered when scanning left-to-right represents a new "layer" that requires an operation. A monotonic stack tracks the current layer structure — when a smaller value appears, previous larger layers are popped (they've been handled).

---

## ⚡ Approach — Monotonic Stack

### 🧠 Idea
- Maintain a stack initialized with 0 (representing the base level).
- For each element, pop all stack elements greater than the current value (those layers end here).
- If the current value is strictly greater than the stack top, it's a new layer — increment answer and push.
- Equal values don't need a new operation.

---

## 💻 Code

```cpp
class Solution {
 public:
  int minOperations(vector<int>& nums) {
    int ans = 0;
    stack<int> stack;
    stack.push(0);

    for (const int num : nums) {
      while (!stack.empty() && stack.top() > num)
        stack.pop();
      if (stack.empty() || stack.top() < num) {
        ++ans;
        stack.push(num);
      }
    }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [3, 1, 2, 1]
```
### Steps
```
stack = [0], ans = 0

num=3: 0 < 3, push. stack=[0,3], ans=1
num=1: pop 3 (3>1). 0 < 1, push. stack=[0,1], ans=2
num=2: 1 < 2, push. stack=[0,1,2], ans=3
num=1: pop 2 (2>1). top=1 == 1, no push. stack=[0,1], ans=3

Result: 3
```

---

## ⏱️ Time Complexity
```
O(n) — each element is pushed and popped at most once
```

## 💾 Space Complexity
```
O(n) — for the stack in the worst case
```

---

## ⚠️ Edge Cases
- All zeros → 0 operations
- Strictly increasing array → n operations
- All same non-zero value → 1 operation
- Array with many duplicates → duplicates don't add operations

---

## 🎯 Interview Takeaways
- Monotonic stacks naturally model "layered" structures.
- Initializing the stack with 0 handles the base level elegantly.
- Equal consecutive values share the same operation — only new distinct values cost.

---

## 📌 Key Pattern
👉 **"Monotonic stack to count distinct layers — each new ascending value is a new operation."**

---

## 🔁 Related Problems
- 84. Largest Rectangle in Histogram
- 42. Trapping Rain Water
- 739. Daily Temperatures

---

## 🚀 Final Thoughts
This problem has an elegant monotonic stack solution. The insight is that each contiguous region of equal values at the same "height" can be handled in one operation, and the stack tracks which heights are currently active.

---

✨ **Rule to remember:**
> Count the number of distinct ascending "steps" in an array using a monotonic stack — each step is one operation.
