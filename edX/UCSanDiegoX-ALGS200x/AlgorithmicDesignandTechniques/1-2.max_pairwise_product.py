# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0
# find largest digit in list
index_1 = 0

for idx in range(n):
    if a[idx] > a[index_1]:
        index_1 = idx

# find 2nd largest digit in list
index_2 = 0 if index_1 != 0 else 1


for idx in range(n):
    if a[idx] > a[index_2]:
        if idx != index_1:
            index_2 = idx


result = a[index_1] * a[index_2]
# for i in range(0, n):
#     for j in range(i+1, n):
#         if a[i]*a[j] > result:
#             result = a[i]*a[j]

print(result)
