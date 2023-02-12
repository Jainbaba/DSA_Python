"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        itr = head
        while itr:
            newItr = Node(itr.val)
            temp = itr.next
            itr.next = newItr
            newItr.next = temp
            itr = itr.next.next
        itr = head
        while itr:
            if itr.random:
                itr.next.random = itr.random.next
            itr = itr.next.next
        itr = head
        dummy = Node(0)
        prev = dummy
        while itr:
            temp = itr.next.next
            prev.next = itr.next
            itr.next = temp
            prev = prev.next
            itr = itr.next
        return dummy.next

    
        
        