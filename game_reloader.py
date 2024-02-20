# TODO: Add the all necessary annotations!

import config
from gui import MineSweeperGui
from utils import MinesInstaller, MinesCalc, BtnConsoleRepr
from click_handling import ClickHandling


class GameReloader:
    GUI = MineSweeperGui()

    MINES_INIT = MinesInstaller()
    MINES_CALC = MinesCalc()
    CLICK_HANDLING = ClickHandling()
    PRNT = BtnConsoleRepr()

    # def __init__(self):
    #     self.game_gu
    #     self.mines_installer = GameReloader.MINES_INIT.setting_mines()
    #     self.adjacent_mines_count = GameReloader.MINES_CALC
    #     self.click_handling = GameReloader.CLICK_HANDLING
    #     self.prnt = GameReloader.PRNT

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

        GameReloader.GUI.create_widgets()  # Creating the GUI widgets.
        print("Creating the GUI widgets")

        menu.create_menu_bar()  # Creating the menu bar widgets.
        print("Creating the menu bar widgets")

        GameReloader.MINES_INIT.setting_mines(config.BUTTONS)
        print("Mines are installed")

        GameReloader.MINES_CALC.mines_calc_init(config.BUTTONS)
        print("Adjacent mines count is completed")

        GameReloader.PRNT.print_btn(config.BUTTONS)
        print("Print the tkinter buttons representation")

        GameReloader.CLICK_HANDLING.btn_click_bind()
        print("Click handling")
