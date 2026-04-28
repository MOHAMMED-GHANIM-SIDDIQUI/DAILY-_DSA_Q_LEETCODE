# 2780. Minimum Index of a Valid Split

## 🔗 Problem Link
https://leetcode.com/problems/minimum-index-of-a-valid-split/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Hash Table, Sorting

---

## 🧩 Problem Summary
Given an array `nums` with a dominant element (appears more than half the time), find the minimum index `i` such that splitting at `i` gives two non-empty subarrays where the dominant element of the original array is dominant in both halves. Return -1 if no such split exists.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `nums` has exactly one dominant element

---

## 💭 Intuition
👉 Track the frequency of each element in the left and right partitions as we sweep the split point. For the dominant element to be dominant in both halves, its frequency must exceed half the size of each partition.

---

## ⚡ Approach — Sweep with Dual Frequency Maps

### 🧠 Idea
- Initialize `rightCount` with all frequencies, `leftCount` empty.
- Sweep split index from 0 to n-1: move `nums[i]` from right to left.
- Check if any element is dominant in both halves: `leftFreq * 2 > (i+1)` and `rightFreq * 2 > (n-i-1)`.

---

## 💻 Code

```cpp
class Solution {
public:
    int minimumIndex(std::vector<int>& nums) {
        int n = nums.size();
        std::unordered_map<int, int> leftCount, rightCount;

        // Step 1: Count frequencies of all elements in rightCount
        for (int num : nums)
            rightCount[num]++;

        // Step 2: Iterate through the array and check the dominant condition
        for (int i = 0; i < n; ++i) {
            int num = nums[i];

            // Move element from rightCount (right side) to leftCount (left side)
            leftCount[num]++;
            rightCount[num]--;

            int leftFreq = leftCount[num];
            int rightFreq = rightCount[num];

            // Check if num is dominant in both left and right parts
            if (leftFreq * 2 > (i + 1) && rightFreq * 2 > (n - i - 1))
                return i; // Found the valid index
        }

        return -1; // No valid index found
    }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [1,2,2,2]
```
### Steps
```
rightCount = {1:1, 2:3}

i=0 (num=1): left={1:1}, right={1:0,2:3}
  1: leftFreq=1, 1*2>1? Yes. rightFreq=0, 0*2>3? No.

i=1 (num=2): left={1:1,2:1}, right={1:0,2:2}
  2: leftFreq=1, 1*2>2? No.

i=2 (num=2): left={1:1,2:2}, right={1:0,2:1}
  2: leftFreq=2, 2*2>3? Yes. rightFreq=1, 1*2>1? Yes!
  Return 2

Answer: 2
```

---

## ⏱️ Time Complexity
```
O(n)
```

## 💾 Space Complexity
```
O(n) for the hash maps
```

---

## ⚠️ Edge Cases
- Dominant element is at the very start or end — may not split validly
- Array of length 2 with both elements the same
- All elements are the same — any split works, return 0

---

## 🎯 Interview Takeaways
- Only the dominant element of the full array can be dominant in both halves (by pigeonhole principle).
- A single pass with two frequency counters is sufficient.

---

## 📌 Key Pattern
👉 **"Sweep line partition — maintain left/right frequency counts to check dominance"**

---

## 🔁 Related Problems
- 169. Majority Element
- 229. Majority Element II
- 915. Partition Array into Disjoint Intervals

---

## 🚀 Final Thoughts
The key mathematical insight is that only the overall dominant element can possibly be dominant in both partitions. This means we only need to track one element's frequency across the split, making the solution clean and efficient.

---

✨ **Rule to remember:**
> When splitting an array to preserve a dominant element in both halves, sweep the partition point and track left/right frequencies.
