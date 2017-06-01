# the-football-fest-6

# 1
# 10 23
# P 86
# P 63
# P 60
# B
# P 47
# B
# P 99
# P 9
# B
# B

from basic_stack_implementation import Stack

N = int(raw_input())
# N = 1

for k in range(0,N):
	temp = raw_input()
	tempList = temp.split(" ")
	n = int(tempList[0])
	s = Stack()
	s.push(int(tempList[1]))
	# initId = 
	for k in range(0,n):
		temp = raw_input()
		tempList = temp.split(" ")
		print "input"
		print tempList[0]
		if tempList[0] == "P":
			s.push(int(tempList[1]))
		else:
			s.pop()
		print "last"
		print s.peek()

	print s.peek()