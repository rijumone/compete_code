"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
	   self.data = data
	   self.next = next_node

 return back the head of the linked list in the below method. 

Input (stdin)
4 cases

3
1 2 3
0

3
1 2 3
1

3
1 2 3
2

5
4 3 2 5 1
2

Your Output (stdout)
23
1
Expected Output
23
13
12
4351
"""

class Node(object):
	
	def __init__(self, data=None, next_node=None):
	   self.data = data
	   self.next = next_node

	def __str__(self):
		return str(self.data) + " " + str(self.next)

def Delete(head, position):
	# if head is None:
	# 	return head
	
	if position == 0:
		return head.next

	current = head
	prev = Node(None,head)
	while position > 1:
		# print position
		prev = current
		# print prev
		current = current.next
		position -= 1
	# print prev
	# print current
	# prev.next = current.next
	current.next = current.next.next
	return head

ll = Node(4,Node(3,Node(2,Node(5,Node(1,None)))))

print ll

Delete(ll, 2)

print ll