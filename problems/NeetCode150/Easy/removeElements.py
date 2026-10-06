from typing import Optional

class Node:
    def __init__(self, val=0, next=None): 
        self.val = val 
        self.next = next 

class Solution:
    def removeElement(self, head: Optional[Node], val: int) -> Optional[Node]: 
        if head is None: 
            return head 

        curr = head
        while curr: 
            if curr.val == val : 
                curr = curr.next

        return head 
