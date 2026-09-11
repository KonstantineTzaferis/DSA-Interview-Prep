class Node: 
    def __init__(self, val): 
        self.val = val 
        self.next = None 
        self.prev = None 

class doublyLinkedList: 
    def __init__(self): 
        self.head = None
        self.tail = None 
        self.size = 0 

    def get(self, index: int) -> int: 
        if index < 0 or index > self.size -1: 
            return -1
        curr = self.head 
        for _ in range(index): 
            curr = curr.next 
        return curr.val 

    def addAtHead(self, val: int) -> None: 
        value = Node(val)
        if self.head is None: 
            self.head = value 
            self.tail = value 
            self.size += 1
            return 
        else: 
            value.next = self.head 
            self.head.prev = value 
            self.head = value
            self.size += 1

    def addAtTail(self, val: int) -> None: 
        value = Node(val)
        if self.tail is None: 
            self.addAtHead(val)
            return 
        else: 
            self.tail.next = value 
            value.prev = self.tail 
            value.next = None 
            self.tail = value 
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None: 
        if index < 0 or index > self.size: 
            return
        value = Node(val)
        if index == 0: 
            self.addAtHead(val)
        elif index == self.size -1: 
            previous = self.tail.prev 
            previous.next = value 
            value.prev = previous 
            value.next = self.tail 
            self.tail.prev = value
            self.size += 1    
        elif index == self.size: 
            self.addAtTail(val)
        else: 
            curr = self.head 
            for _ in range(index): 
                curr = curr.next 
            previous = curr.prev
            previous.next = value 
            value.next = curr
            curr.prev = value 
            value.prev = previous 
            self.size += 1

    def deleteAtIndex(self, index: int) -> None: 
        if index < 0 or index > self.size - 1: 
            return 
        if self.size == 1: 
            self.head = None 
            self.tail = None 
            self.size = 0 
        if index == 0: 
            self.head = self.head.next
            self.head.prev = None 
            self.size -= 1
        elif index == self.size - 1: 
            self.tail = self.tail.prev 
            self.tail.next = None 
            self.size -= 1
        else: 
            curr = self.head 
            for _ in range(index): 
                curr = curr.next 
            next = curr.next 
            previous = curr.prev
            previous.next = next 
            next.prev = previous 
            self.size -= 1
        
    def getValues(self): 
        if self.head is None: 
            return []

        values = []
        curr = self.head 
        while curr: 
            values.append(curr.val)
            curr = curr.next 

        return values 





        