from gui import MyButton
import tkinter as tk
import config


class AllCellShow:
    """
    Opening the closed minefield cells when the end game event has occurred.
        Methods:
            - show_all_cell: Opening the closed minefield cells when the end
            game event has occurred.

    """

    @staticmethod
    def show_all_cell(buttons: list[list[MyButton]]) -> None:
        """
        Opening the closed minefield cells when the end game event
        has occurred.
        :param buttons: The List of lists represents a grid of Tkinter
        buttons.
        :return: None.
        """
        for i in range(1, config.ROW + 1):
            for j in range(1, config.COLUMN + 1):
                btn = buttons[i][j]
                if btn.is_mine and not btn.is_open:
                    btn.state(["disabled"])
                    btn["text"] = "🚩"
                elif (
                    not btn.is_mine
                    and not btn.is_open
                    and btn.adjacent_mines_count != 0
                ):
                    btn["text"] = f"{btn.adjacent_mines_count}"
                    btn.state(["disabled"])

                elif (
                    not btn.is_mine
                    and not btn.is_open
                    and btn.adjacent_mines_count == 0
                ):
                    btn["text"] = None
                    btn.state(["disabled"])
