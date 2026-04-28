# 2560. House Robber IV

## 🔗 Problem Link
https://leetcode.com/problems/house-robber-iv/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Binary Search, Greedy

---

## 🧩 Problem Summary
A robber wants to steal from at least `k` houses. They cannot rob two adjacent houses. The robber's capability is the maximum amount stolen from any single house. Return the minimum possible capability needed to rob at least `k` houses.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= k <= ceil(nums.length / 2)`

---

## 💭 Intuition
👉 Binary search on the answer (capability). For a given capability `mid`, greedily count how many non-adjacent houses can be robbed with values <= `mid`. If we can rob >= k houses, try a smaller capability; otherwise, increase it.

---

## ⚡ Approach — Binary Search + Greedy

### 🧠 Idea
- Binary search over the range `[min(nums), max(nums)]` for the capability.
- For each candidate capability `mid`, greedily scan left to right: if `nums[i] <= mid`, rob it and skip the next house.
- If the count of robbed houses >= k, the capability is feasible.

---

## 💻 Code

```cpp
class Solution {
public:
    int minCapability(vector<int>& nums, int k) {
        int left = *min_element(nums.begin(), nums.end());
        int right = *max_element(nums.begin(), nums.end());

        while (left < right) {
            int mid = (left + right) / 2;
            if (numStolenHouses(nums, mid) >= k)
                right = mid;
            else
                left = mid + 1;
        }

        return left;
    }

private:
    int numStolenHouses(const vector<int>& nums, int capacity) {
        int stolenHouses = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] <= capacity) {
                stolenHouses++;
                i++;  // Skip the next house (can't steal two consecutive houses)
            }
        }
        return stolenHouses;
    }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [2,3,5,9], k = 2
```
### Steps
```
left=2, right=9
mid=5: houses with val<=5 (non-adj): index0(2), skip1, index2(5) => 2 >= 2, right=5
mid=3: houses with val<=3 (non-adj): index0(2), skip1, index2(5>3 skip), index3(9>3 skip) => 1 < 2, left=4
mid=4: houses with val<=4 (non-adj): index0(2), skip1, index2(5>4 skip), index3(9>4 skip) => 1 < 2, left=5
left==right==5 => return 5
```

---

## ⏱️ Time Complexity
```
O(n log(max - min))
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- `k = 1`: answer is the minimum element in the array
- All elements are the same value
- Array of length 1 with `k = 1`

---

## 🎯 Interview Takeaways
- "Binary search on the answer" is a powerful pattern when the feasibility check is monotonic.
- The greedy non-adjacent selection is optimal: always rob the first feasible house you encounter.

---

## 📌 Key Pattern
👉 **"Binary search on the answer with a greedy feasibility check"**

---

## 🔁 Related Problems
- 198. House Robber
- 875. Koko Eating Bananas
- 2616. Minimize the Maximum Difference of Pairs

---

## 🚀 Final Thoughts
This elegantly combines binary search (on capability) with a greedy validation (non-adjacent house selection). The monotonicity of the feasibility function guarantees binary search correctness.

---

✨ **Rule to remember:**
> When minimizing the maximum value under constraints, binary search on the answer and greedily validate.
