'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Ref: https://leetcode.com/problems/first-bad-version/
'''
from asyncio.events import AbstractEventLoopPolicy
from loguru import logger
api_counter = 0


def main(n):
    # return brute_force(n)
    return efficient(n)


def brute_force(n):
    for i in range(1, n+1):
        if is_bad_version(i):
            return i


def efficient(n):
    if n == 1:
        return 1
    begin = 1
    end = n
    while begin < end:
        mid = begin+(end-begin)/2
        if is_bad_version(mid):
            end = mid
        else:
            begin = mid+1
    return int(begin)


def is_bad_version(q):
    global api_counter
    api_counter += 1
    logger.debug(api_counter)
    if q >= fbv:
        return 1
    return 0


if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    n = 99
    fbv = 1
    assert main(n) == fbv
    logger.info(api_counter)
    logger.debug(perf_counter() - start)
