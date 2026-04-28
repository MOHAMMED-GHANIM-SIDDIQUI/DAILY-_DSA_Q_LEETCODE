# 2845. Count of Interesting Subarrays

## 🔗 Problem Link
https://leetcode.com/problems/count-of-interesting-subarrays/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Hash Map, Prefix Sum, Modular Arithmetic

---

## 🧩 Problem Summary
Given an array `nums` and two integers `modulo` and `k`, count the number of "interesting" subarrays. A subarray `nums[l..r]` is interesting if the count of indices `i` in `[l, r]` where `nums[i] % modulo == k` is itself congruent to `k` modulo `modulo`.

### 📌 Constraints
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= modulo <= 10^9
- 0 <= k < modulo

---

## 💭 Intuition
👉 Transform each element to 1 if `nums[i] % modulo == k` and 0 otherwise, then use prefix sums modulo `modulo`. A subarray `[l, r]` is interesting when `(prefix[r] - prefix[l-1]) % modulo == k`, which is a classic prefix sum + hash map pattern.

---

## ⚡ Approach — Prefix Sum with Hash Map

### 🧠 Idea
- Maintain a running prefix sum (mod `modulo`) of how many elements satisfy the condition.
- For each position, compute the target prefix value needed: `(prefix - k + modulo) % modulo`.
- Look up how many times that target appeared before using a frequency map.
- Increment the frequency of the current prefix.

---

## 💻 Code

```cpp
class Solution {
public:
    long long countInterestingSubarrays(vector<int>& nums, int modulo, int k) {
        unordered_map<int, long long> freq;
        freq[0] = 1;  // Starting with prefix sum 0

        long long ans = 0;
        int prefix = 0;

        for (int num : nums) {
            if (num % modulo == k) {
                prefix = (prefix + 1) % modulo;
            } else {
                prefix = prefix % modulo;
            }

            // Find how many previous prefixes match the needed one
            int target = (prefix - k + modulo) % modulo;
            ans += freq[target];

            freq[prefix]++;
        }

        return ans;
    }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [3, 2, 4], modulo = 2, k = 1
```
### Steps
```
Initial: freq = {0: 1}, prefix = 0, ans = 0

i=0, num=3: 3%2==1 → prefix = (0+1)%2 = 1
  target = (1-1+2)%2 = 0 → freq[0]=1 → ans=1
  freq = {0:1, 1:1}

i=1, num=2: 2%2==0 → prefix = 1%2 = 1
  target = (1-1+2)%2 = 0 → freq[0]=1 → ans=2
  freq = {0:1, 1:2}

i=2, num=4: 4%2==0 → prefix = 1%2 = 1
  target = (1-1+2)%2 = 0 → freq[0]=1 → ans=3
  freq = {0:1, 1:3}

Output: 3
```

---

## ⏱️ Time Complexity
```
O(n) — single pass through the array with O(1) hash map operations
```

## 💾 Space Complexity
```
O(min(n, modulo)) — the hash map stores at most `modulo` distinct prefix values
```

---

## ⚠️ Edge Cases
- `k = 0`: Every element not satisfying the condition still contributes to valid subarrays.
- `modulo = 1`: All subarrays are interesting since everything mod 1 equals 0.
- All elements satisfy `nums[i] % modulo == k`.

---

## 🎯 Interview Takeaways
- Prefix sum + hash map is the go-to pattern for counting subarrays with a specific sum/count property.
- Modular arithmetic on prefix sums allows extending the pattern to modular conditions.
- Always initialize the frequency map with `freq[0] = 1` for the empty prefix.

---

## 📌 Key Pattern
👉 **"Prefix Sum with Modular Arithmetic + Hash Map for Subarray Counting"**

---

## 🔁 Related Problems
- 560. Subarray Sum Equals K
- 974. Subarray Sums Divisible by K
- 523. Continuous Subarray Sum

---

## 🚀 Final Thoughts
This problem elegantly combines prefix sums with modular arithmetic. The key transformation is reducing each element to a binary indicator (satisfies condition or not), then using the classic "count subarrays with target sum" technique on the transformed prefix sums modulo `modulo`.

---

✨ **Rule to remember:**
> When counting subarrays by a modular condition on element counts, transform to prefix sums mod m and use a hash map to find matching pairs.
