# Uses python3
# import sys
from loguru import logger
from math import sqrt


def optimal_summands(n):
    summands = []
    '''
    sum_until_now = 0
    _ctr = 0
    while sum_until_now < n:
        _ctr += 1
        # logger.info(f'{sum(summands)}, {summands}')
        remaining = n - sum(summands)
        summands.append(min(_ctr, remaining))
        sum_until_now = sum(summands)

    last_elem = summands[-1]
    if last_elem in summands[:-1]:
        del summands[-1]
        summands[-1] += last_elem
    '''
    e, f = solve_polynomial(a=1, b=2, c=((-2 * n) + 2))
    logger.info(f'{e} {f}')
    if e > 1:
        uptil = int(e)
    else:
        uptil = int(f)
    for _ in range(1, uptil):
        # print(_)
        summands.append(_)
    # import pdb
    # pdb.set_trace()
    # logger.info(sum(summands))
    summands.append(n - sum(summands))
    return summands


def solve_polynomial(a, b, c):
    i = b**2-4 * a * c
    d = sqrt(i)
    e = (-b + d) / 2 * a
    f = (-b-d) / 2 * a
    return e, f


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n = int(input)
    n = 19
    summands = optimal_summands(n)
    print(summands)
    print(len(summands))
    print(sum(summands))
    assert sum(summands) == n
    # for x in summands:
    #     print(x, end=' ')
