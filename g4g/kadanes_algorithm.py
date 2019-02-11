in_lst = [1, 2, 3, -2, 5, -4, -6]

max_yet = 0
max_ending_here = 0

for item in in_lst:
	max_ending_here += item
	if max_ending_here < 0:
		max_ending_here = 0
	if max_yet < max_ending_here:
		max_yet = max_ending_here

print(max_yet)