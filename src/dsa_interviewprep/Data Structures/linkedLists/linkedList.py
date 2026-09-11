class Node: 
    def __init__(self, val): 
        self.val = val 
        self.next: Node | None 

class linkedList: 
    def __init__(self): 
        self.head: Node | None 
        self.size = 0 

    def get(self, index: int) -> int: 
        if index < 0 or index >= self.size: 
            return -1
        
        curr = self.head
        for _ in range(index): 
            curr = curr.next 
        val = curr.val 
        return val 

    def insertHead(self, val) -> None: 
        new_node = Node(val)
        new_node.next = self.head 
        self.head = new_node 
        self.size += 1

    def insertTail(self, val) -> None: 
        new_node = Node(val)
        if self.head is None: 
            self.head = new_node 
            self.size += 1
            return 

        curr = self.head 
        while curr.next: 
            curr = curr.next 
        curr.next = new_node 
        self.size += 1

    def remove(self, index: int) -> bool: 
        if index < 0 or index >= self.size: 
            return False 

        if index == 0: 
            assert self.head is not None 
            self.head = self.head.next 
            self.size -= 1
            return True 
        else: 
            curr = self.head 
            for _ in range(index-1): 
                curr = curr.next 
            curr.next = curr.next.next
            self.size -=1 
            return True

    def get_values(self): 
        if self.head is None: 
            return []

        values = []
        curr = self.head
        while curr: 
            values.append(curr.val)
            curr = curr.next 

        return values

    def reverse_list(self): 
        if self.head is None: 
            return []

        previous = None 
        curr = self.head 
        after = curr.next 

        while curr is not None:          
            curr.next = previous 
            previous = curr 
            curr = after 

        self.head = previous 
            






            
        

    