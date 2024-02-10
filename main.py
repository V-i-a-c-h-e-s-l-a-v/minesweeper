"""
Minesweeper is a logic puzzle video game that runs on Windows PC.

The game features a grid of clickable cells with hidden mines scattered throughout
the board among empty cells.

The objective is to clear the board without detonating any mines, with help from
clues about the number of neighboring mines in each field.

Main module runs the following modules:
- config: Provides the main window of the application and contains the global variable values,
- gui: Provides GUI for the application,
- settings: Allows the gamer to change the application settings.
"""

from gui import MineSweeperGui as Gui
from config import WINDOW
from settings import MenuBar as Menu
from utils import Utilities as Ut


# TODO: Скопировать в мэйн
class Game:

    """
    Game class runs the applications modules: gui, settings and config.

    Methods:
        - main: runs the applications modules: gui, settings and config.

    """

    @staticmethod
    def main():
        game_gui = Gui()  # The class instance provides the GUI of the application.
        game_menu = (
            Menu()
        )  # The class instance provides the application's menu interface.
        utils = Ut()
        game_gui.create_widgets()
        game_menu.create_menu_bar()
        utils.setting_mines(game_gui.buttons)

        WINDOW.mainloop()


if __name__ == "__main__":
    minesweeper = Game()
    minesweeper.main()
