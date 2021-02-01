'''

https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem


Print the minimum number of jumps needed to win the game.

Sample Input:
7
0 0 1 0 0 1 0

Sample Output:
4

Explanation:
The player must avoid  c[2] and c[5]. The game can be won with a minimum of 4 jumps:

'''


def main(c):
    n_steps = 0
    _ctr = 0
    len_c = len(c)
    while True:
        if _ctr == len_c - 1:
            break
        # check if +2 exists
        if _ctr + 2 < len_c:
            # check if +2 is safe
            if c[_ctr + 2] == 0:
                n_steps += 1
                _ctr += 2
                continue
        # check if +1 exists
        if _ctr + 1 < len_c:
            # check if +1 is safe
            if c[_ctr + 1] == 0:
                n_steps += 1
                _ctr += 1
                continue

    return n_steps


if __name__ == '__main__':
    n_steps = main(c=[0, 0, 1, 0, 0, 1, 0, ])
    print(n_steps)
