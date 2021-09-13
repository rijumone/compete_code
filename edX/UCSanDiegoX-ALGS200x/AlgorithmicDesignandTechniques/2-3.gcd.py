# Uses python3
import pickle
from time import perf_counter
from loguru import logger


def gcd_naive(a, b):
    '''
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd
    '''
    return a if not b else gcd_naive(b, a % b)
    if a == b:
        return a
    current_gcd = 1
    # primes = load_primes()
    primes = gen_primes(min(a, b))
    # logger.info(primes)
    pfs_a = get_prime_factors(a, primes)
    pfs_b = get_prime_factors(b, primes)
    logger.info(pfs_a)
    logger.info(pfs_b)

    # factorization
    q_a = a
    # prime factors product a
    pfsp_a = []
    for prime in pfs_a:
        while True:
            if q_a % prime != 0:
                break
            q_a = int(q_a / prime)
            pfsp_a.append(prime)
            # logger.info(q_a)

    q_b = b
    # prime factors product a
    pfsp_b = []
    for prime in pfs_b:
        while True:
            if q_b % prime != 0:
                break
            q_b = int(q_b / prime)
            pfsp_b.append(prime)
            # logger.info(q_b)
    logger.info(pfsp_a)
    logger.info(pfsp_b)

    check_against = pfsp_a if len(pfsp_a) > len(pfsp_b) else pfsp_b
    iter_over = pfsp_b if len(pfsp_b) < len(pfsp_a) else pfsp_a
    print(iter_over, check_against)
    for _ in iter_over:
        if _ in check_against:
            current_gcd *= _
            check_against.remove(_)
    return current_gcd


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def gen_primes(n):
    # primes = []
    # for i in range(2, n + 1):
    #     if is_prime(i):
    #         primes.append(i)
    # return primes
    """sieveOfEratosthenes(n): return the list of the primes < n."""

    if n <= 2:
        return []
    sieve = list(range(3, n, 2))
    top = len(sieve)
    for si in sieve:
        if si:
            bottom = (si * si - 3) // 2
            if bottom >= top:
                break
            sieve[bottom::si] = [0] * -((bottom - top) // si)
    return [2] + [el for el in sieve if el]


def dump_primes(primes):
    with open('primes.pkl', 'wb') as pkl:
        pickle.dump(primes, pkl)


def load_primes():
    with open('primes.pkl', 'rb') as pkl:
        return pickle.load(pkl)


def get_prime_factors(k, primes):
    prime_factors = []
    for prime in primes:
        if prime > k:
            break
        if k % prime == 0:
            prime_factors.append(prime)
    return prime_factors


def assertions():
    assert gcd_naive(56, 8) == 8
    assert gcd_naive(14159572, 63967072) == 4
    assert gcd_naive(18, 24) == 6
    assert gcd_naive(226553150, 1023473145) == 5
    assert gcd_naive(100000000, 100000000) == 100000000


if __name__ == "__main__":
    ts = perf_counter()
    # input = input()
    # a, b = map(int, input.split())
    # logger.info(gcd_naive(a, b))

    # primes = gen_primes(99999)

    # dump_primes(primes)
    # primes = load_primes()
    # logger.info(primes)
    # pfs = get_prime_factors((290990700 * 23 * 29), primes)
    # logger.info(pfs)

    # gcd = gcd_naive(56, 8)
    # gcd = gcd_naive(18, 24)
    # gcd = gcd_naive(14159572, 63967072)
    # gcd = gcd_naive(100000000, 100000000)
    # gcd = gcd_naive(226553150, 1023473145)
    gcd = gcd_naive(226553150, 1023473145)
    logger.info(gcd)
    # assertions()
    logger.info(perf_counter() - ts)
