# 3186. Maximum Total Damage With Spell Casting

## 🔗 Problem Link
https://leetcode.com/problems/maximum-total-damage-with-spell-casting/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Hash Table, Dynamic Programming, Sorting, Counting

---

## 🧩 Problem Summary
Given an array `power` where each element is a spell's damage, you can cast spells but cannot cast spells with damage values that differ by 1 or 2. Spells with the same damage can all be cast together. Find the maximum total damage you can deal.

### 📌 Constraints
- 1 <= power.length <= 10^5
- 1 <= power[i] <= 10^9

---

## 💭 Intuition
👉 Group identical damage values, sort unique values, and apply DP similar to House Robber — but with a gap of 2 (can't use values within distance 2).

---

## ⚡ Approach — DP on Sorted Unique Values

### 🧠 Idea
- Count frequency of each damage value
- Sort unique damage values
- Use dp[i][0/1] where 0 = skip i-th damage, 1 = use i-th damage
- When using damage i, look back to find the nearest compatible damage (differs by > 2)
- Multiply damage by its count when used

---

## 💻 Code

```cpp
class Solution {
 public:
  long long maximumTotalDamage(vector<int>& power) {
    unordered_map<int, int> count;

    for (const int damage : power)
      ++count[damage];

    const vector<int> uniqueDamages = getSortedUniqueDamages(count);
    const int n = uniqueDamages.size();
    // dp[i][k] := the maximum damage using uniqueDamages[0..i], where k
    // indicates if the i-th damage is used
    vector<vector<long>> dp(n, vector<long>(2));

    for (int i = 0; i < n; ++i) {
      const long damage = uniqueDamages[i];
      if (i == 0) {
        dp[0][0] = 0;
        dp[0][1] = damage * count[damage];
        continue;
      }
      dp[i][0] = ranges::max(dp[i - 1]);
      dp[i][1] = damage * count[damage];
      if (i >= 1 && uniqueDamages[i - 1] != damage - 1 &&
          uniqueDamages[i - 1] != damage - 2) {
        dp[i][1] += max(dp[i - 1][0], dp[i - 1][1]);
      } else if (i >= 2 && uniqueDamages[i - 2] != damage - 2) {
        dp[i][1] += max(dp[i - 2][0], dp[i - 2][1]);
      } else if (i >= 3) {
        dp[i][1] += max(dp[i - 3][0], dp[i - 3][1]);
      }
    }

    return ranges::max(dp.back());
  }

 private:
  vector<int> getSortedUniqueDamages(const unordered_map<int, int>& count) {
    vector<int> uniqueDamages;
    for (const auto& [damage, _] : count)
      uniqueDamages.push_back(damage);
    ranges::sort(uniqueDamages);
    return uniqueDamages;
  }
};
```

---

## 🧠 Dry Run
### Input
```
power = [1, 1, 3, 4]
```
### Steps
```
count: {1:2, 3:1, 4:1}
uniqueDamages: [1, 3, 4]
i=0 (damage=1): dp[0]=[0, 2]
i=1 (damage=3): dp[1][0]=max(0,2)=2, 3-1=2!=3-1, 3-1=2!=3-2 -> check i-1: 1!=3-1=2 and 1!=3-2=1? 1==1 fail -> i>=2? No -> dp[1][1]=3
  Actually: uniqueDamages[0]=1, damage=3, 1!=2 and 1!=1? 1==1 -> fail. i>=2? No. -> dp[1][1]=3
i=2 (damage=4): dp[2][0]=max(2,3)=3, uniqueDamages[1]=3, 3==4-1? Yes -> check i-1 fails.
  i>=2: uniqueDamages[0]=1, 1!=4-2=2? Yes -> dp[2][1]=4+max(0,2)=6
dp = [[0,2],[2,3],[3,6]]
Result: max(3,6) = 6
```

---

## ⏱️ Time Complexity
```
O(n log n) — sorting unique damages; DP is O(n)
```

## 💾 Space Complexity
```
O(n) — for count map, unique damages array, and dp array
```

---

## ⚠️ Edge Cases
- All spells have the same damage — sum them all
- All damage values are consecutive — House Robber variant
- Large gaps between values — can take all groups

---

## 🎯 Interview Takeaways
- Grouping identical values and sorting unique values is a standard preprocessing step
- The "can't use within distance 2" constraint requires looking back up to 3 positions
- Careful case analysis for which previous state is compatible

---

## 📌 Key Pattern
👉 **"House Robber DP on sorted unique values with distance-2 exclusion"**

---

## 🔁 Related Problems
- 198. House Robber
- 740. Delete and Earn
- 3185. Count Pairs That Form a Complete Day II

---

## 🚀 Final Thoughts
This extends the classic "Delete and Earn" / "House Robber" pattern to a distance-2 exclusion. The key complication is looking back the right number of positions based on the actual value gaps, not just index gaps.

---

✨ **Rule to remember:**
> Group by value, sort, then DP with distance-2 exclusion — a generalized House Robber.
