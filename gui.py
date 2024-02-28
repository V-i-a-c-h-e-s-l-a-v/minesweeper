"""
Gui modul provides GUI for the application with classes:
- MyButton,
- MineSweeper Gui.
"""


import tkinter as tk


import config


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
        self.is_open = False
        self.is_mine = False

    def __repr__(self):
        """
        Magic method.
        :return: Returns a new description of the class instance for
        debugging purposes.
        """
        return f"Button_{self.number} {self.x} {self.y} {self.is_mine} {self.adjacent_mines_count} {self.is_mine}"


class MineSweeperGui:
    """
    MineSweeperGui is a base class to use Tkinter widgets of the GUI.

    Methods:
        - CONFIG: Provides the instance of class Confing from module confing
        used to provide the Tkinter base widget of the application and contains
        the global variable values.;
        - __init__: Construct class MineSweeperGui;
        - create_widgets: create Tkinter button widgets.

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

        # self.buttons = MineSweeperGui.CONFIG.BUTTONS
        # self.rows = MineSweeperGui.CONFIG.ROW
        # self.columns = MineSweeperGui.CONFIG.COLUMN
        # self.window = MineSweeperGui.CONFIG.WINDOW

        number = 1  # Counting the number of cells.
        self.timer = None

        for i in range(config.ROW + 2):
            temp = []  # List representing the grid row of tkinter buttons.
            for j in range(config.COLUMN + 2):
                btn = MyButton(
                    config.WINDOW,
                    i,
                    j,
                    number,
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
                    number += 1
            config.BUTTONS.append(temp)

    @staticmethod
    def create_button_widgets() -> None:
        """
        Create Tkinter button widgets.
        :return: None
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
        timer_bar = tk.Label(config.WINDOW)
        timer_bar.grid(row=config.ROW + 1, column=0, columnspan=3)
        self.timer = tk.Label(timer_bar, text="", font="Arial 10")
        self.timer.grid(row=0, column=0)

    @staticmethod
    def create_mines_left_bar(mines_num):
        mines_left_bar = tk.Label(config.WINDOW)
        mines_left_bar.grid(row=config.ROW + 1, column=3, columnspan=2)

        mines_left = tk.Label(
            mines_left_bar, text=f"Mines: {mines_num}", font="Arial 10"
        )
        mines_left.grid(row=0, column=1)
