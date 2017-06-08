N = int(raw_input())

arr = raw_input().split(" ")

printStr = ""


for m in range(0,len(arr)):
	printStr = printStr + str(arr[len(arr)-m-1]) + " "

# for j in range(0,len(arrR)):
print printStr