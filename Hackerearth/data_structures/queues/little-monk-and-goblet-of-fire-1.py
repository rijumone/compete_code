# let's implement a list for this

# 5
# E 1 1
# E 2 1
# E 1 2
# D
# D

Q = int(raw_input())

mainList = []

lastSchoolPos = {}

for x in range(0,Q):
	# print x
	op = raw_input()
	opList = op.split(" ")
	

	# print opList
	if opList[0] == "E":
		insertPos = len(mainList)
		# print insertPos
		for k in range(0,len(mainList)):
			if mainList[k][0] == int(opList[1]):
				insertPos = k + 1
		# print insertPos
		mainList.insert(insertPos,[int(opList[1]),int(opList[2])])
		# print mainList
	else:
		print(str(mainList[0][0]) + " " + str(mainList[0][1]))
		del mainList[0]