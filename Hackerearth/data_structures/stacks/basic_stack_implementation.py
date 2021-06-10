'''
LIFO
'''

class Node:
    data, next = None, None
    def __init__(self, value) -> None:
        self.data = value
    def __repr__(self):
        return f'{self.data} -> {self.next}'

class Stack:
    top = None

    def is_empty(self) -> bool:
        if self.top:
            return False
        return True

    def peek(self):
        '''
        returns top Node
        '''
        return self.top.data

    def push(self, value):
        '''
        new Node created and made top
        '''
        n = Node(value)
        n.next = self.top
        self.top = n

    def pop(self):
        '''
        remove top Node
        '''
        self.top = self.top.next

    def __repr__(self):
        return str(self.top)

if __name__ == '__main__':
    s = Stack()
    print(s.is_empty())
    s.push(5)

    print(s.peek())

    s.push(6)
    s.push(7)
    print(s.peek())
    
    print(s)

    s.pop()
    print(s)

    s.pop()
    print(s)

    print(s.is_empty())