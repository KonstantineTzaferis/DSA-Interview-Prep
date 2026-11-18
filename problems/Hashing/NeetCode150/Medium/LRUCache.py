from typing import Optional 

class Node: 
    def __init__(self, key: Optional[int], val: Optional[int]) -> None: 
        self.key = key 
        self.val = val
        self.next: Optional[Node] = None 
        self.prev: Optional[Node] = None   

    
class LRUCache: 
    def __init__(self, capacity: int) -> None: 
        self.capacity = capacity 
        self.cache: dict[int, int] = {}
        self.left = Node(0, 0) # Dummy left node
        self.right = Node(0, 0) # Dummy right node 
        self.left.next = self.right
        self.right.prev = self.left 

    def insert(self, node) -> None: 
        prev, nxt = self.right.prev, self.right 
        prev.next = nxt.prev = node 
        node.prev, node.next = prev, nxt

    def remove(self, node) -> None: 
        prev, next = node.prev, node.next 
        prev.next, next.prev = next, prev


    def printCache(self) -> list[Optional[int]]: 
        stack = []

        if self.right == self.left: 
            return []

        curr = self.left.next

        while curr: 
            if curr == self.right: 
                break 
            stack.append([curr.key, curr.val])
            curr = curr.next

        return stack

    def get(self, key): 
        if key in self.cache: 
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None: 
        if key in self.cache: 
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity: 
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]





