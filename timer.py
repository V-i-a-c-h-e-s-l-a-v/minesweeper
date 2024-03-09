import config
from gui import MineSweeperGui
from tkinter.messagebox import showinfo
from end_game_handler import AllCellShow


class Timer:
    def __init__(self, gui: MineSweeperGui, show_all_cell: AllCellShow):
        self.gui = gui
        self.show_all_cell = show_all_cell
        self.flag = False
        self.stop = False

    def timer_restart(self):
        self.flag = True
        self.gui.timer_label.destroy()
        self.gui.create_timer_bar()
        self.flag = False
        self.timer_launch()

    def timer_countdown(self, duration):
        if duration > 0 and not self.flag and not self.stop:
            self.gui.timer_label.after(
                0, self.timer_label_config, Timer.time_format(duration)
            )
            self.gui.timer_label.after(1000, self.timer_countdown, duration - 1)
        elif duration == 0:
            self.show_all_cell.show_all_cell(config.BUTTONS)
            showinfo("Game over!", "Time is over!")
        elif self.stop:
            self.gui.timer_label.config(text=f"{self.time_format(duration)}")

    def timer_launch(self):
        self.timer_label_config(self.time_format(config.TIME_PRESET))
        self.timer_countdown(config.TIME_PRESET)

    def timer_label_config(self, time_value: str):
        self.gui.timer_label.config(text=time_value)

    @staticmethod
    def time_format(seconds):
        m, s = divmod(int(seconds), 60)
        return f"Time:{m:02d}:{s:02d}"
