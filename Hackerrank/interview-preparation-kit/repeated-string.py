""" There is a string, s, of lowercase English letters that 
is repeated infinitely many times. Given an integer, n , 
find and print the number of letter a's in the first n 
letters of the infinite string.

https://www.hackerrank.com/challenges/repeated-string/problem
 """


def main():
    s = 'abcaa'
    n = 7
    _chk_char = 'a'

    _ctr = 0
    c_s = len(s)

    if n <= c_s:
        # at max, will fill once
        # check in substring
        for _char in s[:n]:
            if _char != _chk_char:
                continue
            _ctr += 1

        return _ctr

    times_filled_completely = int(n / c_s)

    # count _chk_char occurrences in one complete set
    for _char in s:
        if _char != _chk_char:
            continue
        _ctr += 1

    _ctr *= times_filled_completely

    # now count the remaining  _chk_char occurrences
    remaining_chars = n % c_s

    for _char in s[:remaining_chars]:
        if _char != _chk_char:
            continue
        _ctr += 1

    return _ctr


if __name__ == '__main__':
    o = main()
    print(o)
