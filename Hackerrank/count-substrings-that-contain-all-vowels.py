'''
ref: https://www.geeksforgeeks.org/count-substrings-that-contain-all-vowels-set-2/
'''


from loguru import logger

#
# Complete the 'vowelsubstring' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

vowels = ['a', 'e', 'i', 'o', 'u']


def check_valid_substrings(sub_str):
    logger.debug(f'sub_str: {sub_str}')
    count = 0

    # check that substring contains
    # ALL vowels at least once
    for v in vowels:
        if v not in sub_str:
            return count

    letter_cnt_dct = {}
    for l in sub_str:
        # initialise letter count dict with 0
        letter_cnt_dct[l] = 0
    # logger.debug(letter_cnt_dct)

    len_sub_str = len(sub_str)
    # to keep track of sub_string's index
    index = 0

    for _ in range(len_sub_str):
        # update dict
        letter_cnt_dct[sub_str[_]] += 1
        logger.debug(letter_cnt_dct)
        # ensure that all the vowels are present in the dict at least once
        # (we will keep updating this dict)
        while (letter_cnt_dct['a'] > 0 and letter_cnt_dct['e'] > 0 and letter_cnt_dct['i'] > 0
               and letter_cnt_dct['o'] > 0 and letter_cnt_dct['u'] > 0):

            # logger.debug(count, len_sub_str, _)

            logger.debug(f'_: {_}')
            # with prefix as word made till now, updating count
            count += len_sub_str - _
            logger.debug(f'count: {count}')
            # updating letter_cnt_dct since that
            # particular vowel has been counted once
            # logger.debug(f'sub_str: {sub_str}')
            # logger.debug(f'index: {index}')
            letter_cnt_dct[sub_str[index]] -= 1
            logger.debug(letter_cnt_dct)
            index += 1

        # logger.debug(_, index)

    return count


def vowelsubstring(s):
    count = 0
    sub_str = ''
    for _ in range(len(s)):
        if s[_] in vowels:
            sub_str += s[_]
            continue

        # consonant encountered
        if sub_str != '':
            # check if sub_str generated has any smaller substrings
            count += check_valid_substrings(sub_str)
        # reset sub_str
        sub_str = ''
    # after loop if there are any valid substrings left
    if sub_str != '':
        count += check_valid_substrings(sub_str)

    return count


if __name__ == '__main__':

    # s = input()
    # s = 'aeouisddaaeeiouua'
    s = 'bcaekfaaeioau'

    result = vowelsubstring(s)

    logger.debug(f'result: {result}')
