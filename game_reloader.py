"""
     This module is used to provide the game reload functionality.
"""
import config
from gui import MineSweeperGui
from utils import MinesInstaller, MinesCalc, BtnConsoleRepr
from click_handling import ClickHandling
from settings import MenuBar
from i_game_reloader import IGameReloader


class GameReloader(IGameReloader):
    """
    The GameReloader class is used to provide the game reload functionality.

    Attributes:
        - GUI: Provides the instance of the class MineSweeperGui which is a
        base class to use Tkinter widgets of the GUI;
        - MINES_INIT: Provides the instance of the class MinesInstaller is used to
         randomly place mines on the minefield grid;
        - MINES_CALC: Provides the instance of the class MinesCalc  is used for
         calculation the number of mines on the adjacent cells.
        - CLICK_HANDLING: Provides the instance of the class ClickHandling is used
         for the button click event handling.
        - PRNT: Provides the instance of the class BtnConsoleRepr is used to print
         the tkinter buttons representation into the console for debugging purposes.

    """

    def __init__(self, gui, mines_init, mines_calc, click_handling, menu_bar) -> None:
        self.gui = gui
        self.mines_init = mines_init
        self.mines_calc = mines_calc
        self.click_handling = click_handling
        self.menu_bar = menu_bar

    def reload(self):
        """
        Starting a new game by reloading the application GUI.
        :return: None
        """

        self.menu_bar = MenuBar()
        print("Re-create the class MenuBar")

        config.BUTTONS = []

        print("Reloaded")
        for child in config.WINDOW.winfo_children():
            # Iterating through the objects of the WINDOW to close them directly
            # using the destroy() method.

            child.destroy()
        # # ReloadGame.reload()

        self.gui = MineSweeperGui()
        print("Re-create the class MineSweeperGui")

        self.gui.create_widgets()
        print("Creating the GUI widgets")

        self.menu_bar.create_menu_bar()
        print("Creating the menu bar widgets")

        self.mines_init.setting_mines(config.BUTTONS)
        print("Mines are installed")

        self.mines_calc.mines_calc_init(config.BUTTONS)
        print("Adjacent mines count is completed")

        BtnConsoleRepr.print_btn(config.BUTTONS)
        print("Print the tkinter buttons representation")

        self.click_handling.btn_click_bind()
        print("Click handling")
