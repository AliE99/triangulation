from math import sqrt
from UI import Ui
from model.Models import Point

MAX = 1000000.0
diameter = []


def isNotSide(points, p1, p2):
    for i in range(0, len(points) - 1):
        if (p1 == points[i] and p2 == points[i + 1]) or (p1 == points[i + 1] and p2 == points[i]):
            return False

    if (p1 == points[len(points) - 1] and p2 == points[0]) or (p1 == points[0] and p2 == points[len(points) - 1]):
        return False

    return True


def cost(points, i, j, k):
    p1 = points[i]
    p2 = points[j]
    p3 = points[k]
    totalcost = 0
    if isNotSide(points, p1, p2):
        totalcost = totalcost + distance(p1, p2)
    if isNotSide(points, p2, p3):
        totalcost = totalcost + distance(p2, p3)
    if isNotSide(points, p3, p1):
        totalcost = totalcost + distance(p3, p1)

    return totalcost / 2


def distance(p1, p2):
    sqr = sqrt((p1.x - p2.x) * (p1.x - p2.x) +
               (p1.y - p2.y) * (p1.y - p2.y))
    return sqr


def findDiameter(i, j, k, points, matrixp):
    if j - i < 2:
        return

    if isNotSide(points, points[i], points[j]):
        diameter.append(i)
        diameter.append(j)

    findDiameter(i, k, matrixp[i][k], points, matrixp)
    findDiameter(k, j, matrixp[k][j], points, matrixp)
    return diameter


def triangulation(points, size):
    if size < 3:
        return 0

    w, h = size, size
    array = [[0 for x in range(w)] for y in range(h)]
    matrixP = [[0 for x in range(w)] for y in range(h)]
    for gap in range(0, size):
        i = -1
        for j in range(gap, size):
            i = i + 1

            if j < i + 2:
                array[i][j] = 0
            else:
                array[i][j] = MAX
                for k in range(i + 1, j):
                    value = array[i][k] + array[k][j] + cost(points, i, j, k)
                    if array[i][j] > value:
                        array[i][j] = value
                        matrixP[i][j] = k

    result = findDiameter(0, size - 1, matrixP[0][size - 1], points, matrixP)
    print(matrixP)
    print("Cost is : " + str(array[0][size - 1]))
    return result


if __name__ == '__main__':
    print("------------------------------------------------------------------------")
    choice = int(
        input("Enter 0 for default data and 1 for for your own data : "))
    pointList = []

    if choice == 0:
        n = int(input("1-Polygon, 2-Octagonal(1), 3-Octagonal(2), 4-Rectangle : "))
        if n == 1:
            pointList = [Point(10, 10), Point(25, 10), Point(40, 20), Point(25, 30), Point(10, 30)]
            text_name = "Polygon"


        elif n == 2:
            pointList = [Point(15, 5), Point(25, 5), Point(30, 10), Point(30, 15),
                         Point(25, 20), Point(15, 20), Point(10, 15), Point(10, 10)]
            text_name = "Octagonal"

        elif n == 3:
            pointList = [Point(40, 30), Point(30, 40), Point(20, 40), Point(10, 30),
                         Point(10, 20), Point(20, 10), Point(30, 10), Point(40, 20)]
            text_name = "Octagonal"

        else:
            pointList = [Point(10, 10), Point(20, 10), Point(20, 20), Point(10, 20)]
            text_name = "Rectangle"

    else:
        text_name = "*"
        size = int(input("Enter the number of vertices : "))
        print("Enter the coordinates of the point : ")
        for i in range(0, size):
            print(f"vertice {i + 1} : ")
            x = int(input("X : "))
            y = int(input("Y : "))
            pointList.append(Point(x, y))

    dia = triangulation(pointList, len(pointList))
    Ui.Graphic.draw(pointList, dia, text_name)


