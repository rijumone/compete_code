def binary_search(low, high, x, lst):
    # import pdb
    # pdb.set_trace()
    if high < low:
        # print(high, low)
        return -1
    mid = (low + high) // 2
    if x == lst[mid]:
        return mid
    elif x > lst[mid]:
        low = mid + 1
        return binary_search(low, high, x, lst)
    else:  # x < lst[mid]
        high = mid - 1
        return binary_search(low, high, x, lst)


def main(lst, x):
    print(lst, x)
    # define and init low and high pointers
    low = 0
    high = len(lst) - 1

    idx = binary_search(low, high, x, lst)

    print(idx)


if __name__ == '__main__':
    # given a list,
    # return index of x if exists
    # else return -1
    lst = [-2, -1, 5, 7, 13, 17, 18]

    main(lst, x=7)
    # expected: 3

    main(lst, x=17)
    # expected: 5

    main(lst, x=-1)
    # expected: 1

    main(lst, x=99)
    # expected: -1

    main(lst, x=-99)
    # expected: -1
