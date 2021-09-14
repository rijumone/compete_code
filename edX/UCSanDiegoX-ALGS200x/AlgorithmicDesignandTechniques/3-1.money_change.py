# Uses python3

def get_change(m):
    '''
    Return minimum number of coins needed
    to change m in denominations of 1, 5, 10
    '''
    # init remaining money
    rem_m = m

    # starting with 10
    tens = rem_m // 10
    rem_m = rem_m % 10

    # then 5
    fives = rem_m // 5
    rem_m = rem_m % 5

    # finally whatever remains is ones
    ones = rem_m

    return tens + fives + ones


if __name__ == '__main__':
    # m = int(input())
    m = 28  # expected output 6
    print(get_change(m))
