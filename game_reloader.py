"""
     This module is used to provide the game reload functionality.
"""


import config
from gui import MineSweeperGui
from utils import MinesInstaller, MinesCalc, BtnConsoleRepr
from click_handling import ClickHandling
from i_game_reloader import IGameReloader
from timer import Timer
import tkinter as tk
import music_manager


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
        - timer: Provides the instance of the class Timer is used to provide the
        time countdown;
        - click_handling: Provides the instance of the class ClickHandling is used to
        handle mouse click button events;
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
        :param mines_init: The instance of the class MinesInstaller;
        :param mines_calc: The instance of the class MinesCalc;
        :param timer: The Timer class instance provides the countdown time function;
        :param click_handling: The instance of the class ClickHandling;
        :param prnt: The instance of the class BtnConsoleRepr.
        """
        self.gui = gui
        self.mines_init = mines_init
        self.mines_calc = mines_calc
        self.timer = timer
        self.click_handling = click_handling
        self.prnt = prnt

    def reload(self) -> None:
        """
        Running the new session of the game.

        :return: None.
        """

        music_manager.music_play()

        config.BUTTONS = []  # Sets up the empty list instead of the list of
        # button lists.
        config.MINES_LEFT = config.MINES

        print()
        print("______ New Game _______")
        print()

        for child in config.WINDOW.winfo_children():
            # Iterating through the objects of the Tkinter package base widget except the
            # Menu widget to close them directly by using the 'destroy' method.

            if not isinstance(child, tk.Menu):
                child.destroy()

        self.gui.__init__()  # Reinitializing the MineSweeperGui class by its constructor
        # method.
        self.gui.create_list_of_buttons_list()
        self.gui.create_button_widgets()
        self.gui.create_mines_left_bar(config.MINES_LEFT)
        self.click_handling.first_click_done = False  # Reset the left-click first event
        # indicator to the default value.
        self.click_handling.btn_click_bind()
        self.gui.create_timer_bar()
        self.timer.timer_restart()
