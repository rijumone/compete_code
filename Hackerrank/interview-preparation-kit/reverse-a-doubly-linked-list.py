from dataclasses import dataclass


@dataclass
class DoublyLinkedListNode:
    data: int
    next: None
    prev: None


def main():
    ddln1 = DoublyLinkedListNode(1, None, None)
    ddln2 = DoublyLinkedListNode(2, None, None)
    ddln3 = DoublyLinkedListNode(3, None, None)
    ddln4 = DoublyLinkedListNode(4, None, None)

    ddln1.next = ddln2
    ddln2.next = ddln3
    ddln3.next = ddln4

    ddln4.prev = ddln3
    ddln3.prev = ddln2
    ddln2.prev = ddln1

    print(ddln1)

    reverse(ddln1)

    # print(ddln4)


def reverse(head):
    # import pdb
    # pdb.set_trace()
    if head is None:
        return head

    _tmp = head.next
    head.next = head.prev
    head.prev = _tmp

    reverse(head.prev)

    first = head
    while first.prev is not None:
        first = first.prev

    return first


if __name__ == '__main__':
    main()
