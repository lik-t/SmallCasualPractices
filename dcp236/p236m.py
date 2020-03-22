# Problem #236 [Medium]. This problem is asked by Nvidia.
# You are given a list of `N` points
#   (X_1, Y_1),
#   (X_2, Y_2), ...,
#   (X_N, Y_N)
# representing a polygon. You can assume these points are given in order;
# that is, you can construct the polygon by connecting point `1` to point
# `2`, point `2` to point `3`, and so on, finally looping around to connect
# point `N` to point `1`.
# Determine if a new point `p` lies inside this polygon. (If `p` is on the
# boundary of the polygon, you should return `False`).
import math


def distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def isonline(self, lin):
        if lin.p1.x == lin.p2.x:
            if self.x == lin.p1.x:
                return True
        elif lin.p1.y == lin.p2.y:
            if self.y == lin.p1.y:
                return True
        else:
            slope = (lin.p1.x - lin.p2.x) / (lin.p1.x - lin.p2.y)
            if (self.x - lin.p2.x) / (self.y - lin.p2.y) - slope == 0:
                return True

    def distance_to(self, obj):
        if isinstance(obj, Point):
            return math.sqrt((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2)
        elif isinstance(obj, Line):
            if self.isonline(obj):
                return 0
            else:
                if obj.p1.x == obj.p2.x:
                    return abs(self.x - obj.p1.x)
                elif obj.p1.y == obj.p2.y:
                    return abs(self.y - obj.p1.y)
                else:
                    result = abs((obj.p1.y - obj.p2.y) * self.x + (
                            obj.p2.x - obj.p1.x) * self.y + (
                                         (obj.p2.y - obj.p1.y) *
                                         obj.p1.x - (
                                                 obj.p2.x - obj.p1.x) * obj.p1.y)) / math.sqrt(
                        (obj.p1.y - obj.p2.y) ** 2 + (
                                obj.p2.x - obj.p1.x) ** 2)
                    return result

    def isintriangle(self, tri):
        abc = tri.area
        print(abc)
        pab = Triangle(self, tri.p1, tri.p2).area
        print(pab)
        pbc = Triangle(self, tri.p2, tri.p3).area
        print(pbc)
        pca = Triangle(self, tri.p3, tri.p1).area
        print(pca)
        print(pab + pbc + pca)
        return abc == pab + pbc + pca


class Line:

    def __init__(self, point1, point2):
        self.p1 = point1
        self.p2 = point2


class Triangle:

    def __init__(self, point1, point2, point3):
        self.p1 = point1
        self.p2 = point2
        self.p3 = point3

    @property
    def area(self):
        return abs(self.p1.x * (self.p2.y - self.p3.y) + self.p2.x * (
                    self.p3.y - self.p1.y) + self.p3.x * (
                               self.p1.y - self.p2.y)) / 2