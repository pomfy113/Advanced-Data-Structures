#!python

def fibonacci(n):
    """fibonacci(n) returns the n-th number in the Fibonacci sequence,
    which is defined with the recurrence relation:
    fibonacci(0) = 0
    fibonacci(1) = 1
    fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2), for n > 1"""
    # Check if n is negative or not an integer (invalid input)
    if not isinstance(n, int) or n < 0  :
        raise ValueError('fibonacci is undefined for n = {!r}'.format(n))
    # Implement fibonacci_recursive, _memoized, and _dynamic below, then
    # change this to call your implementation to verify it passes all tests
    # return fibonacci_recursive(n)
    return fibonacci_memoized(n, [0, 1] + ([None] * (n-1)))
    # return fibonacci_dynamic(n)


def fibonacci_recursive(n):
    # Check if n is one of the base cases
    if n == 0 or n == 1:
        return n
    # Check if n is larger than the base cases
    elif n > 1:
        # Call function recursively and add the results together
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_memoized(n, memo):
    # Memoize the fibonacci function's recursive implementation here
    # Check if n is larger than the base cases
    if n == 0 or n == 1:
        return n
    if memo[n]:
        return memo[n]
    else:
        # Call function recursively and add the results together
        memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
        return memo[n]

    # Once implemented, change fibonacci (above) to call fibonacci_memoized
    # to verify that your memoized implementation passes all test cases


def fibonacci_dynamic(n):
    # Implement the fibonacci function with dynamic programming here
    # Check if n is one of the base cases
    if n == 0 or n == 1:
        return n
    else:
        # I originally kept appending to a list with [1, 1], but why do that
        # When we can just keep adding variables up?
        num1 = 0
        num2 = 1
        for i in range(1, n):
            final = num1 + num2
            num1 = num2
            num2 = final

        return final
    # Once implemented, change fibonacci (above) to call fibonacci_dynamic
    # to verify that your dynamic implementation passes all test cases


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 1:
        num = int(args[0])
        result = fibonacci(num)
        print('fibonacci({}) => {}'.format(num, result))
    else:
        print('Usage: {} number'.format(sys.argv[0]))


if __name__ == '__main__':
    main()
