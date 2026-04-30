# 2348. Number of Zero-Filled Subarrays

## 🔗 Problem Link
https://leetcode.com/problems/number-of-zero-filled-subarrays/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Math

---

## 🧩 Problem Summary
Given an integer array `nums`, return the number of subarrays filled entirely with 0s.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## 💭 Intuition
👉 Each zero at index `i` contributes `(i - lastNonZeroIndex)` new zero-filled subarrays ending at `i`. Track the index of the last non-zero element and accumulate.

---

## ⚡ Approach — Linear Scan with Running Count

### 🧠 Idea
- Maintain `indexBeforeZero` as the index of the last non-zero element (initialized to -1).
- For each index `i`, if `nums[i] != 0`, update `indexBeforeZero = i`.
- Otherwise, add `i - indexBeforeZero` to the answer (number of zero-filled subarrays ending at `i`).

---

## 💻 Code

```cpp
class Solution {
 public:
  long long zeroFilledSubarray(vector<int>& nums) {
    long ans = 0;
    int indexBeforeZero = -1;

    for (int i = 0; i < nums.size(); ++i)
      if (nums[i])
        indexBeforeZero = i;
      else
        ans += i - indexBeforeZero;

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [1,3,0,0,2,0,0,4]
```
### Steps
```
i=0: nums[0]=1, indexBeforeZero=0
i=1: nums[1]=3, indexBeforeZero=1
i=2: nums[2]=0, ans += 2-1 = 1. ans=1
i=3: nums[3]=0, ans += 3-1 = 2. ans=3
i=4: nums[4]=2, indexBeforeZero=4
i=5: nums[5]=0, ans += 5-4 = 1. ans=4
i=6: nums[6]=0, ans += 6-4 = 2. ans=6
i=7: nums[7]=4, indexBeforeZero=7

Result: 6
```

---

## ⏱️ Time Complexity
```
O(n) — single pass through the array.
```

## 💾 Space Complexity
```
O(1) — only two variables.
```

---

## ⚠️ Edge Cases
- No zeros in the array: answer is 0.
- Entire array is zeros: answer is n*(n+1)/2.
- Single element array.

---

## 🎯 Interview Takeaways
- A contiguous run of `k` zeros contributes `k*(k+1)/2` subarrays total.
- Tracking the "boundary" index simplifies counting incrementally.
- No need to explicitly find runs — just track the last non-zero position.

---

## 📌 Key Pattern
👉 **"Count subarrays ending at each position using a boundary tracker."**

---

## 🔁 Related Problems
- 713. Subarray Product Less Than K
- 1248. Count Number of Nice Subarrays
- 2461. Maximum Sum of Distinct Subarrays With Length K

---

## 🚀 Final Thoughts
This is a clean O(n) solution that avoids explicitly computing run lengths. By tracking the last non-zero index, each zero contributes its count in O(1), making the solution both simple and efficient.

---

✨ **Rule to remember:**
> "Each zero at index i adds (i - lastNonZero) new all-zero subarrays ending there."
