class Solution:
	def minEatingSpeed(self, piles: list[int], h: int) -> int:
		# Instantiating the banana eating speed (k)
		L, R = 1, max(piles)

		while L <= R:
			k = (L + R) // 2

			i = 0
			iter_hours = 0
			while i < len(piles):
				iter_hours += (piles[i] + k - 1) // k
				i += 1

			if iter_hours > h:
				L = k + 1
			elif iter_hours <= h:
				R = k - 1

		return L
