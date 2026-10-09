from typing import Any

class MyHashMap: 
    def __init__(self): 
        self.myMap: dict[Any, Any] = {}

    def put(self, key: int, value: int) -> None: 
        if key in self.myMap: 
            self.myMap[key] = value 
            return 
        
        self.myMap[key] = value 

    def get(self, key: int) -> int: 
        for dict_key, value in self.myMap.items(): 
            if key == dict_key: 
                return value 

        return -1 

    def remove(self, key: int) -> None: 
        if key in self.myMap: 
            del(self.myMap[key])

    