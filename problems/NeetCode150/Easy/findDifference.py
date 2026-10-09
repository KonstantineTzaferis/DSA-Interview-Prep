class Solution: 
    def findDifference(self, s: str, t: str) -> str|None: 
        frequency: dict[str, int] = {}
        for i in range(len(t)): 
            if t[i] not in frequency: 
                frequency[t[i]] = 1
            else: 
                frequency[t[i]] += 1
                
        for char in s: 
            frequency[char] -= 1

        for key, value in frequency.items(): 
            if value == 1: 
                return key

