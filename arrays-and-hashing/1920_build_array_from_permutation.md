# 1920. Build Array from Permutation

## 🔗 Problem Link
https://leetcode.com/problems/build-array-from-permutation/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Simulation

---

## 🧩 Problem Summary
Given a zero-based permutation `nums`, build an array `ans` of the same length where `ans[i] = nums[nums[i]]` and return it.

### 📌 Constraints
- `1 <= nums.length <= 1000`
- `0 <= nums[i] < nums.length`
- The elements in `nums` are distinct

---

## 💭 Intuition
👉 This is a direct application problem — simply follow the formula `ans[i] = nums[nums[i]]` for each index.

---

## ⚡ Approach — Direct Simulation

### 🧠 Idea
- Create an empty result array.
- For each index `i`, push `nums[nums[i]]` into the result.
- Return the result array.

---

## 💻 Code

```cpp
class Solution {
public:
    vector<int> buildArray(vector<int>& nums) {
        vector<int>ans;
        int n=nums.size();
        for(int i=0;i<n;i++)
        {
            ans.push_back(nums[nums[i]]);
        }
        return ans;
    }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [0, 2, 1, 5, 3, 4]
```
### Steps
```
i=0: ans[0] = nums[nums[0]] = nums[0] = 0
i=1: ans[1] = nums[nums[1]] = nums[2] = 1
i=2: ans[2] = nums[nums[2]] = nums[1] = 2
i=3: ans[3] = nums[nums[3]] = nums[5] = 4
i=4: ans[4] = nums[nums[4]] = nums[3] = 5
i=5: ans[5] = nums[nums[5]] = nums[4] = 3
ans = [0, 1, 2, 4, 5, 3]
```

---

## ⏱️ Time Complexity
```
O(n), where n is the length of nums
```

## 💾 Space Complexity
```
O(n) for the result array
```

---

## ⚠️ Edge Cases
- Array of length 1 → `nums = [0]`, result is `[0]`
- Identity permutation → result equals input
- Follow-up: Can you solve it in O(1) extra space? (Encode two values per cell using modular arithmetic)

---

## 🎯 Interview Takeaways
- Permutation composition is a fundamental concept in mathematics and CS.
- The O(1) space follow-up uses the encoding `nums[i] = nums[i] + n * (nums[nums[i]] % n)` to store both old and new values.

---

## 📌 Key Pattern
👉 **"Permutation composition: ans[i] = nums[nums[i]]"**

---

## 🔁 Related Problems
- 2011. Final Value of Variable After Performing Operations
- 1929. Concatenation of Array
- 2149. Rearrange Array Elements by Sign

---

## 🚀 Final Thoughts
A simple warm-up problem that tests basic array indexing. The interesting follow-up about O(1) space introduces the technique of encoding multiple values in a single cell using modular arithmetic.

---

✨ **Rule to remember:**
> For O(1) space permutation building, encode `new_val * n + old_val` in each cell and decode later.
