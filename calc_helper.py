from sympy import Point, Polygon
from sympy.plotting import plot

def printTriangleCentroid(a=(0,0), b=(1,0), c=(1,1)):

    p1, p2, p3 = map(Point, [a, b, c])
    polygon = Polygon(p1, p2, p3)
    print(polygon.centroid)
    return