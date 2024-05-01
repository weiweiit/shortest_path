"""App.py"""

import tkinter as tk

from map import Map


class App(tk.Tk):
    """Class containing the application."""

    def __init__(self):
        super().__init__()

        self.geometry("800x600")
        self.title("Shortest path")

        canvas = tk.Canvas(self, width=600, height=400, bg="blue")
        canvas.pack(anchor=tk.CENTER, expand=True)

        my_map = Map(20)
        my_map.build()
        my_map.draw(canvas=canvas)
