"""
https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
"""


def main():
    d = 3
    a = [1, 2, 3, 4, 5, ]

    lst = a
    n = len(lst)

    if d > n:
        d = d % n

    # print(d)
    lst1 = [None] * n
    print(lst)
    for i in range(n):
        new_pos = i - d
        # if new_pos < 0:
        #     new_pos += n

        # print(lst[i], new_pos, new_pos if new_pos >= 0 else n + new_pos)
        lst1[new_pos] = lst[i]

    print(lst1)
    return lst1


if __name__ == '__main__':
    main()
