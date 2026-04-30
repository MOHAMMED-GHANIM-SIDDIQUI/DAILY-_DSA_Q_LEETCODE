# 2402. Meeting Rooms III

## 🔗 Problem Link
https://leetcode.com/problems/meeting-rooms-iii/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Sorting, Heap (Priority Queue), Simulation

---

## 🧩 Problem Summary
Given `n` rooms numbered 0 to n-1 and a list of meetings `[start, end)`, assign each meeting to the lowest-numbered available room. If no room is free, delay the meeting until the earliest room becomes available. Return the room number that held the most meetings.

### 📌 Constraints
- `1 <= n <= 100`
- `1 <= meetings.length <= 10^5`
- `meetings[i].length == 2`
- `0 <= starti < endi <= 5 * 10^5`

---

## 💭 Intuition
👉 Use two heaps: one for available room IDs (min-heap by ID) and one for occupied rooms (min-heap by end time, then ID). For each meeting, free up rooms that have finished, then assign to the lowest available room or delay using the earliest-ending occupied room.

---

## ⚡ Approach — Two Min-Heaps Simulation (C++ Version)

### 🧠 Idea
- Sort meetings by start time.
- Maintain a min-heap `availableRoomIds` for free rooms and a min-heap `occupied` for `(endTime, roomId)`.
- For each meeting, move rooms from `occupied` to `available` if they finish by the meeting's start.
- If a room is available, use the lowest-numbered one. Otherwise, pop the earliest-ending room and delay the meeting.
- Track meeting counts per room; return the room with the highest count (lowest ID on tie).

---

## 💻 Code

```cpp
struct T {
  long endTime;
  int roomId;
};

class Solution {
 public:
  int mostBooked(int n, vector<vector<int>>& meetings) {
    vector<int> count(n);

    ranges::sort(meetings);

    auto compare = [](const T& a, const T& b) {
      return a.endTime == b.endTime ? a.roomId > b.roomId
                                    : a.endTime > b.endTime;
    };
    priority_queue<T, vector<T>, decltype(compare)> occupied(compare);
    priority_queue<int, vector<int>, greater<>> availableRoomIds;

    for (int i = 0; i < n; ++i)
      availableRoomIds.push(i);

    for (const vector<int>& meeting : meetings) {
      const int start = meeting[0];
      const int end = meeting[1];
      // Push meetings ending before this `meeting` in occupied to the
      // `availableRoomsIds`.
      while (!occupied.empty() && occupied.top().endTime <= start)
        availableRoomIds.push(occupied.top().roomId), occupied.pop();
      if (availableRoomIds.empty()) {
        const auto [newStart, roomId] = occupied.top();
        occupied.pop();
        ++count[roomId];
        occupied.push({newStart + (end - start), roomId});
      } else {
        const int roomId = availableRoomIds.top();
        availableRoomIds.pop();
        ++count[roomId];
        occupied.push({end, roomId});
      }
    }

    return ranges::max_element(count) - count.begin();
  }
};
```

---

## 🧠 Dry Run
### Input
```
n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
```
### Steps
```
Sort: [[0,10],[1,5],[2,7],[3,4]]
available = [0,1], occupied = []

[0,10]: room 0 free → assign. occupied={(10,0)}, available=[1], count=[1,0]
[1,5]:  room 1 free → assign. occupied={(5,1),(10,0)}, available=[], count=[1,1]
[2,7]:  no room free. Pop (5,1) → delay to 5, end=5+(7-2)=10.
         occupied={(10,0),(10,1)}, count=[1,2]
[3,4]:  no room free. Pop (10,0) → delay to 10, end=10+(4-3)=11.
         occupied={(10,1),(11,0)}, count=[2,2]

count = [2,2] → max_element index = 0
Result: 0
```

---

## ⏱️ Time Complexity
```
O(m log m + m log n) where m = number of meetings, n = number of rooms.
Sorting is O(m log m), heap operations are O(log n) per meeting.
```

## 💾 Space Complexity
```
O(n + m) — heaps and count array.
```

---

## ⚠️ Edge Cases
- Only one room: all meetings are sequential.
- All meetings overlap: all get delayed sequentially.
- Tie in count: return the lowest-numbered room.

---

## 🎯 Interview Takeaways
- Two-heap pattern (available + occupied) is a classic for resource scheduling.
- Delayed meetings preserve their duration, just shift the start time.
- Using `long` for endTime prevents overflow when delays accumulate.

---

## 📌 Key Pattern
👉 **"Two heaps for resource scheduling: one for free resources, one for busy resources."**

---

## 🔁 Related Problems
- 253. Meeting Rooms II
- 1882. Process Tasks Using Servers
- 2054. Two Best Non-Overlapping Events

---

## 🚀 Final Thoughts
This C++ version uses a custom struct `T` and comparator for the occupied heap, which is more verbose than Python's `heapq` but gives full control over comparison logic. The `long` endTime type handles potential overflow from accumulated delays.

---

✨ **Rule to remember:**
> "Two heaps: one for what's free, one for what's busy — schedule greedily."
