# 2444. Count Subarrays With Fixed Bounds

## 🔗 Problem Link
https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Queue, Sliding Window, Monotonic Queue

---

## 🧩 Problem Summary
Given an integer array `nums` and two integers `minK` and `maxK`, count the number of subarrays where the minimum value is `minK` and the maximum value is `maxK`.

### 📌 Constraints
- `2 <= nums.length <= 10^5`
- `1 <= nums[i], minK, maxK <= 10^6`

---

## 💭 Intuition
👉 Track three indices: last position of `minK`, last position of `maxK`, and last "bad" position (element outside [minK, maxK]). For each index, the number of valid subarrays ending there is determined by how far back we can start.

---

## ⚡ Approach — Three-Pointer Tracking

### 🧠 Idea
- Scan left to right, maintaining:
  - `lastMinIndex`: last index where `nums[i] == minK`
  - `lastMaxIndex`: last index where `nums[i] == maxK`
  - `lastBadIndex`: last index where `nums[i]` is outside `[minK, maxK]`
- At each index, valid subarrays can start from `lastBadIndex + 1` up to `min(lastMinIndex, lastMaxIndex)`.
- If `min(lastMinIndex, lastMaxIndex) > lastBadIndex`, add that difference to the count.

---

## 💻 Code

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    long long countSubarrays(vector<int>& nums, int minK, int maxK) {
        long long count = 0; // total valid subarrays

        int lastMinIndex = -1; // last index where nums[i] == minK
        int lastMaxIndex = -1; // last index where nums[i] == maxK
        int lastBadIndex = -1; // last index where nums[i] < minK || nums[i] > maxK

        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] < minK || nums[i] > maxK) {
                lastBadIndex = i; // bad number found
            }
            if (nums[i] == minK) {
                lastMinIndex = i; // found minK
            }
            if (nums[i] == maxK) {
                lastMaxIndex = i; // found maxK
            }

            int validStart = min(lastMinIndex, lastMaxIndex); // earliest we can start a valid subarray
            if (validStart > lastBadIndex) {
                count += (validStart - lastBadIndex);
            }
            // else, no valid subarray ending at i
        }

        return count;
    }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [1,3,5,2,7,5], minK = 1, maxK = 5
```
### Steps
```
i=0: nums[0]=1==minK. lastMin=0, lastMax=-1, lastBad=-1.
     validStart=min(0,-1)=-1. -1 <= -1 → no valid subarray.
i=1: nums[1]=3, in range. lastMin=0, lastMax=-1, lastBad=-1.
     validStart=-1. skip.
i=2: nums[2]=5==maxK. lastMin=0, lastMax=2, lastBad=-1.
     validStart=min(0,2)=0. 0 > -1 → count += 0-(-1) = 1. count=1.
i=3: nums[3]=2, in range. lastMin=0, lastMax=2, lastBad=-1.
     validStart=0. 0 > -1 → count += 1. count=2.
i=4: nums[4]=7 > maxK. lastBad=4.
     validStart=min(0,2)=0. 0 <= 4 → skip.
i=5: nums[5]=5==maxK. lastMax=5, lastBad=4.
     validStart=min(0,5)=0. 0 <= 4 → skip.

Result: 2
```

---

## ⏱️ Time Complexity
```
O(n) — single pass through the array.
```

## 💾 Space Complexity
```
O(1) — only three index variables.
```

---

## ⚠️ Edge Cases
- `minK == maxK`: count subarrays where all elements equal that value.
- No valid subarray exists: return 0.
- Entire array is within [minK, maxK] with both bounds present.

---

## 🎯 Interview Takeaways
- Tracking "last occurrence" indices enables O(1) counting per element.
- The "bad index" acts as a barrier — no valid subarray can cross it.
- The number of valid starting positions is `min(lastMin, lastMax) - lastBad`.

---

## 📌 Key Pattern
👉 **"Three-pointer tracking: last min, last max, last bad — count valid starts per position."**

---

## 🔁 Related Problems
- 795. Number of Subarrays with Bounded Maximum
- 1248. Count Number of Nice Subarrays
- 992. Subarrays with K Different Integers

---

## 🚀 Final Thoughts
This is an elegant O(n) solution to what seems like a complex counting problem. The three-pointer approach avoids any nested loops or sliding window mechanics by directly computing the count of valid subarrays ending at each position.

---

✨ **Rule to remember:**
> "Track last min, last max, and last bad — valid subarrays start between bad+1 and min(lastMin, lastMax)."
