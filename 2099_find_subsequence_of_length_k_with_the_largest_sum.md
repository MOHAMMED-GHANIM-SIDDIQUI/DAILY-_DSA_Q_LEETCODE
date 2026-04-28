# 2099. Find Subsequence of Length K With the Largest Sum

## 🔗 Problem Link
https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Hash Table, Sorting, Heap (Priority Queue)

---

## 🧩 Problem Summary
Given an integer array `nums` and an integer `k`, return a subsequence of `nums` of length `k` that has the largest sum. A subsequence must maintain the relative order of elements from the original array.

### 📌 Constraints
- `1 <= nums.length <= 1000`
- `-10^5 <= nums[i] <= 10^5`
- `1 <= k <= nums.length`

---

## 💭 Intuition
👉 Find the k largest values using partial sort (`nth_element`), then collect them from the original array in order to preserve the subsequence property.

---

## ⚡ Approach — nth_element + Order Preservation

### 🧠 Idea
- Copy the array and use `nth_element` to find the k-th largest value (threshold).
- Count how many elements are strictly larger than the threshold and how many equal to the threshold are needed.
- Iterate through the original array, collecting elements in order: always include elements > threshold, and include elements == threshold until the quota is filled.

---

## 💻 Code

```cpp
class Solution {
 public:
  vector<int> maxSubsequence(vector<int>& nums, int k) {
    vector<int> ans;
    vector<int> arr(nums);
    nth_element(arr.begin(), arr.end() - k, arr.end());
    const int threshold = arr[arr.size() - k];
    const int larger =
        ranges::count_if(nums, [&](int num) { return num > threshold; });
    int equal = k - larger;

    for (const int num : nums)
      if (num > threshold) {
        ans.push_back(num);
      } else if (num == threshold && equal) {
        ans.push_back(num);
        --equal;
      }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [2, 1, 3, 3], k = 2
```
### Steps
```
arr = [2, 1, 3, 3]
nth_element partitions so arr[2..3] are the 2 largest: threshold = arr[2] = 3
larger = count of nums > 3 = 0
equal = 2 - 0 = 2
Iterate nums:
  2 < 3, skip
  1 < 3, skip
  3 == 3, equal=2 > 0 -> add 3, equal=1
  3 == 3, equal=1 > 0 -> add 3, equal=0
ans = [3, 3]
```

---

## ⏱️ Time Complexity
```
O(n) average due to nth_element (O(n) average, O(n^2) worst case)
```

## 💾 Space Complexity
```
O(n) for the copied array
```

---

## ⚠️ Edge Cases
- k equals array length: return the entire array
- All elements are the same: return any k of them
- Negative numbers: works the same, largest sum means least negative
- Duplicate threshold values: the `equal` counter handles correct count

---

## 🎯 Interview Takeaways
- `nth_element` is O(n) average and avoids full sorting.
- Preserving original order requires a second pass through the input.
- Handling duplicates at the threshold boundary is the tricky part.

---

## 📌 Key Pattern
👉 **"Find top-k values with nth_element, then collect in original order"**

---

## 🔁 Related Problems
- 215. Kth Largest Element in an Array
- 347. Top K Frequent Elements
- 1005. Maximize Sum Of Array After K Negations

---

## 🚀 Final Thoughts
This problem tests the understanding of subsequence (order-preserving) vs subset (order-independent). The key insight is separating "which elements to pick" from "in what order to return them."

---

✨ **Rule to remember:**
> For top-k subsequences, find the k largest values first, then collect them in their original order.
