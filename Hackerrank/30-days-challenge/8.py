N = int(raw_input())

mainDict = {}
for k in range(0,N):
	entry = raw_input().split(" ")
	mainDict[entry[0]] = entry[1]


temp = raw_input()
while not temp == "":
	if temp in mainDict:
		print temp + "=" + mainDict[temp]
	else :
		print "Not found"
	temp = raw_input()