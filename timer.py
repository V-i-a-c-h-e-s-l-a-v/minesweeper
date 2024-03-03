import config
from gui import MineSweeperGui


class Timer:
    def __init__(self, gui: MineSweeperGui):
        self.gui = gui
        self.flag = False

    def timer_restart(self):
        self.flag = True
        self.gui.timer_label.destroy()
        self.gui.create_timer_bar()
        self.flag = False
        self.timer_launch()

    def timer_countdown(self, duration):
        if duration > 0 and not self.flag:
            self.gui.timer_label.after(
                0, self.timer_label_config, Timer.time_format(duration)
            )
            self.gui.timer_label.after(1000, self.timer_countdown, duration - 1)

    def timer_launch(self):
        self.timer_label_config(self.time_format(config.TIME_PRESET))
        self.timer_countdown(config.TIME_PRESET)

    def timer_label_config(self, time_value: str):
        self.gui.timer_label.config(text=time_value)

    @staticmethod
    def time_format(seconds):
        m, s = divmod(int(seconds), 60)
        return f"Time:{m:02d}:{s:02d}"
