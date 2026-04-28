# 3408. Design Task Manager

## 🔗 Problem Link
https://leetcode.com/problems/design-task-manager/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Design, Hash Table, Ordered Set, Heap

---

## 🧩 Problem Summary
Design a task manager that supports adding tasks with userId, taskId, and priority, editing a task's priority, removing a task, and executing the highest-priority task (returning its userId). If priorities are equal, execute the task with the higher taskId first.

### 📌 Constraints
- 1 <= tasks.length <= 10^5
- 0 <= userId, taskId, priority <= 10^9
- At most 2 * 10^5 total calls to add, edit, rmv, and execTop

---

## 💭 Intuition
👉 Use a sorted set (ordered by priority descending, then taskId descending) for O(log n) access to the top-priority task, combined with a hash map for O(1) lookup by taskId.

---

## ⚡ Approach — Sorted Set + Hash Map

### 🧠 Idea
- `taskSet`: an ordered set of Task structs, sorted by (priority desc, taskId desc).
- `taskMap`: maps taskId → Task for quick lookup.
- `add`: insert into both structures.
- `edit`: erase old task from set, insert updated task.
- `rmv`: erase from both structures.
- `execTop`: pop the first element from the set (highest priority).

---

## 💻 Code

```cpp
struct Task {
  int userId;
  int taskId;
  int priority;

  Task() = default;
  Task(int u, int t, int p) : userId(u), taskId(t), priority(p) {}

  bool operator<(const Task& other) const {
    return priority == other.priority ? taskId > other.taskId
                                      : priority > other.priority;
  }
};

class TaskManager {
 public:
  unordered_map<int, Task> taskMap;  // {taskId: Task}
  set<Task> taskSet;  // Stores tasks sorted by priority and taskId.

  TaskManager(vector<vector<int>>& tasks) {
    for (const auto& task : tasks)
      add(task[0], task[1], task[2]);
  }

  void add(int userId, int taskId, int priority) {
    const Task task(userId, taskId, priority);
    taskMap[taskId] = task;
    taskSet.insert(task);
  }

  void edit(int taskId, int newPriority) {
    const Task task = taskMap[taskId];
    taskSet.erase(task);
    const Task editedTask = Task(task.userId, task.taskId, newPriority);
    taskSet.insert(editedTask);
    taskMap[taskId] = editedTask;
  }

  void rmv(int taskId) {
    const Task task = taskMap[taskId];
    taskSet.erase(task);
    taskMap.erase(taskId);
  }

  int execTop() {
    if (taskSet.empty())
      return -1;
    const Task task = *taskSet.begin();
    taskSet.erase(task);
    taskMap.erase(task.taskId);
    return task.userId;
  }
}
```

---

## 🧠 Dry Run
### Input
```
tasks = [[1, 101, 10], [2, 102, 20], [3, 103, 15]]
Operations: execTop(), edit(102, 5), execTop()
```
### Steps
```
After init: taskSet = {(102,p=20), (103,p=15), (101,p=10)}

execTop() → task=(102,p=20), userId=2, remove 102
  taskSet = {(103,p=15), (101,p=10)}

edit(102, 5) → ERROR (102 removed), but assuming valid:
edit(101, 25) → remove (101,p=10), insert (101,p=25)
  taskSet = {(101,p=25), (103,p=15)}

execTop() → task=(101,p=25), userId=1
```

---

## ⏱️ Time Complexity
```
O(log n) per operation — set insert/erase/begin are all O(log n)
```

## 💾 Space Complexity
```
O(n) — storing all tasks in set and map
```

---

## ⚠️ Edge Cases
- execTop on empty manager → return -1
- Editing a task to same priority → no effective change
- Multiple tasks with same priority → higher taskId executes first

---

## 🎯 Interview Takeaways
- Combining a sorted container (set) with a hash map gives both ordered access and O(1) lookup.
- Custom comparators must define a strict weak ordering.
- For edit operations, erase-then-reinsert is the standard pattern with ordered sets.

---

## 📌 Key Pattern
👉 **"Ordered set + hash map for priority-based design problems"**

---

## 🔁 Related Problems
- 355. Design Twitter
- 295. Find Median from Data Stream
- 1845. Seat Reservation Manager

---

## 🚀 Final Thoughts
This is a classic design problem combining two data structures. The ordered set handles priority ordering while the hash map provides direct access by taskId, making all operations efficient.

---

✨ **Rule to remember:**
> For design problems needing both ordered iteration and key-based lookup, pair an ordered set with a hash map.
