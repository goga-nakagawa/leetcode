import re
x = None
for i in ['bird', 'goat', 'pig', 'chicken', 'dog'][::-1]:
    x = (i, x)

print x

def probe(node, search):
    if node is None:
        return -1
    else:
        while node[0] != search:
            node = node[1]
        if node[1] is None:
            return -1
        else:
            return node[0]


print probe(x, 'goat')


# def flatten(arr, res=[]):
#     if isinstance(arr, list):
#         for a in arr:
#             flatten(a, res)
#     else:
#         res += [arr]

#     return res

# arr = [[1,2],[3,4,5,[6,7]]]
# print flatten(arr)



# compiled = re.compile(r"(\d+)\[([a-zA-Z]+)\]")
# print compiled.findall("12[ak]")