'''
https://www.hackerrank.com/challenges/ctci-ransom-note/problem
'''


def main():

    magazine, note = None, None
    with open('input14.txt') as in_f:
        _ctr = 0
        for line in in_f.readlines():
            if _ctr == 1:
                magazine = line.strip('\n').split(' ')
            if _ctr == 2:
                note = line.strip('\n').split(' ')
            _ctr += 1
    # save count of magazine words in dct
    magazine_dct = {}
    magazine_words_lst = magazine
    for word in magazine_words_lst:
        if word not in magazine_dct:
            magazine_dct[word] = 0
        magazine_dct[word] += 1
    note_possible = False

    note_words_lst = note
    for word in note_words_lst:
        if word not in magazine_dct.keys():
            note_possible = False
            break
        if magazine_dct[word] < 1:
            note_possible = False
            break
        magazine_dct[word] -= 1
        note_possible = True

    if note_possible:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
