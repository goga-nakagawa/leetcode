


# memos
def fib(n, memo={1:1, 2:1}):
    if n in memo.keys():
        return memo[n]
    else:
        memo[n] = fib(n - 2, memo) + fib(n - 1, memo)
        return memo[n]

print fib(10)
