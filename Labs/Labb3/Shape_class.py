class Shapes():
    """Bas klass för olika geometriska former."""

    def __init__(self, x, y):
        """
        Skapar en ny Shape-instans.

        Args:
            x (float): X-koordinaten för formens mittpunkt.
            y (float): Y-koordinaten för formens mittpunkt.
        """
        self.x = x
        self.y = y

    # ... Andra metoder som __lt__, __gt__, __le__, __ge__, __repr__, __str__ ...

    def translate(self, dx, dy):
        """
        Flyttar formen enligt angivna värden.

        Args:
            dx (float): Förskjutning i X-led.
            dy (float): Förskjutning i Y-led.

        Raises:
            ValueError: Om dx eller dy inte är nummer.
        """
        try:
            dx = float(dx)
            dy = float(dy)
        except ValueError:
            raise ValueError("Båda translationsvärdena måste vara nummer")

        self.x += dx
        self.y += dy

    def calculate_area(self):
        """Räknar ut och returnerar formens area. Denna metod ska överskuggas i subklasser."""
        raise NotImplementedError("Denna metod ska överskuggas i subklasser")
