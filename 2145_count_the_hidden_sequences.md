# 2145. Count the Hidden Sequences

## 🔗 Problem Link
https://leetcode.com/problems/count-the-hidden-sequences/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Prefix Sum

---

## 🧩 Problem Summary
Given an array `differences` where `differences[i] = hidden[i+1] - hidden[i]`, and integers `lower` and `upper`, find the number of possible hidden sequences where every element is in `[lower, upper]`.

### 📌 Constraints
- `n == differences.length`
- `1 <= n <= 10^5`
- `-10^5 <= differences[i] <= 10^5`
- `-10^5 <= lower <= upper <= 10^5`

---

## 💭 Intuition
👉 The differences define the shape of the hidden sequence up to a starting value. Compute the prefix sums to find the min and max offsets from the start. The valid range of starting values is determined by keeping all elements within [lower, upper].

---

## ⚡ Approach — Prefix Sum Range

### 🧠 Idea
- Compute prefix sums of differences to get offsets from `hidden[0]`.
- Find `minPrefix` and `maxPrefix` (minimum and maximum offsets).
- The starting value `hidden[0]` must satisfy: `lower - minPrefix <= hidden[0] <= upper - maxPrefix`.
- Count of valid starting values = `max(0, (upper - maxPrefix) - (lower - minPrefix) + 1)`.

---

## 💻 Code

```cpp
class Solution {
public:
    int numberOfArrays(vector<int>& differences, int lower, int upper) {
        long minPrefix = 0, maxPrefix = 0;
        long curr = 0;

        for (int diff : differences) {
            curr += diff;
            minPrefix = min(minPrefix, curr);
            maxPrefix = max(maxPrefix, curr);
        }

        long left = (long)lower - minPrefix;
        long right = (long)upper - maxPrefix;

        if (left > right) return 0;
        return (int)(right - left + 1);
    }
};
```

---

## 🧠 Dry Run
### Input
```
differences = [1, -3, 4], lower = 1, upper = 6
```
### Steps
```
curr=0, minPrefix=0, maxPrefix=0
diff=1: curr=1, maxPrefix=1
diff=-3: curr=-2, minPrefix=-2
diff=4: curr=2, maxPrefix=2
left = 1 - (-2) = 3
right = 6 - 2 = 4
right - left + 1 = 4 - 3 + 1 = 2
Return 2
```

---

## ⏱️ Time Complexity
```
O(n), single pass through the differences array
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- All differences are 0: any value in [lower, upper] works, answer = upper - lower + 1
- Prefix range exceeds [lower, upper] span: return 0
- Single difference: two elements to constrain
- Large positive/negative swings: use `long` to avoid overflow

---

## 🎯 Interview Takeaways
- Prefix sums reveal the "shape" of the sequence relative to the starting point.
- The valid starting range is `[lower - minPrefix, upper - maxPrefix]`.
- This is an elegant O(n) single-pass solution with O(1) space.

---

## 📌 Key Pattern
👉 **"Prefix sum min/max determines the valid range of the starting value"**

---

## 🔁 Related Problems
- 2132. Stamping the Grid
- 370. Range Addition
- 1109. Corporate Flight Bookings

---

## 🚀 Final Thoughts
This problem elegantly reduces to prefix sum analysis. Instead of trying all starting values, we compute the constraints on the starting value in one pass. A beautiful example of how prefix sums simplify range problems.

---

✨ **Rule to remember:**
> When differences fix the sequence shape, the prefix sum min/max determines how many starting values keep all elements in bounds.
