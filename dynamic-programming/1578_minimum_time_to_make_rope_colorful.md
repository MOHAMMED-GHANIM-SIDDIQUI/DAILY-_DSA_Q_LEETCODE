# 1578. Minimum Time to Make Rope Colorful

## 🔗 Problem Link
https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, String, Dynamic Programming, Greedy

---

## 🧩 Problem Summary
Alice has balloons arranged on a rope, each with a color and a removal time. She wants no two consecutive balloons to have the same color. Return the minimum total time to remove balloons to achieve this. For each group of consecutive same-colored balloons, keep the one with the highest removal time and remove the rest.

### 📌 Constraints
- `n == colors.length == neededTime.length`
- `1 <= n <= 10^5`
- `1 <= neededTime[i] <= 10^4`
- `colors` consists of lowercase English letters.

---

## 💭 Intuition
👉 For each group of consecutive same-colored balloons, we must remove all but one. To minimize total cost, keep the balloon with the maximum `neededTime` and remove all others. The cost for a group is `sum(group) - max(group)`.

---

## ⚡ Approach — Greedy (Keep Maximum, Remove Rest)

### 🧠 Idea
- Traverse the string, tracking the maximum `neededTime` in the current group of consecutive same-colored balloons.
- When the color changes, reset the tracking.
- When colors match consecutively, add the minimum of the current max and the new balloon's time (the cheaper one gets removed).
- Update the running max for the group.

---

## 💻 Code

```cpp
class Solution {
 public:
  int minCost(string colors, vector<int>& neededTime) {
    int ans = 0;
    int maxNeededTime = neededTime[0];

    for (int i = 1; i < colors.length(); ++i)
      if (colors[i] == colors[i - 1]) {
        ans += min(maxNeededTime, neededTime[i]);
        // For each continuous group, Bob needs to remove every balloon except
        // the one with the maximum `neededTime`. So, he should hold the balloon
        // with the highest `neededTime` in his hand.
        maxNeededTime = max(maxNeededTime, neededTime[i]);
      } else {
        // If the current balloon is different from the previous one, discard
        // the balloon from the previous group and hold the new one in hand.
        maxNeededTime = neededTime[i];
      }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
colors = "aabaa", neededTime = [1, 2, 3, 4, 1]
```
### Steps
```
maxNeededTime = 1
i=1: colors[1]='a'==colors[0]='a'
  ans += min(1, 2) = 1, ans=1
  maxNeededTime = max(1, 2) = 2
i=2: colors[2]='b'!='a'
  maxNeededTime = 3
i=3: colors[3]='a'!='b'
  maxNeededTime = 4
i=4: colors[4]='a'==colors[3]='a'
  ans += min(4, 1) = 1, ans=2
  maxNeededTime = max(4, 1) = 4
Answer: 2 (remove first 'a' with cost 1 and last 'a' with cost 1)
```

---

## ⏱️ Time Complexity
```
O(n), single pass through the arrays
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- No consecutive duplicates — answer is 0.
- All same color — remove all except the one with maximum time.
- All `neededTime` values equal — remove `groupSize - 1` balloons from each group.

---

## 🎯 Interview Takeaways
- Greedy choice: in each group of consecutive same-colored items, always keep the most expensive one.
- The `min(maxNeededTime, neededTime[i])` trick handles the pairwise comparison elegantly.
- This pattern applies broadly: "minimize removal cost to eliminate consecutive duplicates."

---

## 📌 Key Pattern
👉 **"Greedy group processing — keep the maximum-cost element, remove the rest"**

---

## 🔁 Related Problems
- 1246 — Palindrome Removal
- 2216 — Minimum Deletions to Make Array Beautiful
- 1531 — String Compression II

---

## 🚀 Final Thoughts
This problem is a clean greedy exercise. The key observation is that within each consecutive group, the optimal strategy is always to keep the most expensive balloon. The running-max technique handles groups of any length without needing to explicitly identify group boundaries.

---

✨ **Rule to remember:**
> "To minimize removal cost of consecutive duplicates, always keep the most expensive item in each group."
