'''
Goal is to know the X and Y coordinate of each node (leaf) in space,
so that they can be conveniently printed on the display.

Donald Knuth's TWO principles:
1. The edges of the tree should not cross each other.
2. All nodes at the same depth should be drawn on the same horizontal
    line.
'''
from pprint import pprint
from dataclasses import dataclass


@dataclass
class Tree:
    data: None
    left_child: None = None
    right_child: None = None
    x: None = None  # coordinates in
    y: None = None  # space to print


class DrawTree:
    def __init__(self, tree, depth: int) -> None:
        self.x = -1  # since it is unknown at this point of time
        self.y = depth  # integer to denote depth of tree at this point
        self.tree = tree  # pointer to the current tree root node
        _tmp_children = []
        for t in [tree.left_child, tree.right_child]:
            if not t:
                continue
            _tmp_children.append(t)
        self.children = [
            DrawTree(t, depth+1) for t in _tmp_children
        ]   # children are being inited as their own DrawTree classes
        # albeit with an additional depth since they are children

    def __repr__(self) -> str:
        return f'({self.x},{self.y})'


i = 0  # global counter being used as the "x" variable, then incremented
# at each node


def knuth_layout(tree, depth):
    global i
    '''Using in-order traversal
    left child, current, right child'''
    if tree.left_child:
        knuth_layout(tree.left_child, depth+1)
    tree.x = i
    tree.y = depth
    i += 1  # incrementing the global counter, since this x coordinate is
    # being "taken up"
    if tree.right_child:
        knuth_layout(tree.right_child, depth+1)


def main():
    t = Tree(
        left_child=Tree(data=1),
        right_child=Tree(data=3),
        data=2
    )
    dt = DrawTree(t, depth=0)
    print(dt)
    knuth_layout(t, 0)
    pprint(t)


if __name__ == '__main__':
    main()
