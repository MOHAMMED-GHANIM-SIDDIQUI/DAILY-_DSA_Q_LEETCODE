# 1488. Avoid Flood in the City

## 🔗 Problem Link
https://leetcode.com/problems/avoid-flood-in-the-city/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Hash Table, Greedy, Binary Search, Ordered Set

---

## 🧩 Problem Summary
Given an array `rains` where `rains[i] > 0` means it rains over lake `rains[i]` on day `i`, and `rains[i] == 0` means a dry day where you can choose one lake to dry. Return an array of answers where you assign which lake to dry on each dry day, such that no lake floods. Return an empty array if flooding is unavoidable.

### 📌 Constraints
- `1 <= rains.length <= 10^5`
- `0 <= rains[i] <= 10^9`

---

## 💭 Intuition
👉 When a lake that is already full gets rained on again, we must have dried it on some dry day between the two rain events. We greedily pick the earliest available dry day after the lake was last filled, using an ordered set for efficient lookup.

---

## ⚡ Approach — Greedy with Ordered Set

### 🧠 Idea
- Track which day each lake was last filled using a hash map.
- Maintain a sorted set of dry day indices.
- When a lake that is already full is about to be rained on, find the closest dry day after it was last filled using `upper_bound`.
- If no such dry day exists, return empty (flood is unavoidable).
- Otherwise, use that dry day to empty the lake.
- Fill remaining unused dry days with an arbitrary lake (e.g., lake 1).

---

## 💻 Code

```cpp
class Solution {
 public:
  vector<int> avoidFlood(vector<int>& rains) {
    vector<int> ans(rains.size(), -1);
    unordered_map<int, int> lakeIdToFullDay;
    set<int> emptyDays;  // indices of rains[i] == 0

    for (int i = 0; i < rains.size(); ++i) {
      const int lakeId = rains[i];
      if (lakeId == 0) {
        emptyDays.insert(i);
        continue;
      }
      if (const auto itFullDay = lakeIdToFullDay.find(lakeId);
          itFullDay != lakeIdToFullDay.cend()) {
        // The lake was full in a previous day. Greedily find the closest day
        // to make the lake empty.
        const auto itEmptyDay = emptyDays.upper_bound(itFullDay->second);
        if (itEmptyDay == emptyDays.cend())  // Not found.
          return {};
        // Empty the lake at this day.
        ans[*itEmptyDay] = lakeId;
        emptyDays.erase(itEmptyDay);
      }
      // The lake with `lakeId` becomes full at the day `i`.
      lakeIdToFullDay[lakeId] = i;
    }

    // Empty an arbitrary lake if there are remaining empty days.
    for (const int emptyDay : emptyDays)
      ans[emptyDay] = 1;

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
rains = [1, 2, 0, 0, 2, 1]
```
### Steps
```
Day 0: rain on lake 1 → lakeIdToFullDay = {1:0}, ans = [-1,...]
Day 1: rain on lake 2 → lakeIdToFullDay = {1:0, 2:1}, ans = [-1,-1,...]
Day 2: dry day → emptyDays = {2}
Day 3: dry day → emptyDays = {2, 3}
Day 4: rain on lake 2, already full at day 1 → upper_bound(1) = 2 → ans[2] = 2, emptyDays = {3}
Day 5: rain on lake 1, already full at day 0 → upper_bound(0) = 3 → ans[3] = 1, emptyDays = {}
Answer: [-1, -1, 2, 1, -1, -1]
```

---

## ⏱️ Time Complexity
```
O(n log n), where n is the length of rains (set operations are O(log n))
```

## 💾 Space Complexity
```
O(n) for the hash map and ordered set
```

---

## ⚠️ Edge Cases
- No dry days but a lake is rained on twice — return `[]`.
- All dry days — fill answer with arbitrary lake (e.g., 1).
- Lakes rained on only once — no drying needed.

---

## 🎯 Interview Takeaways
- Greedy choice: always pick the earliest available dry day after the last fill to maximize flexibility.
- Using an ordered set with `upper_bound` enables efficient lookup of the next available dry day.
- This is a classic scheduling/greedy problem disguised as simulation.

---

## 📌 Key Pattern
👉 **"Greedy scheduling with ordered set — find the earliest valid slot after a constraint"**

---

## 🔁 Related Problems
- 621 — Task Scheduler
- 1353 — Maximum Number of Events That Can Be Attended
- 253 — Meeting Rooms II

---

## 🚀 Final Thoughts
This problem tests the ability to recognize a greedy scheduling pattern. The key insight is that dry days are a limited resource that must be assigned optimally — always to the most urgently needed lake, using the earliest possible slot.

---

✨ **Rule to remember:**
> "When scheduling limited resources greedily, always pick the earliest valid slot to maximize future flexibility."
