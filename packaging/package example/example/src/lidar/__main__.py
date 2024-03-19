from .point import CartesianPoint
import sys

if __name__ == "__main__":
    point = CartesianPoint(1, 1, 1)
    print(f"Here, have a lidar point: {point}")
    print(sys.argv)
