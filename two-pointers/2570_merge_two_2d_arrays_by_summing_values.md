# 2570. Merge Two 2D Arrays by Summing Values

## 🔗 Problem Link
https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Hash Table, Two Pointers, Sorting

---

## 🧩 Problem Summary
Given two 2D integer arrays `nums1` and `nums2` where each element is `[id, val]` sorted by id, merge them into a single array. If both arrays contain the same id, sum the values. The result should be sorted by id.

### 📌 Constraints
- `1 <= nums1.length, nums2.length <= 200`
- `nums1[i].length == nums2[j].length == 2`
- `1 <= id_i, val_i <= 1000`
- Both arrays are sorted in strictly ascending order by id.

---

## 💭 Intuition
👉 Combine all `(id, val)` pairs, sort by id, then merge consecutive entries with the same id by summing their values.

---

## ⚡ Approach — Merge and Aggregate

### 🧠 Idea
- Collect all pairs from both arrays into a single list.
- Sort by id.
- Iterate and merge entries with matching ids by summing values.

---

## 💻 Code

```cpp
class Solution {
public:
    vector<vector<int>> mergeArrays(vector<vector<int>>& nums1, vector<vector<int>>& nums2) {
        vector<pair<int, int>> help;

        // Merge all elements from nums1 into help
        for (int i = 0; i < nums1.size(); i++) {
            help.push_back({nums1[i][0], nums1[i][1]});
        }

        // Merge all elements from nums2 into help
        for (int i = 0; i < nums2.size(); i++) {
            help.push_back({nums2[i][0], nums2[i][1]});
        }

        // Sort by the first element of each pair
        sort(help.begin(), help.end());

        // Merging the values of the same first element
        vector<vector<int>> ans;
        int n = help.size();

        for (int i = 0; i < n; i++) {
            if (i == 0 || help[i].first != help[i-1].first) {
                ans.push_back({help[i].first, help[i].second});
            } else {
                ans.back()[1] += help[i].second;
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
nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
```
### Steps
```
help = [(1,2),(2,3),(4,5),(1,4),(3,2),(4,1)]
sorted = [(1,2),(1,4),(2,3),(3,2),(4,5),(4,1)]

i=0: new id=1, ans=[[1,2]]
i=1: same id=1, ans=[[1,6]]
i=2: new id=2, ans=[[1,6],[2,3]]
i=3: new id=3, ans=[[1,6],[2,3],[3,2]]
i=4: new id=4, ans=[[1,6],[2,3],[3,2],[4,5]]
i=5: same id=4, ans=[[1,6],[2,3],[3,2],[4,6]]

Result: [[1,6],[2,3],[3,2],[4,6]]
```

---

## ⏱️ Time Complexity
```
O((m + n) log(m + n)) where m and n are the lengths of nums1 and nums2
```

## 💾 Space Complexity
```
O(m + n)
```

---

## ⚠️ Edge Cases
- No overlapping ids between the two arrays
- All ids overlap — every entry needs summing
- One array is empty

---

## 🎯 Interview Takeaways
- Since both arrays are already sorted, a two-pointer merge (like merge sort) would be O(m+n) and more optimal.
- The sort-based approach is simpler to implement but slightly less efficient.

---

## 📌 Key Pattern
👉 **"Merge sorted arrays and aggregate by key"**

---

## 🔁 Related Problems
- 88. Merge Sorted Array
- 21. Merge Two Sorted Lists
- 1229. Meeting Scheduler

---

## 🚀 Final Thoughts
A simple merge problem. The two-pointer approach leveraging the pre-sorted input would be more efficient, but the concatenate-sort-aggregate approach shown here is clean and easy to understand.

---

✨ **Rule to remember:**
> When merging two sorted key-value arrays, use two pointers for O(m+n) or concatenate-sort for simplicity.
