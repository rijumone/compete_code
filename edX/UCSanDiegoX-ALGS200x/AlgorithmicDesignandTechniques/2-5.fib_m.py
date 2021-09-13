# Uses python3
from loguru import logger


# Calculate and return Pisano Period
# The length of a Pisano Period for
# a given m ranges from 3 to m * m
def get_pisano_period(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current \
            = current, (previous + current) % m

        # A Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i + 1


def get_fibonacci_huge_naive(n, m):
    # Getting the period
    pisano_period = get_pisano_period(m)

    # Taking mod of N with
    # period length
    n = n % pisano_period

    previous, current = 0, 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    for i in range(n-1):
        previous, current \
            = current, previous + current

    return (current % m)


if __name__ == '__main__':
    # input = input()
    # n, m = map(int, input.split())
    n, m = 99999999999999999, 2
    # n, m = 281621358815590, 30524
    # n, m = 1548276540, 235
    print(get_fibonacci_huge_naive(n, m))
