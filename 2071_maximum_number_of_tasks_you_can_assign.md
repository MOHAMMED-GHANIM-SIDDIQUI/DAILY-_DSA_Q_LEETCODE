# 2071. Maximum Number of Tasks You Can Assign

## 🔗 Problem Link
https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Binary Search, Greedy, Sorting, Multiset

---

## 🧩 Problem Summary
You have `tasks` with strength requirements and `workers` with strength values. You also have `pills` magical pills, each increasing a worker's strength by `strength`. Each worker can do at most one task and take at most one pill. Return the maximum number of tasks that can be completed.

### 📌 Constraints
- `1 <= tasks.length, workers.length <= 5 * 10^4`
- `0 <= pills <= workers.length`
- `0 <= tasks[i], workers[i], strength <= 10^9`

---

## 💭 Intuition
👉 Binary search on the number of tasks `k` that can be assigned. For a given `k`, greedily assign the `k` easiest tasks to the `k` strongest workers, using pills optimally.

---

## ⚡ Approach — Binary Search + Greedy with Multiset

### 🧠 Idea
- Sort both tasks and workers.
- Binary search on `k` (number of tasks assignable).
- For a given `k`, take the `k` easiest tasks and `k` strongest workers.
- Process tasks from hardest to easiest: try to assign without a pill first (find a worker >= task), otherwise use a pill (find a worker >= task - strength).
- Use a multiset for efficient lookup and removal.

---

## 💻 Code

```cpp
class Solution {
public:
    bool canAssign(int k, vector<int>& tasks, vector<int>& workers, int pills, int strength) {
        multiset<int> s(workers.end() - k, workers.end()); // strongest k workers
        int p = pills;

        for (int i = k - 1; i >= 0; --i) {
            int task = tasks[i];
            auto it = s.lower_bound(task);
            if (it != s.end()) {
                s.erase(it); // assign directly
            } else {
                if (p == 0) return false;

                // Try using a pill: find someone with strength + pill >= task
                it = s.lower_bound(task - strength);
                if (it == s.end()) return false;

                s.erase(it);
                --p;
            }
        }
        return true;
    }

    int maxTaskAssign(vector<int>& tasks, vector<int>& workers, int pills, int strength) {
        sort(tasks.begin(), tasks.end());
        sort(workers.begin(), workers.end());

        int low = 0, high = min((int)tasks.size(), (int)workers.size());
        int ans = 0;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (canAssign(mid, tasks, workers, pills, strength)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return ans;
    }
};
```

---

## 🧠 Dry Run
### Input
```
tasks = [3, 2, 1], workers = [0, 3, 3], pills = 1, strength = 1
```
### Steps
```
Sort: tasks=[1,2,3], workers=[0,3,3]
Binary search: low=0, high=3
  mid=1: canAssign(1, ...) -> task[0]=1, workers={3}, 3>=1, assign -> true, ans=1, low=2
  mid=2: canAssign(2, ...) -> s={3,3}, task[1]=2: 3>=2 assign, task[0]=1: 3>=1 assign -> true, ans=2, low=3
  mid=3: canAssign(3, ...) -> s={0,3,3}, task[2]=3: 3>=3 assign, task[1]=2: 3>=2 assign, task[0]=1: 0<1, pill: lower_bound(1-1=0)=0, assign with pill -> true, ans=3
Return 3
```

---

## ⏱️ Time Complexity
```
O(n log n * log(min(m, n))), where n = max(tasks, workers)
```

## 💾 Space Complexity
```
O(n) for the multiset
```

---

## ⚠️ Edge Cases
- No pills available: direct assignment only
- All tasks require pills
- Workers much weaker than tasks even with pills
- pills > workers: pills are capped at worker count

---

## 🎯 Interview Takeaways
- Binary search on the answer when the check function is monotonic.
- Greedy assignment: hardest tasks first, save pills for when truly needed.
- Multiset provides O(log n) lower_bound and erase, ideal for this pattern.

---

## 📌 Key Pattern
👉 **"Binary search on answer + greedy matching with multiset"**

---

## 🔁 Related Problems
- 2141. Maximum Running Time of N Computers
- 1482. Minimum Number of Days to Make m Bouquets
- 2064. Minimized Maximum of Products Distributed to Any Store

---

## 🚀 Final Thoughts
This is a challenging problem that combines binary search on the answer with a sophisticated greedy verification. The multiset is key to efficiently finding and removing the best worker for each task.

---

✨ **Rule to remember:**
> When checking "can we do k?", use the k easiest tasks and k strongest workers, assigning hardest tasks first and saving pills for the weakest workers.
