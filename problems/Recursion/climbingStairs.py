class Solution: 
    def climbStairs(self, n: int, memo: dict = {}) -> int:
        if n in memo: 
            return memo[n]
        else: 
            if n < 0: 
                return 0
            elif n == 0: 
                return 1
            else: 
                left = self.climbStairs(n-2)
                right = self.climbStairs(n-1)
                memo[n] = left+right 

                return left+right
