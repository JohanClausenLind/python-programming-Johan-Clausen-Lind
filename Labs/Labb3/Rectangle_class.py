from Shape_class import Shapes

class Rectangle(Shapes):
    def __init__(self, x, y, length, width):
        try:
            self.x = float(x)
            self.y = float(y)
            self.length = float(length)
            self.width = float(width)
            if self.length <= 0 or self.width <= 0:
                raise ValueError("Length and width must be greater than 0")
        except ValueError as e:
            print(f"Invalid value for rectangle: {e}")
            raise

    def __repr__(self):
        return f"rektangle x={self.x}, y={self.y}, length={self.length}, width={self.width}"
    
    def __str__(self):
        return f"The rektangle of value x={self.x} and y={self.y} has the length={self.length} and width={self.width}"
   
    def calculate_area(self):
        return int(self.width * self.length)
    
    def calculate_parameter(self):
        return int(2 * (self.width + self.length))
    
    def is_square(self):
        return self.length == self.width
    
    def get_center(self):
        centerX = self.x + (self.width / 2)
        centerY = self.y + (self.length / 2)
        return {centerX, centerY}
    
    def is_point_inside(self, px, py):
        # Assuming (x, y) is the top-left corner of the rectangle
        return self.x <= px <= self.x + self.width and self.y <= py <= self.y + self.length