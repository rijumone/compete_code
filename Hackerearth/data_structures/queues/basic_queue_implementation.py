'''
FIFO
'''

class Node:
    data, next = None, None
    def __init__(self, value) -> None:
        self.data = value
    def __repr__(self):
        return f'{self.data} -> {self.next}'

class Queue:
    # pointers
    head = None # remove from head
    tail = None # add to tail
    
    def is_empty(self):
        if self.head:
            return True
        return False

    def peek(self):
        if self.head:
            return self.head.data
    
    def add(self, value):
        n = Node(value)
        if self.tail:
            # here the Node object is being set
            self.tail.next = n
        # update the tail pointer
        self.tail = n
        if not self.head:
            # in case Queue is empty
            self.head = n

    def remove(self):
        if not self.head:
            return
        data = self.head.data
        self.head = self.head.next
        if not self.head:
            # in case Queue becomes empty
            # update the tail pointer
            self.tail = None
        return data

    def __repr__(self) -> str:
        return str(self.head)

if __name__ == '__main__':
    q = Queue()
    q.add(5)
    q.add(6)

    print(q)
    print(q.peek())
    print(q.remove())
    print(q)

    q.add(7)
    q.add(8)

    print(q)