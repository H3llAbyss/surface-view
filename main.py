from abc import ABC, abstractmethod


class Figure():

    points_array = [] #

    def create(self): #should draw the figure on screen. Add args if necessary {e.g. Point.create("point")}

        def create_points() -> list: # TODO

            array = []
            self.points_array = array
            return



        pass

    def delete(self):
        pass

    def copy(self):
        pass

    pass


class Point(Figure):

    # x, y, z = 0, 0, 0

    def __init__(self, *args):
        if len(args) == 0:
            self.x, self.y, self.z = 0, 0, 0
        elif len(args) == 3:
            self.x, self.y, self.z = float(args[0]), float(args[1]), float(args[2])
        else:
            raise Exception("Zero or three values expected")


    def set_x(self, _x):
        self.x = _x

    def set_y(self, _y):
        self.y = _y

    def set_z(self, _z):
        self.z = _z

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def get_coords(self):
        return (self.x, self.y, self.z)

class Vector3(Figure):

    x, y, z = 1, 1, 1

    def __init__(self):
        self.x, self.y, self.z = 1, 1, 1

    def __init__(self, _x, _y, _z):
        self.x, self.y, self.z = _x, _y, _z

    def __init__(self, _point):
        self.x, self.y, self.z = _point.get_x, _point.get_y, _point.get_z

    def set_x(self, _x):
        self.x = _x

    def set_y(self, _y):
        self.y = _y

    def set_z(self, _z):
        self.z = _z

    def get_x(self, _x):
        return self.x

    def get_y(self, _y):
        return self.y

    def get_z(self, _z):
        return self.z




class Line(Figure):

    points = [Point(), Point()]

    def __init__(self):
        self.points = [Point(0, 0, 0), Point(0, 0, 1)]

    def __init__(self, _point1, _point2):
        self.points = [_point1, _point2]

    def __init__(self, _x1, _y1, _z1, _x2, _y2, _z2):
        self.points = [Point(_x1, _y1, _z1), Point(_x2, _y2, _z2)]

    def __init__(self, _x1, _y1, _z1, _point2):
        self.points = [Point(_x1, _y1, _z1), _point2]

    def __init__(self, _point1: Point, _x2, _y2, _z2):
        self.points = [_point1, Point(_x2, _y2, _z2)]


    pass

class Curve(Figure): # TODO (not implemented yet)
    _t = 1
    x_function = _t
    y_function = _t
    z_function = _t
    def __init__(self):
        pass

    pass

class Cone(Figure):

    curve = Curve()
    point = Point()

    def __init__(self):
        self.curve = Curve()
        self.point = Point()

    def __init__(self,_curve,_point):
        self.curve = _curve
        self.point = _point

    def __init__(self, _curve, _x, _y, _z):
        self.curve = _curve
        self.point = Point(_x, _y, _z)


    pass

class Cylinder(Figure):




    pass

class Plane(Figure):
    pass

if __name__ == "__main__":
    print(Point(4,4,5).get_coords())





