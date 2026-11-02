class Solution:
	def climbStairs(self, n: int) -> int:
		memo: dict = {}

		def recursive(number: int):
			if number in memo:
				return memo[number]
			else:
				if number < 0:
					return 0
				elif number == 0:
					return 1
				else:
					left = recursive(number - 1)
					right = recursive(number - 2)
					ways = left + right
					memo[number] = ways

			return memo[number]

		return recursive(n)
