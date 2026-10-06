class Solution: 
    def searchRange(self, nums: list[int], target: int) -> list[int]: 
        positions = []
        for i in range(len(nums)): 
            if nums[i] == target: 
                positions.insert(0, i)
                break 
        for j in range(len(nums)-1, -1, -1): 
            if nums[j] == target: 
                positions.insert(1, j)
                break 

        if not positions: 
            return [-1, -1]
        return positions

                
s = Solution()

