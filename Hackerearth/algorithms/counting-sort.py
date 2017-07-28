N = int(raw_input())
tL = raw_input().split(" ")
iL = [int(i) for i in tL]

oD = {}

for k in iL:
	if k in oD:
		oD[k] = oD[k] + 1
	else:
		oD[k] = 1


for k in oD:
	print "%d %d" % (k,oD[k])