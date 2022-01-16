'''
https://leetcode.com/problems/sum-of-two-integers/
'''


def main(a, b):
    pass


def sum_bit(a, b):
    '''
    Calculate sum of binary digits passed in args.
    Args:
        a (int): binary integer, 0 or 1 only
        b (int): binary integer, 0 or 1 only
    Returns:
        sum (int): binary integer, 0 or 1 only
        carryover (int): binary integer, 0 or 1 only
    '''
    for bit in (a, b):
        if bit not in (0, 1):
            raise ValueError(f'{bit} is not a bit.')
    if (a, b) == (0, 0):
        return 0, 0
    if (a, b) == (0, 1):
        return 1, 0
    if (a, b) == (1, 0):
        return 1, 0
    if (a, b) == (1, 1):
        return 0, 1


if __name__ == '__main__':

    assert sum_bit(0, 0) == (0, 0)
    assert sum_bit(0, 1) == (1, 0)
    assert sum_bit(1, 0) == (1, 0)
    assert sum_bit(1, 1) == (0, 1)
    a = 1
    b = 2

    o = main(a, b)
    assert o == 3

class TenBitNumber:
    tenth_place = None
'''
Decimal
053
10^2 * 0 
10^1 * 5 
10^0 * 3

253
10^2 * 2
10^1 * 5 
10^0 * 3

306
(10^2 * 0) + (10^2 * 2) + (10^2 * 1)(c) = 10^2 * 3
(10^1 * 5) + (10^1 * 5) = 10^1 * 10 = (10^1 * 0) + (10^2 * 1)(c)
(10^0 * 3) + (10^0 * 3) = 10^0 * 6

'''
'''
Binary
53
2^6 * 0
2^5 * 1
2^4 * 1
2^3 * 0
2^2 * 1
2^1 * 0
2^0 * 1

15
2^6 * 0
2^5 * 0
2^4 * 0
2^3 * 1
2^2 * 1
2^1 * 1
2^0 * 1

68 (calc)
2^6 * 1
2^5 * 0
2^4 * 0
2^3 * 0
2^2 * 1
2^1 * 0
2^0 * 0

68 (actual)
2^6 * 1
2^5 * 0
2^4 * 0
2^3 * 0
2^2 * 1
2^1 * 0
2^0 * 0

1000
2^10 * 0
2^9  * 1
2^8  * 1
2^7  * 1
2^6  * 1
2^5  * 1
2^4  * 0
2^3  * 1
2^2  * 0
2^1  * 0
2^0  * 0


'''
