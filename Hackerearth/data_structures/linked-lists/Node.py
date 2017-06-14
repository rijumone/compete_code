class Node:
	def __init__(self,data=None,next_node=None):
		self.data = data
		self.next_node = next_node

	def get_next(self):
		return self.next_node

	def set_next(self,next_node):
		self.next_node = next_node

	def get_data(self):
		return self.data


class LinkedList(object):
	def __init__(self, head=None):
		self.head = head

	
	

n = Node("a")
m = Node("b", n )

# print n.get_data()
# print m.get_next().get_data()
# print m.get_data()


mainList = [2,5,2,6,8,3,5]

for k in mainList:
	n = Node(k) 

# traverse
# highest
# find
# merge