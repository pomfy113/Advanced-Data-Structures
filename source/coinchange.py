#!/bin/python3

"""
    So I can't be honest and say I did it without any large hints, but I caved.

    The cascading effect is interesting.
    -   At the beginning, you can create combinations with multiples. With 10, 4, [2, 5, 3, 6]
        if you do prints, you'll notice that multiples of 2, with just the 2 coin, increase
    -   The other coins make it more interesting. Due to how indexes work, you'll grab combinations
        that work out to that index.
            ie: Say we're looking for 5, and have 1, 2 and 3.
                If there's two ways to get to 2 - {1, 1} and {2}, and you can use a 3 to get 5.
                list[2] should have 2 - that is, it knows it can use those 2 combinations.
                We add those 2 combinations with 3 to make 5: {1, 1, 3}, and {2, 3}.
                If 5 is also available, we add {5} to that combination. So now we have:
                {1, 1, 3}, {2, 3}, and add the {5} for a total of 3 combos!
                5 does not affect any lower combinations, however.
    -   We simply print the last number. You can actually print how to get to other
        change combos as well!
"""

# Complete the getWays function below.
def getWays(total, coins):
    # n is what we need to go up to
    coinlen = len(coins)
    memo = [1] + ([0] * total)

    # Going through each coin, 1 by 1
    for coin in range(0, coinlen):
        # Now for the combinations, startin
        for combo in range(coins[coin], total+1):
            # There is a weird cascade effect with coin combinations
            # Will explain in DOCSTRING
            memo[combo] += memo[combo - coins[coin]]
    return memo[total]

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    print(getWays(n, c))
