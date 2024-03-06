"""
     This module is used to provide the game reload functionality.
"""


import config
from gui import MineSweeperGui
from utils import MinesInstaller, MinesCalc, BtnConsoleRepr, ExitHandling
from click_handling import ClickHandling
from i_game_reloader import IGameReloader
from settings import MenuBar
from timer import Timer
import threading
import tkinter as tk


class GameReloader(IGameReloader):
    """
    The GameReloader class is used to provide the game reload functionality.

    Attributes:
        - gui: Provides the instance of the class MineSweeperGui which is a
        base class to use Tkinter widgets of the GUI;
        - menu: Provides the instance of the class MenuBar which is a
        base class to use widget Menu of Tkinter module;
        - mines_init: Provides the instance of the class MinesInstaller is used to
         randomly place mines on the minefield grid;
        - mines_calc: Provides the instance of the class MinesCalc  is used for
         calculation the number of mines on the adjacent cells;
        - click_handling: Provides the instance of the class ClickHandling is used
         for the button click event handling;
        - prnt: Provides the instance of the class BtnConsoleRepr is used to print
         the tkinter buttons representation into the console for debugging purposes.

    Methods:
        - __init__: Construct class GameReloader;
        - reload: Running the new session of the game.

    """

    def __init__(
        self,
        gui: MineSweeperGui,
        mines_init: MinesInstaller,
        mines_calc: MinesCalc(),
        timer: Timer,
        click_handling: ClickHandling,
        prnt: BtnConsoleRepr(),
    ):
        """
        Construct class GameReloader.

        :param gui: The instance of the class MineSweeperGui;
        :param menu: The instance of the class MineSweeperGui;
        :param mines_init: The instance of the class MinesInstaller;
        :param mines_calc: The instance of the class MinesCalc;
        :param click_handling: The instance of the class ClickHandling;
        :param prnt: The instance of the class BtnConsoleRepr.
        """
        self.gui = gui
        self.mines_init = mines_init
        self.mines_calc = mines_calc

        self.timer = timer
        self.click_handling = click_handling
        self.prnt = prnt

    # def thread_control(self) -> bool:
    #     return self.thread_1.is_alive()

    def reload(self) -> None:
        """
        Running the new session of the game.
        :return: None
        """

        config.BUTTONS = []

        print("Reloaded")
        for child in config.WINDOW.winfo_children():
            # Iterating through the objects of the WINDOW to close them directly
            # using the destroy() method.
            if not isinstance(child, tk.Menu):
                child.destroy()

        self.gui.__init__()  # Initialise the class MineSweeperGui again.
        print("Initialise the class MineSweeperGui again.")

        # self.menu.__init__()  # Initialise the class MenuBar again.
        # print("Initialise the class MenuBar again")

        self.gui.create_button_widgets()
        print("Creating the button widgets")

        self.gui.create_mines_left_bar(config.MINES)
        print("Creating the mines left bar widget")

        # self.menu.create_menu_bar(self.exit_handling)
        # print("Creating the menu bar widgets")
        self.click_handling.first_click_done = False
        self.click_handling.btn_click_bind()
        print("Click handling")
        self.gui.create_timer_bar()
        self.timer.timer_restart()
