class Solution: 
    def getConcatenation(self, nums: list[int]) -> list[int]: 
        new_capacity = 2 * len(nums)
        ans = [0] * new_capacity 

        k = 0 
        for j in range(2): 
            for i in range(len(nums)): 
                ans[k] = nums[i]
                k += 1
    
        return ans


