"""
This module is used to provide the time countdown.
The Current module includes the Timer class.
"""

import config
from gui import MineSweeperGui
from tkinter.messagebox import showinfo
from end_game_handler import AllCellShow


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

    def __init__(self, gui: MineSweeperGui, show_all_cell: AllCellShow):
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
        self.show_all_cell = show_all_cell
        self.countdown_stop = False
        self.countdown_restart = False
        self.minefield_init = False

    def timer_launcher(self):
        if self.countdown_restart:
            self.timer_restart()
        elif not self.countdown_stop:
            self.timer_start()
        # elif self.countdown_stop:
        #     self.timer_stop()

    def timer_start(self):
        self.timer_countdown(config.TIME_PRESET)

    # def timer_stop(self):
    #     print("STOP")
    #     self.gui.timer_label.destroy()
    #     self.gui.create_timer_bar()
    #     self.gui.timer_label.config(self.time_format(config.TIME_PRESET))

    def timer_restart(self):
        self.countdown_stop = True
        self.gui.timer_label.destroy()
        self.gui.create_timer_bar()
        self.gui.timer_label.config(text=self.time_format(config.TIME_PRESET_TEMP))
        self.countdown_stop = False
        self.timer_countdown(config.TIME_PRESET_TEMP)

    def timer_countdown(self, duration: int):
        config.TIME_PRESET = duration
        if self.countdown_stop:
            print("STOP")
            self.timer_label_config(self.time_format(config.TIME_PRESET))
            return
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

    # def timer_restart(self) -> None:
    #     """
    #     Restarting the timer.
    #     :return: None.
    #     """
    #     self.countdown_stop = True
    #     self.gui.timer_label.destroy()
    #     self.gui.create_timer_bar()
    #     self.countdown_stop = False
    #     self.timer_launch()
    #
    # def timer_countdown(self, duration) -> None:
    #     """
    #     Implementing the time countdown.
    #     :param duration: The starting value of the time countdown.
    #     :return: None.
    #     """
    #     if duration > 6 and not self.countdown_stop and not self.countdown_restart:
    #         self.gui.timer_label.after(
    #             0, self.timer_label_config, Timer.time_format(duration)
    #         )
    #         self.gui.timer_label.after(1000, self.timer_countdown, duration - 1)
    #     elif 1 <= duration <= 6 and not self.countdown_stop and not self.countdown_restart:
    #         if duration % 2 == 0:
    #             self.gui.timer_label.after(
    #                 0, self.timer_label_config, Timer.time_format(duration)
    #             )
    #             self.gui.timer_label.after(1000, self.timer_countdown, duration - 1)
    #         else:
    #             self.gui.timer_label.after(
    #                 0, self.timer_label_config_1, Timer.time_format(duration)
    #             )
    #             self.gui.timer_label.after(1000, self.timer_countdown, duration - 1)
    #
    #     elif duration == 0 and self.minefield_init:
    #         self.show_all_cell.show_all_cell(config.BUTTONS)
    #         showinfo("Game over!", "Time is over!")
    #     elif duration == 0 and not self.minefield_init:
    #         showinfo("Game over!", "Time is over!")
    #     elif self.countdown_restart:
    #         self.gui.timer_label.config(text=f"{self.time_format(duration)}")
    #
    # def timer_launch(self) -> None:
    #     """
    #     Running the time countdown.
    #     :return: None.
    #     """
    #     self.timer_label_config(self.time_format(config.TIME_PRESET))
    #     self.timer_countdown(config.TIME_PRESET)

    def timer_label_config(self, time_value: str) -> None:
        """
        Representing the current value of the timer.
        :param time_value: The current value of the timer.
        :return: None.
        """
        self.gui.timer_label.config(text=time_value, fg="black")

    #
    # def timer_label_config_1(self, time_value: str) -> None:
    #     """
    #     Representing the current value of the timer.
    #     :param time_value: The current value of the timer.
    #     :return: None.
    #     """
    #     self.gui.timer_label.config(text=time_value, fg="red")

    @staticmethod
    def time_format(seconds) -> str:
        """
        Setting the proper timer value representation.
        :param seconds: The time value in seconds.
        :return: String.
        """
        m, s = divmod(int(seconds), 60)
        return f"Time:{m:02d}:{s:02d}"
