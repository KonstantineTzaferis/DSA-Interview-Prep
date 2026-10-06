class Solution: 
    def missingNumber(self, nums: list[int]) -> int: 
        times: set[int] = set()

        for i in range(len(nums)): 
            times.add(nums[i])
        for i in range(len(nums)+1): 
            if i not in times: 
                return i
            
             
s = Solution()
print(s.missingNumber([3, 0, 1])) 
            

        