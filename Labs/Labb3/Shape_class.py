
class Shapes():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        if not isinstance(other, Shapes):
            return NotImplemented
        return self.calculate_area() < other.calculate_area()
    
    def __gt__(self, other):
        if not isinstance(other, Shapes):
            return NotImplemented
        return self.calculate_area() > other.calculate_area()
    
    def __le__(self, other):
        if not isinstance(other, Shapes):
            return NotImplemented
        return self.calculate_area() <= other.calculate_area()
    
    def __ge__(self, other):
        if not isinstance(other, Shapes):
            return NotImplemented
        self.calculate_area() >= other.calculate_area()

    def __repr__(self):
        return f'shapes(x= {self.x}, y={self.y})'

    def __str__(self):
        return f'Shape with center at ({self.x}, {self.y})'
        
    def translate(self, dy, dx):
        self.x += dx
        self.y += dy

    def is_point_inside(self, dx, dy):
        return self.x >= dx >= 0 and (self.y >= dy >= 0)
    class Shapes():
    # ... existing methods ...

    def translate(self, dx, dy):
        try:
            dx = float(dx)
            dy = float(dy)
        except ValueError:
            raise ValueError("Both translation values must be numbers")

        self.x += dx
        self.y += dy
