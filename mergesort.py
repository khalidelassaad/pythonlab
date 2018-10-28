def mergesort(L:list) -> list:
    if len(L) < 2:
        return L
    # pick a midpoint and split into left and right
    midpoint = len(L)//2
    left = mergesort(L[:midpoint])
    right = mergesort(L[midpoint:])
    # merge left and right
    storeIndex = 0
    li = 0
    ri = 0
    while li < len(left) and ri < len(right):
        if left[li] < right[ri]:
            L[storeIndex] = left[li]
            li += 1
            storeIndex += 1
        else:
            L[storeIndex] = right[ri]
            ri += 1
            storeIndex += 1

    for v in left[li:]+right[ri:]:
        L[storeIndex] = v
        storeIndex += 1
    return L

L = [3,2,5,3,6,7,7,8,3,4,5,2,1,1,1,7]
mergesort(L)
print(L)