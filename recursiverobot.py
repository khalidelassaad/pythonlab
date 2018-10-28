"""
Imagine a robot sitting on the upper left hand corner of an NxN grid. The robot can
only move in two directions: right and down. How many possible paths are there for
the robot?
FOLLOW UP
Imagine certain squares are “off limits”, such that the robot can not step on them.
Design an algorithm to get all possible paths for the robot. TESTING GIT COMMIT

"""

"""
          
          ___ robot @ grid right___. . . etc...
        /
robot
@    ------ robot @ grid right___. . . etc...
grid




"""

def robogrid(gridsize:int, offlimits:[("x","y")]=[], coordx=0, coordy=0):
#Return number of possible paths for robot.
    if (coordx, coordy) in offlimits: #no path here boss!
        return 0
    if gridsize - 1 == coordx and gridsize - 1 == coordy:
        return 1
    if coordx >= gridsize or coordx < 0 or \
        coordy >= gridsize or coordy < 0:#no off the board paths
        return 0
    return robogrid(gridsize, offlimits, coordx+1, coordy) \
           + robogrid(gridsize, offlimits, coordx, coordy+1)

def printassert(size, expect):
    received = robogrid(size)
    print("Size: {} Expected/Received = {}/{}".format(str(size),str(expect),str(received)))
    print(["Correct.","FAILED!"][expect != received])
    return

#printassert(2,2)

def showboard(size, offlimits):
    L = [["_" for i in range(size)] for i in range(size)]
    for x, y in offlimits:
        L[x][y]="#"
    L[0][0]="$"
    L[size-1][size-1] = "x"
    for row in L:
        print(" ".join(row))
    print("Paths found: {}".format(robogrid(size,offlimits)))

showboard(5, [])

showboard(5,[(1,x) for x in range(5)])

showboard(5,[(1,x) for x in range(0,5,2)]+[(3,x) for x in [0,1,2,3]])