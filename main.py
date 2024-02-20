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
        self.GUI = MineSweeperGui()
        self.MENU = MenuBar()
        self.CLICK = ClickHandling()
        self.MINES_INST = MinesInstaller()
        self.MINES_CALC = MinesCalc()
        self.PRINT_INTO_CONSOLE = BtnConsoleRepr

    def main(self):
        """
        Running the methods from the modules mentioned above in
        a certain order to run the game functionality.
        :return: None
        """

        self.GUI.create_widgets()
        self.MENU.create_menu_bar()

        self.MINES_INST.setting_mines(BUTTONS)
        self.MINES_CALC.mines_calc_init(BUTTONS)

        # button_prnt.print_all_buttons(Config.BUTTONS)
        self.PRINT_INTO_CONSOLE.print_btn(BUTTONS)
        self.CLICK.btn_click_bind()
        WINDOW.mainloop()


if __name__ == "__main__":
    minesweeper = Game()
    minesweeper.main()
