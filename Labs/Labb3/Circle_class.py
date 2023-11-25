from Shape_class import Shapes

class Circle(Shapes):
    def __init__(self, x, y, radius):
        try:
            self.x = float(x)
            self.y = float(y)
            self.radius = float(radius)
            if self.radius <= 0:
                raise ValueError("Radius must be greater than 0")
        except ValueError as e:
            print(f"Invalid value for circle: {e}")
            raise

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

    def is_point_inside(self, px, py):
        distance = ((self.x - px) ** 2 + (self.y - py) ** 2) ** 0.5
        return distance <= self.radius