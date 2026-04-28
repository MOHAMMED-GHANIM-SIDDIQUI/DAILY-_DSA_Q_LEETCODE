# 2411. Smallest Subarrays With Maximum Bitwise OR

## 🔗 Problem Link
https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Bit Manipulation, Sliding Window

---

## 🧩 Problem Summary
Given an array `nums`, for each index `i`, find the minimum length of a subarray starting at `i` such that the bitwise OR of the subarray is maximized. Return an array of these minimum lengths.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`

---

## 💭 Intuition
👉 For each bit position, track the closest index to the right that has that bit set. The answer for index `i` is determined by the farthest such closest index across all 30 bit positions.

---

## ⚡ Approach — Reverse Scan with Closest Bit Tracking

### 🧠 Idea
- Scan from right to left.
- For each bit position `j` (0 to 29), maintain `closest[j]` = the nearest index (to the right) where bit `j` is set.
- When processing index `i`, update `closest[j] = i` for each set bit in `nums[i]`.
- `ans[i] = max over all j of (closest[j] - i + 1)`, with a minimum of 1.

---

## 💻 Code

```cpp
class Solution {
 public:
  vector<int> smallestSubarrays(vector<int>& nums) {
    constexpr int kMaxBit = 30;
    vector<int> ans(nums.size(), 1);
    // closest[j] := the closest index i s.t. the j-th bit of nums[i] is 1
    vector<int> closest(kMaxBit);

    for (int i = nums.size() - 1; i >= 0; --i)
      for (int j = 0; j < kMaxBit; ++j) {
        if (nums[i] >> j & 1)
          closest[j] = i;
        ans[i] = max(ans[i], closest[j] - i + 1);
      }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [1,0,2,1,3]
```
### Steps
```
Scan right to left:
i=4: nums[4]=3 (bits 0,1). closest[0]=4, closest[1]=4. ans[4]=max(1,1,1)=1
i=3: nums[3]=1 (bit 0). closest[0]=3. ans[3]=max(1, 3-3+1=1, 4-3+1=2)=2
i=2: nums[2]=2 (bit 1). closest[1]=2. ans[2]=max(1, 3-2+1=2, 2-2+1=1)=2
i=1: nums[1]=0. ans[1]=max(1, 3-1+1=3, 2-1+1=2)=3
i=0: nums[0]=1 (bit 0). closest[0]=0. ans[0]=max(1, 0-0+1=1, 2-0+1=3)=3

Result: [3,3,2,2,1]
```

---

## ⏱️ Time Complexity
```
O(n * 30) = O(n) — scan each element and check 30 bits.
```

## 💾 Space Complexity
```
O(30) = O(1) — closest array of fixed size.
```

---

## ⚠️ Edge Cases
- All zeros: each answer is 1.
- Single element: answer is [1].
- All elements are the same.

---

## 🎯 Interview Takeaways
- Tracking the nearest occurrence of each bit position is a powerful technique for OR-related problems.
- Reverse scanning lets you efficiently answer "what's the closest bit to my right?"
- OR is monotonically non-decreasing as you extend a subarray.

---

## 📌 Key Pattern
👉 **"Track the closest index for each bit position — reverse scan for rightward queries."**

---

## 🔁 Related Problems
- 898. Bitwise ORs of Subarrays
- 2401. Longest Nice Subarray
- 1521. Find a Value of a Mysterious Function Closest to Target

---

## 🚀 Final Thoughts
The key insight is that the maximum OR for a subarray starting at `i` requires reaching the nearest index that contributes each missing bit. By tracking these per-bit closest indices, we avoid brute-force computation.

---

✨ **Rule to remember:**
> "For maximum OR starting at i, you need to reach the closest set bit for each bit position."
