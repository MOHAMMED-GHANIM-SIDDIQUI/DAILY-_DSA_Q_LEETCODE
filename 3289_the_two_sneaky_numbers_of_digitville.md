# 3289. The Two Sneaky Numbers of Digitville

## 🔗 Problem Link
https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Hash Table

---

## 🧩 Problem Summary
Given an array `nums` of size n+2 containing numbers from 0 to n-1 where exactly two numbers appear twice, find and return those two duplicate numbers.

### 📌 Constraints
- 2 <= n <= 100
- nums.length == n + 2
- 0 <= nums[i] < n
- Exactly two elements appear twice

---

## 💭 Intuition
👉 Use a set to track seen numbers. When a number appears for the second time, it's one of the sneaky numbers.

---

## ⚡ Approach — Hash Set Detection

### 🧠 Idea
- Iterate through nums
- For each number, check if it appears exactly twice using count (or use a set for efficiency)
- Track seen duplicates to avoid adding the same number twice

---

## 💻 Code

```python
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        seen = set()
        for i in nums:
            if nums.count(i) == 2 and i not in seen:
                ans.append(i)
                seen.add(i)
        return ans
```

---

## 🧠 Dry Run
### Input
```
nums = [0, 1, 1, 0, 2]
```
### Steps
```
i=0: count(0)=2, not seen -> ans=[0], seen={0}
i=1: count(1)=2, not seen -> ans=[0,1], seen={0,1}
i=1: count(1)=2, already seen -> skip
i=0: count(0)=2, already seen -> skip
i=2: count(2)=1 -> skip
Result: [0, 1]
```

---

## ⏱️ Time Complexity
```
O(n^2) — nums.count() is O(n) called for each element
```

## 💾 Space Complexity
```
O(n) — set for tracking seen duplicates
```

---

## ⚠️ Edge Cases
- Duplicates are the smallest and largest numbers (0 and n-1)
- Duplicates are adjacent in the array
- Duplicates are at the very beginning or end

---

## 🎯 Interview Takeaways
- For small constraints (n <= 100), O(n^2) with count() is acceptable
- A more optimal approach would use a frequency array or set-based detection in O(n)
- The problem guarantees exactly two duplicates, so no validation needed

---

## 📌 Key Pattern
👉 **"Find duplicates using frequency counting or hash set"**

---

## 🔁 Related Problems
- 287. Find the Duplicate Number
- 442. Find All Duplicates in an Array
- 217. Contains Duplicate

---

## 🚀 Final Thoughts
A straightforward duplicate detection problem. While the given solution uses O(n^2) count(), the small constraints make it perfectly acceptable. An optimized O(n) solution would use a set and check for membership as elements are processed.

---

✨ **Rule to remember:**
> Track seen elements with a set; when you see a number twice, it's a duplicate.
