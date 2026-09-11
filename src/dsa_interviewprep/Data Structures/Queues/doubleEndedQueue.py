class Node:
    def __init__(self, val):
        self.val = val
        self.next: Node|None = None
        self.prev: Node|None = None 

class Deque:
    def __init__(self):
        self.right: Node|None = None 
        self.left: Node|None = None 

    def isEmpty(self) -> bool:
        return self.right is None and self.left is None

    def append(self, value: int) -> None:
        new_node = Node(value)
        if self.isEmpty(): 
            self.right = self.left = new_node 
            return 
        
        self.right.next = new_node
        new_node.prev = self.right 
        self.right = new_node 

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        if self.isEmpty(): 
            self.left = self.right = new_node 
            return 
        
        new_node.next = self.left
        self.left.prev = new_node 
        self.left = new_node

    def pop(self) -> int:
        if self.isEmpty(): 
            return -1

        if self.right == self.left: 
            ret = self.right.val 
            self.right = self.left = None 
            return ret 

        ret = self.right.val      
        self.right = self.right.prev
        self.right.next = None 
        return ret
        
    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        if self.right == self.left:
            ret = self.left.val
            self.right = self.left = None 
            return ret 

        ret = self.left.val
        self.left = self.left.next
        self.left.prev = None
        return ret
