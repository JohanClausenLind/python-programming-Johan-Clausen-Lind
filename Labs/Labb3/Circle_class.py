from Shape_class import Shapes

class Circle(Shapes):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def __repr__(self):
        return f"Circle(x={self.x}, y={self.y}, radius={self.radius})"

    def __str__(self):
        return f"Circle with radius {self.radius} at center ({self.x}, {self.y})"
 
    def get_center(self):
        return {self.x, self.y}
        
    def is_unit_circle(self):
        return self.radius == 1

    def calculate_area(self):
        return int(3.14 * self.radius ** 2)

    def calculate_perimeter(self):
        return int(2 * 3.14 * self.radius)
