from math import sqrt


class Solution:
    def KClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        def euclidean(point: list[int]) -> int | float:
            return sqrt((point[0] - 0) ** 2 + (point[1] - 0) ** 2)

        def quicksort(arr, start, end):
            if start >= end:
                return

            pivot = end
            left = start

            for i in range(start, end):
                if euclidean(arr[i]) <= euclidean(arr[pivot]):
                    arr[left], arr[i] = arr[i], arr[left]
                    left += 1

            arr[left], arr[end] = arr[end], arr[left]

            quicksort(arr, start, left - 1)
            quicksort(arr, left + 1, end)

        start = 0
        end = len(points) - 1

        quicksort(points, start, end)

        return points[:k]
