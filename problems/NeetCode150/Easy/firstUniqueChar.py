class Solution: 
    def firstUniqueChar(self, s: str) -> int: 
        indexes = {}
        for i in range(len(s)): 
            if s[i] not in indexes: 
                indexes[s[i]] = 1
            else: 
                indexes[s[i]] += 1

        for key, value in indexes.items(): 
            if value == 1: 
                return s.index(key)

        return -1
