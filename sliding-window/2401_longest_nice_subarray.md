# 2401. Longest Nice Subarray

## 🔗 Problem Link
https://leetcode.com/problems/longest-nice-subarray/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Bit Manipulation, Sliding Window

---

## 🧩 Problem Summary
A subarray is "nice" if the bitwise AND of every pair of elements is 0. Given an array of positive integers, return the length of the longest nice subarray.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

---

## 💭 Intuition
👉 If all elements in a subarray have pairwise AND = 0, then no two elements share any set bit. Use bitwise OR to track used bits and a two-pointer/sliding window approach: when a new element overlaps, shrink the window from the left.

---

## ⚡ Approach — Sliding Window with Bitwise OR Tracking

### 🧠 Idea
- Maintain a `bitwiseUsed` variable representing the OR of all elements in the current window.
- Expand the right pointer. If `bitwiseUsed & nums[r] != 0`, shrink from the left by XORing out `nums[l]`.
- After resolving conflicts, OR in `nums[r]` and update the maximum length.

---

## 💻 Code

```cpp
class Solution {
public:
    int longestNiceSubarray(std::vector<int>& nums) {
        int maxLength = 0;  // To store the maximum length of the nice subarray
        int bitwiseUsed = 0;  // To track the bitwise OR of the current subarray elements

        // Two-pointer approach: left pointer 'l' and right pointer 'r'
        for (int l = 0, r = 0; r < nums.size(); ++r) {
            // Move the left pointer 'l' to the right as long as the current subarray has overlapping bits
            while (bitwiseUsed & nums[r]) {
                bitwiseUsed ^= nums[l++];
            }

            // Include the current element at index 'r' into the subarray
            bitwiseUsed |= nums[r];

            // Update the maximum subarray length
            maxLength = std::max(maxLength, r - l + 1);
        }

        return maxLength;  // Return the length of the longest nice subarray
    }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [1,3,8,48,10]
```
### Steps
```
r=0: bitwiseUsed=0, no conflict. OR in 1 → bitwiseUsed=1. maxLen=1
r=1: bitwiseUsed=1 & 3=1 → conflict. XOR out nums[0]=1, l=1. bitwiseUsed=0.
     OR in 3 → bitwiseUsed=3. maxLen=1
r=2: bitwiseUsed=3 & 8=0 → no conflict. OR in 8 → bitwiseUsed=11. maxLen=2
r=3: bitwiseUsed=11 & 48=0 → no conflict. OR in 48 → bitwiseUsed=59. maxLen=3
r=4: bitwiseUsed=59 & 10=10 → conflict. XOR out 3, l=2. bitwiseUsed=56 & 10=8 → conflict.
     XOR out 8, l=3. bitwiseUsed=48 & 10=0 → no conflict. OR in 10 → bitwiseUsed=58. maxLen=3

Result: 3
```

---

## ⏱️ Time Complexity
```
O(n) — each element is added and removed at most once.
```

## 💾 Space Complexity
```
O(1) — only a few variables.
```

---

## ⚠️ Edge Cases
- All elements are the same (e.g., all 1s): each nice subarray is length 1.
- All elements use disjoint bits: entire array is nice.
- Single element: answer is 1.

---

## 🎯 Interview Takeaways
- Bitwise OR accumulates set bits; XOR removes them (since no bits overlap in a nice subarray).
- The sliding window invariant is: no two elements in the window share a set bit.
- This pattern generalizes to any "no-overlap" constraint on bits.

---

## 📌 Key Pattern
👉 **"Sliding window with bitwise OR to track used bits — shrink when bits conflict."**

---

## 🔁 Related Problems
- 1611. Minimum One Bit Operations to Make Integers Zero
- 898. Bitwise ORs of Subarrays
- 2411. Smallest Subarrays With Maximum Bitwise OR

---

## 🚀 Final Thoughts
The elegant insight is that "pairwise AND = 0" is equivalent to "no shared set bits," which can be tracked with a single OR variable. The sliding window then operates in O(n) time.

---

✨ **Rule to remember:**
> "No shared bits = OR tracks everything, XOR removes cleanly."
