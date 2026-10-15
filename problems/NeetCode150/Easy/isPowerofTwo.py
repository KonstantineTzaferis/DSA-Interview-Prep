class Solution:
	def isPowerofTwo(self, n: int) -> bool:
		for i in range(n // 2 + 1):
			if 2**i == n:
				return True
		return False


s = Solution()
print(s.isPowerofTwo(2147483647))
