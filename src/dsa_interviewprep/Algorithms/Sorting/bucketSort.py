class Solution:
	def bucketSort(self, arr: list[int], k: int) -> list[int]:
		counts = [0] * (k + 1)

		for num in arr:
			counts[num] += 1

		index = 0
		for i in range(len(counts)):
			for _ in range(counts[i]):
				arr[index] = i
				index += 1

		return arr
