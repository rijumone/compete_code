l = raw_input()
mainL = []
while l != "":
	el = l.split("=")
	mainL.append(el[1].strip(" "))
	prntStr = ""
	for k in mainL:
		prntStr += str(k) + " --> "
	prntStr += "NULL"
	print prntStr
	l = raw_input()




# NULL, data = 2
# 2 --> NULL, data = 3