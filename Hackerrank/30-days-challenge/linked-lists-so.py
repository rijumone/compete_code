# linked list implement krne k lie humesha at least 2 class chye honge
# ek node and ek linkedlist khud

class Node(object):
    def __init__(self, data, next=None):
        # node ko init krne k lie kewal 2 attributes chye
        self.data = data # ek data 
        self.next = next # or ek next member
    def __str__(self):
        # ek function uska data return krne k lie
        return str(self.data)

class LinkedList(object):
    def __init__(self):
        # linkedlist ko init krne k lie ek hi attribute chye
        self.head = None # head k kiska ref saved hoga
    def append(self, data):
        # ab aate h append p
        if not self.head: # pehla hi element h
            n = Node(data) # node k naya object h "n" mein, usko data s init kr dia, "n" k next None h abi
            self.head = n # linkedlist k head m current element "n" save kr dia
            return
        else:
            n = self.head # pehla element ni h, isse phle koi aya ta
            while n.next != None: # akhir wale element tk phchne k lie
                n = n.next # "n" m akhir wala element h abi
            new_node = Node(data) # ek nye node m apna data append kr dia
            n.next = new_node; # akhir wale elemt 
            return

    def isEmpty(self):
        return not self.head

    def printList(self):
        n = self.head

        while n:
            print str(n)
            n = n.next

ll = LinkedList()
elems = [1, 2, 3, 54, 6]
for elem in elems:
    ll.append(elem)

ll.printList()