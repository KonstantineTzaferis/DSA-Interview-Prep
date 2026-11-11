class Solution:
	def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

		def binarySearch(arr: list[int], target: int) -> bool:
			L, R = 0, len(arr) - 1

			while L <= R:
				mid = (L + R) // 2

				if target > arr[mid]:
					L = mid + 1
				elif target < arr[mid]:
					R = mid - 1
				else:
					return True

			return False

		top = 0
		bottom = len(matrix) - 1

		while top <= bottom:
			mid = (top + bottom) // 2

			if target >= matrix[mid][0] and target <= matrix[mid][-1]:
				break
			elif target > matrix[mid][0]:
				top = mid + 1
			else:
				bottom = mid - 1

		return binarySearch(matrix[mid], target)
