score = input()

score_A = 0
score_B = 0

i = 0
while i < len(score) - 1:
	j = i + 1
	if score[i] == "A":
		score_A += int(score[j])
	else:
		score_B += int(score[j])

	i += 2

if score_A > score_B:
	print("A")
else:
	print("B")
