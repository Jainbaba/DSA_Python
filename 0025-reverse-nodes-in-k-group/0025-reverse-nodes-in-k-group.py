# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        prev = dummy
        curr = dummy
        nex = dummy
        dummy.next = head
        
        itr = head
        count = 0
        while itr:
            count += 1
            itr = itr.next
            
        while(k <= count):
            curr = prev.next
            nex = curr.next
            for _ in range(k-1):
                curr.next = nex.next
                nex.next = prev.next
                prev.next = nex
                nex = curr.next
            prev = curr
            count -= k
        return dummy.next
            
            
        
        