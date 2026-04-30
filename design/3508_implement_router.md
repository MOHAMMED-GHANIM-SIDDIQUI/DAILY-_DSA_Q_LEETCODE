# 3508. Implement Router

## 🔗 Problem Link
https://leetcode.com/problems/implement-router/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Design, Queue, Hash Set, Binary Search, Ordered Map

---

## 🧩 Problem Summary
Design a router with a memory limit that supports adding packets (rejecting duplicates), forwarding the oldest packet (FIFO), and counting packets to a given destination within a time range. Packets are identified by (source, destination, timestamp) tuples.

### 📌 Constraints
- `1 <= memoryLimit <= 10^5`
- Timestamps are non-decreasing for add operations
- Up to 10^5 operations total

---

## 💭 Intuition
👉 Use a **queue** for FIFO ordering, a **set** for O(log n) duplicate detection, and a **map of sorted vectors** for efficient binary-search-based time range counting. Track processed packet indices to exclude forwarded packets from counts.

---

## ⚡ Approach — Queue + Set + Binary Search

### 🧠 Idea
- `addPacket`: Check set for duplicates; if at capacity, forward first; add to queue, set, and destination timestamps.
- `forwardPacket`: Pop from queue, remove from set, increment processed index for that destination.
- `getCount`: Binary search on timestamps (from processed index onward) for [startTime, endTime] range.

---

## 💻 Code

```cpp
struct Packet {
  int source;
  int destination;
  int timestamp;

  bool operator<(const Packet& other) const {
    return source < other.source ||
           (source == other.source && destination < other.destination) ||
           (source == other.source && destination == other.destination &&
            timestamp < other.timestamp);
  }
};

class Router {
 public:
  Router(int memoryLimit) : memoryLimit(memoryLimit) {}

  bool addPacket(int source, int destination, int timestamp) {
    const Packet packet{source, destination, timestamp};
    if (uniquePackets.find(packet) != uniquePackets.end())
      return false;
    if (packetQueue.size() == memoryLimit)
      forwardPacket();
    packetQueue.push(packet);
    uniquePackets.insert(packet);
    destinationTimestamps[destination].push_back(timestamp);
    return true;
  }

  vector<int> forwardPacket() {
    if (packetQueue.empty())
      return {};
    const Packet nextPacket = packetQueue.front();
    packetQueue.pop();
    uniquePackets.erase(nextPacket);
    ++processedPacketIndex[nextPacket.destination];
    return {nextPacket.source, nextPacket.destination, nextPacket.timestamp};
  }

  int getCount(int destination, int startTime, int endTime) {
    if (destinationTimestamps.find(destination) == destinationTimestamps.end())
      return 0;
    const vector<int>& timestamps = destinationTimestamps[destination];
    const int startIndex = processedPacketIndex[destination];
    const auto lowerBound = lower_bound(timestamps.begin() + startIndex,
                                        timestamps.end(), startTime);
    const auto upperBound =
        upper_bound(timestamps.begin() + startIndex, timestamps.end(), endTime);
    return upperBound - lowerBound;
  }

 private:
  const int memoryLimit;
  set<Packet> uniquePackets;
  queue<Packet> packetQueue;
  map<int, vector<int>> destinationTimestamps;
  map<int, int> processedPacketIndex;
};
```

---

## 🧠 Dry Run
### Input
```
Router(2)
addPacket(1, 3, 10) -> true
addPacket(2, 3, 20) -> true
addPacket(1, 3, 10) -> false (duplicate)
getCount(3, 5, 25) -> 2
forwardPacket() -> [1, 3, 10]
getCount(3, 5, 25) -> 1
```
### Steps
```
addPacket(1,3,10): queue=[{1,3,10}], set has it, dest[3]=[10]. Return true.
addPacket(2,3,20): queue=[{1,3,10},{2,3,20}], dest[3]=[10,20]. Return true.
addPacket(1,3,10): found in set. Return false.
getCount(3,5,25): timestamps=[10,20], startIndex=0, lower_bound(5)=0, upper_bound(25)=2 -> 2.
forwardPacket(): pop {1,3,10}, processedIndex[3]=1. Return [1,3,10].
getCount(3,5,25): startIndex=1, search [20], lower_bound(5)=0, upper_bound(25)=1 -> 1.
```

---

## ⏱️ Time Complexity
```
O(log n) — for addPacket (set insert), forwardPacket (set erase), getCount (binary search)
```

## 💾 Space Complexity
```
O(n) — for storing all packets and timestamps
```

---

## ⚠️ Edge Cases
- Forward from empty router → return empty vector
- Duplicate packet detection across add/forward cycles
- getCount with no packets for that destination

---

## 🎯 Interview Takeaways
- Combine multiple data structures (queue, set, map) for different query patterns.
- Using a processed index instead of erasing from timestamp vectors avoids costly deletions.
- Custom comparator for structs enables clean set-based duplicate detection.

---

## 📌 Key Pattern
👉 **"Multi-data-structure design: queue for FIFO, set for dedup, sorted vector + binary search for range queries."**

---

## 🔁 Related Problems
- 146. LRU Cache
- 355. Design Twitter
- 1172. Dinner Plate Stacks

---

## 🚀 Final Thoughts
This is a well-rounded design problem testing the ability to choose complementary data structures. The clever use of a processed index avoids O(n) deletions from the timestamps vector.

---

✨ **Rule to remember:**
> When designing systems with multiple access patterns, combine specialized data structures — each handles one type of query efficiently.
