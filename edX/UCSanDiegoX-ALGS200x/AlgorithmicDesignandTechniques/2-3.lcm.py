# Uses python3
import math


def gcd(a, b):
    return a if not b else gcd(b, a % b)


def lcm_naive(a, b):
    return (a * b) // gcd(a, b)


def assertions():
    assert lcm_naive(226553150, 1023473145) == 46374212988031350


if __name__ == '__main__':
    # a, b = 18, 24
    # a, b = 2000000000, 1999999999
    # a, b = 226553150, 1023473145
    # print(lcm_naive(a, b))
    assertions()
