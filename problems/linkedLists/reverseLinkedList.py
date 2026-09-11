from typing import Optional

class Node: 
    def __init__(self, val=0): 
        self.val = val 
        self.next: Optional[Node|None]

class Solution: 
    def reverseList(self, head: Optional[Node|None]) -> Optional[Node|None]: 
        if head is None: 
            return head
        
        previous = None 
        curr = head 
        after = curr.next 

        while curr is not None: 
            curr.next = previous 
            previous = curr 
            curr = after 

        head = previous 
        return head 


s = Solution()
s.reverseList(Node(30))
s.reverseList(Node(20))
 