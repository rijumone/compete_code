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
	"""
	head will either contain "None" 
	meaning the LinkedList is empty
	or head of the existing LinkedList
	"""
	t = Node(data)
	"""
	create a new Node in any case
	"""
	if head is None:
		head = t
		"""
		head is the newly created Node
		"""
	else:
		l = head
		while not l.next is None:
			l = l.next
			"""
			looping through the LinkedList until
			current node's next element is "None"
			"""
		l.next = t
		"""
		set the newly created Node as the next element
		"""
		"""
		in this case head to be returned is the
		same head received as the first parameter
		of the Insert function
		"""
	return head