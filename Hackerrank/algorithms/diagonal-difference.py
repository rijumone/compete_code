#!/bin/python3

import os
import sys

#
# Complete the diagonalDifference function below.
#
def diagonalDifference(a):
    #
    # Write your code here.
    #
    # get both diagonals first
    sum_diag_0 = 0
    sum_diag_1 = 0

    for i,row in enumerate(a):
        # print(row)
        # print(i)
        sum_diag_0 += row[i]
        sum_diag_1 += row[len(a) - 1 - i]
    return abs(sum_diag_0 - sum_diag_1)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)

    # print(str(result) + '\n')
    f.write(str(result) + '\n')

    f.close()
