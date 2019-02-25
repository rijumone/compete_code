# designer-pdf-viewer.py

"""
sample input:

1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
abc

sample output:

9

"""

alphabet_height_lst = input().split(' ')
alphabet_height_dict = {}
ctr = 0
for k in [
	'a', 'b', 'c', 'd',
	'e', 'f', 'g', 'h',
	'i', 'j', 'k', 'l',
	'm', 'n', 'o', 'p',
	'q', 'r', 's', 't',
	'u', 'v', 'w', 'x',
	'y', 'z', 
	]:
	alphabet_height_dict[k] = int(alphabet_height_lst[ctr])
	ctr += 1
input_str = input()
tallest_letter = 0
for l in input_str:
	if tallest_letter < alphabet_height_dict[l]:
		tallest_letter = alphabet_height_dict[l]
area = tallest_letter * len(input_str)
print(area)