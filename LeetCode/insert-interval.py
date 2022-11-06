'''https://leetcode.com/problems/insert-interval/

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''
from loguru import logger


def main(intervals, new_interval):
    return_lst = []
    # new_interval begin lies in index interval
    n_i_b_idx = None
    # new_interval end lies in index interval
    n_i_e_idx = None
    for idx, interval in enumerate(intervals):
        if interval[0] <= new_interval[0] <= interval[1]:
            n_i_b_idx = idx
        elif interval[0] <= new_interval[1] <= interval[1]:
            n_i_e_idx = idx

        try:
            if interval[0] < new_interval[1] < intervals[idx+1][0]:
                n_i_e_idx = idx
        except IndexError:
            pass

    print(n_i_e_idx)
    # append all before new interval start
    for idx in range(n_i_b_idx):
        return_lst.append(intervals[idx])

    # append start from start and end from end
    return_lst.append([
        intervals[n_i_b_idx][0],
        intervals[n_i_e_idx][1],
    ])

    # append all after new interval end
    for idx in range(n_i_e_idx+1, len(intervals)):
        return_lst.append(intervals[idx])

    return return_lst


if __name__ == '__main__':
    intervals = [[1, 3], [6, 9]]
    new_interval = [2, 5]
    # intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    # new_interval = [4, 8]
    o = main(intervals, new_interval)
    print(o)
