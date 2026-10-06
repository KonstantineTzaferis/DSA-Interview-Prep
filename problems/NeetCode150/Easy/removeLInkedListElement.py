from typing import Optional 

class Node: 
    def __init__(self, val=0, next=None): 
        self.val = val 
        self.next = next 

class Solution: 
    def removeElements(self, head: Optional[Node], val: int) -> Optional[Node]: 
        curr = head 
        tmp = head 
        while curr: 
            if head.val == val: 
                curr = curr.next 
                tmp = curr 
                head = curr 
            elif curr.val != val: 
                tmp = curr 
                curr = curr.next 
            else: 
                curr = curr.next 
                tmp.next = curr 

        return head 