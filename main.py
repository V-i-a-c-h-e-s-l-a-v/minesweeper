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
- utils: The Utils module is used to implement the game logic;
- game_reloader: This module is used to provide the game reload functionality.
"""
import config
from game_reloader import GameReloader
from gui import MineSweeperGui
from config import WINDOW, BUTTONS
from settings import MenuBar
from click_handling import ClickHandling
from utils import MinesInstaller, MinesCalc, BtnConsoleRepr
from timer import Timer
import threading


class Game:
    """
        The Game class runs the methods from the modules mentioned above in
    a certain order to provide the player with the game experience.


        - __init__: Construct class Game;
        - main: Running the methods from the modules mentioned above in
        a certain order to run the game functionality.

    """

    def __init__(self):
        """
                Attributes:
        - gui: Provides the instance of the class MineSweeperGui which is a
        base class to use Tkinter widgets of the GUI;
        - menu: Provides the instance of the class MenuBar which is a
        base class to use widget Menu of Tkinter module;
        - click_handling: Provides the instance of the class Click is used for the
        button click event handling;
        - mines_init: Provides the instance of the class MinesInstaller
        is used to randomly place mines on the minefield grid;
        - mines_calc: Provides the instance of the class MinesCalc is used to
        calculate the number of mines on the adjacent cells;
        - prnt: Provides the instance of the class BtnConsoleRepr
        is used to print the tkinter buttons representation
        into the console for debugging purposes;
        - game_reloader: Provides the instance of the class GameReloader s used to run the game again.
        """

        self.gui = MineSweeperGui()
        self.menu = MenuBar()

        self.click_handling = ClickHandling()

        self.mines_init = MinesInstaller()
        self.mines_calc = MinesCalc()
        self.prnt = BtnConsoleRepr()
        self.timer = Timer(self.gui, config.TIME_PRESET)
        self.thread_1 = threading.Thread(target=self.timer.start)

        self.game_reloader = GameReloader(
            self.gui,
            self.menu,
            self.mines_init,
            self.mines_calc,
            self.click_handling,
            self.prnt,
            self.timer,
            self.thread_1,
        )
        self.menu.set_reloader(self.game_reloader)

    def main(self):
        """
        Running the methods from the modules mentioned above in
        a certain order to run the game functionality.
        :return: None
        """

        self.gui.create_button_widgets()
        self.menu.create_menu_bar()
        self.mines_init.setting_mines(BUTTONS)

        self.mines_calc.mines_calc_init(BUTTONS)

        # button_prnt.print_all_buttons(Config.BUTTONS)
        self.prnt.print_btn(BUTTONS)
        self.click_handling.btn_click_bind()
        self.gui.create_timer_bar(config.TIME_PRESET)
        self.thread_1.start()
        print(self.thread_1.is_alive())

        self.gui.create_mines_left_bar(config.MINES_LEFT)
        WINDOW.mainloop()


if __name__ == "__main__":
    minesweeper = Game()
    minesweeper.main()
