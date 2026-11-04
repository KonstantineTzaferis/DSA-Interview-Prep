class Solution:
	def findLucky(self, arr: list[int]) -> int:
		counter: dict = {}

		for i in range(len(arr)):
			if arr[i] not in counter:
				counter[arr[i]] = 1
			else:
				counter[arr[i]] += 1

		max = -1
		for key, value in counter.items():
			if key == value:
				if key > max:
					max = key

		return max
