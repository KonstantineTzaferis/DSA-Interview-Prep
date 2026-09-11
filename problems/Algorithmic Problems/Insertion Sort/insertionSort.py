class Pair: 
    def __init__(self, key: int, value: str): 
        self.key = key 
        self.value = value 

class Solution: 
    def insertionSort(self, pairs: list[Pair]) -> list[list[Pair]]: 
        # checking for empty list 
        if not pairs: 
            return []

        final_array = []
        final_array.append(pairs.copy())

        for i in range(1, len(pairs)): 
            j = i - 1
            while j >= 0 and pairs[j].key > pairs[j+1].key: 
                temp = pairs[j+1]
                pairs[j+1] = pairs[j]
                pairs[j] = temp 
                j -= 1
            final_array.append(pairs.copy())

        return final_array 
