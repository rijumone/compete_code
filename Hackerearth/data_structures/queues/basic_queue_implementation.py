class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def printQ(self):
        return self.items



q = Queue()

q.enqueue(1)
q.enqueue(3)
q.enqueue(5)
q.enqueue(7)


print q.printQ()

q.dequeue()

print q.printQ()