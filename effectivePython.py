


# recursive and memos 
def fib(n, memo={1:1, 2:1}):
    if n in memo.keys():
        return memo[n]
    else:
        memo[n] = fib(n - 2, memo) + fib(n - 1, memo)
        return memo[n]

print fib(10)

def pow(n, memo={0:1}):
    if n in memo.keys():
        return memo[n]
    else:
        memo[n] = n*pow(n - 1, memo)
        return memo[n]

print pow(6)

def comb(n, k, memo):
    if n in memo.keys():
        return memo[n]
    else:
        memo[n] = comb(n, k-1, memo) * (n - k + 1) / k
        return memo[n]

print comb(6, 3, memo={(6, 0): 1, (6, 6): 1})