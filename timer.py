import threading
import time
import config
from gui import MineSweeperGui
from threading import Thread


class Timer:
    def __init__(self, gui: MineSweeperGui):
        self.time_preset = config.TIME_PRESET
        self.gui = gui
        self.flag = False
        self.thread: Thread | None = None

    def timer_thread_launch(self):
        self.thread = Thread(target=self.timer_thread)
        self.timer_thread()

    def timer_thread_relaunch(self):
        print("Launch")
        self.time_preset = config.TIME_PRESET
        self.flag = True
        # self.thread.join()
        self.flag = False
        self.thread = None
        self.timer_thread_launch()

    def timer_thread(self):
        duration = self.time_preset
        while duration and not self.flag:
            m, s = divmod(int(duration), 60)
            min_sec_format = f"{m:02d}:{s:02d}"
            self.gui.timer.config(text=f"Time: {min_sec_format}")
            # self.gui.timer["text"] = f"Time: {min_sec_format}"
            self.gui.timer.update()
            time.sleep(1)
            duration -= 1

        # print(self.thread.is_alive())
