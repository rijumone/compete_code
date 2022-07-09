'''
Input:
5
2 3 9 2 2

Output:
1
'''
from loguru import logger


def brute_force(lst):
    '''
    Given a list of integers, determine
    whether list contains a "majority element"
    i.e. an item which occurs greater than n/2 times.

    Args:
        lst (list)
    '''
    _dct = {}
    for item in lst:
        if item not in _dct:
            _dct[item] = 0
        _dct[item] += 1
    for _k, _v in _dct.items():
        if _v > len(lst) // 2:
            return 1
    return 0


def divide_and_conquer(lst):
    '''
    Given a list of integers, determine
    whether list contains a "majority element"
    i.e. an item which occurs greater than n/2 times.

    Args:
        lst (list)
    '''
    def majority_elem(lo, hi):
        '''
        Determine the majority element
        in the list between passed slices.
        Args:
            lo (int): starting index
            hi (int): ending index
        '''
        print(f'List received: {[lst[_] for _ in range(lo, hi+1,)]}')
        # tacking the base case first,
        # the only element in an array of len = 1,
        # is the majority element
        if lo == hi:
            print(f'lo == hi; lst[lo] = {lst[lo]} ')
            return lst[lo]

        # DIVIDE lst into left and right halves
        # get their majority_elem()
        mid = (hi - lo) // 2 + lo
        left_m_e = majority_elem(lo, mid)
        print(f'left_m_e = {left_m_e}')
        right_m_e = majority_elem(mid + 1, hi)
        print(f'right_m_e = {right_m_e}')

        # logger.info(right_m_e)
        # If majority_elem() is the same for both
        # left and right halves, return it
        if left_m_e == right_m_e:
            print(f'left_m_e == right_m_e = {left_m_e}')
            return left_m_e

        # otherwise, count each element in the list
        left_cnt = sum(1 for i in range(lo, hi + 1)
                       if lst[i] == left_m_e)
        right_cnt = sum(1 for i in range(lo, hi + 1)
                        if lst[i] == right_m_e)

        # return the one with most count
        return left_m_e if left_cnt > right_cnt \
            else right_m_e

    return majority_elem(0, len(lst)-1)


if __name__ == '__main__':
    # _o = brute_force('2 3 9 2 2'.split(' '))
    # _o = divide_and_conquer('2 3 9 2 2'.split(' '))
    # _o = divide_and_conquer('1 2 3 4'.split(' '))
    _o = divide_and_conquer(
        [int(_) for _ in '1 3 3 4 4 7 7 9 9 9'.split(' ')])
    print(_o)
