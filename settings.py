"""
    The settings module allows a gamer to change the application settings
using the MenuBar class functionality.
    This module uses the functionality of the following modules:
    - config: Provides the main the Tkinter base widget of the application
    and contains the global variable values;
    - i_game_reloader: Inheritance-based solution to a cyclic import problem pattern.
"""


import tkinter as tk
import config
from i_game_reloader import IGameReloader
from utils import ExitHandling
from threading import Thread
from timer import Timer


class MenuBar:

    """
        Class MenuBar is a base class to use widget Menu of Tkinter module.

    Attributes:
        - reloader: The instance of the IGameReloader class (default value None);
    Methods:
        - __init__: Construct the class MenuBar;
        - set_reloader: Provide the instance of the IGameReloader class;
        - settings_apply: Implement the button 'Apply' functionality;
        - create_settings_win: Create the cascade window with a settings menu;

        - create_menu_bar: Creating a menu bar 'Menu'.
        - reload_game: Running the new session of the game.
    """

    def set_reloader(self, reloader: IGameReloader) -> None:
        """
            Provide the instance of the IGameReloader class.
        :param reloader: The instance of the IGameReloader class.
        :return: None
        """
        self.reloader = reloader

    def settings_apply(self, row: tk.Entry, column: tk.Entry, mines: tk.Entry) -> None:
        """
            Implements the functionality of the 'Apply' button, which is used
        to apply a new game settings.
        :param row: The number of minefield grid rows;
        :param column: The number of minefield grid columns;
        :param mines: The number of mines on the minefield grid.
        :return: None
        """
        config.ROW = int(row.get())
        config.COLUMN = int(column.get())
        config.MINES = int(mines.get())
        self.reload_game()

    def create_settings_win(self) -> None:
        """
        Create the cascade window with the following settings menu:
        - Rows number;
        - Columns number;
        - Mines number;
        - Cancel;
        - Apply.
        :return: None
        """
        win_settings = tk.Toplevel(config.WINDOW)
        win_settings.title("Settings")

        tk.Label(win_settings, text="Rows number:").grid(row=0, column=0)
        rows_entry = tk.Entry(win_settings)
        rows_entry.grid(row=0, column=1, padx=3, pady=3)
        rows_entry.insert(0, str(config.ROW))

        tk.Label(win_settings, text="Columns number:").grid(row=1, column=0)
        columns_entry = tk.Entry(win_settings)
        columns_entry.grid(row=1, column=1, padx=3, pady=3)
        columns_entry.insert(0, str(config.COLUMN))

        tk.Label(win_settings, text="Mines number:").grid(row=2, column=0)
        mines_entry = tk.Entry(win_settings)
        mines_entry.grid(row=2, column=1, padx=3, pady=3)
        mines_entry.insert(0, str(config.MINES))

        tk.Button(win_settings, text="Cancel", command=win_settings.destroy).grid(
            row=3, column=0
        )
        tk.Button(
            win_settings,
            text="Apply",
            command=lambda: self.settings_apply(rows_entry, columns_entry, mines_entry),
        ).grid(row=3, column=1)

    def create_menu_bar(self, exit: ExitHandling) -> None:
        self.exit = exit

        """
        Creating a menu bar 'Menu' with the following options:
        - New Game;
        - Settings;
        - Exit.
        :return: None
        """
        menu_bar = tk.Menu(config.WINDOW)
        config.WINDOW.config(
            menu=menu_bar
        )  # Configuring the menu of WINDOW to be menu_bar.
        settings_menu = tk.Menu(menu_bar)
        settings_menu.add_command(label="New Game", command=self.reload_game)
        settings_menu.add_command(label="Settings", command=self.create_settings_win)
        settings_menu.add_command(label="Exit", command=lambda: self.exit.exit())
        menu_bar.add_cascade(label="Menu", menu=settings_menu)

    def reload_game(self):
        """
        Running the new session of the game.
        :return: None

        """
        self.reloader.reload()
