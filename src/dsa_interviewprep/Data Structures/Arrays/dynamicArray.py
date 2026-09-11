class DynamicArray: 
    def __init__(self, capacity: int): 
        self.capacity = capacity 
        self.arr = [0] * self.capacity 
        self.size = 0 

    def get(self, i: int) -> int: 
        if i >=0 and self.size > i: 
            return self.arr[i]
        else: 
            return -1 

    def set(self, i: int, n: int) -> None: 
        # Assuming the i is valid we do not need to resize
        self.arr[i] = n 

    def pushback(self, n: int) -> None:
        if self.size == self.capacity: 
            self.resize()
        self.arr[self.size] = n 
        self.size += 1

    def popback(self) -> int: 
        pop_element = self.arr[self.size-1]
        self.arr[self.size-1] = 0
        self.size -= 1
        return pop_element 
        
    def resize(self) -> None:
        new_arr = [0] * 2 * self.capacity
        for i in range(self.size): 
            new_arr[i] = self.arr[i]
        self.capacity *= 2
        self.arr = new_arr 
            
    def getSize(self) -> int: 
        return self.size

    def getCapacity(self) -> int: 
        return self.capacity 







    
        
    
        