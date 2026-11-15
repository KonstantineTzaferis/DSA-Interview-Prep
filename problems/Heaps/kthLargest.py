class kthLargest:
	def __init__(self, k: int, nums: list[int]) -> None:
		self.heap = self.heapify(nums)
		self.k = k

	def heapify(self, array: list[int]) -> list[int]:
		heap = [0]

		for i in range(len(array)):
			self.push(array[i], heap)

		return heap

	def push(self, val: int, array: list[int]) -> None:
		array.append(val)

		i = len(array) - 1

		while array[i] < array[i // 2] and i > 1:
			tmp = array[i]
			array[i] = array[i // 2]
			array[i // 2] = tmp
			i = i // 2

	def pop(self, heap: list[int]) -> int:

		if len(heap) == 2:
			return heap.pop()

		res = heap[1]

		heap[1] = heap.pop()
		i = 1
		while 2 * i < len(heap):
			if (
				2 * i + 1 < len(heap)
				and heap[i] > heap[2 * i + 1]
				and heap[2 * i] > heap[2 * i + 1]
			):
				tmp = heap[i]
				heap[i] = heap[2 * i + 1]
				heap[2 * i + 1] = tmp
				i = 2 * i + 1
			elif heap[i] > heap[2 * i]:
				tmp = heap[i]
				heap[i] = heap[2 * i]
				heap[2 * i] = tmp
				i = 2 * i
			else:
				break

		return res

	def add(self, val: int) -> int:
		self.push(val, self.heap)
		while len(self.heap) > self.k + 1:
			self.pop(self.heap)

		print(self.heap)
		kthLargest = self.heap[1]
		return kthLargest
