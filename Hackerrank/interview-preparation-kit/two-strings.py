'''
https://www.hackerrank.com/challenges/two-strings/problem
'''


def main():
    s1 = 'hello'
    s2 = 'world'
    char_found = False
    for s in s2:
        if s in s1:
            char_found = True
            break
    if char_found:
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    o = main()
    print(o)
