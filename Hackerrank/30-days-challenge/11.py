n = 6

mainList = []

for k in range(0,n):
	mainList.append(raw_input().split(" "))

# print mainList
	

def getElements(init_x,init_y):
	sumList = []
	for x in range(0,3):
		# print mainList[init_x]
		# print mainList[init_x][init_y]
		# print mainList[init_x][init_y + x]
		sumList.append(int(mainList[init_x][init_y + x]))

	sumList.append(int(mainList[init_x + 1][init_y + 1]))

	for x in range(0,3):
		sumList.append(int(mainList[init_x + 2][init_y + x]))

	return sum(sumList)

# print getElements(3,2)

sums = []

for k in range(0,n-2):
	for m in range(0,n-2):
		sums.append(getElements(k,m))


print max(sums)	