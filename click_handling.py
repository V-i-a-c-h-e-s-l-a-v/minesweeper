"""
The click_handling module is used to handle the button click event.
"""

import tkinter as tk
from tkinter.messagebox import showinfo
import config
from gui import MineSweeperGui, MyButton
from timer import Timer
import utils


class ClickHandling:
    """
    The class ClickHandling is used for the button click event handling.
    Methods:
        - get_click: Implement the click button commands.
        - breadth_first_search: This method is used for
        algorithmically searching all non-mined adjacent cells.
        - get_click: Implement the click button commands
    """

    # GUI = MineSweeperGui()

    def __init__(
        self,
        gui: MineSweeperGui,
        mines_init: utils.MinesInstaller,
        mines_calc: utils.MinesCalc,
        prnt: utils.BtnConsoleRepr,
        timer: Timer,
    ):
        self.gui = gui
        self.mines_init = mines_init
        self.mines_calc = mines_calc
        self.prnt = prnt
        self.timer = timer

    def minefield_init(self, click_btn: MyButton):
        click_btn_number = click_btn.number
        self.mines_init.setting_mines(config.BUTTONS, click_btn_number)
        self.mines_calc.mines_calc_init(config.BUTTONS)
        self.prnt.print_btn(config.BUTTONS)
        self.left_click_handling(click_btn)

    def btn_click_bind(self):
        for i in range(1, config.ROW + 1):
            for j in range(1, config.COLUMN + 1):
                btn = config.BUTTONS[i][j]
                btn.config(command=lambda click_btn=btn: self.minefield_init(click_btn))
                btn.bind("<Button-3>", self.right_click_handling)

    def left_click_handling(self, click_btn: MyButton):
        """
        Implement the clicked button commands.

        :param click_btn: The bound method of MyButton.
        :return: None
        """
        # Freeze the clicked button (only one click is possible).
        click_btn.config(state="disabled")
        # Make the clicked button is sunken.
        if not click_btn.is_mine:
            click_btn.config(relief=tk.SUNKEN)

        if click_btn.is_mine:
            # print(click_btn.__dict__)
            # If the cell has a mine "*" is printed on the cell.
            click_btn.is_open = True
            click_btn.config(
                text="*",
                disabledforeground="black",
                state="disabled",
            )
            self.timer.flag = True
            for i in range(1, config.ROW + 1):
                for j in range(1, config.COLUMN + 1):
                    btn = config.BUTTONS[i][j]
                    if btn.is_mine:
                        btn.config(
                            text="*",
                            disabledforeground="black",
                            state="disabled",
                        )
                    else:
                        btn.config(
                            text=f"{btn.adjacent_mines_count}",
                            state="disabled",
                            relief=tk.SUNKEN,
                        )
            showinfo("Game over!", "Game over!")

        elif not click_btn.is_mine and click_btn.adjacent_mines_count != 0:
            # print(click_btn.__dict__)
            # Displaying the number of mines in the adjacent cells.
            click_btn.config(
                text=f"{click_btn.adjacent_mines_count}", disabledforeground="black"
            )
            click_btn.is_open = True
            self.timer.timer_restart()

        else:
            # print(click_btn.__dict__)
            self.breadth_first_search(click_btn)
            self.timer.timer_restart()

    def right_click_handling(self, event):
        cur_btn: MyButton = event.widget

        if cur_btn["state"] == "normal" and config.MINES_LEFT > 0:
            cur_btn["state"] = "disabled"
            cur_btn["text"] = "🚩"
            config.MINES_LEFT -= 1
            self.gui.mines_left_label.destroy()
            self.gui.create_mines_left_bar(config.MINES_LEFT)

        elif cur_btn["text"] == "🚩":
            cur_btn["text"] = ""
            cur_btn["state"] = "normal"
            config.MINES_LEFT += 1
            self.gui.mines_left_label.destroy()
            self.gui.create_mines_left_bar(config.MINES_LEFT)

    @staticmethod
    def breadth_first_search(click_btn: MyButton):
        btn_queue = [click_btn]

        while btn_queue:
            current_btn = btn_queue.pop()

            if current_btn.adjacent_mines_count != 0:
                current_btn.config(
                    text=current_btn.adjacent_mines_count, disabledforeground="black"
                )

                # Freeze the clicked button (only one click is possible).
                current_btn.config(state="disabled")
                # Make the clicked button is sunken.
                click_btn.config(relief=tk.SUNKEN)
                current_btn.is_open = True
            else:
                current_btn.config(text="", disabledforeground="black")
            current_btn.is_open = True
            # Freeze the clicked button (only one click is possible).
            current_btn.config(state="disabled")
            # Make the clicked button is sunken.
            current_btn.config(relief=tk.SUNKEN)
            if current_btn.adjacent_mines_count == 0:
                # It is used to obtain the coordinates of adjacent cells.
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        # if not abs(dx - dy) == 1:
                        #     continue

                        next_btn: MyButton = config.BUTTONS[dx + current_btn.x][
                            dy + current_btn.y
                        ]

                        if (
                            not next_btn.is_open
                            and next_btn.number != 0
                            and next_btn not in btn_queue
                        ):
                            btn_queue.append(next_btn)
