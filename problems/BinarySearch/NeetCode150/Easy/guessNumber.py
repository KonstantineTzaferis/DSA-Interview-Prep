class Solution:
	def guess(self, n: int) -> int:
		return n

	def guessNumber(self, n: int) -> int | None:
		low = 1
		high = n

		while low <= high:
			mid = (low + high) // 2
			result = self.guess(mid)

			if result == 0:
				return mid
			elif result == -1:
				high = mid - 1
			else:
				low = mid + 1
