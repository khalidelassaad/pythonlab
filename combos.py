"""Given an array of integers, find out how many combinations in the array satisfy the equation x+y+z=w where x and y and z and w belong to the array such that x precedes y precedes z precedes w. Elements are unique

[2, 8, 4, 1, 7]
should return
tuple (2,4,1,7) #2+4+1=6
"""

import itertools

def combos(Input):
    d = dict()  # maps sums to their index in input IF they exist
    for i, e in enumerate(Input):
        d[e] = i
    triplets = itertools.combinations(Input, 3)
    returnlist = []
    for triplet in triplets:
        try:
            index = d[sum(triplet)]
        except KeyError:
            index = -1
        if index != -1:
            returnlist.append([t for t in triplet] + [Input[index]])
    return returnlist

print(combos([2,8,4,1,7,24,63,12,639,31,647]))
