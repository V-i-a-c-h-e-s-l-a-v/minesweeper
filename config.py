"""
    Provides the main the Tkinter base widget of the application
and contains the global variable values.
"""

from tkinter import *
from tkinter import ttk
from gui import MyButton


# ---- All styles of GUI ----
class AllStylesOfGUI:
    def __init__(self, style: ttk.Style):
        self.style = style
        self.style.configure("Cell.TButton", width=3, font="Calibri 15 bold")
        self.style.configure(
            "Time_countdown.TLabel",
            font="Arial 10",
        )
        self.style.configure(
            "Mines_left.TLabel",
            font="Arial 10",
        )

    #     self.style.configure(
    #         "Cl-btn.TButton",
    #         **self.new_style_definition("Cell.TButton", foreground="#483D8B")
    #     )
    #
    # def new_style_definition(self, name: str, **kwargs) -> dict:
    #     existing_properties = self.style.configure(name)
    #     for key, value in kwargs.items():
    #         existing_properties[key] = value
    #     return existing_properties


# ---- The GUI main window ----

WINDOW = Tk()  #

# ---- Main presets ------
ROW: int = 5
COLUMN: int = 5
MINES: int = 3
BUTTONS: list[list[MyButton]] = []
TIME_PRESET: int = 10
TIME_PRESET_TEMP = 10
MINES_LEFT: int = MINES
MUSIC_VALUE: float = 0.5
MUSIC_ON = False
MUSIC_OFF = False
GAME_OVER = False


# ----- Colors presets ----

COLORS_PRESET = {
    "🚩": "red",
    1: "#03e3fc",
    2: "#03a9fc",
    3: "#0341fc",
    4: "#5603fc",
    5: "#9d03fc",
    6: "#f403fc",
    7: "#fc03a5",
    8: "#fc0328",
}

# ---- Music file ----

MUSIC_FILE = "DasBoot.mid"
