# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        d1 = headA
        d2 = headB
        while d1 != d2:
            if not d1:
                d1 = headB
            if not d2:
                d2 = headA  
            if d1 == d2:
                break
            d1 = d1.next
            d2 = d2.next
        return d1 
        