# m_p_bricks.py
"""
helper matrix
+-------------------------------+
| i | M | P | bricks | bricks c |
+---+---+-----------------------+
| 1 | 1 | 2 | 3      | 3        |
| 2 | 2 | 4 | 6      | 9        |
| 3 | 3 | 6 | 9      | 18       |
| 4 | 4 | 8 | 12     | 30       |
| 5 | 5 | 10| 15     | 45       |
+---+---+---+--------+----------+

"""
total_bricks = int(input())
# total_bricks = 13
# total_bricks = 4321

# generate qudratic equation
a = 1
b = 1
c = -1 * (total_bricks * 2) / 3
# print(c)
# import complex math module
import cmath
import math

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
soln_lst = []
soln_lst.append((-b-cmath.sqrt(d))/(2*a))
soln_lst.append((-b+cmath.sqrt(d))/(2*a))
# print(soln_lst)
_n = math.ceil([_.real for _ in soln_lst if _.real >= 0][0])
# print(n)
# now n is the number of rounds for m and p
# import pdb; pdb.set_trace()
# calculate the max total of bricks altogether possible
max_total_bricks = (_n/2)*((3*_n)+3)

# m is the upper limit of number of bricks laid that round
m = 3 + (_n-1)*3

# deficit is the bricks we are falling short
deficit = max_total_bricks - total_bricks
# print(deficit)

actual_bricks_laid_last_round = m - deficit
if actual_bricks_laid_last_round <= _n:
	print('Patlu')
else:
	print('Motu')
