# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.
    # calculate value per weight
    v_p_w_lst = []
    for i in range(len(values)):
        v_p_w_lst.append(
            {
                'value': values[i],
                'weight': weights[i],
                'v_p_w': values[i] / weights[i],
            }
        )

    # sort it
    v_p_w_lst = sorted(v_p_w_lst, key=lambda x: x['v_p_w'], reverse=True)
    # this way we have the most valuable items at the top

    # init updated_capacity
    updated_capacity = capacity
    for v_p_w in v_p_w_lst:
        if updated_capacity <= 0:
            break
        c_value = v_p_w['value']
        c_weight = v_p_w['weight']
        permissible_weight = min(c_weight, updated_capacity)
        permissible_value = c_value / (c_weight / permissible_weight)
        value += permissible_value
        updated_capacity -= c_weight

    return value


if __name__ == "__main__":
    # data = list(map(int, sys.stdin.read().split()))
    # n, capacity = data[0:2]
    # values = data[2:(2 * n + 2):2]
    # weights = data[3:(2 * n + 2):2]
    capacity = 50
    # capacity = 10
    values = [60, 100, 120]
    # values = [500, ]
    weights = [20, 50, 30]
    # weights = [30, ]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
