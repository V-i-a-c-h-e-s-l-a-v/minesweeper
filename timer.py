import time

import _tkinter

import config
from gui import MineSweeperGui


class Timer:
    def __init__(self, gui: MineSweeperGui):
        self.time_preset = config.TIME_PRESET
        self.gui = gui
        self.flag = False

    def start(self):
        duration = self.time_preset
        while duration and not self.flag:
            m, s = divmod(int(duration), 60)
            min_sec_format = f"{m:02d}:{s:02d}"
            self.gui.timer["text"] = f"Time: {min_sec_format}"
            self.gui.timer.update()
            time.sleep(1)
            duration -= 1
        self.time_preset = config.TIME_PRESET
        # self.__init__(self.gui)
