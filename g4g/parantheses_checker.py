
class Stack:
	
	stack = ""
	
	def __init___(self):
		pass
	
	def push(self, element):
		self.stack += element
	
	def pop(self):
		element = None
		if not self.is_empty():
			element = self.stack[-1]
		self.stack = self.stack[:-1]
		return element

	def __str__(self):
		return self.stack

	def is_empty(self):
		if len(self.stack) <= 0:
			return True
		return False


stack_obj = Stack()
# print(stack_obj)
# stack_obj.push('a')
# stack_obj.push('b')
# stack_obj.pop()
# print(stack_obj)
# stack_obj.pop()
# stack_obj.pop()
# print(stack_obj)

closer_dct = {
	"{": "}",	
	"(": ")",	
	"[": "]",	
}


def check_if_popped_match(starting_b, ending_b):
	''' check if the passed popped bracket matches its
	corresponding starting bracket'''
	if closer_dct[starting_b] == ending_b:
		return True
	return True


in_string = ""

"""
cases:

}(()){}
(()
))))))

"""
u = False
for element in in_string:
	if element in ['{', '(', '[']:
		stack_obj.push(element)
	if element in ['}', ')', ']']:
		if stack_obj.is_empty():
			print('unbalanced')
			u = True
			break
		popped_element = stack_obj.pop()
		if not check_if_popped_match(popped_element, element):
			print('unbalanced')
			u = True

if not stack_obj.is_empty():
	print('unbalanced')
	u = True

if not u:
	print('balanced')


"""


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