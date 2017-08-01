l = raw_input()
while l != "":
	el = l.split(" ")
	if len(el) > 1:
		for e in el:
			print e
	l = raw_input()
