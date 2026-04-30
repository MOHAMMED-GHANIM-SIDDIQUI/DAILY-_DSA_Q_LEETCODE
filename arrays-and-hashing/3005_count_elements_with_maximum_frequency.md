# 3005. Count Elements With Maximum Frequency

## 🔗 Problem Link
https://leetcode.com/problems/count-elements-with-maximum-frequency/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Hash Table, Counting

---

## 🧩 Problem Summary
Given an array of positive integers, find the maximum frequency among all elements, then return the total count of all elements that have this maximum frequency.

### 📌 Constraints
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100

---

## 💭 Intuition
👉 First pass: build a frequency map and track the maximum frequency. Second pass: sum up the frequencies of all elements that match the maximum frequency.

---

## ⚡ Approach — Two-Pass Frequency Counting

### 🧠 Idea
- Build a hash map of element frequencies while tracking the maximum frequency.
- Iterate through the map: for every element whose frequency equals the max, add that frequency to the answer.

---

## 💻 Code

```cpp
class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        unordered_map<int,int>mpp;
        int maxfreq=0;
        for(int i:nums)
        {
            mpp[i]++;
            if(mpp[i]>maxfreq)
            maxfreq=mpp[i];
        }
        int ans=0;
        for(auto it:mpp)
        {
            if(it.second==maxfreq)
            {
                ans+=maxfreq;
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
nums = [1, 2, 2, 3, 1, 4]
```
### Steps
```
Build frequency map:
  mpp = {1:2, 2:2, 3:1, 4:1}
  maxfreq = 2

Count elements with maxfreq:
  1 has freq 2 → ans += 2 → ans = 2
  2 has freq 2 → ans += 2 → ans = 4

Output: 4
```

---

## ⏱️ Time Complexity
```
O(n) — two passes: one to build the map, one to count
```

## 💾 Space Complexity
```
O(n) — for the hash map
```

---

## ⚠️ Edge Cases
- All elements are the same: answer equals the array length.
- All elements are unique: every element has frequency 1, answer equals array length.
- Single element: answer is 1.

---

## 🎯 Interview Takeaways
- Two-pass approach is clean: first find max, then count matches.
- Can be done in one pass by maintaining a running total that resets when a new max is found.
- Hash map is the natural choice for frequency counting.

---

## 📌 Key Pattern
👉 **"Frequency counting + max frequency aggregation"**

---

## 🔁 Related Problems
- 347. Top K Frequent Elements
- 451. Sort Characters By Frequency
- 1838. Frequency of the Most Frequent Element

---

## 🚀 Final Thoughts
A straightforward frequency counting problem. The two-pass approach is easy to understand and implement. The key is remembering to sum ALL elements with the maximum frequency, not just count how many distinct elements have that frequency.

---

✨ **Rule to remember:**
> Total frequency count of max-frequency elements = maxFreq * (number of elements with that frequency).
