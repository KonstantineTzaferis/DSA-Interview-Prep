"""
Majority element, we need to find the element in an array that appears more than n/2 times in the array 

"""
class Solution: 
    def majorityElement(self, nums: list[int]) -> int: 
        times: dict[int, int] = {}

        for i in range(len(nums)): 
            if nums[i] not in times: 
                times[nums[i]] = 1
            else: 
                times[nums[i]] += 1

        for key, value in times.items(): 
            if value > len(nums) / 2: 
                return key

s = Solution()
print(s.majorityElement([2, 2, 2])) 