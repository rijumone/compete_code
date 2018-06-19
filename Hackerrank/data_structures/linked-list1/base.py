# base.py

class Node:

	def __init__(self, node_data):
		self.data = node_data
		self.next = None

class LL:

	def __init__(self):
		self.head = None
		self.tail = None

	def insert_node(self, node_data):
		node = Node(node_data)

		if not self.head:
			self.head = node
		else:
			self.tail.next = node # updating previous node's tail

		self.tail = node

if __name__ == '__main__':

	ll_obj = LL()
	for item in ['a', 'b', 'c', 'd']:
		ll_obj.insert_node(item)


	ll_obj_ = ll_obj.head
	while ll_obj_ is not None:
		print(ll_obj_.data)
		ll_obj_ = ll_obj_.next
