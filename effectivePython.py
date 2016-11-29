def comb(arr, k, selected=[]):
    if k == 0:
        print selected
    elif len(arr) == k:
        print selected + arr[:k + 1]
    else:
        comb(arr[1:], k - 1, selected + [arr[0]])
        comb(arr[1:], k, selected)

# comb([1,2,3,4,5], 3)

# recursive with generator
def icomb(arr, k, selected=[]):
    if k == 0:
        yield selected
    elif len(arr) == k:
        yield selected + arr[:k + 1]
    else:
        for c in icomb(arr[1:], k - 1, selected + [arr[0]]):
            yield c + arr[1:]
        for c in icomb(arr[1:], k, selected):
            yield arr[1:]


for c in icomb([1,2,3,4,5], 3):
    print c