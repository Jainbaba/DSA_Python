# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
         
        prev = head
        curr = head
        itrhead = head
        count = 0
        while itrhead:
            count += 1
            itrhead = itrhead.next
        
        if count < k:
            k = k % count
        if count == k:
            return head
        for i in range(count - k):
            prev = curr
            curr = curr.next
        prev.next = None
        if curr:
            itr = curr
            while itr.next:
                itr = itr.next
            itr.next = head
            return curr
        else:
            return head