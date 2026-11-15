class Solution:
	def heapify(self, array: list[int]) -> list[int]:
		heap = [0]

		for i in range(len(array)):
			self.push(array[i], heap)

		return heap

	def push(self, val: int, array: list[int]) -> None:
		array.append(val)

		i = len(array) - 1

		while i > 1 and array[i] > array[i // 2]:
			tmp = array[i]
			array[i] = array[i // 2]
			array[i // 2] = tmp
			i = i // 2

	def pop(self, array: list[int]) -> int:

		if len(array) == 2:
			return array.pop()

		res = array[1]

		array[1] = array.pop()

		i = 1
		while 2 * i < len(array):
			if (
				2 * i + 1 < len(array)
				and array[i] < array[2 * i + 1]
				and array[2 * i] < array[2 * i + 1]
			):
				tmp = array[i]
				array[i] = array[2 * i + 1]
				array[2 * i + 1] = tmp
				i = 2 * i + 1
			elif array[i] < array[2 * i]:
				tmp = array[i]
				array[i] = array[2 * i]
				array[2 * i] = tmp
				i = 2 * i
			else:
				break

		return res

	def lastStoneWeight(self, stones: list[int]) -> int:

		stones = self.heapify(stones)

		while len(stones) > 2:
			max_weight: int = self.pop(stones)
			second_max: int = self.pop(stones)
			diff = abs(max_weight - second_max)
			self.push(diff, stones)

		return stones[1]


s = Solution()
print(s.lastStoneWeight([1, 2, 3, 4, 5]))
