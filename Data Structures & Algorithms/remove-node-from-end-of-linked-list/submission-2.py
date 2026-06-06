# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        jon = head
        cnt = 0
        while jon != None:
            cnt += 1
            jon = jon.next

        jon = head
        for i in range(cnt-n-1):
            jon = jon.next
        if cnt-n-1 == -1:
            return head.next
        if jon.next != None:
            ron = jon.next.next
            jon.next = ron
        
        return head