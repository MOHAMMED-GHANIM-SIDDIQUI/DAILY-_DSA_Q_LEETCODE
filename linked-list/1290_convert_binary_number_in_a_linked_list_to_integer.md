# 1290. Convert Binary Number in a Linked List to Integer

## 🔗 Problem Link
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Linked List, Math

---

## 🧩 Problem Summary

Given the head of a singly linked list where each node's value is either 0 or 1, the linked list represents a binary number (MSB first). Return the decimal value of that binary number.

### 📌 Constraints
- The linked list is not empty.
- Number of nodes will not exceed 30.
- Each node's value is either 0 or 1.

---

## 💭 Intuition

👉 The head is the most significant bit. We need to know the total length to determine each bit's positional value, or we can use bit shifting (`ans = ans * 2 + bit`).

👉 This solution uses a two-pass approach: first count the length, then compute the value using powers of 2.

---

## ⚡ Approach — Two-Pass with Power of 2

### 🧠 Idea
- First pass: count the number of nodes to determine the highest power of 2.
- Second pass: for each node, add `2^position * node_value` to the answer, decrementing the position.

---

## 💻 Code

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    int getDecimalValue(ListNode* head) {
        ListNode* temp=head;
        int ans=0;
        int cnt=0;
        while(temp)
        {
            cnt++;
            temp=temp->next;
        }
        temp=head;
        cnt-=1;
        while(temp)
        {
            ans+=pow(2,cnt)*(temp->val);
            cnt--;
            temp=temp->next;

        }
        return ans;

    }
};
```

---

## 🧠 Dry Run

### Input
```
Linked list: 1 → 0 → 1
```

### Steps
```
Pass 1: count nodes → cnt = 3

Pass 2: cnt = 2 (cnt-1)
  Node 1: ans += pow(2,2) * 1 = 4, cnt=1
  Node 0: ans += pow(2,1) * 0 = 0, cnt=0
  Node 1: ans += pow(2,0) * 1 = 1, cnt=-1

ans = 4 + 0 + 1 = 5
Output: 5 (binary 101 = 5)
```

---

## ⏱️ Time Complexity
```
O(n)
```
Two passes through the linked list, each O(n).

---

## 💾 Space Complexity
```
O(1)
```
Only a few integer variables are used.

---

## ⚠️ Edge Cases
- Single node with value 0 → return 0.
- Single node with value 1 → return 1.
- All zeros → return 0.
- All ones → return `2^n - 1`.

---

## 🎯 Interview Takeaways
- A one-pass alternative exists: `ans = ans * 2 + node->val` (bit shifting approach).
- Using `pow` for integer powers can have floating-point precision issues — bit shifting is safer.
- Two-pass approach is straightforward but the single-pass version is more elegant.
- This is a fundamental linked list traversal problem.

---

## 📌 Key Pattern
👉 **"Binary to decimal conversion — either use positional powers or the shift-and-add technique (ans = ans * 2 + bit)."**

---

## 🔁 Related Problems
- 206 - Reverse Linked List
- 405 - Convert a Number to Hexadecimal
- 1009 - Complement of Base 10 Integer

---

## 🚀 Final Thoughts
A simple linked list problem that tests binary number conversion. While this two-pass approach works, the single-pass `ans = ans * 2 + val` method is preferred in interviews for its elegance and avoidance of floating-point issues.

---

✨ **Rule to remember:**
> "To convert binary digits arriving MSB-first, use ans = ans * 2 + bit — no need to know the length upfront."
