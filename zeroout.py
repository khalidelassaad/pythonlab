def zeroOut(M:[[int]]) -> None:
    width = len(M)
    height = len(M[0])
    zeroCols, zeroRows = [], []
    for i in range(width):
        for j in range(height):
            if M[i][j] == 0:
                zeroCols.append(i)
                zeroRows.append(j)
    for col in zeroCols:
        M[col] = [0]*height
    for i in range(width):
        for row in zeroRows:
            M[i][row] = 0
    return

def print2D(M):
    for row in M:
        print(row)

M = [
    [2,4,5,7,3],
    [6,0,3,3,3],
    [1,2,1,1,1],
    [0,2,3,4,5]
]

zeroOut(M)
print2D(M)