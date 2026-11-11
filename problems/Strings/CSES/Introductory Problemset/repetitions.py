string = input()

start = 1
count = 1

i = 1

while i < len(string):
	j = i - 1

	if string[i] == string[j]:
		count += 1
	else:
		count = 1

	start = max(start, count)

	i += 1

print(start)
