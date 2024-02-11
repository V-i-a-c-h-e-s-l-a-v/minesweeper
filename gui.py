"""
Gui modul provides GUI  for the application with classes:
- MyButton,
- MineSweeper Gui.
"""


import tkinter as tk
from typing import Optional

from config import Config, WINDOW
from utils import Click


click = Click()
config = Config()
# Provides the main window of the application
# and contains the global variable values.


class MyButton(tk.Button):
    """
    Subclass MyButtons based on the superclass tk.Button and extend its
    functionality by adding the magic method __repr__ which returns a new description of
    the class instance for debugging purposes.

    Attributes:
        - master: Tkinter base widget,
        - x: Number of the minefield row,
        - y: Number of the minefield column,
        - number: The position coordinate of the cell,
        - adjacent_mines_count: The number of mines on the adjacent cells.
    Methods:
        -__init__: Construct subclass MyButton based on the superclass tk.Button,
        -__repr__: Returns a new description of the class instance for
        debugging purposes.
    """

    x: int
    y: int
    number: int
    master: tk.Tk
    adjacent_mines_count: Optional[int] = None

    def __init__(
        self,
        master,
        x,
        y,
        number,
        adjacent_mines_count,
        *args,
        **kwargs,
    ):
        """
        Construct subclass MyButton based on the superclass tk.Button.
        :param master: Tkinter base widget,
        :param x: Number of the minefield row,
        :param y: umber of the minefield column,
        :param number: The position coordinate of the cell,
        :param adjacent_mines_count: The number of mines on the adjacent cells,
        :param args:   :param kwargs: other arguments of the Button widgets.
        """

        super(MyButton, self).__init__(master, *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.adjacent_mines_count = adjacent_mines_count

        self.is_mine = False

    def __repr__(self):
        """
        Magic method.
        :return: Returns a new description of the class instance for debugging purposes.
        """
        return f"Button_{self.number} {self.x} {self.y} {self.is_mine}"


class MineSweeperGui:
    """
    MineSweeperGui is a base class to use Tkinter widgets of the GUI.

    Methods:
        - __init__: Construct class MineSweeperGui,
        - create_widgets: create Tkinter widgets,

    """

    buttons: list[list[tk.Button]]
    temp: list[MyButton]
    btn: tk.Button

    def __init__(self):
        """
        Construct class MineSweeperGui.

        Attributes:
            - buttons: The list of the cells on the minefield.
        """

        self.buttons = []  # The list of lists representing a grid of tkinter buttons.
        number = 1  # Counting the number of cells.

        for i in range(config.ROW + 2):
            temp = []  # List representing the grid row of tkinter buttons.
            for j in range(config.COLUMN + 2):
                btn = MyButton(
                    WINDOW,
                    i,
                    j,
                    number,
                    adjacent_mines_count=None,
                    width=3,
                    font="Calibri 15 bold",
                )
                btn.config(command=lambda button=btn: click.get_click(button))
                temp.append(btn)
                if i in [0, config.ROW + 1] or j in [0, config.COLUMN + 1]:
                    btn.number = 0
                else:
                    number += 1
            self.buttons.append(temp)

    def create_widgets(self):
        """
        Create Tkinter widgets.
        :return: None
        """
        menubar = tk.Menu(WINDOW)
        WINDOW.config(menu=menubar)

        for i in range(1, config.ROW + 1):
            for j in range(1, config.COLUMN + 1):
                btn = self.buttons[i][j]
                btn.grid(row=i, column=j, stick="WESN")

        for i in range(config.ROW):
            # Fixing the bug of the cells size by setting the proportional weight
            # of the rows and columns.
            tk.Grid.rowconfigure(WINDOW, i, weight=1)
        for j in range(config.COLUMN):
            tk.Grid.columnconfigure(WINDOW, j, weight=1)
