import time
from gui import MineSweeperGui


class Timer:
    def __init__(self, gui: MineSweeperGui, time_preset: int):
        self.time_preset = time_preset
        self.gui = gui

    def start(self):
        duration = self.time_preset

        while duration:
            m, s = divmod(int(duration), 60)
            min_sec_format = f"{m:02d}:{s:02d}"
            self.gui.timer["text"] = min_sec_format
            self.gui.timer.update()
            time.sleep(1)
            duration -= 1

    def time(self):
        return "01:32"
