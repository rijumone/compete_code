# Uses python3

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    # Pisano Period for % 10 is 60
    remainder = n % 60

    # Checking the remainder
    if remainder == 0:
        return 0

    # The loop will range from 2 to
    # two terms after the remainder
    for _ in range(2, remainder + 3):
        f = (previous + current) % 60
        previous = current
        current = f

    sum = (current - 1) % 10
    return(sum)


if __name__ == '__main__':
    # input = input()
    # n = int(input)
    n = 239
    print(fibonacci_sum_naive(n))
