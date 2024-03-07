"""
This module is used to create the game GUI.
The module 'qui' has the following classes:
- MyButton,
- MineSweeper Gui.
"""


import tkinter as tk
import config


class MyButton(tk.Button):
    """
    Subclass MyButtons based on the superclass tk.Button which represents the Button widget
    from the Python builtin package Tkinter and extends its functionality by adding a dunder
    method and some additional attributes.

    Attributes:
        - master: Tkinter base widget,
        - x: Number of the minefield row,
        - y: Number of the minefield column,
        - number: The position coordinate of the cell,
        - adjacent_mines_count: The number of mines on the adjacent cells.
    Methods:
        -__init__: Construct subclass MyButton based on the superclass tk.Button;
        -__repr__: Returns a new description of the class instance for
        debugging purposes.
    """

    # The used type annotations.
    x: int
    y: int
    number: int
    master: tk.Tk
    adjacent_mines_count: int

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
        :param y: Number of the minefield column,
        :param number: The position coordinate of the cell,
        :param adjacent_mines_count: The number of mines on the adjacent cells,
        :param args:   :param kwargs: other arguments of the Button widgets.
        """

        super(MyButton, self).__init__(master, *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.adjacent_mines_count = adjacent_mines_count
        self.is_open = False
        self.is_mine = False

    def __repr__(self):
        """
        Magic method.

        :return: Returning a new description of the class instance for debugging purposes.
        """
        return f"Button_{self.number} {self.x} {self.y} {self.is_mine} {self.adjacent_mines_count} {self.is_mine}"


class MineSweeperGui:
    """
    MineSweeperGui is a base class for creating the game GUI based on the widgets
    of the Tkinter package.

    Methods:
        - __init__: Constructing class MineSweeperGui;
        - create_list_of_buttons_list: Creating the 2D list of button widgets,
    setting the values to the extra button attributes and saving this list as
    a value of config.BUTTONS variable.
        - create_button_widgets: Creating Tkinter button widgets;
        - create_timer_bar: Creating the time bar;
        - create_mines_left_bar: Creating the mines left bur.

    """

    def __init__(self):
        """
        Construct class MineSweeperGui.
        Attributes:
        - buttons: The list of lists representing a grid of tkinter buttons;
        - rows: The number of rows in the minefield;
        - columns: The number of rows in the minefield;
        - window: Tkinter base widget.
        """

        self.number = 1  # Counting the number of cells.
        self.timer_label = None
        self.mines_left_label = None

    def create_list_of_buttons_list(self) -> None:
        """
        Creating the 2D list of button widgets, setting the values to the extra button
        attributes and saving this list as a value of config.BUTTONS variable.

        :return: None.
        """
        for i in range(config.ROW + 2):
            temp = []  # List representing the grid row of tkinter buttons.
            for j in range(config.COLUMN + 2):
                btn = MyButton(
                    config.WINDOW,
                    i,
                    j,
                    self.number,
                    adjacent_mines_count=0,
                    width=3,
                    font="Calibri 15 bold",
                )
                temp.append(btn)
                # The two cell types should determine the position coordinate
                # of the cell:
                # - The first one is a border cell, which gets coordinate zero;
                # - The second one is a non-border cell, which gets it own number.
                # The first type of cell always does not have a mine, but the
                # second type of cell may or may not be mined.
                if i in [0, config.ROW + 1] or j in [
                    0,
                    config.COLUMN + 1,
                ]:
                    btn.number = 0
                else:
                    self.number += 1
            config.BUTTONS.append(temp)

    @staticmethod
    def create_button_widgets() -> None:
        """
        Creating Tkinter button widgets.
        :return: None.
        """
        # menubar = tk.Menu(config.WINDOW)
        # config.WINDOW.config(menu=menubar)

        for i in range(1, config.ROW + 1):
            for j in range(1, config.COLUMN + 1):
                btn = config.BUTTONS[i][j]
                btn.grid(row=i, column=j, stick="WESN")

        # Fixing the bug of the cell size by setting the proportional weight
        # of the rows and columns.
        for i in range(1, config.ROW + 1):
            tk.Grid.rowconfigure(config.WINDOW, i, weight=1)
        for j in range(1, config.COLUMN + 1):
            tk.Grid.columnconfigure(config.WINDOW, j, weight=1)
        tk.Grid.rowconfigure(config.WINDOW, config.ROW + 2, weight=1)

    def create_timer_bar(self) -> None:
        """
         Creating Tkinter button widgets.

        :return: None.
        """
        self.timer_label = tk.Label(config.WINDOW, text="", font="Arial 10")
        self.timer_label.grid(row=config.ROW + 1, column=0, columnspan=3)

    def create_mines_left_bar(self, mines_left: int) -> None:
        """
        Creating the mines left bur.
        :param mines_left: The number of mines left.

        :return: None.
        """
        self.mines_left_label = tk.Label(
            config.WINDOW, text=f"Mines: {mines_left}", font="Arial 10"
        )
        self.mines_left_label.grid(row=config.ROW + 1, column=3, columnspan=2)
