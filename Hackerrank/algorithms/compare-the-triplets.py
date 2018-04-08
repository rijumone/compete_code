# compare-the-triplets.py

"""
Sample Input
5 6 7
3 6 10

Sample Output
1 1 
"""

#!/bin/python3

import os
import sys

#
# Complete the solve function below.
#
def solve(a0, a1, a2, b0, b1, b2):
    a_final = 0
    b_final = 0
    
    if a0 > b0:
        a_final += 1
    elif b0 > a0:
        b_final += 1
    
    if a1 > b1:
        a_final += 1
    elif b1 > a1:
        b_final += 1
    
    if a2 > b2:
        a_final += 1
    elif b2 > a2:
        b_final += 1
    
    return (a_final, b_final)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    a0A1A2 = input().split()
    a0 = int(a0A1A2[0])
    a1 = int(a0A1A2[1])
    a2 = int(a0A1A2[2])
    b0B1B2 = input().split()
    b0 = int(b0B1B2[0])
    b1 = int(b0B1B2[1])
    b2 = int(b0B1B2[2])
    result = solve(a0, a1, a2, b0, b1, b2)
    # print(' '.join(map(str, result)))
    f.write(' '.join(map(str, result)))
    f.write('\n')
    f.close()
