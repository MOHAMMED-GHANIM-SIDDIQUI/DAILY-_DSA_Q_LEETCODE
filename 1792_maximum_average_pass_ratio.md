# 1792. Maximum Average Pass Ratio

## 🔗 Problem Link
https://leetcode.com/problems/maximum-average-pass-ratio/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Greedy, Heap (Priority Queue)

---

## 🧩 Problem Summary
There is a school with several classes. Each class has a number of students who will pass and a total number of students. You are given `extraStudents` brilliant students who are guaranteed to pass. Assign each extra student to a class to maximize the average pass ratio across all classes.

### 📌 Constraints
- `1 <= classes.length <= 10^5`
- `classes[i] = [pass_i, total_i]`
- `1 <= pass_i <= total_i <= 10^5`
- `1 <= extraStudents <= 10^5`

---

## 💭 Intuition
👉 Each extra student should go to the class where they increase the pass ratio the most. Use a max-heap keyed by the marginal gain — the difference in pass ratio that one additional passing student would create.

---

## ⚡ Approach — Greedy with Max-Heap

### 🧠 Idea
- For each class, compute the "extra pass ratio" — the marginal gain from adding one brilliant student: `(pass+1)/(total+1) - pass/total`.
- Push all classes into a max-heap ordered by this marginal gain.
- For each extra student, pop the class with the highest marginal gain, add the student, recompute the new marginal gain, and push it back.
- After all extra students are assigned, sum up `pass/total` for all classes and divide by the number of classes.

---

## 💻 Code

```cpp
class Solution {
 public:
  double maxAverageRatio(vector<vector<int>>& classes, int extraStudents) {
    // (extra pass ratio, pass, total)
    priority_queue<tuple<double, int, int>> maxHeap;

    for (const vector<int>& c : classes) {
      const int pass = c[0];
      const int total = c[1];
      maxHeap.emplace(extraPassRatio(pass, total), pass, total);
    }

    for (int i = 0; i < extraStudents; ++i) {
      const auto [_, pass, total] = maxHeap.top();
      maxHeap.pop();
      maxHeap.emplace(extraPassRatio(pass + 1, total + 1), pass + 1, total + 1);
    }

    double ratioSum = 0;

    while (!maxHeap.empty()) {
      const auto [_, pass, total] = maxHeap.top();
      maxHeap.pop();
      ratioSum += pass / static_cast<double>(total);
    }

    return ratioSum / classes.size();
  }

 private:
  // Returns the extra pass ratio if a brilliant student joins.
  double extraPassRatio(int pass, int total) {
    return (pass + 1) / static_cast<double>(total + 1) -
           pass / static_cast<double>(total);
  }
};
```

---

## 🧠 Dry Run
### Input
```
classes = [[1,2],[3,5],[2,2]], extraStudents = 2
```
### Steps
```
Initial marginal gains:
  Class [1,2]: (2/3 - 1/2) = 0.1667
  Class [3,5]: (4/6 - 3/5) = 0.0667
  Class [2,2]: (3/3 - 2/2) = 0.0000

Heap (by gain): [(0.1667, 1, 2), (0.0667, 3, 5), (0.0, 2, 2)]

Extra student 1: Pop (0.1667, 1, 2) → becomes (2, 3)
  New gain: (3/4 - 2/3) = 0.0833
  Push (0.0833, 2, 3)

Extra student 2: Pop (0.0833, 2, 3) → becomes (3, 4)
  New gain: (4/5 - 3/4) = 0.05
  Push (0.05, 3, 4)

Final ratios: 3/4 + 3/5 + 2/2 = 0.75 + 0.6 + 1.0 = 2.35
Average: 2.35 / 3 = 0.7833

Result: 0.78333
```

---

## ⏱️ Time Complexity
```
O((n + k) * log n) — n classes pushed to heap, k extra students each requiring a pop and push
```

## 💾 Space Complexity
```
O(n) — for the max-heap storing all classes
```

---

## ⚠️ Edge Cases
- A class with 100% pass rate (pass == total) → marginal gain is 0, never selected
- All classes have the same initial ratio → extra students distributed to maximize diminishing returns
- `extraStudents` is very large → each class eventually approaches 100%
- Single class → all extra students go to it

---

## 🎯 Interview Takeaways
- Greedy assignment with a heap is the standard pattern when you need to repeatedly pick the "best" option.
- The marginal gain function `(p+1)/(t+1) - p/t` correctly captures diminishing returns — larger classes benefit less.
- Using structured bindings (`auto [_, pass, total]`) in C++17 makes heap code cleaner.
- Always recalculate the key after modification before re-inserting into the heap.

---

## 📌 Key Pattern
👉 **"Greedy with max-heap on marginal gain — always assign the next resource to where it helps the most."**

---

## 🔁 Related Problems
- 502. IPO
- 857. Minimum Cost to Hire K Workers
- 1834. Single-Threaded CPU
- 2208. Minimum Operations to Halve Array Sum

---

## 🚀 Final Thoughts
This is a textbook greedy-with-heap problem. The insight is that the benefit of adding a student diminishes as you add more to the same class, so a max-heap on marginal gain naturally handles the optimal assignment order. The `extraPassRatio` helper encapsulates the key computation cleanly.

---

✨ **Rule to remember:**
> "When distributing limited resources for maximum total gain, use a max-heap on marginal benefit — greedily pick the option with the highest incremental improvement."
