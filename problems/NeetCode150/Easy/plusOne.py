class Solution: 
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits)-1, 0, -1): 
            if digits[i] + 1 > 9: 
                digits[i] = 0 
            else: 
                digits[i] += 1
                return digits
        
        if digits[0] + 1 > 9: 
            digits[0] = 0 
            digits = [1] + digits
        else: 
            digits[0] += 1

        return digits
        