# 1399. Count Largest Group

## 🔗 Problem Link
https://leetcode.com/problems/count-largest-group/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Hash Table, Math

---

## 🧩 Problem Summary
Given an integer `n`, group all integers from `1` to `n` by the sum of their digits. Return how many groups have the largest size (i.e., the most elements).

### 📌 Constraints
- `1 <= n <= 10^4`

---

## 💭 Intuition
👉 Compute the digit sum of each number from 1 to n, group by digit sum using a hash map, find the maximum group size, then count how many groups achieve that maximum.

---

## ⚡ Approach — Hash Map Grouping by Digit Sum

### 🧠 Idea
- For each number `i` from 1 to `n`, compute its digit sum.
- Use a hash map to count how many numbers share each digit sum.
- Find the maximum count across all groups.
- Count how many groups have that maximum count.

---

## 💻 Code

```cpp
class Solution {
    int sumofdigs(int num)
    {
        int sum=0;
        while(num)
        {
            sum+=num%10;
            num/=10;
        }
        return sum;
    }
public:
    int countLargestGroup(int n) {
        unordered_map<int,int>mpp;
        int maxi=INT_MIN;
        int ans=0;
        for(int i=1;i<=n;i++)
        {
            mpp[sumofdigs(i)]++;
            if(maxi<mpp[sumofdigs(i)])
            {
                maxi=mpp[sumofdigs(i)];

            }
        }
        for(auto it:mpp)
        {
            if(it.second==maxi)
            ans++;
        }
        return ans;
    }
};
```

---

## 🧠 Dry Run
### Input
```
n = 13
```
### Steps
```
Digit sums: 1→1, 2→2, ..., 9→9, 10→1, 11→2, 12→3, 13→4
Groups: {1:[1,10], 2:[2,11], 3:[3,12], 4:[4,13], 5:[5], 6:[6], 7:[7], 8:[8], 9:[9]}
Sizes:   1→2, 2→2, 3→2, 4→2, 5→1, 6→1, 7→1, 8→1, 9→1
Max size = 2, groups with size 2 = 4
Result = 4
```

---

## ⏱️ Time Complexity
```
O(n * d) where d is the number of digits (at most 5)
```

## 💾 Space Complexity
```
O(n) — for the hash map (at most 36 distinct digit sums for n ≤ 10^4)
```

---

## ⚠️ Edge Cases
- `n = 1` → only one group {1}, return 1
- `n = 9` → nine groups each of size 1, return 9
- Large `n` where multiple groups tie for the maximum

---

## 🎯 Interview Takeaways
- Digit sum is computed by repeatedly taking `num % 10` and dividing by 10.
- Two-pass approach: first build groups, then find and count the max.
- Hash maps are ideal for grouping problems.

---

## 📌 Key Pattern
👉 **"Group by computed key (digit sum) → find max group size → count groups with that size."**

---

## 🔁 Related Problems
- 1051. Height Checker
- 258. Add Digits
- 202. Happy Number

---

## 🚀 Final Thoughts
A straightforward grouping problem. Compute digit sums, group with a hash map, and count the groups that tie for the largest size.

---

✨ **Rule to remember:**
> Group by digit sum, then count how many groups tie for the maximum size.
