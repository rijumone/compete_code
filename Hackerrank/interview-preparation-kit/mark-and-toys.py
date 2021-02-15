def main(prices):

    k = 140

    # need to sort the list and then
    # count first n elements which
    # sum to <= k

    print(prices)
    # prices = bubble_sort(prices)
    prices = selection_sort(prices)
    print(prices)

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
    def merge(lst_a, lst_b):
        # both lists in args are individually sorted
        # just merge them and return one list
        pass
    len_lst = len(lst)
    return lst


if __name__ == '__main__':
    main(prices=[int(_) for _ in '1 12 5 111 200 1000 10'.split(' ')])
    # prices = []
    # from random import randrange
    # for _ in range(99999):
    #     prices.append(randrange(9999))
    # main(prices=prices)
