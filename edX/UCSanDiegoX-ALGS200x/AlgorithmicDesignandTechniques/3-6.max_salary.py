# Uses python3


def largest_number_1(a):
    a = sorted(a)
    res = ""
    while True:
        curr_max_idx = get_largest_value(a)
        curr_max = a[curr_max_idx]
        res += curr_max
        # print(a)
        a = [_ for i, _ in enumerate(a) if i != curr_max_idx]
        # a.remove(curr_max)
        # print(a)
        if not len(a):
            break
    return res


def get_largest_value(lst):
    max_till_now = 0
    max_idx = 0
    # print(lst)
    for idx, _ in enumerate(lst):
        loop_max = int(_[0])
        # if len(_) > 1 and int(_[1]) == 0:
        #     continue

        if loop_max > max_till_now:
            max_till_now = loop_max
            max_idx = idx
    return max_idx


def largest_number_2(a):
    resultant = ''
    while len(a):
        for i in range(len(a)):
            ith = a[i]
            max_ith = 0
            for j in range(i, len(a)):
                jth = a[j]
                pd_ith, pd_jth = get_padded(ith, jth)
                if pd_ith > pd_jth:
                    max_ith = ith
                print(max_ith)
        break


def get_larger_value(a, b):
    if int(a+b) > int(b+a):
        return a
    return b


def largest_number(a):
    resultant = ''
    while len(a):
        current_max = 0
        for digit in a:
            current_max = get_larger_value(str(current_max), digit)

        resultant += str(current_max)
        a.remove(str(current_max))
    return resultant


def get_padded(ith, jth):
    if len(ith) == len(jth):
        return int(ith), int(jth)
    if len(ith) > len(jth):
        diff = len(ith) - len(jth)
        jth += '0'*diff
    else:
        diff = len(jth) - len(ith)
        ith += '0'*diff
    return int(ith), int(jth)


if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = input.split()
    # a = data[1:]
    # lst_str = '2 8 2 3 6 4 1 1 10 6 3 3 6 1 3 8 4 6 1 10 8 4 10 4 1 3 2 3 2 6 1 5 2 9 8 5 10 8 7 9 6 4 2 6 3 8 8 9 8 2 9 10 3 10 7 5 7 1 7 5 1 4 7 6 1 10 5 4 8 4 2 7 8 1 1 7 4 1 1 9 8 6 5 9 9 3 7 6 3 10 8 10 7 2 5 1 1 9 9 5'
    # lst_str = '10 1'
    # lst_str = '10 2'
    # lst_str = '21 2'
    # lst_str = '989 979'
    # lst_str = '10 10 11'
    lst_str = '345 299 29 2919 298 1'

    # a = ['21', '2']
    a = lst_str.split(' ')
    print(largest_number(a))

'''
9999999998888888888887777777776666666666555555554444444443333333333222222222111011101011101010111101111101011
9999999998888888888887777777776666666666555555554444444443333333333222222222111111111111111101010101010101010

https://towardsdatascience.com/course-1-algorithmic-toolbox-part-2-big-o-and-greedy-6265d9065f05

'''
