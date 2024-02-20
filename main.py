"""
    Minesweeper is a logic puzzle video game that runs on Windows PC.

    The game features a grid of clickable cells with hidden mines scattered throughout
the board among empty cells.

    The game's goal is to clear the board without detonating any mines, with help from
clues about the number of neighboring mines in each field.

Main module runs the following modules:
- config: Provides the main the Tkinter base widget of the application
and contains the global variable values;
- gui: Provides GUI for the application;
- settings: Allows the gamer to change the application settings;
- click_handling: Handling the click event of any buttons or menu labels;
- utils: The Utils module is used to implement the game logic.
"""

from gui import MineSweeperGui
from config import WINDOW, BUTTONS
from settings import MenuBar
from click_handling import ClickHandling
from utils import MinesInstaller, MinesCalc, BtnConsoleRepr
from game_reloader import GameReloader


class Game:
    """
        The Game class runs the methods from the modules mentioned above in
    a certain order to provide the player with the game experience.

    Methods:

        - __init__: Construct class Game;
        - main: Running the methods from the modules mentioned above in
        a certain order to run the game functionality.

    """

    def __init__(self):
        """
        Construct class Game

        Attributes:
        - CONFIG: Provides the instance of the class Confing from module confing
        used to provide the Tkinter base widget of the application and
        contains the global variable values;
        - GUI: Provides the instance of the class MineSweeperGui which is a
        base class to use Tkinter widgets of the GUI;
        - MENU: Provides the instance of the class MenuBar which is a
        base class to use widget Menu of Tkinter module;
        - CLICK: Provides the instance of the class Click is used for the
        button click event handling;
        - MINES_INST: Provides the instance of the class MinesInstaller
        is used to randomly place mines on the minefield grid;
        - MINES_CALC: Provides the instance of the class MinesCalc is used to
        calculate the number of mines on the adjacent cells;
        - PRINT_INTO_CONSOLE: Provides the instance of the class BtnConsoleRepr
        is used to print the tkinter buttons representation
        into the console for debugging purposes;

        """
        self.gui = MineSweeperGui()
        self.click = ClickHandling()
        self.mine_inst = MinesInstaller()
        self.mines_calc = MinesCalc()
        self.menu = MenuBar()
        self.game_reloader = GameReloader(self.gui, self.mine_inst, self.mines_calc, self.click, self.menu)
        self.menu.set_reloader(self.game_reloader)

    def main(self):
        """
        Running the methods from the modules mentioned above in
        a certain order to run the game functionality.
        :return: None
        """

        self.gui.create_widgets()
        self.menu.create_menu_bar()

        self.mine_inst.setting_mines(BUTTONS)
        self.mines_calc.mines_calc_init(BUTTONS)

        # button_prnt.print_all_buttons(Config.BUTTONS)
        BtnConsoleRepr.print_btn(BUTTONS)
        self.click.btn_click_bind()
        WINDOW.mainloop()


if __name__ == "__main__":
    minesweeper = Game()
    minesweeper.main()
