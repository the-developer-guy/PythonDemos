import sys
from .math.vector import cartesian_length, spherical_to_cartesian


class PointCalculationError(ArithmeticError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class CartesianPoint:
    def __init__(self, x: int | float,
                 y: int | float,
                 z: int | float) -> None:
        self.x = x
        self.y = y
        self.z = z
        print("I'm a point!")

    def length(self):
        return cartesian_length(self.x, self.y, self.z)

    def __add__(self, param):
        match param:
            case x, y, z:
                return CartesianPoint(self.x + x, self.y + y, self.z + z)
            case CartesianPoint():
                return CartesianPoint(self.x + param.x, self.y + param.y, self.z + param.z)
            case SphericalPoint():
                converted_cartesian = spherical_to_cartesian(param.distance, param.azimuth, param.polar)
                return CartesianPoint(self.x + converted_cartesian[0], self.y + converted_cartesian[1],
                                      self.z + converted_cartesian[2])
            case _:
                raise PointCalculationError(f"Wrong parameter is given: {param}")

    def __imul__(self, num: int | float):
        self.x *= num
        self.y *= num
        self.z *= num
        return self


class SphericalPoint:
    def __init__(self, distance: int | float,
                 azimuth: int | float,
                 polar: int | float) -> None:
        self.distance = distance
        self.azimuth = azimuth
        self.polar = polar

    def length(self):
        return self.distance

class PointCloud:
    def __init__(self, *points):
        self.points = []
        for point in points:
            match point:
                case list():
                    for p in point:
                        self.points.append(p)
                case x, y, z:
                    self.points.append(CartesianPoint(x, y, z))
        print(f"Point cloud made with {len(self.points)} items.")


    def point_cloud(self):
        for point in self.points:
            yield point
        return

    def __iter__(self):
        return self.point_cloud()


def module_demo():
    print("Lidar executed as module!")
    print("We even accept command line args! See?")
    print(sys.argv)

if __name__ == "__main__":
    print("Started point.py as a main")
    module_demo()
