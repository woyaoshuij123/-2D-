"""Graphics utilities for 2D rendering."""

class Canvas:
    """2D canvas for drawing."""

    def __init__(self, width, height):
        """Initialize canvas.
        
        Args:
            width: Canvas width
            height: Canvas height
        """
        self.width = width
        self.height = height
        self.pixels = [[0] * width for _ in range(height)]

    def clear(self):
        """Clear the canvas."""
        self.pixels = [[0] * self.width for _ in range(self.height)]

    def draw_point(self, x, y, color):
        """Draw a point on the canvas.
        
        Args:
            x: X coordinate
            y: Y coordinate
            color: Color value
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            self.pixels[y][x] = color
