# 1732. Find the Highest Altitude

## 🔗 Problem Link
https://leetcode.com/problems/find-the-highest-altitude/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Prefix Sum

---

## 🧩 Problem Summary

A biker rides through a series of points. You are given an array `gain` where `gain[i]` is the net altitude change between point `i` and point `i+1`. The biker starts at altitude 0. Return the highest altitude reached at any point along the trip.

### 📌 Constraints
- `n == gain.length`
- `1 <= n <= 100`
- `-100 <= gain[i] <= 100`

---

## 💭 Intuition

👉 The altitude at any point is just the running prefix sum of the gains. Accumulate the sum step by step and keep track of the maximum value seen (including the starting altitude 0).

---

## ⚡ Approach — Running Prefix Sum

### 🧠 Idea
- Initialize `cur_sum = 0` (current altitude) and `ans = 0` (best altitude, starts at the initial position).
- Walk through each `cur` in `gain`, adding it to `cur_sum` to get the new altitude.
- After each addition, update `ans = max(ans, cur_sum)`.
- Return `ans` after processing all gains.

---

## 💻 Code

```python
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur_sum = 0
        ans = 0
        for cur in gain:
            cur_sum +=cur
            ans=max(ans , cur_sum)
        return ans
```

---

## 🧠 Dry Run

### Input
```
gain = [-5, 1, 5, 0, -7]
```

### Steps
```
cur_sum=0, ans=0
cur=-5 -> cur_sum=-5, ans=max(0,-5)=0
cur= 1 -> cur_sum=-4, ans=max(0,-4)=0
cur= 5 -> cur_sum= 1, ans=max(0, 1)=1
cur= 0 -> cur_sum= 1, ans=max(1, 1)=1
cur=-7 -> cur_sum=-6, ans=max(1,-6)=1
return 1
```

---

## ⏱️ Time Complexity
```
O(n)
```
Single pass over the `gain` array.

---

## 💾 Space Complexity
```
O(1)
```
Only two scalar variables are kept.

---

## ⚠️ Edge Cases
- All gains negative → answer stays at 0 (the starting altitude).
- Single-element array → answer is `max(0, gain[0])`.
- Highest point occurs in the middle, not at the end.

---

## 🎯 Interview Takeaways
- Recognize "net change between consecutive points" as a prefix-sum signal.
- Always seed the max with the starting altitude (0), since the biker begins there.
- No need to store the full prefix-sum array; a running total suffices.

---

## 📌 Key Pattern
👉 **"Running prefix sum + track maximum"**

---

## 🔁 Related Problems
- 0303 - Range Sum Query Immutable
- 1480 - Running Sum of 1d Array
- 0053 - Maximum Subarray

---

## 🚀 Final Thoughts
A clean introductory prefix-sum problem. The trick is realizing each altitude is a cumulative sum and that the start (0) must be considered when all gains are negative.

---

✨ **Rule to remember:**
> "When asked for the peak of cumulative changes, track the running sum and its max in one pass."
