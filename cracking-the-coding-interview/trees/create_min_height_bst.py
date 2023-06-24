'''
GIVEN A SORTED ARRAY OF INTEGERS, INSERT THEM INTO A BINARY
SEARCH TREE WITH MINIMUM HEIGHT AND RETURN THE ROOT
'''

from dataclasses import dataclass


@dataclass
class Node:
    body: int
    left: None = None
    right: None = None

    def __repr__(self, ):
        return f'<Node\n\tbody={self.body}\tleft={self.left}\tright={self.right}>'


def main(lst, parent, parent_idx):
    ''''''
    print(f'==== {lst}')
    
    print(f'parent_idx_value: {lst[parent_idx]}')
    # pick left parent
    
    lefts = lst[:parent_idx]
    if lefts:
        left_idx = int(len(lefts)/2)
        print(f'lefts: {lefts}')
        print(f'left_idx_value: {lefts[left_idx]}')
        parent.left = Node(lefts[left_idx])
        main(lefts, parent.left, parent_idx=int(len(lefts)/2))
    
    print(f'lst: {lst}')
    rights = lst[parent_idx+1:]
    if rights:
        right_idx = int(len(rights)/2)
        print(f'rights: {rights}')
        print(f'right_idx_value: {rights[right_idx]}')
        parent.right = Node(rights[right_idx])
        main(rights, parent.right, parent_idx=int(len(rights)/2))
    
    print(f'parent: {parent}')
    return parent
    

if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7, 8]
    parent_idx = int(len(lst)/2)
    parent = Node(lst[parent_idx])
    parent = main(lst, parent, parent_idx=int(len(lst)/2))
    # import pdb;pdb.set_trace()
