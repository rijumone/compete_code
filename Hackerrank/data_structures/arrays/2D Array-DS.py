mainList = []

for k in range(6):
	mainList.append([int(k) for k in raw_input().split(" ")])


maxSum = -99999999999

def findSum(i,j):
	isum = 0
	for k in range(3):
		isum += mainList[i][j+k]
	isum += mainList[i+1][j+1]
	for k in range(3):
		isum += mainList[i+2][j+k]

	return isum

for l in range(4):
	for m in range(4):
		comp = findSum(l,m)
		# print comp
		if maxSum < comp:
			maxSum = comp

print maxSum