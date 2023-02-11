# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return None

        slow = head.next
        fast = slow.next

        while slow != fast:
            slow = slow.next
            try:
                fast = fast.next.next
            except AttributeError:
                return None    
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
