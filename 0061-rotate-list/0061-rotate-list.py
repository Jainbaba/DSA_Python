# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None or k == 0:
            return head
         
        itrhead = head
        count = 1
        while itrhead.next:
            count += 1
            itrhead = itrhead.next
        k = k % count
        if count == k:
            return head
        itrhead.next = head
        end = count - k
        while(end):
            itrhead = itrhead.next
            end -= 1
        head = itrhead.next
        itrhead.next = None
        return head
         