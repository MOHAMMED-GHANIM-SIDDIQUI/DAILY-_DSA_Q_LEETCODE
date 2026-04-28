# 1493. Longest Subarray of 1's After Deleting One Element

## 🔗 Problem Link
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Sliding Window, Dynamic Programming

---

## 🧩 Problem Summary
Given a binary array `nums`, you must delete exactly one element from it. Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.

---

## 💭 Intuition
👉 Since we must delete exactly one element, we need the longest window of 1's that contains at most one 0. This is a classic sliding window problem where we maintain a window with at most one zero and track the maximum window size minus one (for the deleted element).

---

## ⚡ Approach — Sliding Window

### 🧠 Idea
- Use two pointers `l` and `r` for the sliding window.
- Track the count of zeros in the current window.
- When zeros reach 2, shrink from the left until zeros drop below 2.
- The answer is `r - l` (not `r - l + 1`, because we must delete one element).

---

## 💻 Code

```cpp
class Solution {
 public:
  int longestSubarray(vector<int>& nums) {
    int ans = 0;
    int zeros = 0;

    for (int l = 0, r = 0; r < nums.size(); ++r) {
      if (nums[r] == 0)
        ++zeros;
      while (zeros == 2)
        if (nums[l++] == 0)
          --zeros;
      ans = max(ans, r - l);
    }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [1, 1, 0, 1, 1, 1, 0, 1]
```
### Steps
```
r=0: nums[0]=1, zeros=0, ans=max(0,0-0)=0
r=1: nums[1]=1, zeros=0, ans=max(0,1-0)=1
r=2: nums[2]=0, zeros=1, ans=max(1,2-0)=2
r=3: nums[3]=1, zeros=1, ans=max(2,3-0)=3
r=4: nums[4]=1, zeros=1, ans=max(3,4-0)=4
r=5: nums[5]=1, zeros=1, ans=max(4,5-0)=5
r=6: nums[6]=0, zeros=2, shrink: l=0(1),l=1(1),l=2(0)→zeros=1,l=3
      ans=max(5,6-3)=5
r=7: nums[7]=1, zeros=1, ans=max(5,7-3)=5
Answer: 5 (delete the 0 at index 2, subarray [1,1,1,1,1])
```

---

## ⏱️ Time Complexity
```
O(n), where n is the length of nums
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- All 1's — must still delete one, so answer is `n - 1`.
- All 0's — answer is `0`.
- Single element — answer is `0` (must delete the only element).

---

## 🎯 Interview Takeaways
- This is a variation of "longest subarray with at most K replacements" where K=1.
- Using `r - l` instead of `r - l + 1` elegantly accounts for the mandatory deletion.
- Sliding window with a constraint counter is a fundamental pattern.

---

## 📌 Key Pattern
👉 **"Sliding window with at most one zero allowed — track window size minus one for mandatory deletion"**

---

## 🔁 Related Problems
- 1004 — Max Consecutive Ones III
- 424 — Longest Repeating Character Replacement
- 487 — Max Consecutive Ones II

---

## 🚀 Final Thoughts
The sliding window approach makes this problem straightforward. The subtle detail is that the answer is `r - l` (not `r - l + 1`) because exactly one element must be deleted, even if the entire array is 1's.

---

✨ **Rule to remember:**
> "For longest subarray of 1's with one deletion, use a sliding window allowing at most one zero and subtract one from window size."
