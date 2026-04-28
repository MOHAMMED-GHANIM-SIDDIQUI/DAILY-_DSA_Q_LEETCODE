# 3191. Minimum Operations to Make Binary Array Elements Equal to One I

## 🔗 Problem Link
https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Greedy, Bit Manipulation, Sliding Window

---

## 🧩 Problem Summary
Given a binary array, you can flip any 3 consecutive elements in one operation. Return the minimum number of operations to make all elements equal to 1, or -1 if impossible.

### 📌 Constraints
- 3 <= nums.length <= 10^5
- nums[i] is 0 or 1

---

## 💭 Intuition
👉 Greedily flip from left to right: whenever you encounter a 0, flip the window of 3 starting at that position. If the last two elements aren't 1 at the end, it's impossible.

---

## ⚡ Approach — Greedy Left-to-Right Flip

### 🧠 Idea
- Scan from left to right
- When nums[i] == 0, flip nums[i], nums[i+1], nums[i+2] (XOR with 1)
- After processing up to n-3, check if the last two elements are both 1
- If not, return -1

---

## 💻 Code

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n = nums.size();
        int ans = 0;

        for (int i = 0; i + 2 < n; ++i) {
            if (nums[i] == 0) {
                nums[i + 1] ^= 1; // Toggle the second next element
                nums[i + 2] ^= 1; // Toggle the third next element
                ++ans;
            }
        }

        // If the last two elements are zero, it's impossible to make the array all ones
        return (nums[n - 1] == 0 || nums[n - 2] == 0) ? -1 : ans;
    }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [0, 1, 1, 1, 0, 0]
```
### Steps
```
i=0: nums[0]=0 -> flip [0,1,2]: [1,0,0,1,0,0], ans=1
i=1: nums[1]=0 -> flip [1,2,3]: [1,1,1,0,0,0], ans=2
i=2: nums[2]=1 -> skip
i=3: nums[3]=0 -> flip [3,4,5]: [1,1,1,1,1,1], ans=3
Check: nums[4]=1, nums[5]=1 -> return 3
```

---

## ⏱️ Time Complexity
```
O(n) — single pass through the array
```

## 💾 Space Complexity
```
O(1) — in-place modifications
```

---

## ⚠️ Edge Cases
- Array already all 1s — 0 operations
- Impossible case (e.g., [0, 0]) — return -1
- Array of length exactly 3

---

## 🎯 Interview Takeaways
- Greedy left-to-right flipping works because each 0 must be fixed, and the leftmost 0 can only be fixed by flipping starting at its position
- The order of operations doesn't matter for the count, but left-to-right is easiest to reason about
- XOR is the natural toggle operation for binary values

---

## 📌 Key Pattern
👉 **"Greedy left-to-right window flip for binary array"**

---

## 🔁 Related Problems
- 995. Minimum Number of K Consecutive Bit Flips
- 3192. Minimum Operations to Make Binary Array Elements Equal to One II

---

## 🚀 Final Thoughts
This is a simplified version of the K Consecutive Bit Flips problem with k=3. The greedy approach is optimal because flipping at the leftmost 0 is the only way to fix it without affecting already-fixed positions to its left.

---

✨ **Rule to remember:**
> Flip at the leftmost 0 greedily; if the tail can't be fixed, return -1.
