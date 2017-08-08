
class Node(object):
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next = next_node

	def __str__(self):
		return str(self.data) + " " + str(self.next)


def ReversePrint(head):
	nl = Node(head)
	while not nl.next is None:
		nl.next = head.next
	print nl


ll = Node(2,Node(1,Node(4,Node(5,None))))

print ll

ReversePrint(ll)