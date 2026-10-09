class Solution: 
    def canConstruct(self, ransomNote: str, magazine: str) -> bool: 
        my_dict = {}

        for char in ransomNote: 
            if char not in my_dict: 
                my_dict[char] = 1
            else: 
                my_dict[char] += 1

        for char in magazine: 
            if char in my_dict: 
                my_dict[char] -= 1

        for key, value in my_dict.items(): 
            if value > 0: 
                return False 

        return True 
    