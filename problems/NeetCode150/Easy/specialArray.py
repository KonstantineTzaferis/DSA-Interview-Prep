class Solution: 
    def isArraySpecial(self, nums: list[int]) -> bool: 
        for i in range(len(nums) - 1): 
            j = i + 1
            if nums[i] % 2 == 0: 
                if nums[j] % 2 == 0: 
                    return False 
                else: 
                    continue 

            if nums[i] % 2 != 0: 
                if nums[j] % 2 != 0: 
                    return False
                else: 
                    continue 

        return True

        