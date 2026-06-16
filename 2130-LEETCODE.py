# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        my_list = []
        temp = head
        while temp:
            my_list .append(temp.val)
            temp= temp.next
        n = len(my_list)
        ans = 0
        for i in range(n//2):
            ans = max(ans , my_list[i] + my_list[n-1-i])
        return ans
        
