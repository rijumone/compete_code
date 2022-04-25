from loguru import logger


def binary_search(a, x):
    left, right = 0, len(a)
    # logger.info(f'{a}, {x}')
    while left < right:
        mid = int((left + right) / 2)
        # logger.info(f'{left}, {right}, {mid}')
        if a[mid] == x:
            return mid
        if a[mid] > x:
            right = mid
        else:
            left = mid + 1
        # logger.info(f'{left}, {right}')
    return -1


def main():
    for x in [int(_) for _ in '8 1 23 1 11'.split(' ')]:
        o = binary_search(a, x)
        logger.info(f'o, {o}')


if __name__ == '__main__':
    a = [int(_) for _ in '1 5 8 12 13'.split(' ')]
    main()
