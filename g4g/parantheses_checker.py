in_string = "(())"

"""
closer_dct = {
	"{": "}",	
	"(": ")",	
	"[": "]",	
}

next_closer_str = ""

u = False

for i in range(len(in_string)):
	print('--------\nitem:', in_string[i])
	if i == 0 and in_string[i] not in closer_dct:
		print('unbalanced')
		u = True
		break
	if in_string[i] in closer_dct:
		next_closer = closer_dct[in_string[i]]
		next_closer_str += next_closer
		# print('next_closer_str(opener): ', next_closer_str)
	else:
		# print('next_closer: ', next_closer)
		# print('next_closer_str: ', next_closer_str)
		if in_string[i] != next_closer:
			print('unbalanced')
			u = True
			break
		else:
			if len(next_closer_str) == 0:
				print('unbalanced')
				u = True
				break	
			next_closer_str = next_closer_str[:-1] if len(next_closer_str) > 1 else next_closer_str
			print('next_closer_str: ', next_closer_str)
			next_closer = next_closer_str[-1]
			next_closer_str = "" if len(next_closer_str) == 1 else next_closer_str
			# print('next_closer: ', next_closer)

if not u:
	print('balanced')
"""

class Stack:
	stack = ""
	def __init___(self):
		pass
	def push(self, element):
		pass
	def pop(self, element):
		pass