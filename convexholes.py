""" PROJECT EULER 252
Given a set of points on a plane, we define a convex hole to be a convex polygon having as vertices any of the given
points and not containing any of the given points in its interior (in addition to the vertices, other given points may
lie on the perimeter of the polygon).
"""

import matplotlib.pyplot as plt

def give_n_points(n):
    returnlist = []
    svalues = [290797]
    nexts = lambda x : (x ** 2) % 50515093
    coord = lambda x : (svalues[x] % 2000) - 1000
    for i in range(0, n*4):
        svalues.append(nexts(svalues[i-1]))
    for x in range(1, n*2, 2):
        returnlist.append((coord(2*x),coord(2*x+1)))
    return returnlist

points = give_n_points(20)

xs = [x for x,y in points]
ys = [y for x,y in points]

plt.plot(xs, ys, "ro")
plt.grid()
plt.show()