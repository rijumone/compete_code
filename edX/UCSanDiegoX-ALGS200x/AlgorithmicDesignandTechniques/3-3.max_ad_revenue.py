# Uses python3


def max_dot_product(a, b):
    # write your code here
    res = 0
    a = sorted(a)
    b = sorted(b)
    for i in range(len(a)):
        res += a[i] * b[i]
    return res


if __name__ == '__main__':
    # input = input()
    # data = list(map(int, input.split()))
    # n = data[0]
    n = 3
    # a = data[1:(n + 1)]
    a = [1, 3, - 5]
    # b = data[(n + 1):]
    b = [-2, 4, 1]
    print(max_dot_product(a, b))
