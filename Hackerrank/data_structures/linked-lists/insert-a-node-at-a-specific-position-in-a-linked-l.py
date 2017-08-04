"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
 

 return back the head of the linked list in the below method. 
"""
#This is a "method-only" submission.
#You only need to complete this method.


class Node(object):
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next = next_node

	def __str__(self):
		return str(self.data) + " " + str(self.next)




"""
def InsertNth(head, data, position):
	t = Node(data)
	if head is None:
		head = t
	else:
		l = head
		ctr = 0
		d = l.next
		while ctr < position:
			l = l.next
			d = l.next
			ctr += 1
		l.next = d
		t.next = l
	return head
"""  
  
ll = Node(3,Node(5,Node(4,Node(2))))
print ll
print InsertNth(ll,10,0)

ll = Node(3,Node(5,Node(4,Node(2))))
print ll
print InsertNth(ll,10,1)

def InsertNth(head, data, position):
	start = head # keep copy of starting node (head)
	if position == 0: # to be inserted at first position
		return Node(data,head) # create new node with next node as head node
	while position > 1: # looping from position to 1 (position number of times)
		head = head.next # iterating the list
		position -= 1 # decrementing position to reach 1 eventually
	head.next = Node(data, head.next) # when position reached 
	return start