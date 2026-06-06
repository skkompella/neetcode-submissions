# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None:
            return
        # traverse whole list
        h = head
        length = 0
        while head != None:
            head = head.next
            length += 1
        head = h

        if length == 1:
            return

        # while head != None:
        #     print(head.val)
        #     head = head.next
        # head = h


        # split list in half
        i = 0
        while i < math.ceil(length/2)-1:
            head = head.next
            i += 1
        l2_head = head.next # list.next is none
        head.next = None # separate list
        head = h
        h2 = l2_head

        # while head != None:
        #     print(head.val)
        #     head = head.next
        # head = h
        # print("goon")
        # while l2_head != None:
        #     print(l2_head.val)
        #     l2_head = l2_head.next
        # l2_head = h2

        # reverse second list
        curr = l2_head
        nxt = l2_head.next
        while nxt != None:
            tmp = nxt
            nxt = nxt.next
            tmp.next = curr
            curr = tmp
        l2_head.next = None
        l2_head = curr

        # while head != None:
        #     print(head.val)
        #     head = head.next
        # head = h
        # print("goon")
        # while l2_head != None:
        #     print(l2_head.val)
        #     l2_head = l2_head.next
        # l2_head = curr

        # merge lists
        while l2_head != None:
            tmp1 = head.next
            tmp2 = l2_head.next
            head.next = l2_head
            l2_head.next = tmp1
            head = tmp1
            l2_head = tmp2
            
            # tmp = head.next
            # tmp2 = l2_head
            # l2_head = l2_head.next
            # head.next = tmp2
            # head = head.next
            # head.next = tmp
            # head = head.next
        head=h
