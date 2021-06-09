'''
Module to implement a Binary tree
'''

class Node:
    
    data = None
    left, right = None, None
    
    def __init__(self, data) -> None:
        self.data = data

    def insert(self, value):
        '''
        Will insert passed value to either the
        left or right of the current Node.
        Will travel down if necessary.
        '''
        if value <= self.data:
            if not self.left:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self, value) -> bool:
        '''
        Will check whether passed value
        exists in any of the Nodes
        '''
        if value == self.data:
            return True
        elif value < self.data:
            if not self.left:
                return False
            else:
                return self.left.contains(value)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(value)

    def in_order_traversal(self, ):
        '''
        Given a graph:
          A
         | \
        B   C
        traverse nodes in the order: B, A, C  
        '''
        if self.left:
            self.left.in_order_traversal()
        
        print(f'{self.data} -> ', end=' ')
        
        if self.right:
            self.right.in_order_traversal()


    def pre_order_traversal(self, ):
        '''
        Given a graph:
          A
         | \
        B   C
        traverse nodes in the order: A, B, C  
        '''
        print(f'{self.data} -> ', end=' ')

        if self.left:
            self.left.in_order_traversal()
        
        if self.right:
            self.right.in_order_traversal()


    def post_order_traversal(self, ):
        '''
        Given a graph:
          A
         | \
        B   C
        traverse nodes in the order: B, C, A  
        '''

        if self.left:
            self.left.in_order_traversal()
        
        if self.right:
            self.right.in_order_traversal()

        print(f'{self.data} -> ', end=' ')




    def __repr__(self, ):
        
        return f'<d: {self.data}, l: {self.left}'\
            + f', r: {self.right}>'



if __name__ == '__main__':
    n = Node(15)
    n.insert(10)
    n.insert(9)

    n.insert(17)

    print(n.contains(10))
    print(n.contains(8))

    n.insert(8)

    print(n.contains(8))


    print(n)

    n.in_order_traversal()
    print('\n')
    n.pre_order_traversal()
    print('\n')
    n.post_order_traversal()
    print('\n')

    