'''
Ref: https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem
'''

def main(arr):
    
    '''
    min_abs_diff = 999999999999999
    pairs = []

    # compute pairs
    for i, item_0 in enumerate(arr):
        for j, item_1 in enumerate(arr):
            if i == j:
                continue
            pairs.append((item_0, item_1))

    # print(pairs)
    
    for pair in pairs:
        diff = pair[0] - pair[1]
        if diff < 0:
            diff *= -1
        if diff < min_abs_diff:
            min_abs_diff = diff
    '''

    min_abs_diff = 9999999999
    # first sort the list
    sorted_lst = sorted(arr)

    for idx in range(len(sorted_lst) - 1):
        item = sorted_lst[idx]
        next_item = sorted_lst[idx+1]

        current_abs_diff = abs(item - next_item)
        if current_abs_diff < min_abs_diff:
            min_abs_diff = current_abs_diff

    return min_abs_diff


if __name__ == '__main__':
    arr = []
    with open('minimum-absolute-difference-in-an-array-input.txt') as _f:
        _ctr = 0
        for line in _f.readlines():
            _ctr += 1
            if _ctr == 1:
                continue
            arr = [int(_) for _ in line.split()]

    # Expected output: 25
    min_abs_diff = main(arr)

    print(min_abs_diff)
