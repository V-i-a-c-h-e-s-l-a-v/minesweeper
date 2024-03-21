"""
This module is used to provide the time countdown.
The Current module includes the Timer class.
"""
from tkinter import ttk
from tkinter import *

import config
from gui import MineSweeperGui
from show_all_cell import AllCellShow
from tkinter.messagebox import showinfo

# from end_game_handler import AllCellShow


class Timer:
    """
    This module is used to provide the time countdown.
    Methods:
        - __init__: Construct class Timer;
        - timer_restart: Restarting the timer;
        - timer_countdown: Implementing the time countdown;
        - timer_launch: Running the time countdown;
        - timer_label_config: Representing the current value of the timer;
        - time_format: Setting the proper timer value representation.
    """

    def __init__(
        self,
        style: ttk.Style,
        gui: MineSweeperGui,
        show_all_cell: AllCellShow,
    ):
        """
        Construct class Timer.
        :param gui: The instance of the class MineSweeperGui which is a
        base class to use Tkinter widgets of the GUI;
        :param show_all_cell: The instance of the class AllCellShow is used to
        open the closed minefield cells when the end game event has occurred;

        Attributes:
        - gui: The instance of the class MineSweeperGui which is a
        base class to use Tkinter widgets of the GUI;
        - show_all_cell: The instance of the class AllCellShow is used to
        open the closed minefield cells when the end game event has occurred;
        - flag: This flag indicates the end of game session;
        - stop: This flag stops the timer.


        """
        self.gui = gui
        self.style = style
        self.string_var = StringVar()
        self.show_all_cell = show_all_cell
        self.countdown_stop = False
        self.countdown_restart = False
        self.minefield_init = False

    def timer_launcher(self):
        if self.countdown_restart:
            self.timer_restart()
        elif not self.countdown_stop:
            self.timer_start()

    def timer_start(self):
        self.timer_countdown(config.TIME_PRESET)

    def timer_restart(self):
        self.countdown_stop = True
        self.gui.timer_label.destroy()
        self.gui.create_timer_bar()
        self.gui.timer_label.config(text=self.time_format(config.TIME_PRESET_TEMP))
        self.countdown_stop = False
        self.timer_countdown(config.TIME_PRESET_TEMP)

    def timer_countdown(self, duration: int):
        config.TIME_PRESET = duration
        if not config.GAME_OVER:
            if self.countdown_stop:
                self.timer_label_config(self.time_format(config.TIME_PRESET))
                return
            elif 1 < config.TIME_PRESET <= 6 and not self.countdown_stop:
                if config.TIME_PRESET % 2 == 0:
                    self.gui.timer_label.after(
                        0,
                        self.timer_label_config_1,
                        self.time_format(config.TIME_PRESET),
                    )
                    self.gui.timer_label.after(
                        1000, self.timer_countdown, config.TIME_PRESET - 1
                    )
                else:
                    self.gui.timer_label.after(
                        0,
                        self.timer_label_config,
                        self.time_format(config.TIME_PRESET),
                    )
                    self.gui.timer_label.after(
                        1000, self.timer_countdown, config.TIME_PRESET - 1
                    )
            elif config.TIME_PRESET and not self.countdown_stop:
                self.gui.timer_label.after(
                    0, self.timer_label_config, self.time_format(config.TIME_PRESET)
                )
                self.gui.timer_label.after(
                    1000, self.timer_countdown, config.TIME_PRESET - 1
                )

            elif not config.TIME_PRESET and not self.countdown_stop:
                self.show_all_cell.show_all_cell(config.BUTTONS)
                showinfo("Game over!", "Time is over!")
                config.GAME_OVER = True
        else:
            return

    def timer_label_config(self, time_value: str) -> None:
        """
        Representing the current value of the timer.
        :param time_value: The current value of the timer.
        :return: None.
        """
        print("Timer")
        self.string_var.set("Time: " + time_value + "sec.")
        self.gui.timer_label["textvariable"] = self.string_var
        self.gui.timer_label["foreground"] = "black"

    def timer_label_config_1(self, time_value: str) -> None:
        """
        Representing the current value of the timer.
        :param time_value: The current value of the timer.
        :return: None.
        """
        self.string_var.set("Time: " + time_value + "sec.")
        self.gui.timer_label["textvariable"] = self.string_var
        self.gui.timer_label["foreground"] = "red"

    @staticmethod
    def time_format(seconds) -> str:
        """
        Setting the proper timer value representation.
        :param seconds: The time value in seconds.
        :return: String.
        """
        m, s = divmod(int(seconds), 60)
        return f"Time:{m:02d}:{s:02d}"
