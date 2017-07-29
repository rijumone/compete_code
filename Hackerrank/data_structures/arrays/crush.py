with open('input07.txt', 'r') as inputFile:
	temp = inputFile.readline().split(" ")
	n = int(temp[0])
	q = int(temp[1])

	lst = {}

	# for k in range(n):
	# 	lst.append(0)

	for k in range(q):
		op = inputFile.readline().split(" ")
		a = int(op[0])-1
		b = int(op[1])-1
		# print "st"
		for l in range(a,b+1):
			# print "a+l"
			# print a+l
			if 0 <= a+l < len(lst):
				pass
			else:
				lst[a+l] = 0
		c = int(op[2])
		# index = a
		print lst
		# print a
		# print b
		for m in range(b-a+1):
			lst[m+a] += c
		# for m in lst[a:b+1]:
		# 	lst[index] += c
		# 	index += 1

	print max(lst.values())