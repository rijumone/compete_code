n = int(raw_input())
strLst = []
for k in range(n):
	strLst.append(raw_input())

q = int(raw_input())

for k in range(q):
	comp = raw_input()
	ctr = 0
	for m in strLst:
		if comp == m:
			ctr += 1
	print ctr
