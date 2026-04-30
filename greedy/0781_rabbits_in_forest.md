# 781. Rabbits in Forest

## 🔗 Problem Link
https://leetcode.com/problems/rabbits-in-forest/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Hash Table, Math, Greedy

---

## 🧩 Problem Summary
Each rabbit in a forest says how many other rabbits have the same color as it. Given an array of these answers, return the minimum number of rabbits that could be in the forest.

### 📌 Constraints
- `1 <= answers.length <= 1000`
- `0 <= answers[i] < 1000`

---

## 💭 Intuition
👉 If a rabbit says `k`, it belongs to a group of `k+1` rabbits of the same color. We can fit at most `k+1` rabbits giving the same answer `k` into one group. If more than `k+1` rabbits say `k`, we need multiple groups.

---

## ⚡ Approach — Greedy Grouping with Hash Map

### 🧠 Idea
- Count how many rabbits gave each answer using a hash map.
- For each answer `k` with count `v`, the group size is `k+1`.
- Number of groups needed = `ceil(v / (k+1))`.
- Total rabbits from this answer = `groups * (k+1)`.

---

## 💻 Code

```cpp
class Solution {
public:
    int numRabbits(vector<int>& answers) {
        unordered_map<int, int> count;
        int total = 0;

        for (int ans : answers) {
            count[ans]++;
        }

        for (auto& [k, v] : count) {
            // Group size is k+1
            int groupSize = k + 1;
            // Number of such groups needed: ceil(v / groupSize)
            int groups = (v + groupSize - 1) / groupSize;
            total += groups * groupSize;
        }

        return total;
    }
};
```

---

## 🧠 Dry Run
### Input
```
answers = [1, 1, 2]
```
### Steps
```
count = {1: 2, 2: 1}

For k=1, v=2: groupSize=2, groups=ceil(2/2)=1, total += 1*2 = 2
For k=2, v=1: groupSize=3, groups=ceil(1/3)=1, total += 1*3 = 3

Total = 5
```

---

## ⏱️ Time Complexity
```
O(n), where n is the length of answers
```

## 💾 Space Complexity
```
O(n) for the hash map
```

---

## ⚠️ Edge Cases
- All rabbits say `0`: each is a unique color, total = number of rabbits.
- All rabbits give the same answer: group them into ceil(count / (answer+1)) groups.
- Single rabbit: return `answers[0] + 1`.

---

## 🎯 Interview Takeaways
- Greedy grouping by ceiling division is a powerful technique.
- The key insight is that `k+1` rabbits can share the same answer `k` in one group.
- Hash map counting followed by math-based grouping is a clean pattern.

---

## 📌 Key Pattern
👉 **"Greedy grouping: fit as many as possible into each group, then ceil-divide for overflow"**

---

## 🔁 Related Problems
- 1647. Minimum Deletions to Make Character Frequencies Unique
- 2244. Minimum Rounds to Complete All Tasks

---

## 🚀 Final Thoughts
This is a great example of a counting and greedy problem. The trick is realizing that rabbits with the same answer can share a group, but only up to a limit. The ceiling division formula neatly handles the overflow case.

---

✨ **Rule to remember:**
> "If k+1 rabbits can share one color group, ceil-divide the count by k+1 to find minimum groups needed."
