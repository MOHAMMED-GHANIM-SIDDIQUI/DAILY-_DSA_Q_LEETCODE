# 61. Rotate List

## 🔗 Problem Link
https://leetcode.com/problems/rotate-list/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Linked List, Two Pointers

---

## 🧩 Problem Summary
Given the `head` of a linked list, rotate the list to the right by `k` places.

### 📌 Constraints
- The number of nodes in the list is in the range `[0, 500]`.
- `-100 <= Node.val <= 100`
- `0 <= k <= 2 * 10^9`

---

## 💭 Intuition
👉 Rotating a list right by `k` is equivalent to **cutting** the list at position `n - k` (from the start) and gluing the second piece in front. Since `k` can be larger than `n`, normalize with `k = k % n`. The cleanest mechanic is: connect the tail to head to form a circle, walk `n - k - 1` steps to find the new tail, then break the circle there.

---

## ⚡ Approach 1 — Make Circular, Then Break (O(1) Space)

### 🧠 Idea
- Find the length `n` of the list and the tail node.
- Connect `tail.next = head` to form a cycle.
- Normalize `k = k % n`. The new tail is `n - k - 1` steps from the original head.
- The new head is `new_tail.next`. Break the cycle by setting `new_tail.next = None`.

---

## 💻 Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Find length and tail
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1
        
        # Step 2: Make circular
        tail.next = head
        
        # Step 3: Normalize k
        k = k % n
        
        # Step 4: Find new tail
        steps_to_new_tail = n - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
        
        # Step 5: Break the circle
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
```

---

## ⚡ Approach 2 — Array Buffer (O(n) Space)

### 🧠 Idea
- Copy all node values into an array.
- Slice as `arr[-k:] + arr[:-k]` after `k %= n`.
- Rebuild a fresh linked list from the rotated array using a dummy head.
- Easier to reason about, but uses extra memory and rebuilds nodes.

```python
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        arr = []
        cur = head
        
        while cur:
            arr.append(cur.val)
            cur = cur.next
        
        n = len(arr)
        k = k % n  
        
        arr = arr[-k:] + arr[:-k]
        
        dummy_head = ListNode()
        temp = dummy_head
        
        for i in range(n):
            temp.next = ListNode(arr[i])
            temp = temp.next
        
        return dummy_head.next
```

---

## 🧠 Dry Run
### Input
```
head = [1, 2, 3, 4, 5], k = 2
```
### Steps (Approach 1)
```
n = 5, tail = node(5)
Make circular: 1 -> 2 -> 3 -> 4 -> 5 -> 1 ...
k = 2 % 5 = 2
steps_to_new_tail = 5 - 2 - 1 = 2
new_tail walk: 1 → 2 → 3   (new_tail = node(3))
new_head = node(4)
Break: node(3).next = None
Result: 4 -> 5 -> 1 -> 2 -> 3
```

---

## ⏱️ Time Complexity
```
Approach 1: O(n) — one pass to find length, one partial pass to find new tail
Approach 2: O(n) — one pass to copy, one pass to rebuild
```

## 💾 Space Complexity
```
Approach 1: O(1) — pointer manipulation only
Approach 2: O(n) — array buffer + rebuilt list nodes
```

---

## ⚠️ Edge Cases
- Empty list (`head is None`) → return `head`
- Single node → no rotation needed
- `k == 0` → no rotation
- `k` is a multiple of `n` (e.g., `k = n`, `2n`, ...) → after `k %= n`, `k == 0`, return original head
- `k > n` → normalize with modulo
- `k < 0` is not allowed by constraints, so no need to handle

---

## 🎯 Interview Takeaways
- Rotation by `k` on a list of length `n` only depends on `k % n`.
- The "make it circular, then break" trick is the canonical O(1) space pattern for circular-shift problems on linked lists.
- The new tail sits at index `n - k - 1` (0-indexed from the original head), and the new head is the node right after it.
- Always handle `not head`, single-node, and `k == 0` early to keep the main logic clean.

---

## 📌 Key Pattern
👉 **"Make the list circular, then break it at the right point"**

---

## 🔁 Related Problems
- 189. Rotate Array
- 86. Partition List
- 143. Reorder List
- 25. Reverse Nodes in k-Group

---

## 🚀 Final Thoughts
Two clean approaches: the in-place pointer rewiring is the interview favorite (O(1) space, single structure), while the array rebuild is a straightforward fallback when pointer manipulation feels error-prone. Mastering the circular-then-break pattern transfers directly to many linked-list problems.

---

✨ **Rule to remember:**
> Rotate a linked list right by `k`: form a cycle, walk `n - k - 1` steps, then cut.
