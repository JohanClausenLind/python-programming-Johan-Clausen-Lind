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
