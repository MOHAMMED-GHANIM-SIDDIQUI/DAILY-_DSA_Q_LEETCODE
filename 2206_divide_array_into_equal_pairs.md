# 2206. Divide Array Into Equal Pairs

## 🔗 Problem Link
https://leetcode.com/problems/divide-array-into-equal-pairs/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Hash Table, Counting

---

## 🧩 Problem Summary
Given an array `nums` of `2n` integers, determine if it can be divided into `n` pairs such that each pair consists of equal elements.

### 📌 Constraints
- `nums.length == 2 * n`
- `1 <= n <= 500`
- `1 <= nums[i] <= 500`

---

## 💭 Intuition
👉 Every element must appear an even number of times — if any element has an odd frequency, pairing is impossible.

---

## ⚡ Approach — Frequency Count

### 🧠 Idea
- Count the frequency of each element using a hash map.
- If any element has an odd count, return false.
- Otherwise, return true.

---

## 💻 Code

```cpp
class Solution {
public:
    bool divideArray(vector<int>& nums) {
        unordered_map<int,int>mpp;
        for(int i:nums)
        mpp[i]++;
        for(auto it:mpp)
        {
            if(it.second%2!=0)
            return false;
        }
        return true;
    }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [3, 2, 3, 2, 2, 2]
```
### Steps
```
Frequency: {3:2, 2:4}
3 → count 2 (even ✓)
2 → count 4 (even ✓)
All even → return true
```

---

## ⏱️ Time Complexity
```
O(n) — single pass to count, single pass to verify
```

## 💾 Space Complexity
```
O(n) — for the frequency map
```

---

## ⚠️ Edge Cases
- All elements are the same → always true (2n is even)
- All elements are distinct → always false (each appears once)
- Single pair (n=1) → two elements must be equal

---

## 🎯 Interview Takeaways
- Frequency counting is the go-to technique for pairing/grouping problems.
- Even frequency is necessary and sufficient for equal pairing.
- Could also use XOR or sorting, but hash map is most direct.

---

## 📌 Key Pattern
👉 **"Check that every element frequency is even for complete pairing"**

---

## 🔁 Related Problems
- 217. Contains Duplicate
- 2154. Keep Multiplying Found Values by Two
- 383. Ransom Note

---

## 🚀 Final Thoughts
A simple frequency-based problem. The core insight — every value needs an even count — makes this a one-pass verification after counting.

---

✨ **Rule to remember:**
> "To pair all elements equally, every value must appear an even number of times."
