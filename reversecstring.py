def reverse(S:list):
    lastCharPos=len(S) - 2
    firstCharPos=0
    while(lastCharPos - firstCharPos > 0):
        S[lastCharPos],S[firstCharPos] = S[firstCharPos],S[lastCharPos]
        lastCharPos = lastCharPos - 1
        firstCharPos = firstCharPos + 1
    return S

print(str(reverse(["a","b","c","d","X"])))
print(str(reverse(["X"])))
print(str(reverse(["a","X"])))
print(str(reverse(["a","b","X"])))