import time

import _tkinter

import config
from gui import MineSweeperGui


class Timer:
    def __init__(self, gui: MineSweeperGui, time_preset: int):
        self.time_preset = time_preset
        self.gui = gui
        self.flag = False

    def start(self):
        duration = self.time_preset

        while duration:
            if not self.flag:
                m, s = divmod(int(duration), 60)
                min_sec_format = f"{m:02d}:{s:02d}"

                self.gui.timer["text"] = f"Time: {min_sec_format}"
                self.gui.timer.update()
                time.sleep(1)
                duration -= 1
            else:
                self.time_preset = config.TIME_PRESET
                break

    def time(self):
        return "01:32"
