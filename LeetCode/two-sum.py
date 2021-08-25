"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Ref: https://leetcode.com/problems/two-sum/
"""

from time import perf_counter


def brute(lst, target):
    # brute force solution
    for idx_1 in range(len(lst)):
        for idx_2 in range(len(lst)):
            if idx_1 == idx_2:
                continue
            if (lst[idx_1] + lst[idx_2]) == target:
                return [idx_1, idx_2]


def optimised(lst, target):
    # optimised solution
    dct = {}
    for idx_1, val_1 in enumerate(lst):
        remaining_val = (target - val_1)
        if remaining_val in dct:
            return [idx_1, dct[remaining_val]]
        dct[val_1] = idx_1


def main(lst, target):
    return optimised(lst, target)


if __name__ == '__main__':
    start_ts = perf_counter()

    lst = [2, 7, 11, 15]
    target = 9
    # expected output = [0, 1]
    output = main(lst, target)
    print(output)

    lst = [3, 2, 4]
    target = 6
    # expected output = [1, 2]
    output = main(lst, target)
    print(output)

    lst = [3, 3]
    target = 6
    # expected output = [0, 1]
    output = main(lst, target)
    print(output)

    print(perf_counter() - start_ts)
