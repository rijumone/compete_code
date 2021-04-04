import time


def main(prices):

    k = 999999

    # need to sort the list and then
    # count first n elements which
    # sum to <= k

    print(prices)
    # prices = bubble_sort(prices)
    # prices = selection_sort(prices)
    prices = merge_sort(prices)
    print(f'prices: {prices}')

    sum_till_now = 0
    _ctr = 0
    for _ in prices:
        if sum_till_now >= k:
            break
        # import pdb
        # pdb.set_trace()
        sum_till_now += _
        _ctr += 1

    print(sum_till_now)
    if sum_till_now > k:
        print(_ctr - 1)
    else:
        print(_ctr)


def bubble_sort(lst):
    len_lst = len(lst)
    for i in range(len_lst):
        for j in range(len_lst - (i + 1)):
            if lst[j] > lst[j+1]:
                _tmp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = _tmp

    return lst


def selection_sort(lst):
    len_lst = len(lst)
    for i in range(len_lst):
        lowest_idx = i
        for j in range(i, len_lst):
            if lst[j] < lst[lowest_idx]:
                lowest_idx = j
        _tmp = lst[lowest_idx]
        lst[lowest_idx] = lst[i]
        lst[i] = _tmp

    return lst


def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    middle = len(lst) // 2
    left_half = lst[:middle]
    right_half = lst[middle:]

    # recursive call on each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # iterators for traversal
    i_l = 0
    i_r = 0

    i = 0

    # while there are still items remaining
    # in both lists for traversal
    while i_l < len(left_half) and i_r < len(right_half):
        if left_half[i_l] < right_half[i_r]:
            # the left halves value is smaller
            # it needs to go in the original list

            lst[i] = left_half[i_l]
            # move the iterator forward
            i_l += 1
        else:
            # the right halves value is smaller
            # or is equal, in either case:
            # it needs to go in the original list

            lst[i] = right_half[i_r]
            # move the iterator forward
            i_r += 1

        # irrespective of either of the above cases
        # move the iterator forward
        # for the original list
        i += 1

    # now for items remaining
    # in the left_half
    while i_l < len(left_half):
        # p.s: this condition is the same as
        # the first part of the above condition
        lst[i] = left_half[i_l]
        i += 1
        i_l += 1

    # in the right_half
    while i_r < len(right_half):
        # p.s: this condition is the same as
        # the second part of the above condition
        # print(lst, i)
        # print(right_half, i_r)
        lst[i] = right_half[i_r]
        i += 1
        i_r += 1

    # either of the conditions above would
    # evaluate to true
    # not both

    return lst


if __name__ == '__main__':
    # main(prices=[int(_) for _ in '1 12 5 111 200 1000 10'.split(' ')])
    start_ts = time.time()
    prices = []
    from random import randrange
    for _ in range(9):
        prices.append(randrange(99))
    main(prices=prices)
    print(time.time() - start_ts)
