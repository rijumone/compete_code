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
    start = 1
    end = n
    first_bad_version = None
    if n <= 2:
        for i in range(1, n+1):
            if is_bad_version(i):
                first_bad_version = i
                return first_bad_version

    while end - start != 1:
        mid = int((end-start)/2) + start
        logger.debug(start)
        logger.debug(mid)
        logger.debug(end)

        if is_bad_version(mid):
            first_bad_version = mid
            end = mid

        else:
            start = mid

    logger.debug(first_bad_version)
    if not first_bad_version:
        for i in range(start, end+1):
            print(i)
            if is_bad_version(i):
                first_bad_version = i
                return first_bad_version

    return first_bad_version


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
