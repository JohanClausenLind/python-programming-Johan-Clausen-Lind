from Shape_class import Shapes

class Circle(Shapes):
    """Representerar en cirkel som är en form av en Shape."""

    def __init__(self, x, y, radius):
        """
        Skapar en ny instans av Circle.

        Args:
            x (float): X-koordinaten för cirkelns mittpunkt.
            y (float): Y-koordinaten för cirkelns mittpunkt.
            radius (float): Cirkelns radie.

        Raises:
            ValueError: Om radien inte är större än 0.
        """
        try:
            self.x = float(x)
            self.y = float(y)
            self.radius = float(radius)
            if self.radius <= 0:
                raise ValueError("Radien måste vara större än 0")
        except ValueError as e:
            print(f"Ogiltigt värde för cirkeln: {e}")
            raise

    def __repr__(self):
        """Returnerar en representation av cirkeln."""
        return f"Circle(x={self.x}, y={self.y}, radius={self.radius})"

    def __str__(self):
        """Returnerar en strängrepresentation av cirkeln."""
        return f"Circle with radius {self.radius} at center ({self.x}, {self.y})"

    def get_center(self):
        """Returnerar cirkelns mittpunkt."""
        return {self.x, self.y}
        
    def is_unit_circle(self):
        """Kontrollerar om cirkeln är en enhetscirkel."""
        return self.radius == 1

    def calculate_area(self):
        """Returnerar cirkelns area."""
        return int(3.14 * self.radius ** 2)

    def calculate_perimeter(self):
        """Returnerar cirkelns omkrets."""
        return int(2 * 3.14 * self.radius)

    def is_point_inside(self, px, py):
        """Kontrollerar om en punkt ligger inuti cirkeln."""
        distance = ((self.x - px) ** 2 + (self.y - py) ** 2) ** 0.5
        return distance <= self.radius
