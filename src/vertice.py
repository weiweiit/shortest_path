"""Base class for a vertice."""

import random
import tkinter as tk


class Vertice:
    """Base class for a vertice."""

    def __init__(
        self,
        coord_x: int = None,
        coord_y: int = None,
        side_size: int = None,
        weight: int = random.randrange(100),
    ) -> None:
        self.weight: int = weight
        self.coord_x: int = coord_x
        self.coord_y: int = coord_y
        self.side_size: int = side_size

    def __str__(self) -> str:
        """Built-in string function overload.

        Returns:
            str: string representation of a vertice.
        """
        return f"Vertice informations : coords = ({self.coord_x}, {self.coord_y}), size = {self.side_size}, weigth = {self.weight}"

    def build_from_parameters(
        self, coord_x: int, coord_y: int, side_size: int, weight: int
    ) -> None:
        """Set vertice attributes after initialisation.

        Args:
            coord_x (int): x coordinates of the vertice
            coord_y (int): y coordinates of the vertice
            side_size (int): size of the visual representation of the vertice (in px, per side)
            weight (int): weight of the vertice
        """
        self.weight = weight
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.side_size = side_size

    def draw(self, canvas: tk.Canvas) -> None:
        """Visual representation of a vertice.

        Args:
            canvas (tk.Canvas): the canvas to draw on.

        Raises:
            ValueError: if not all values are initialized
        """
        if (
            self.coord_x is not None
            and self.coord_y is not None
            and self.side_size is not None
        ):
            canvas.create_rectangle(
                self.coord_x * self.side_size,
                self.coord_y * self.side_size,
                (self.coord_x + 1) * self.side_size,
                (self.coord_y + 1) * self.side_size,
            )
        else:
            raise ValueError("Vertice coords and/or size are not defined.")
