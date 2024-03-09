"""
    Minesweeper is a logic puzzle video game that runs on Windows PC.

    The game features a grid of clickable cells with hidden mines scattered throughout
the board among empty cells.

    The game's goal is to clear the board without detonating any mines, with help from
clues about the number of neighboring mines in each field.


Main module uses the following modules:
- config: Provides the Tkinter base widget of the application
and contains the global variable values;
- gui: This module is used to create the game GUI;
- settings: This module is used to change the game presets;
- click_handling: This module is used to handle mouse click button events;
- utils: This module is used to implement the game base functionality;
- game_reloader: This module is used to provide the game reloading;
- end_game_handler: This module has the tools for handling game win event and opens
 all non-opened cells of the minefield grid after any stop-game events;
- timer: This module is used to provide the time countdown.
"""

import config
from gui import MineSweeperGui
from settings import MenuBar
from click_handling import ClickHandling
from utils import MinesInstaller, MinesCalc, BtnConsoleRepr, ExitHandling
from game_reloader import GameReloader
from end_game_handler import AllCellShow, WinEventHandling
from timer import Timer


class Game:
    """
        The Game class runs the methods from the modules mentioned above in
    a certain order to start the game.

        Methods:
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
        - mines_init: Provides the instance of the class MinesInstaller
        is used to randomly place mines on the minefield grid;
        - mines_calc: Provides the instance of the class MinesCalc is used to
        calculate the number of mines on the adjacent cells;
        - click_handling: Provides the instance of the class Click is used for the
        button click event handling;
        - prnt: Provides the instance of the class BtnConsoleRepr is used to print
        the tkinter buttons representation into the console for debugging purposes;
        - show_all_cell: Provides the instance of the class AllCellShow is used to
        open the closed minefield cells when the end game event has occurred;
        - win_event_handling: The instance of the class WinEventHandling is used to
        handle the event when the player wins the game;
        - timer: Provides the instance of the class Timer is used to provide the time countdown;
        - click_handling: Provides the instance of the class ClickHandling is used to
        handle mouse click button events;
        - game_reloader: Provides the instance of the class GameReloader is used to run the game again;
        - exit_handling: Provides the instance of the class ExitHandling is used to
        properly implement the game exit procedure.
        """

        self.gui = MineSweeperGui()
        self.menu = MenuBar()
        self.mines_init = MinesInstaller()
        self.mines_calc = MinesCalc()
        self.prnt = BtnConsoleRepr()
        self.show_all_cell = AllCellShow()
        self.win_event_handling = WinEventHandling()
        self.timer = Timer(self.gui, self.show_all_cell)

        self.click_handling = ClickHandling(
            self.gui,
            self.mines_init,
            self.mines_calc,
            self.prnt,
            self.show_all_cell,
            self.win_event_handling,
            self.timer,
        )

        self.game_reloader = GameReloader(
            self.gui,
            self.mines_init,
            self.mines_calc,
            self.timer,
            self.click_handling,
            self.prnt,
        )

        self.exit_handling = ExitHandling(self.timer)

    def main(self) -> None:
        """
        Running the methods from the modules mentioned above in
        a certain order to run the game functionality.
        :return: None
        """
        self.gui.create_list_of_buttons_list()
        self.gui.create_button_widgets()

        self.menu.create_menu_bar(self.exit_handling)
        self.menu.set_reloader(self.game_reloader)
        self.click_handling.btn_click_bind()
        self.gui.create_timer_bar()
        self.timer.timer_launch()
        self.gui.create_mines_left_bar(config.MINES)
        config.WINDOW.mainloop()


if __name__ == "__main__":
    minesweeper = Game()
    minesweeper.main()
