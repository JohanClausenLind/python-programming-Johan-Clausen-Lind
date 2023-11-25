from Shape_class import Shapes
class Rectangle(Shapes):

    def __init__(self, x, y, length, width):
        super().__init__(x, y)
        self.length = length
        self.width = width

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
    