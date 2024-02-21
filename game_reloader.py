"""
     This module is used to provide the game reload functionality.
"""
import config
from gui import MineSweeperGui
from utils import MinesInstaller, MinesCalc, BtnConsoleRepr
from click_handling import ClickHandling


class GameReloader:
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

    def __init__(self):
        self.gui = MineSweeperGui()
        self.mines_init = MinesInstaller()
        self.mines_calc = MinesCalc()
        self.click_handling = ClickHandling()
        self.prnt = BtnConsoleRepr()

    @staticmethod
    def reload():
        """
        Starting a new game by reloading the application GUI.
        :return: None
        """
        from settings import MenuBar

        menu = MenuBar()
        config.BUTTONS = []

        print("Reloaded")
        for child in config.WINDOW.winfo_children():
            # Iterating through the objects of the WINDOW to close them directly
            # using the destroy() method.

            child.destroy()
        # # ReloadGame.reload()

        GameReloader.GUI.__init__()  # Initialise the class MineSweeperGui again.
        print("Initialise the class MineSweeperGui again.")

        menu.__init__()  # Initialise the class MenuBar again.
        print("Initialise the class MenuBar again")

        GameReloader.GUI.create_widgets()
        print("Creating the GUI widgets")

        menu.create_menu_bar()
        print("Creating the menu bar widgets")

        GameReloader.MINES_INIT.setting_mines(config.BUTTONS)
        print("Mines are installed")

        GameReloader.MINES_CALC.mines_calc_init(config.BUTTONS)
        print("Adjacent mines count is completed")

        GameReloader.PRNT.print_btn(config.BUTTONS)
        print("Print the tkinter buttons representation")

        GameReloader.CLICK_HANDLING.btn_click_bind()
        print("Click handling")
