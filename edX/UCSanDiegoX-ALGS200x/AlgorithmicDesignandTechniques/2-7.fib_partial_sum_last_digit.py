# Uses python3

def fibonacci_partial_sum_naive(from_, to):
    fib_n = fibonacci_sum_naive(to)
    fib_m_1 = fibonacci_sum_naive(from_ - 1)
    print(fib_n, fib_m_1)
    return (fibonacci_sum_naive(to)
            - fibonacci_sum_naive(from_ - 1)) % 10


def fibonacci_sum_naive(n):
    if n in (0, 1):
        return n

    previous = 0
    current = 1

    remainder = n % 60

    if remainder == 0:
        return 0

    for _ in range(2, remainder + 3):
        f = (previous + current) % 60
        previous = current
        current = f

    sum = current - 1
    return sum


if __name__ == '__main__':
    # input = input()
    # from_, to = map(int, input.split())
    # from_, to = 10, 12
    from_, to = 0, 0
    print(fibonacci_partial_sum_naive(from_, to))
