"""
    Provides the main the Tkinter base widget of the application
and contains the global variable values.
"""

import tkinter as tk
from gui import MyButton


WINDOW = tk.Tk()  # The GUI main window.
ROW: int = 5
COLUMN: int = 5
MINES: int = 3
BUTTONS: list[list[MyButton]] = []
TIME_PRESET: int = 15
MINES_LEFT: int = MINES
