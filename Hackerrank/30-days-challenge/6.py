T = int(raw_input())

for k in range(0,T):
	string = raw_input()
	ctr = 0
	l1, l2 = "",""
	for m in string:
		if ctr % 2 == 0:
			l1 = l1 + m
		else:
			l2 = l2 + m
		ctr = ctr + 1

	print l1 + " " + l2