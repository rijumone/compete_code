# find_substring_in_string.py

def count_substring(string, sub_string):
    o_count = 0
    len_ss = len(sub_string)
    for i, c_l in enumerate(string):
        if ''.join([_ for _ in string][i: i + len_ss]) == sub_string:
            o_count += 1
    return o_count


if __name__ == '__main__':
    print(count_substring('anunurnuag', 'rnu'))