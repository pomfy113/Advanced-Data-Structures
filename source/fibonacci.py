def memoize(func):
    memo = {}

    def helper(arg):
        if arg not in memo:
            memo[arg] = func(arg)
        return memo[arg]

    return helper

@memoize
def fibonacci(num):
    if num == 0 or num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

def fibonacci2(num):
    fibo = [1, 1]

    for i in range(1, num):
        fibo.append(fibo[i] + fibo[i-1])
    print(fibo)
    return fibo[num]

print(fibonacci(120))
# print(fibonacci2(120))
