"""
Implementation of a min Heap, the opposite comparisons will create a max Heap.
"""

from typing import Optional


class Heap:
	def __init__(self, arr: list[int]) -> None:
		self.heap = self.heapify(arr)

	def heapify(self, arr: list[int]) -> Optional[list[int]]:
		if not arr:
			return []

		arr.append(arr[0])

		curr = (len(arr) - 1) // 2

		while curr > 0:
			i = curr

			while 2 * i < len(arr):
				if 2 * i + 1 < len(arr) and arr[2 * i] > arr[2 * i + 1] and arr[i] > arr[2 * i + 1]:
					tmp = arr[i]
					arr[i] = arr[2 * i + 1]
					arr[2 * i + 1] = tmp
					i = 2 * i + 1
				elif arr[2 * i] < arr[i]:
					tmp = arr[i]
					arr[i] = arr[2 * i]
					arr[2 * i] = tmp
					i = 2 * i
				else:
					break
			curr -= 1
		return arr


h = Heap([15, 14, 3, 6, 7, 6, 1, 2])
print(h.heap)
