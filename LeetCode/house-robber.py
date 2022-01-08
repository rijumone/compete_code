'''
https://leetcode.com/problems/house-robber/
'''
from time import perf_counter
from loguru import logger

mem_dct = {}


def max_at_idx(lst, i):
    '''
    Return max value that can be
    extracted from lst, starting from
    i index.

    Args:
        lst (list)
        i (int): index
    Returns:
        value (int)
    '''
    # check for memoization
    if i in mem_dct:
        return mem_dct[i]
    # base case
    if i >= len(lst):
        # if requested index does not
        # exist in the list,
        # value has to be 0
        return 0
    # make choice
    choice_1 = (lst[i] + max_at_idx(lst, i+2))
    choice_2 = max_at_idx(lst, i+1)

    value = max(choice_1, choice_2)
    mem_dct[i] = value
    return value


def main(lst):
    value = max_at_idx(lst, 0)
    print(value)


if __name__ == '__main__':
    # lst = [1, 2, 3, 1, ]
    # lst = [2, 7, 9, 3, 1]
    lst = [8, 1, 7, 9, 7, 2, 1, 5, ]
    # lst = [183, 219, 57, 193, 94, 233, 202,
    #        154, 65, 240, 97, 234, 100, 249, 186,
    #        66, 90, 238, 168, 128, 177, 235, 50,
    #        81, 185, 165, 217, 207, 88, 80, 112,
    #        78, 135, 62, 228, 247, 211]
    started = perf_counter()
    main(lst)
    print(perf_counter() - started)
