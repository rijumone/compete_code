def main():
    prices = [int(_) for _ in '1 12 5 111 200 1000 10'.split(' ')]
    k = 140

    # need to sort the list and then
    # count first n elements which
    # sum to <= k
    len_prices = len(prices)
    for i in range(len_prices):
        for j in range(len_prices - 1):
            if prices[j] > prices[j+1]:
                _tmp = prices[j]
                prices[j] = prices[j+1]
                prices[j+1] = _tmp

    print(prices)

    sum_till_now = 0
    _ctr = 0
    for _ in prices:
        if sum_till_now >= k:
            break
        # import pdb
        # pdb.set_trace()
        sum_till_now += _
        _ctr += 1

    print(sum_till_now)
    if sum_till_now > k:
        print(_ctr - 1)
    else:
        print(_ctr)


if __name__ == '__main__':
    main()
