from Shape_class import Shapes

class Rectangle(Shapes):
    """Representerar en rektangel som är en form av en Shape."""

    def __init__(self, x, y, length, width):
        """
        Skapar en ny instans av Rectangle.

        Args:
            x (float): X-koordinaten för rektangelns position.
            y (float): Y-koordinaten för rektangelns position.
            length (float): Rektangelns längd.
            width (float): Rektangelns bredd.

        Raises:
            ValueError: Om längden eller bredden inte är större än 0.
        """
        try:
            self.x = float(x)
            self.y = float(y)
            self.length = float(length)
            self.width = float(width)
            if self.length <= 0 or self.width <= 0:
                raise ValueError("Längden och bredden måste vara större än 0")
        except ValueError as e:
            print(f"Ogiltigt värde för rektangel: {e}")
            raise

    def __repr__(self):
        """Returnerar en representation av rektangeln."""
        return f"rektangle x={self.x}, y={self.y}, length={self.length}, width={self.width}"
    
    def __str__(self):
        """Returnerar en strängrepresentation av rektangeln."""
        return f"The rektangle of value x={self.x} and y={self.y} has the length={self.length} and width={self.width}"
   
    def calculate_area(self):
        """Returnerar rektangelns area."""
        return int(self.width * self.length)
    
    def calculate_parameter(self):
        """Returnerar rektangelns omkrets."""
        return int(2 * (self.width + self.length))
    
    def is_square(self):
        """Kontrollerar om rektangeln är en kvadrat."""
        return self.length == self.width
    
    def get_center(self):
        """Beräknar och returnerar rektangelns mittpunkt."""
        centerX = self.x + (self.width / 2)
        centerY = self.y + (self.length / 2)
        return {centerX, centerY}
    
    def is_point_inside(self, px, py):
        """Kontrollerar om en punkt ligger inuti rektangeln."""
        return self.x <= px <= self.x + self.width and self.y <= py <= self.y + self.length
