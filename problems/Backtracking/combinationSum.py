from typing import Optional 

class Solution: 
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]: 
        res = []
        path = []

        def dfs(i, total): 
            if total == target: 
                res.append(path.copy())
                return 

            if i >= len(nums) or total > target: 
                return 

            path.append(nums[i])
            dfs(i, total+nums[i])

            path.pop()
            dfs(i+1, total)


        dfs(0, 0)
        return res

s = Solution()
print(s.combinationSum([1, 2], 2))
            