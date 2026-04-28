# 1262. Greatest Sum Divisible by Three

## 🔗 Problem Link
https://leetcode.com/problems/greatest-sum-divisible-by-three/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Dynamic Programming, Greedy

---

## 🧩 Problem Summary

Given an array of integers `nums`, return the maximum possible sum of elements such that the sum is divisible by three.

### 📌 Constraints
- `1 <= nums.length <= 4 * 10^4`
- `1 <= nums[i] <= 10^4`

---

## 💭 Intuition

👉 Track the maximum achievable sum for each remainder class (0, 1, 2) when divided by 3.

👉 For each new number, update all three remainder states by considering adding the number to every existing state.

---

## ⚡ Approach — DP with Three Remainder States

### 🧠 Idea
- Maintain `dp[0]`, `dp[1]`, `dp[2]` representing the maximum sum achievable with remainder 0, 1, 2 respectively.
- For each number, create a snapshot of the current DP, then update: `dp[(sum + num) % 3] = max(dp[(sum + num) % 3], sum + num)`.
- Answer is `dp[0]`.

---

## 💻 Code

```cpp
class Solution {
 public:
  int maxSumDivThree(vector<int>& nums) {
    vector<int> dp(3);  // dp[i] := the maximum sum so far s.t. sum % 3 == i

    for (const int num : nums)
      for (const int sum : vector<int>(dp))
        dp[(sum + num) % 3] = max(dp[(sum + num) % 3], sum + num);

    return dp[0];
  }
};
```

---

## 🧠 Dry Run

### Input
```
nums = [3, 6, 5, 1, 8]
```

### Steps
```
Initial dp = [0, 0, 0]

num=3: snapshot=[0,0,0]
  (0+3)%3=0 → dp[0]=max(0,3)=3
  dp = [3, 0, 0]

num=6: snapshot=[3,0,0]
  (3+6)%3=0 → dp[0]=max(3,9)=9
  (0+6)%3=0 → dp[0]=max(9,6)=9
  dp = [9, 0, 0]

num=5: snapshot=[9,0,0]
  (9+5)%3=2 → dp[2]=max(0,14)=14
  (0+5)%3=2 → dp[2]=max(14,5)=14
  dp = [9, 0, 14]

num=1: snapshot=[9,0,14]
  (9+1)%3=1 → dp[1]=max(0,10)=10
  (0+1)%3=1 → dp[1]=max(10,1)=10
  (14+1)%3=0 → dp[0]=max(9,15)=15
  dp = [15, 10, 14]

num=8: snapshot=[15,10,14]
  (15+8)%3=2 → dp[2]=max(14,23)=23
  (10+8)%3=0 → dp[0]=max(15,18)=18
  (14+8)%3=1 → dp[1]=max(10,22)=22
  dp = [18, 22, 23]

Output: dp[0] = 18 (3+6+1+8=18)
```

---

## ⏱️ Time Complexity
```
O(n)
```
One pass through the array, with 3 inner iterations per element (constant).

---

## 💾 Space Complexity
```
O(1)
```
Only a fixed-size array of 3 elements is used.

---

## ⚠️ Edge Cases
- All elements divisible by 3 → sum them all.
- Single element → return it if divisible by 3, else 0.
- All elements have the same remainder → pick multiples of 3 of them.

---

## 🎯 Interview Takeaways
- Remainder-based DP is a powerful technique for divisibility problems.
- Making a snapshot copy of DP before updating prevents using the same element twice in one iteration.
- Only 3 states needed regardless of input size — extremely space efficient.
- This pattern generalizes to "max/min sum divisible by k."

---

## 📌 Key Pattern
👉 **"Remainder DP — track the best achievable value for each remainder class."**

---

## 🔁 Related Problems
- 416 - Partition Equal Subset Sum
- 494 - Target Sum
- 1043 - Partition Array for Maximum Sum

---

## 🚀 Final Thoughts
A compact and elegant DP solution. The key insight is that divisibility by 3 only depends on the remainder, so tracking just 3 states captures all the information needed.

---

✨ **Rule to remember:**
> "For divisibility constraints, track remainders — the actual sum doesn't matter, only its residue."
