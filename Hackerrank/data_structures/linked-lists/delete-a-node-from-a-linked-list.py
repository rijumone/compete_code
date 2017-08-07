"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
	if head is None:
		return head
	
	current = head

	while position > 1:
		current = current.next
		position -= 1

	nex = current.next
	current.next = nex.next
	return head