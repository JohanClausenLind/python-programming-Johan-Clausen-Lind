
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

   