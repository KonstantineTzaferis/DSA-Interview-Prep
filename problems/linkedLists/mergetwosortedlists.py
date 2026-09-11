from typing import Optional

class Node: 
    def __init__(self, val:int | None = None): 
        self.val: Optional[int] 
        self.next: Optional[Node]

class Solution: 
    def mergeTwoSortedLists(self, list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]: 
        curr1 = list1
        curr2 = list2

        final_head = Node(None)
        curr = final_head 
        if curr1 is None:
            return curr2
        elif curr2 is None: 
            return curr1 
        else: 
            while curr1 and curr2: 
                if curr1.val < curr2.val: 
                    curr.next = curr1
                    curr1 = curr1.next 
                    curr =  curr.next
                elif curr2.val <= curr1.val: 
                    curr.next = curr2
                    curr2 = curr2.next
                    curr = curr.next
                    
        if curr2 is None: 
            curr.next = curr1
        else: 
            curr.next = curr2
        
        return final_head.next
