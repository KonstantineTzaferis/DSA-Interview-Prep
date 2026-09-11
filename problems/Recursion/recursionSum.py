class RecursiveSum:
    def recursive_sum(self, nums: list[int], i: int = 0) -> int:
        if i == len(nums) - 1:
            return nums[i]

        return nums[i] + self.recursive_sum(nums, i + 1)