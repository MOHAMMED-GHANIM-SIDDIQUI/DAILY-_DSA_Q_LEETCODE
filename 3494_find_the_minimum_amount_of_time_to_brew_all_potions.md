# 3494. Find the Minimum Amount of Time to Brew All Potions

## 🔗 Problem Link
https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-all-potions/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Simulation, Greedy, Prefix Sum

---

## 🧩 Problem Summary
Given arrays `skill` (wizard brewing speeds) and `mana` (mana for each potion), wizards brew potions sequentially. Each wizard must finish potion j-1 before starting potion j, and wizard i+1 cannot start potion j until wizard i finishes potion j. Find the minimum total time to brew all potions.

### 📌 Constraints
- `1 <= skill.length <= 10^5`
- `1 <= mana.length <= 10^5`
- `1 <= skill[i], mana[j] <= 10^6`

---

## 💭 Intuition
👉 The bottleneck is the dependency chain: each wizard must wait for either themselves to finish the previous potion, or the previous wizard to finish the current potion. By tracking cumulative end times and propagating backwards, we can compute the optimal schedule.

---

## ⚡ Approach — Backward Propagation with Running Max

### 🧠 Idea
- Initialize with the first potion: last wizard finishes at `sumSkill * mana[0]`.
- For each subsequent potion, sweep backwards through wizards to find the latest necessary start time.
- Use `max()` to resolve the two constraints (own previous potion vs. next wizard's current potion).
- Add `sumSkill * mana[j]` to advance forward.

---

## 💻 Code

```cpp
class Solution {
 public:
  long long minTime(vector<int>& skill, vector<int>& mana) {
    long sumSkill = accumulate(skill.begin(), skill.end(), 0L);
    long prevWizardDone = sumSkill * mana[0];

    for (int j = 1; j < mana.size(); ++j) {
      long prevPotionDone = prevWizardDone;
      for (int i = skill.size() - 2; i >= 0; --i) {
        // start time for wizard i brewing potion j
        // = max(end time for wizard i brewing potion j - 1,
        //       the earliest start time for wizard i + 1 brewing potion j
        //       (coming from previous iteration)
        //       - time for wizard i brewing potion j)
        prevPotionDone -= static_cast<long>(skill[i + 1]) * mana[j - 1];
        prevWizardDone =
            max(prevPotionDone,
                prevWizardDone - static_cast<long>(skill[i]) * mana[j]);
      }
      prevWizardDone += sumSkill * mana[j];
    }

    return prevWizardDone;
  }
};
```

---

## 🧠 Dry Run
### Input
```
skill = [1, 2, 3], mana = [2, 4]
```
### Steps
```
sumSkill = 6
prevWizardDone = 6 * 2 = 12 (after potion 0)

Potion j=1 (mana=4):
  prevPotionDone = 12
  i=1: prevPotionDone = 12 - 3*2 = 6, prevWizardDone = max(6, 12 - 2*4) = max(6, 4) = 6
  i=0: prevPotionDone = 6 - 2*2 = 2, prevWizardDone = max(2, 6 - 1*4) = max(2, 2) = 2
  prevWizardDone = 2 + 6*4 = 26

Result: 26
```

---

## ⏱️ Time Complexity
```
O(n * m) — where n = len(skill) and m = len(mana)
```

## 💾 Space Complexity
```
O(1) — only constant extra space used
```

---

## ⚠️ Edge Cases
- Single wizard → just sum all skill[0] * mana[j]
- Single potion → sumSkill * mana[0]
- Very large values → use long long to prevent overflow

---

## 🎯 Interview Takeaways
- Backward propagation can resolve forward dependency chains efficiently.
- When two constraints compete, `max()` picks the binding one.
- O(1) space is achievable by reusing variables across iterations.

---

## 📌 Key Pattern
👉 **"Backward sweep to resolve cascading dependencies with running max."**

---

## 🔁 Related Problems
- 2141. Maximum Running Time of N Computers
- Assembly line scheduling (DP)
- Job scheduling with dependencies

---

## 🚀 Final Thoughts
This problem models a pipeline scheduling scenario. The backward sweep insight avoids the need for explicit DP tables, achieving O(1) space. Understanding the dependency structure is key.

---

✨ **Rule to remember:**
> When tasks flow through a pipeline with dependencies, sweep backwards to propagate the tightest constraint forward.
