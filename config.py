"""
    Provides the main the Tkinter base widget of the application
and contains the global variable values.
"""

import tkinter as tk

WINDOW = tk.Tk()  # The GUI main window.
ROW: int = 5
COLUMN: int = 5
MINES: int = 3
BUTTONS = []


# class Config:
#     """
#         The class Confing provides the main the Tkinter base widget of the application
#     and contains the global variable values.
#
#         Methods:
#             - ROW: The default number of rows;
#             - COLUMN: The default number of columns;
#             - MINES: The default number of mines;
#             - BUTTONS: The list of lists representing a grid of tkinter buttons;
#             - __repr__: Returns a new description of the class instance for
#             debugging purposes.
#     """
#
#     __instance = None
#
#     ROW: int = 5
#     COLUMN: int = 5
#     MINES: int = 3
#     BUTTONS = []
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#             return cls.__instance
#
#     def __del__(self):
#         Config.__instance = None
#
#     def __repr__(self):
#         """
#         Returns a new description of the class instance for debugging purposes.
#         :return: None
#         """
#         return f"ROW: {Config.ROW} COLUMN: {Config.COLUMN} MINES: {Config.MINES}"
