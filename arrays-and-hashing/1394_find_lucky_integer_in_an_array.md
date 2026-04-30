# 1394. Find Lucky Integer in an Array

## 🔗 Problem Link
https://leetcode.com/problems/find-lucky-integer-in-an-array/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Hash Table, Counting

---

## 🧩 Problem Summary
Given an array of integers `arr`, a lucky integer is an integer that has a frequency in the array equal to its value. Return the largest lucky integer in the array. If there is no lucky integer, return `-1`.

### 📌 Constraints
- `1 <= arr.length <= 500`
- `1 <= arr[i] <= 500`

---

## 💭 Intuition
👉 Count the frequency of each number. A number is "lucky" if its frequency equals its value. Track the maximum such number.

---

## ⚡ Approach — Hash Map Frequency Count

### 🧠 Idea
- Build a frequency map of all elements.
- Iterate through the map; if `frequency[x] == x`, it is lucky.
- Track the maximum lucky integer found.

---

## 💻 Code

```cpp
class Solution {
public:
    int findLucky(vector<int>& arr) {
        unordered_map<int,int>mpp;
        for(int i:arr)
        {
            mpp[i]++;
        }
        int ans=-1;
        for(auto it:mpp)
        {
            if(mpp[it.first]==it.first)
            {
                ans=max(ans,it.first);
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
arr = [2, 2, 3, 4]
```
### Steps
```
Frequency map: {2:2, 3:1, 4:1}
Check 2: freq=2, value=2 → lucky! ans=2
Check 3: freq=1, value=3 → not lucky
Check 4: freq=1, value=4 → not lucky
Result = 2
```

---

## ⏱️ Time Complexity
```
O(n) — one pass to count, one pass to check
```

## 💾 Space Complexity
```
O(n) — for the hash map
```

---

## ⚠️ Edge Cases
- No lucky integer exists → return `-1`
- Multiple lucky integers → return the largest
- `arr = [1]` → `1` appears once → lucky, return `1`

---

## 🎯 Interview Takeaways
- Frequency counting with hash maps is a fundamental technique.
- "Lucky" is simply `count[x] == x` — a straightforward condition.
- Always handle the "not found" case with a sentinel value like `-1`.

---

## 📌 Key Pattern
👉 **"Frequency map + conditional check — count occurrences and match against a criterion."**

---

## 🔁 Related Problems
- 1002. Find Common Characters
- 347. Top K Frequent Elements
- 451. Sort Characters By Frequency

---

## 🚀 Final Thoughts
A simple hash map problem. Count frequencies, check the lucky condition, and track the max. Clean and direct.

---

✨ **Rule to remember:**
> A lucky integer appears exactly as many times as its own value.
