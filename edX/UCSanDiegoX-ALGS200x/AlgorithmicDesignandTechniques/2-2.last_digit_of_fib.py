# Uses python3
from time import perf_counter


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10

    return current % 10


if __name__ == '__main__':

    input = input()
    n = int(input)
    ts = perf_counter()
    print(get_fibonacci_last_digit_naive(n))
    print(perf_counter() - ts)
