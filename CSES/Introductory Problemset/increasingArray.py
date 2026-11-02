n = int(input())

array = list(map(int, input().split()))


moves = 0
for i in range(len(array) - 1):
	j = i + 1
	if array[j] < array[i]:
		moves += array[i] - array[j]
		array[j] += array[i] - array[j]

print(moves)
