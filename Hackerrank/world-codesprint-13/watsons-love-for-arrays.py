# watsons-love-for-arrays.py

#!/bin/python3

import os
import sys

# Complete the howManyGoodSubarrays function below.
def howManyGoodSubarrays(A, m, k):
  # Return the number of good subarrays of A.
  good_arr_cnt = 0
  # print(1111111111)
  for i, i_v in enumerate(A):
    # print(i_v)
    prod = 1
    for j, j_v in enumerate(A):
      # print(j)
      # print(i)
      if j >= i:
        prod = prod * j_v
        # print(prod)
        # print(m)
        # print(k)
        # print('=======')
        if prod % m == k:
          good_arr_cnt += 1
          # print('good_arr_cnt')
          # print(good_arr_cnt)
  return good_arr_cnt



if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  t = int(input())

  for t_itr in range(t):
    nmk = input().split()

    n = int(nmk[0])

    m = int(nmk[1])

    k = int(nmk[2])

    A = list(map(int, input().rstrip().split()))

    result = howManyGoodSubarrays(A, m, k)
    # print(result)
    fptr.write(str(result) + '\n')

  fptr.close()


# 1
# 5 3 0
# 1 0 3 0 4