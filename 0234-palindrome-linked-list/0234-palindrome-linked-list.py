# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        prev = None
        while head:
            itr = head.next
            head.next = prev
            prev = head
            head = itr
        return prev
    
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow  = head
        fast  = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = self.reverse(slow.next)
        itr = head
        slow = slow.next
        while slow:
            if itr.val != slow.val:
                return False
            slow = slow.next
            itr = itr.next
        return True
        
            
            
        
        