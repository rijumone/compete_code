'''
https://www.hackerrank.com/challenges/ctci-bubble-sort
'''


def main():
    a = [3, 2, 1]

    len_a = len(a)
    n_swaps = 0
    for i in range(len_a):
        for j in range(len_a - 1):
            if a[j] > a[j+1]:
                n_swaps += 1
                _tmp = a[j+1]
                a[j+1] = a[j]
                a[j] = _tmp
    print(f'Array is sorted in {n_swaps} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')


if __name__ == '__main__':
    main()
