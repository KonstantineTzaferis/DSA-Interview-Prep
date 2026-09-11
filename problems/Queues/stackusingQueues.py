class MyStack: 
    def __init__(self): 
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None: 
        self.q1.append(x) 

    def pop(self) -> int|None: 
        for _ in range(len(self.q1)-1): 
            self.q2.append(self.q1.pop(0))
        element = self.q1.pop(0)
        self.q1 = self.q2
        self.q2 = []
        return element 
        
    def top(self) -> int: 
        iter_value: int = self.q1[0]
        i = 0
        while i < len(self.q1): 
            iter_value = self.q1.pop(0)
            self.q2.append(iter_value)
            self.q1.append(self.q2.pop(0))
            i += 1

        return iter_value

    def empty(self) -> bool: 
        return len(self.q1)  == 0

