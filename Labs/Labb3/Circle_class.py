from Shape_class import Shapes

class Circle(Shapes):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def __repr__(self):
        return f"Circle(x={self.x}, y={self.y}, radius={self.radius})"

    def __str__(self):
        return f"Circle with radius {self.radius} at center ({self.x}, {self.y})"
