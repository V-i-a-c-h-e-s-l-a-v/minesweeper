"""
Utils module is to implement all the logic for the game with classes:
- BtnConsoleRepr,
- PrintAllButtons,
- MinesCalc,
- Click,
- MinesInstaller.

"""

from random import shuffle
from config import Config
import tkinter as tk


class BtnConsoleRepr:
    """
    The BtnConsoleRepr class is used to print the tkinter buttons representation
    into the console for debugging purposes.

    Methods:
        - print_btn(buttons): This function is used to print the tkinter buttons
         representation into the console for debugging purposes.
    """

    @staticmethod
    def print_btn(buttons):
        """
        This function is used to print the tkinter buttons representation
        into the console for debugging purposes.
        :param buttons: The List of lists representing a grid of tkinter buttons.
        :return: None
        """
        for i in range(1, Config.ROW + 1):
            for j in range(1, Config.COLUMN + 1):
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
    def print_all_buttons(buttons):
        """
        Method is used to display the content of all Tkinter buttons
        (cells) of the game GUI for debugging purposes.
        :param buttons: The list of lists representing a grid of tkinter buttons.
        :return: None
        """
        for i in range(Config.ROW + 2):
            for j in range(Config.COLUMN + 2):
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
        obtain their coordinates on the minefield grid , which are then sent
        to the 'nearest_cells_check' method.
    """

    @staticmethod
    def nearest_cells_check(buttons, i: int, j: int):
        """
        The method is used to count how many mines are
        on the adjacent cells.
        :param buttons: The list of lists representing a grid of tkinter buttons,
        :param i: The row number of the minefield grid,
        :param j: The column number of the minefield grid.
        :return: How many mines are on the adjacent cells.
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

    def mines_calc_init(self, buttons):
        """
        The method is used to iterate through the cells to
        obtain their coordinates on the minefield grid , which are then sent
        to the 'nearest_cells_check' method.
        :param buttons: The list of lists representing a grid of tkinter buttons.
        :return: None
        """
        for i in range(1, Config.ROW + 2):
            for j in range(Config.COLUMN + 2):
                btn = buttons[i][j]
                if btn.number != 0:
                    mines_num = self.nearest_cells_check(buttons, i, j)
                    btn.adjacent_mines_count = mines_num


class Click:
    """
    Class Click is to implement the handling of the button click.
    Methods:
        - get_click: Implement the click button commands.
    """

    @staticmethod
    def get_click(click_btn):
        """
        Implement the click button commands.

        :param click_btn: The bound method of MyButton.
        :return: None
        """

        if click_btn.is_mine:
            # If the cell has a mine "*" is printed on the cell.
            click_btn.config(text="*", disabledforeground="black")
        elif not click_btn.is_mine and click_btn.adjacent_mines_count != 0:
            # Displaying the number of mines in the adjacent cells.
            click_btn.config(
                text=f"{click_btn.adjacent_mines_count}", disabledforeground="black"
            )
        else:
            # Displaying an empty cell if there are no mines in the adjacent cells.
            click_btn.config(text="")

        # Freeze the clicked button (only one click is possible).
        click_btn.config(state="disable")
        # Sunkening the clicked button.
        click_btn.config(relief=tk.SUNKEN)


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
    def setting_mines(buttons):
        """
        This function is used to randomly place mines on the minefield grid.

        :param buttons: The List of lists representing a grid of tkinter buttons.
        :return: None
        """
        btn_li = buttons
        num_li = [num for num in range(1, (Config.ROW * Config.COLUMN))]
        shuffle(num_li)
        num_li = num_li[: Config.MINES]

        for i in range(1, Config.ROW + 2):
            for j in range(Config.COLUMN + 2):
                btn = btn_li[i][j]
                if btn.number in num_li and btn.number != 0:
                    btn.is_mine = True
