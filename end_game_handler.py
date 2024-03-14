"""
    This module has the tools for handling game win event and opens
all non-opened cells of the minefield grid after any stop-game events.

    The current module includes the following classes:
- AllCellShow,
- WinEventHandling.
"""


from gui import MyButton
import config
from timer import Timer
from tkinter.messagebox import showinfo


class WinEventHandling:
    """
    Handling the event when the player wins the game.
    Methods:
        - win_even_handling: Handling the event when the player wins
       the game.

    """

    def __init__(self, timer: Timer):
        self.timer = timer

    def win_even_handling(self, buttons: list[list[MyButton]]) -> None:
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
            self.timer.countdown_stop = True
            showinfo("Game over!", "All mines found!")
            config.GAME_OVER = True
        elif len(all_btn_li) - len(btn_li_is_open) == 0:
            self.timer.countdown_stop = True
            showinfo("Game over!", "All mines found!")
            config.GAME_OVER = True
