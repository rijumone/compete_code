'''
We have a collection of stones,
each stone has a positive integer weight.

Each turn, we choose the two heaviest stones
and smash them together.  Suppose the stones
have weights x and y with x <= y.

The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed,
and the stone of weight y has new weight y-x.

At the end, there is at most 1 stone left.
Return the weight of this stone (or 0 if there are no stones left.)

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then
that's the value of last stone.


Note:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
'''
import click

@click.command()
@click.option(
    '--weights',
    type=str,
    required=True,
    default='2,7,4,1,8,1',
    help='comma-seperated stone weights',
    )
def main(weights):
    '''
    Entry point for module
    '''
    weights = [int(_.strip()) for _ in weights.split(',')]
    while len(weights) > 1:
        # pylint: disable=invalid-name
        # keep doing this until we are down to a single stone
        max_1, max_2 = get_largest_stones(weights)
        if max_2 >= max_1:
            # assigning the nomenclature used in the problem statement
            x = max_1
            y = max_2
        else:
            x = max_2
            y = max_1
        # stones will have to be removed from collection in any case
        weights.remove(x)
        weights.remove(y)
        # difference in weights will be added back only if the weights are unequal
        if x != y:
            weights.append(y-x)

    if len(weights) > 0:
        print('Weight of stone left: {}.'.format(weights[0]))
    else:
        print('No stone left.')



def get_largest_stones(weights):
    '''
    Get 2 largest stones in passed in weights list
    Args:
        weights (list): positive integers list
    Returns:
        max_1 (integer)
        max_2 (integer)
    '''
    # copying the list because we don't want to change the original
    weights_copy = weights.copy()
    # getting first max
    max_1 = max(weights_copy)
    # removing one element of max from list
    # .remove() removes one element and leaves the other elements intact
    # Example:
    # >>> lst = ['a', 'b', 'a', 'c']
    # >>> lst.remove('a')
    # >>> lst
    # ['b', 'a', 'c']
    weights_copy.remove(max_1)
    # getting second max
    max_2 = max(weights_copy)
    # return tuple of two maxes
    return max_1, max_2


if __name__ == '__main__':
    # pylint: disable=no-value-for-parameter
    main()
