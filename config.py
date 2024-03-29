"""
    Provides the main the Tkinter base widget of the application
and contains the global variable values.
"""

import tkinter as tk
from gui import MyButton

# ---- The GUI main window ----

WINDOW = tk.Tk()  #

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
