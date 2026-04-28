# 1550. Three Consecutive Odds

## 🔗 Problem Link
https://leetcode.com/problems/three-consecutive-odds/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array

---

## 🧩 Problem Summary
Given an integer array `arr`, return `true` if there are three consecutive odd numbers in the array, otherwise return `false`.

### 📌 Constraints
- `1 <= arr.length <= 1000`
- `1 <= arr[i] <= 1000`

---

## 💭 Intuition
👉 Use a counter that tracks consecutive odd numbers. Increment on odd, reset on even. If the counter reaches 3, return true.

---

## ⚡ Approach — Counter with Reset

### 🧠 Idea
- Initialize a countdown counter `cnt = 3`.
- For each element: if odd, decrement `cnt`; if even, reset `cnt = 3`.
- If `cnt` reaches 0, we found three consecutive odds — return true.

---

## 💻 Code

```cpp
class Solution {
public:
    bool threeConsecutiveOdds(vector<int>& arr) {

        int cnt=3;
        for(int i:arr)
        {
            if(i%2)
            {
                cnt--;
            }
            else
            {
                cnt=3;
            }
            if(cnt==0)
            return true;
        }
        return false;
    }
};
```

---

## 🧠 Dry Run
### Input
```
arr = [2, 6, 4, 1, 3, 5]
```
### Steps
```
i=2: even, cnt=3
i=6: even, cnt=3
i=4: even, cnt=3
i=1: odd, cnt=2
i=3: odd, cnt=1
i=5: odd, cnt=0 → return true
Answer: true
```

---

## ⏱️ Time Complexity
```
O(n), single pass through the array
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- Array length < 3 — impossible to have three consecutive, return false.
- All odd — return true (first three elements).
- All even — return false.
- Odds separated by evens — counter resets, return false.

---

## 🎯 Interview Takeaways
- Simple counter-based pattern for "K consecutive elements with a property."
- The countdown approach (starting from K and decrementing) is clean and avoids off-by-one errors.
- No need for a sliding window for such a small fixed window size.

---

## 📌 Key Pattern
👉 **"Counter with reset — track consecutive elements satisfying a condition"**

---

## 🔁 Related Problems
- 485 — Max Consecutive Ones
- 1446 — Consecutive Characters
- 1869 — Longer Contiguous Segments of Ones than Zeros

---

## 🚀 Final Thoughts
A minimal problem with a minimal solution. The countdown counter pattern is reusable for any "K consecutive" detection problem. The key is resetting the counter whenever the streak breaks.

---

✨ **Rule to remember:**
> "To detect K consecutive elements with a property, use a counter that decrements on match and resets on mismatch."
