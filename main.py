import calc_helper as calc

def createTriangle():
    a = (0, 0)
    b = (0, 10)
    c = (2, 7)
    return a, b, c

def main():
    triangle = createTriangle()
    calc.printTriangleCentroid(*triangle)
    return

if __name__ == "__main__":
    main()