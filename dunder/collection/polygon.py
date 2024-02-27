class Coordinate:
    def __init__(self, x=0, y=None, z=None) -> None:
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        if self.z is not None:
            return f"{self.x};{self.y};{self.z}"
        elif self.y is not None:
            return f"{self.x};{self.y}"
        else:
             return f"{self.x}"

class Polygon:
    def __init__(self, coordinates:list=None) -> None:
        if coordinates is not None:
            self.coordinates = [coorindate for coorindate in coordinates]
        else:
            self.coordinates = []
    
    def add_point(self, *args):
        match args:
            case Coordinate():
                self.coordinates.append(args)
            case x, y:
                self.coordinates.append(Coordinate(x, y))
            case x, y, z:
                self.coordinates.append(Coordinate(x, y, z))
            case x:
                self.coordinates.append(Coordinate(x))

    
    def __iter__(self):
        self.iterator_index = 0
        return self
    
    def __next__(self):
        try:
            retval = self.coordinates[self.iterator_index] 
        except IndexError:
            raise StopIteration
        else:
            self.iterator_index += 1
            return retval


if __name__ == "__main__":
    polygon = Polygon()
    polygon.add_point(1, 2)
    polygon.add_point(3, 4)
    polygon.add_point(5, 6)

    for point in polygon:
        print(point)
