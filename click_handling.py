"""
The click_handling module is used for the button click event handling.
"""

import tkinter as tk
import config
import utils
from tkinter.messagebox import showinfo
from gui import MineSweeperGui, MyButton
from timer import Timer
from end_game_handler import WinEventHandling
from show_all_cell import AllCellShow


class ClickHandling:
    """
    The class ClickHandling is used for the button click event handling.

    Methods:
        - __init__: Constructing class ClickHandling;
        - minefield_init: Initializing the minefield by placing the mines and
        calculating the number of mines on the adjacent cells;
        - btn_click_bind: The method is used to bind an event handler to both
        right-click and left-click events;
        - left_click_handling: Implementing the left-click event;
        - right_click_handling: Implementing the right-click event;
        - breadth_first_search: This method is used for algorithmically searching
        all non-mined adjacent cells.

    """

    def __init__(
        self,
        gui: MineSweeperGui,
        mines_init: utils.MinesInstaller,
        mines_calc: utils.MinesCalc,
        prnt: utils.BtnConsoleRepr,
        show_all_cell: AllCellShow,
        win_event_handling: WinEventHandling,
        timer: Timer,
    ):
        """
        Constructing class ClickHandling.

        Parameters:
        :param gui: The instance of the class MineSweeperGui which is a
        base class to use Tkinter widgets of the GUI;
        :param mines_init: The instance of the class MinesInstaller is used to randomly
        place mines on the minefield grid;
        :param mines_calc: The instance of the class MinesCalc is used to
        calculate the number of mines on the adjacent cells;
        :param prnt: The instance of the class BtnConsoleRepr is used to print
        the tkinter buttons representation into the console for debugging purposes;
        :param show_all_cell: The instance of the class AllCellShow is used to
        open the closed minefield cells when the end game event has occurred;
        :param win_event_handling: The instance of the class WinEventHandling
        is used to handle the event when the player wins the game;
        :param timer: The instance of the class Timer is used to provide the time countdown.
        Attribute:
        first_click_done: Indicating if the left-click first event of the current game session
        has occurred.

        """
        self.gui = gui
        self.mines_init = mines_init
        self.mines_calc = mines_calc
        self.prnt = prnt
        self.show_all_cell = show_all_cell
        self.win_event_handling = win_event_handling
        self.timer = timer
        self.first_click_done = False

    def minefield_init(self, click_btn: MyButton) -> None:
        """
        Initializing the minefield by placing the mines and calculating the number
        of mines on the adjacent cells.

        :param click_btn: The Button widget of the package Tkinter.
        :return: None.
        """
        if not self.first_click_done:
            click_btn_number = click_btn.number
            self.mines_init.setting_mines(config.BUTTONS, click_btn_number)
            self.timer.timer_launcher()
            self.mines_calc.mines_calc_init(config.BUTTONS)
            self.prnt.print_btn(config.BUTTONS)
            self.left_click_handling(click_btn)
            self.first_click_done = True
        else:
            self.left_click_handling(click_btn)

    def btn_click_bind(self) -> None:
        """
        The method is used to bind an event handler to both right-click and left-click
        events.

        :return: None.
        """
        for i in range(1, config.ROW + 1):
            for j in range(1, config.COLUMN + 1):
                btn = config.BUTTONS[i][j]
                btn.config(command=lambda click_btn=btn: self.minefield_init(click_btn))
                btn.bind("<Button-3>", self.right_click_handling)

    def left_click_handling(self, click_btn: MyButton) -> None:
        """
        Implement the clicked button commands.

        :param click_btn: The Button widget of the package Tkinter.
        :return: None.
        """

        self.win_event_handling.win_even_handling(config.BUTTONS)

        # Freeze the clicked button (only one click is possible).
        click_btn.config(state="disabled")
        # Make the non-mined clicked button is sunken.
        if not click_btn.is_mine:
            click_btn.config(relief=tk.SUNKEN)

        if click_btn.is_mine:
            # If the cell has a mine "*" the game is over.
            click_btn.is_open = True
            self.timer.countdown_stop = True
            self.timer.timer_launcher()
            click_btn.config(
                text="🚩",
                disabledforeground="red",
                state="disabled",
            )
            self.show_all_cell.show_all_cell(config.BUTTONS)
            showinfo("Game over!", "Game over!")

        elif not click_btn.is_mine and click_btn.adjacent_mines_count != 0:
            # Displaying the number of mines in the adjacent cells.
            click_btn.config(
                text=f"{click_btn.adjacent_mines_count}",
                disabledforeground=f"{config.COLORS_PRESET[click_btn.adjacent_mines_count]}",
            )
            click_btn.is_open = True
            self.timer.countdown_restart = True
            self.timer.timer_launcher()  # Restarting the time countdown.

        else:
            self.breadth_first_search(click_btn)
            self.timer.countdown_restart = True
            self.timer.timer_launcher()

    def right_click_handling(self, event) -> None:
        """
        Implementing the right-click event.

        :param event: The right-click event.
        :return: None.
        """

        self.win_event_handling.win_even_handling(config.BUTTONS)

        cur_btn: MyButton = event.widget

        if cur_btn["state"] == "normal" and config.MINES_LEFT > 0:
            cur_btn["state"] = "disabled"
            cur_btn["text"] = "🚩"
            cur_btn["disabledforeground"] = "red"
            cur_btn.is_open = True
            config.MINES_LEFT -= 1
            self.gui.mines_left_label.destroy()
            self.gui.create_mines_left_bar(config.MINES_LEFT)

        elif cur_btn["text"] == "🚩":
            cur_btn["text"] = ""
            cur_btn["state"] = "normal"
            cur_btn.is_open = False
            config.MINES_LEFT += 1
            self.gui.mines_left_label.destroy()
            self.gui.create_mines_left_bar(config.MINES_LEFT)

    def breadth_first_search(self, click_btn: MyButton) -> None:
        """
        This method is used for algorithmically searching all non-mined adjacent cells.

        :param click_btn: The Button widget of the package Tkinter.
        :return: None.
        """

        if self.win_event_handling.win_even_handling(config.BUTTONS):
            self.timer.countdown_restart = True
            showinfo("Game over!", "All mines found!")
            self.show_all_cell.show_all_cell(config.BUTTONS)

        btn_queue = [click_btn]

        while btn_queue:
            if self.win_event_handling.win_even_handling(config.BUTTONS):
                self.timer.countdown_restart = True
                showinfo("Game over!", "All mines found!")
                self.show_all_cell.show_all_cell(config.BUTTONS)

            current_btn = btn_queue.pop()

            if current_btn.adjacent_mines_count != 0:
                current_btn.config(
                    text=current_btn.adjacent_mines_count,
                    disabledforeground=f"{config.COLORS_PRESET[current_btn.adjacent_mines_count]}",
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
