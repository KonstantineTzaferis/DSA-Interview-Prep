class Solution: 
    def removeElement(self, nums: list[int], val: int) -> int | list[int]: 
        k = 0 
        for i in range(len(nums)): 
            if nums[i] != val: 
                nums[k] = nums[i]
                k += 1
        # Return the number of elements that are not equal to val, plus modify the list in place
        return k



