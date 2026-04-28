# 3217. Delete Nodes From Linked List Present in Array

## 🔗 Problem Link
https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Hash Table, Linked List

---

## 🧩 Problem Summary
Given an array of integers `nums` and a linked list `head`, remove all nodes from the linked list whose values exist in `nums`. Return the modified linked list.

### 📌 Constraints
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
- 1 <= Number of nodes <= 10^5
- 1 <= Node.val <= 10^5
- All values in nums are unique

---

## 💭 Intuition
👉 Use a hash set for O(1) lookups and a dummy node to simplify head deletion. Traverse the list, skipping nodes whose values are in the set.

---

## ⚡ Approach — Hash Set + Dummy Node

### 🧠 Idea
- Convert nums to an unordered_set for O(1) membership checks
- Use a dummy node pointing to head to handle potential head deletion
- Traverse with a pointer; if next node's value is in the set, skip it; otherwise advance

---

## 💻 Code

```cpp
class Solution {
 public:
  ListNode* modifiedList(vector<int>& nums, ListNode* head) {
    ListNode dummy(0, head);
    unordered_set<int> numsSet{nums.begin(), nums.end()};

    for (ListNode* curr = &dummy; curr->next != nullptr;)
      if (numsSet.contains(curr->next->val))
        curr->next = curr->next->next;
      else
        curr = curr->next;

    return dummy.next;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [1, 2, 3], head = [1, 2, 3, 4, 5]
```
### Steps
```
Set = {1, 2, 3}
dummy -> 1 -> 2 -> 3 -> 4 -> 5
curr=dummy: next=1, in set -> skip: dummy -> 2 -> 3 -> 4 -> 5
curr=dummy: next=2, in set -> skip: dummy -> 3 -> 4 -> 5
curr=dummy: next=3, in set -> skip: dummy -> 4 -> 5
curr=dummy: next=4, not in set -> advance to 4
curr=4: next=5, not in set -> advance to 5
curr=5: next=null -> stop
Result: 4 -> 5
```

---

## ⏱️ Time Complexity
```
O(n + m) — n = length of nums (set construction), m = length of linked list (traversal)
```

## 💾 Space Complexity
```
O(n) — hash set storing nums values
```

---

## ⚠️ Edge Cases
- All nodes need to be deleted — dummy node handles this
- No nodes need to be deleted — list unchanged
- Head node needs to be deleted — dummy node handles this naturally

---

## 🎯 Interview Takeaways
- Dummy node pattern eliminates special-case handling for head deletion
- Hash set provides efficient membership testing
- The "check next, skip or advance" pattern cleanly handles linked list deletion

---

## 📌 Key Pattern
👉 **"Dummy node + hash set for conditional linked list deletion"**

---

## 🔁 Related Problems
- 203. Remove Linked List Elements
- 237. Delete Node in a Linked List
- 83. Remove Duplicates from Sorted List

---

## 🚀 Final Thoughts
A clean combination of two fundamental patterns: dummy node for safe deletion and hash set for fast lookups. The code is concise and handles all edge cases naturally.

---

✨ **Rule to remember:**
> Use a dummy node to simplify head deletion and a hash set for O(1) membership checks.
