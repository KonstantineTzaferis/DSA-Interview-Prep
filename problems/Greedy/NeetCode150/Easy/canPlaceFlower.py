class Solution:
	def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
		count = 0
		i = 0

		if len(flowerbed) == 1:
			if flowerbed[0] == 0:
				count += 1
			else:
				count = 0

			if count >= n:
				return True
			else:
				return False

		while i < len(flowerbed):
			if i == 0:
				if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
					flowerbed[i] = 1
					count += 1
					i += 1
				else:
					i += 1
			elif i > 0 and i < len(flowerbed) - 1:
				if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
					flowerbed[i] = 1
					count += 1
					i += 1
				else:
					i += 1
			else:
				if flowerbed[i] == 0 and flowerbed[i - 1] == 0:
					flowerbed[i] = 1
					count += 1
					i += 1
				else:
					i += 1

		if count >= n:
			return True

		return False
