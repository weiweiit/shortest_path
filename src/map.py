"""Base class for a map."""

import tkinter as tk
from typing import List
from vertice import Vertice


class Map:
    """Base class for a map.

    A map can be represented as a n x n matrix,
    with each cell corresponding to a vertice.
    """

    def __init__(self, size: int) -> None:
        self.size: int = size
        self.map: List[List[Vertice]] = [
            [Vertice() for s in range(size)] for s in range(size)
        ]

    def __str__(self) -> str:
        """Built-in string function overload.

        Returns:
            str: string representation of a map.
        """
        map_to_string: str = ""
        for row_of_vertices in self.map:
            map_to_string += (
                f"| { " | ".join(str(vertice) for vertice in row_of_vertices) } |\n"
            )
        return map_to_string

    def draw(self, canvas: tk.Canvas) -> None:
        """Visual representation of a map.

        Args:
            canvas (tk.Canvas): the canvas to draw on.
        """
        for row in self.map:
            for vertice in row:
                vertice.draw(canvas)

    def build(self) -> None:
        """Build map."""
        for row_number, row in enumerate(self.map):
            for vertice_number, vertice in enumerate(row):
                vertice.build_from_parameters(vertice_number, row_number, 10, 1)
