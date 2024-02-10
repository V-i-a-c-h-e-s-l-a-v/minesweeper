"""
Provides the main window of the application and contains the global variable values.
"""

import tkinter as tk

WINDOW = tk.Tk()  # The GUI main window.


class Config:
    """
    Methods:
        - ROW: The default number of rows,
        - COLUMN: The default number of columns,
        - MINES: The default number of mines.
        - __repr__: Returns a new description of the class instance for
        debugging purposes.
    """

    ROW: int = 5
    COLUMN: int = 5
    MINES: int = 5

    def __repr__(self):
        """
        Magic method.
        :return: None
        """
        return f"ROW: {Config.ROW} COLUMN: {Config.COLUMN} MINES: {Config.MINES}"
