total_bricks = int(input())
a, b, c = 1, 1, -1 * (total_bricks * 2) / 3
import cmath
import math
d = (b**2) - (4*a*c)
pos_soln = (-b-cmath.sqrt(d))/(2*a)
neg_soln = (-b+cmath.sqrt(d))/(2*a)
if pos_soln.real > neg_soln.real:
	_n = pos_soln.real
else:
	_n = neg_soln.real
max_total_bricks = (_n/2)*((3*_n)+3)
m = 3 + (_n-1)*3
deficit = max_total_bricks - total_bricks
actual_bricks_laid_last_round = m - deficit
if actual_bricks_laid_last_round <= _n:
	print('Patlu')
else:
	print('Motu')
