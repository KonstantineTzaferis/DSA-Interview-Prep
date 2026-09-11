class recContains: 
    def recursive_contains(self, nums: list[int], target: int, i: int=0) -> bool: 
        if i >= len(nums): 
            return False
        elif nums[i] == target: 
            return True
        else: 
            return self.recursive_contains(nums, target, i+1)

c = recContains()
print(c.recursive_contains([1, 2, 3, 4, 5], 100))