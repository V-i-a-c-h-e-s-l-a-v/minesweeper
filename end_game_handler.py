"""
    This module has the tools for handling game win event and opens
all non-opened cells of the minefield grid after any stop-game events.

    The current module includes the following classes:
- AllCellShow,
- WinEventHandling.
"""


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
                    btn.config(
                        text="*",
                        disabledforeground="black",
                        state="disabled",
                    )
                elif not btn.is_mine and not btn.is_open:
                    btn.config(
                        text=f"{btn.adjacent_mines_count}",
                        state="disabled",
                        relief=tk.SUNKEN,
                    )


class WinEventHandling:
    """
    Handling the event when the player wins the game.
    Methods:
        - win_even_handling: Handling the event when the player wins
       the game.

    """

    @staticmethod
    def win_even_handling(buttons: list[list[MyButton]]) -> bool:
        """
        Handling the event when the player wins the game.
        :param buttons: The List of lists represents a grid of Tkinter
        buttons.
        :return: Bool.
        """
        btn_li_is_open: list[MyButton] | None = []
        all_btn_li: list[MyButton] | None = []

        for i in range(1, config.ROW + 1):
            for j in range(1, config.COLUMN + 1):
                btn = buttons[i][j]
                if btn.is_open:
                    btn_li_is_open.append(btn)
                    all_btn_li.append(btn)
                else:
                    all_btn_li.append(btn)

        if len(all_btn_li) - len(btn_li_is_open) == 1:
            return True
        else:
            return False
