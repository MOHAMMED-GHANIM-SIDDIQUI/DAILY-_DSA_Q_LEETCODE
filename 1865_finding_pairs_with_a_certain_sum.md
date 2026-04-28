# 1865. Finding Pairs With a Certain Sum

## 🔗 Problem Link
https://leetcode.com/problems/finding-pairs-with-a-certain-sum/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Hash Table, Design

---

## 🧩 Problem Summary
Design a data structure initialized with two arrays `nums1` and `nums2`. Support `add(index, val)` to add `val` to `nums2[index]`, and `count(tot)` to return the number of pairs `(i, j)` such that `nums1[i] + nums2[j] == tot`.

### 📌 Constraints
- `1 <= nums1.length <= 1000`
- `1 <= nums2.length <= 10^5`
- `1 <= nums1[i], nums2[i] <= 10^9`
- At most `1000` calls to `add` and `count`.

---

## 💭 Intuition
👉 Since `nums1` is small (up to 1000), iterate over it for each `count` query. Maintain a frequency map for `nums2` so lookups are O(1). Update the frequency map on `add` operations.

---

## ⚡ Approach — Hash Map on nums2 with Linear Scan on nums1

### 🧠 Idea
- Store `nums2` values in a frequency hash map (`count2`).
- For `add(index, val)`: decrement old value's count, update `nums2[index]`, increment new value's count.
- For `count(tot)`: iterate over `nums1`, for each element look up `tot - nums1[i]` in the hash map.

---

## 💻 Code

```cpp
class FindSumPairs {
 public:
  FindSumPairs(vector<int>& nums1, vector<int>& nums2)
      : nums1(nums1), nums2(nums2) {
    for (const int num : nums2)
      ++count2[num];
  }

  void add(int index, int val) {
    --count2[nums2[index]];
    nums2[index] += val;
    ++count2[nums2[index]];
  }

  int count(int tot) {
    int ans = 0;
    for (const int num : nums1) {
      const int target = tot - num;
      if (const auto it = count2.find(target); it != count2.cend())
        ans += it->second;
    }
    return ans;
  }

 private:
  vector<int> nums1;
  vector<int> nums2;
  unordered_map<int, int> count2;
};
```

---

## 🧠 Dry Run
### Input
```
nums1 = [1, 1, 2, 2, 2, 3], nums2 = [1, 4, 5, 2, 5, 4]
count(7)
add(3, 2)   // nums2 becomes [1, 4, 5, 4, 5, 4]
count(8)
```
### Steps
```
count(7): For each in nums1, find (7-x) in count2
  x=1: look for 6 -> 0
  x=1: look for 6 -> 0
  x=2: look for 5 -> count2[5]=2, ans+=2
  x=2: look for 5 -> ans+=2
  x=2: look for 5 -> ans+=2
  x=3: look for 4 -> count2[4]=2, ans+=2
  Total = 8

add(3, 2): nums2[3]=2 -> 4. Update count2.

count(8): Similar iteration with updated count2.
```

---

## ⏱️ Time Complexity
```
add: O(1)
count: O(len(nums1))
```

## 💾 Space Complexity
```
O(len(nums2)) for the frequency map
```

---

## ⚠️ Edge Cases
- `tot` is smaller than any possible pair sum: returns 0.
- Multiple identical values in both arrays.
- After many `add` operations, values can grow large.

---

## 🎯 Interview Takeaways
- When one array is much smaller, iterate over it and use a hash map for the larger one.
- Maintaining a frequency map with incremental updates is efficient for dynamic data.
- The asymmetry in array sizes drives the design decision.

---

## 📌 Key Pattern
👉 **"Iterate over the smaller array, hash-lookup in the larger: exploit size asymmetry"**

---

## 🔁 Related Problems
- 1. Two Sum
- 167. Two Sum II
- 170. Two Sum III - Data structure design

---

## 🚀 Final Thoughts
This is a design problem where recognizing the constraint asymmetry (nums1 is small, nums2 is large) is the key. By iterating over nums1 and maintaining a hash map for nums2, both operations stay efficient.

---

✨ **Rule to remember:**
> "When two arrays differ in size, iterate the small one and hash-map the large one for O(small) queries."
