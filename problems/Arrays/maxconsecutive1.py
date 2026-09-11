class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int: 
        cnt = 0
        iter_count = 0
        for i in range(len(nums)): 
            if nums[i] == 1: 
                iter_count += 1
                if iter_count > cnt:
                    cnt = iter_count
            else: 
                iter_count = 0 
                
        return cnt

