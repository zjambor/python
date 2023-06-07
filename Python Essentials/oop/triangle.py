from points import Point


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__points = [vertice1, vertice2, vertice3]

    def perimeter(self):
        """ calculates the perimeter of the triangle described by the three points; the perimeter is the sum of all the lengths of the legs """
        dest_v1_v2 = self.__points[0].distance_from_point(self.__points[1])
        dest_v1_v3 = self.__points[0].distance_from_point(self.__points[2])
        dest_v2_v3 = self.__points[1].distance_from_point(self.__points[2])
        return dest_v1_v2 + dest_v1_v3 + dest_v2_v3


if __name__ == "__main__":
    triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
    print(triangle.perimeter())
    # expected: 3.414213562373095
