"""
This module is used to implement the game base functionality.
The module 'utils' has the following classes:
- ExitHandling,
- BtnConsoleRepr,
- PrintAllButtons,
- MinesCalc,
- Click,
- MinesInstaller.
"""

from random import shuffle
import config
from timer import Timer
from gui import MyButton


class ExitHandling:
    """
    This class is used to properly implement the game exit procedure.

    Methods:
        - __init__: Construct class ExitHandling;
        - exit: Implementing the game exit procedure.
    """

    def __init__(self, timer: Timer):
        """
        Construct class ExitHandling.

        :param timer: The instance of the class Timer.
        """
        self.timer = timer
        self.window = config.WINDOW

    def exit(self) -> None:
        """
        Implementing the game exit procedure.

        :return: None.
        """
        self.timer.countdown_stop = True
        self.window.destroy()


class BtnConsoleRepr:
    """
    The BtnConsoleRepr class is used to print the tkinter buttons representation
    into the console for the debugging purposes.

    Methods:
        - print_btn(buttons): This function is used to print the tkinter buttons
         representation into the console for the debugging purposes.
    """

    @staticmethod
    def print_btn(buttons) -> None:
        """
        This function is used to print the tkinter buttons representation
        into the console for the debugging purposes.
        :param buttons: The List of lists represents a grid of Tkinter buttons.
        :return: None
        """
        for i in range(1, config.ROW + 1):
            for j in range(1, config.COLUMN + 1):
                btn = buttons[i][j]
                if btn.is_mine:
                    print("M", end="")
                else:
                    print(btn.adjacent_mines_count, end="")
            print()


class PrintAllButtons:
    """
    The class PrintAllButtons is used to display the content of all Tkinter
    buttons (cells) of the game GUI for debugging purposes.

    Methods:
        - print_all_buttons(buttons): Method is used to display the content
         of all Tkinter buttons (cells) of the game GUI for debugging purposes.
    """

    @staticmethod
    def print_all_buttons(buttons: list[list[MyButton]]) -> None:
        """
        Method is used to display the content all Tkinter buttons (cells)
        of the game GUI for debugging purposes.

        :param buttons: The list of lists represents a grid of tkinter buttons.
        :return: None.
        """
        for i in range(config.ROW + 2):
            for j in range(config.COLUMN + 2):
                btn = buttons[i][j]
                if btn.is_mine:
                    btn.config(text="*", disabledforeground="black")
                elif not btn.is_mine and btn.adjacent_mines_count != 0:
                    btn.config(
                        text=f"{btn.adjacent_mines_count}", disabledforeground="black"
                    )
                else:
                    btn.config(text="")


class MinesCalc:
    """
    The MinesCalc class is used to calculate the number of mines
    on the adjacent cells.

    Methods:
        - nearest_cells_check: The method is used to count how many mines are
        on the adjacent cells.
        - mines_calc_init: The method is used to iterate through the cells to
        obtain their coordinates on the minefield grid, which are then sent
        to the 'nearest_cells_check' method.
    """

    @staticmethod
    def nearest_cells_check(buttons, i: int, j: int) -> int:
        """
        The method is used to count how many mines are
        on the adjacent cells.

        :param buttons: The list of lists representing a grid of tkinter buttons,
        :param i: The row number of the minefield grid,
        :param j: The column number of the minefield grid.
        :return: Value of how many mines are on the adjacent cells.
        """
        dif = [-1, 0, 1]  # It is used to obtain the coordinates of adjacent cells.
        count = 0
        for x in map(lambda el: i + el, dif):
            for y in map(lambda el: j + el, dif):
                btn = buttons[x][y]
                if btn.is_mine:
                    count += 1
                else:
                    pass
        return count

    def mines_calc_init(self, buttons: list[list[MyButton]]) -> None:
        """
        The method is used to iterate through the cells to
        obtain their coordinates on the minefield grid, which are then sent
        to the 'nearest_cells_check' method.
        :param buttons: The list of lists represents a grid of tkinter buttons.

        :return: None.
        """
        for x in range(1, config.ROW + 1):
            for y in range(config.COLUMN + 1):
                btn = buttons[x][y]
                mines_num = self.nearest_cells_check(buttons, x, y)
                btn.adjacent_mines_count = mines_num


class MinesInstaller:
    """
    The MinesInstaller class is used to randomly place mines on the minefield grid.

    Methods:
        - setting_mines: This function is used to randomly place mines
        on the minefield grid.
        - print_btn: This function is used to print the tkinter
        buttons representation into the console for debugging purposes.
    """

    @staticmethod
    def setting_mines(buttons: list[list[MyButton]], number: int) -> None:
        """
        This function is used to randomly place the mines on the minefield grid.

        :param number: The position coordinate of the cell.z
        :param buttons: The List of lists represents a grid of tkinter buttons.
        :return: None.
        """
        num_li = []
        for num in range(1, (config.ROW * config.COLUMN)):
            if num != number:
                num_li.append(num)

        shuffle(num_li)
        num_li = num_li[: config.MINES]

        for i in range(1, config.ROW + 2):
            for j in range(config.COLUMN + 2):
                btn = buttons[i][j]
                if btn.number in num_li and btn.number != 0:
                    btn.is_mine = True
