# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        head = None
        other = None
        ret = None
        if list1.val <= list2.val:
            head = list1
            ret = list1
            other = list2
        else:
            head = list2
            ret = list2
            other = list1

        def insert(list1, node):
            tmp = list1.next
            tmp2 = node
            list1.next = tmp2
            tmp2.next = tmp

        while head.next != None and other != None:
            if head.next.val > other.val:
                tmp = head.next
                tmp2 = other
                other = other.next
                head.next = tmp2
                tmp2.next = tmp
            head = head.next
        if other != None:
            head.next = other
        return ret
        
