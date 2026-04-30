# 3433. Count Mentions Per User

## 🔗 Problem Link
https://leetcode.com/problems/count-mentions-per-user/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Sorting, Simulation, Hash Table

---

## 🧩 Problem Summary
Given a number of users and a list of events (MESSAGE or OFFLINE), count how many times each user is mentioned. Messages can mention specific users (by id), "ALL" users, or "HERE" (only online users). Users go offline for 60 time units after an OFFLINE event. Events must be processed in timestamp order; OFFLINE events before MESSAGE events at the same timestamp.

### 📌 Constraints
- 1 <= numberOfUsers <= 100
- 1 <= events.length <= 100
- Events are [type, timestamp, data]

---

## 💭 Intuition
👉 Sort events by timestamp (with OFFLINE before MESSAGE at same time). Use a min-heap to track when offline users come back online. Process each event in order, updating mention counts.

---

## ⚡ Approach — Sorting + Priority Queue Simulation

### 🧠 Idea
- Sort events by (timestamp, type) where OFFLINE comes before MESSAGE at same time.
- Track online/offline status with a boolean array and a min-heap for return times.
- For "ALL" mentions, increment a global counter (added to all users at the end).
- For "HERE" mentions, increment only online users.
- For specific mentions, parse user IDs and increment directly.
- Before processing each event, pop expired offline entries from the heap.

---

## 💻 Code

```cpp
struct OfflineUser {
  int returnTimestamp;
  int userId;
  bool operator>(const OfflineUser& other) const {
    return returnTimestamp > other.returnTimestamp;
  }
};

class Solution {
 public:
  vector<int> countMentions(int numberOfUsers, vector<vector<string>>& events) {
    vector<int> ans(numberOfUsers);
    vector<int> online(numberOfUsers, true);
    // min-heap to track users that are offline
    priority_queue<OfflineUser, vector<OfflineUser>, greater<>> offlineQueue;
    int allMentionsCount = 0;

    ranges::sort(events, ranges::less{}, [](const vector<string>& event) {
      const int timestamp = stoi(event[1]);
      const char eventType = event[0][0];
      return pair<int, char>{timestamp, -eventType};
    });

    for (const vector<string>& event : events) {
      const string eventType = event[0];
      const int timestamp = stoi(event[1]);
      // Bring users back online if their offline period has ended.
      while (!offlineQueue.empty() &&
             offlineQueue.top().returnTimestamp <= timestamp)
        online[offlineQueue.top().userId] = true, offlineQueue.pop();
      if (eventType == "MESSAGE") {
        const string mentionsString = event[2];
        if (mentionsString == "ALL") {
          ++allMentionsCount;
        } else if (mentionsString == "HERE") {
          for (int userId = 0; userId < numberOfUsers; ++userId)
            if (online[userId])
              ++ans[userId];
        } else {
          for (const int userId : getUserIds(mentionsString))
            ++ans[userId];
        }
      } else if (eventType == "OFFLINE") {
        const int userId = stoi(event[2]);
        online[userId] = false;
        // Add to queue to bring back online after 60 units.
        offlineQueue.emplace(timestamp + 60, userId);
      }
    }

    // Add the "ALL" mentions to all users.
    for (int userId = 0; userId < numberOfUsers; ++userId)
      ans[userId] += allMentionsCount;
    return ans;
  }

 private:
  vector<int> getUserIds(const string& s) {
    vector<int> integers;
    istringstream iss(s);
    for (string id; iss >> id;)
      integers.push_back(stoi(id.substr(2)));
    return integers;
  }
};
```

---

## 🧠 Dry Run
### Input
```
numberOfUsers = 2
events = [["MESSAGE","10","id0 id1"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]]
```
### Steps
```
Sort: events stay in order (timestamps 10 < 11 < 71)

Event 1: MESSAGE at t=10, "id0 id1"
  → ans[0]++, ans[1]++ → ans=[1,1]

Event 2: OFFLINE at t=11, user 0
  → online[0]=false, queue={(71,0)}

Event 3: MESSAGE at t=71, "HERE"
  → Pop (71,0): 71<=71, online[0]=true
  → Both online: ans[0]++, ans[1]++ → ans=[2,2]

allMentionsCount=0, final ans=[2,2]
```

---

## ⏱️ Time Complexity
```
O(E log E + E * U) — sorting events and processing mentions
```

## 💾 Space Complexity
```
O(U + E) — online array and priority queue
```

---

## ⚠️ Edge Cases
- All messages are "ALL" → every user gets the same count
- User goes offline multiple times → multiple entries in the heap
- OFFLINE and MESSAGE at same timestamp → OFFLINE processed first

---

## 🎯 Interview Takeaways
- Custom sorting with multiple keys is essential for event ordering.
- A min-heap elegantly handles "come back online after X time" logic.
- Deferring "ALL" counts to the end avoids redundant per-user updates.

---

## 📌 Key Pattern
👉 **"Event simulation with priority queue for timed state changes"**

---

## 🔁 Related Problems
- 253. Meeting Rooms II
- 1834. Single-Threaded CPU

---

## 🚀 Final Thoughts
This problem is a realistic simulation exercise combining sorting, state management, and string parsing. The key design choice is using a min-heap for offline expiration and deferring bulk operations.

---

✨ **Rule to remember:**
> For timed status changes, use a priority queue to lazily restore state only when processing the next relevant event.
