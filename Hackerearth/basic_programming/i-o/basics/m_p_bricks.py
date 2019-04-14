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
total_bricks = 3694

# generate qudratic equation
a = 1
b = 1
c = -1 * (total_bricks * 2) / 3

# import complex math module
import cmath
import math

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
soln_lst = []
soln_lst.append((-b-cmath.sqrt(d))/(2*a))
soln_lst.append((-b+cmath.sqrt(d))/(2*a))

n = math.ceil([_.real for _ in soln_lst if _.real >= 0][0])

# now n is the number of rounds for m and p

# m is the number of bricks laid that round
m = 3 + (n-1)*3

# out of m bricks, n has been laid by P

if m > n:
	print('M')
else:
	print('P')