def comb(arr, k, selected=[]):
    if k == 0:
        print selected
    elif len(arr) == k:
        print selected + arr[:k + 1]
    else:
        comb(arr[1:], k - 1, selected + [arr[0]])
        comb(arr[1:], k, selected)

# comb([1,2,3,4,5], 3)



def comb1(arr, k):
    if k == 0:
        yield []
    elif len(arr) == k:
        yield arr[:k + 1]
    else:
        for c in comb1(arr[1:], k - 1):
            yield c + arr[1:]
        for c in comb1(arr[1:], k):
            yield arr[1:]

for c in comb1([1,2,3,4,5], 3):
    print c