'''
Ref: https://www.hackerearth.com/practice/data-structures/queues/basics-of-queues/practice-problems/algorithm/disk-tower-b7cc7a50/
'''
'''
from dataclasses import dataclass


@dataclass
class Item:
    data: None
    next: None = None


class Queue:
    head = None  # remove from here
    tail = None  # add to here

    def enqueue(self, data):
        item = Item(data)
        if self.tail:
            self.tail.next = item
        self.tail = item
        if self.head is None:
            self.head = self.tail

    def dequeue(self,):
        self.tail = None

    def peek(self,):
        return self.head.data
'''


def main(lst):
    # len_lst = len(lst)
    sorted_lst = sorted(lst, reverse=True)

    # q = Queue()
    # for _ in lst:
    #     q.enqueue(_)

    # print(q.head)
    items_received = []
    tower_lst = []
    reserve = []
    for i, item in enumerate(lst):
        items_received.append(item)
        # print(f'items_received: {items_received}')

        for _ in sorted_lst:
            if _ not in tower_lst:
                looking_for = _
                break
        # print(f'looking_for: {looking_for}')
        # import pdb
        # pdb.set_trace()
        reserve.append(item)
        if looking_for in reserve:
            tower_lst += reserve
            reserve_reverse_sorted = sorted(reserve, reverse=True)
            # print(f'reserve_reverse_sorted: {type(reserve_reverse_sorted)}')
            print(' '.join([str(_) for _ in reserve_reverse_sorted]))
            reserve = []
            # print(f'tower_lst: {tower_lst}')

        # print('=======================')


if __name__ == '__main__':
    input()
    lst = [int(_) for _ in input().split(' ')]

    main(lst)
    '''
    expected output:
     
    5 4
    
    
    3 2 1
    '''
