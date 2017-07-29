temp = raw_input().split(" ")
length = int(temp[0])
n = int(temp[1])

lst = [int(k) for k in raw_input().split(" ")]

if n > length:
	firstElement = n-length
else:
	firstElement = n

for k in lst[firstElement:len(lst)]:
	print k,
for k in lst[0:firstElement]:
	print k,