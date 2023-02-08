# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(None,head)
        prev,curr = dummy,head 
        leftprev,leftnode = prev, curr
        for i in range(1,right+1):
            if i <= (left-1):
                prev = curr
                curr = curr.next
                leftprev,leftnode = prev, curr
            else:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
        rightprev,rightnode = prev,curr
        
        leftprev.next = rightprev
        leftnode.next = rightnode
        return dummy.next
        
        
                
            
                
            
        
        

        
