"""
l = raw_input()
mainL = []
while l != "":
	el = l.split("=")
	mainL.append(el[1].strip(" "))
	prntStr = ""
	for k in mainL:
		prntStr += str(k) + " --> "
	prntStr += "NULL"
	print prntStr
	l = raw_input()


# NULL, data = 2
# 2 --> NULL, data = 3

"""

"""
 Insert Node at the end of a linked list 
 head pointer input could be None as well for empty list
 Node is defined as
"""
class Node(object):

	def __init__(self, data=None, next_node=None):
	   self.data = data
	   self.next = next_node

	# return back the head of the linked list in the below method


def Insert(head, data):
	t = Node(data)
	if head is None:
		head = t
	else:
		l = head
		while not l.next is None:
			l = l.next
		l.next = t
	return head