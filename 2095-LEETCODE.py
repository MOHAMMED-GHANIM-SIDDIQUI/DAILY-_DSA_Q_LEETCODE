class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        temp = head

        while temp:
            n += 1
            temp = temp.next

        if n == 1:
            return None

        temp = head
        for _ in range(n // 2 - 1):
            temp = temp.next

        temp.next = temp.next.next

        return head
