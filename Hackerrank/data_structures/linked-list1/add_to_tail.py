def insertNodeAtTail(head, data):
	node = SinglyLinkedListNode(data)
	if head is None:
		head = node
	else:
		new_head = head
		while new_head.next is not None:
			new_head = head
			new_head.next = node
	return head