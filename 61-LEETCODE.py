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
