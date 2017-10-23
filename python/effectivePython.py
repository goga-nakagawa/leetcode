# recursive

def comb(n, m, a = []):
    print a
    if m == 0:
        print a
    elif n == m:
        print range(1, m + 1) + a
    else:
        comb(n - 1, m, a)
        comb(n - 1, m - 1, [n] + a) # nを選んだ

comb(5, 3)
