"""
You are given an integer array coins representing coins of different 
denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that
amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.


Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0


Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

"""


def main(coins, amount):
    # sort the coins in ascending order of denominations
    coins = sorted(coins, reverse=True)
    n_coins = 0
    
    for largest_coin in coins:
        if amount < largest_coin:
            continue
        n_coins += amount // largest_coin
        amount = amount % largest_coin
        if amount == 0:
            return n_coins
        
    return -1


if __name__ == '__main__':
    assert main(coins=[1, 2, 5], amount=11) == 3
    assert main(coins=[2], amount=3) == -1
    assert main(coins=[1], amount=0) == 0
    assert main(coins=[186, 419, 83, 408], amount=6249) == 20
