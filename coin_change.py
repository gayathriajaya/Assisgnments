'''
You are working at the cash counter at a fun-fair,
and you have different types of coins available to you in infinite quantities. The value of each coin is already given.
Can you determine the number of ways of making change for a particular number of units using the given types of coins?

For example, if you have  types of coins, and the value of each type is given as  respectively, you can make change for
 units in three ways: , , and .


    res[j] += res[j - coin];

    This line calculates the number of ways to get j amount of money by using coins. The number is calculated by adding
    number of ways it can be done without using coin "coin" plus the number of ways it can be done with the coin "coin".

'''

import sys


def ways(n, coins):             #total number of ways to make n with coins
    results = [0 for _ in range(n + 1)]
    results[0] = 1
    for coin in coins:
        for i in range(coin, n + 1):
            results[i] += results[i - coin]
    return results[n]


def min_ways(n, coins):  # min number of coins req to make change
    result = [sys.maxsize for _ in range(n + 1)]
    result[0] = 0
    for coin in coins:
        for j in range(coin, n + 1):
            result[j] = min(result[j - coin] + 1, result[j])
    return result[n]


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'
    print(ways(n, c))
    print(min_ways(n, c))
