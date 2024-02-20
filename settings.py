"""
    The settings module allows a gamer to change the application settings
with class MenuBar.
    This module uses the functionality of the following modules:
    - config: Provides the main the Tkinter base widget of the application
    and contains the global variable values;
    - game_reloader: Starting the new game by reloading the application GUI.
"""


import tkinter as tk
import config
from i_game_reloader import IGameReloader


class MenuBar:

    """
    Class MenuBar is a base class to use widget Menu of Tkinter module.

    Attributes:
        - menubar: Creating a menu bar using Tkinter widgets;
        - buttons: The list of lists representing a grid of tkinter buttons;
        - reload: Starting a new game by reloading the application GUI.

    Attributes:
        - RELOAD: Starting a new game by reloading the application GUI;
        Methods:
        - __init__: Construct the class MenuBar to crate menu 'Menu' of the
        application;
        - settings_apply: Implement the button 'Apply' functionality;
        - create_settings_win: Create the cascade window with a settings menu;
        - reload: Starting a new game by reloading the application GUI;
        - create_menu_bar: Creating a menu bar 'Menu'.
    """

    def set_reloader(self, reloader) -> None:
        self.reloader = reloader

    def settings_apply(self, row, column, mines):
        config.ROW = int(row.get())
        config.COLUMN = int(column.get())
        config.MINES = int(mines.get())
        self.reloader.reload()

    def create_settings_win(self):
        """
        Create the cascade window with the following settings menus:
        - Rows number,
        - Columns number,
        - Mines number,
        - Cansel.
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

    def create_menu_bar(self):
        """
        Creating a menu bar 'Menu' and provides such the settings menus as:
        - New Game,
        - Settings,
        - Exit.
        :return: None
        """
        menu_bar = tk.Menu(config.WINDOW)  # tk.Menu(MenuBar.CONFIG.WINDOW)
        config.WINDOW.config(
            menu=menu_bar
        )  # Configuring the menu of WINDOW to be menu_bar.
        settings_menu = tk.Menu(menu_bar)
        settings_menu.add_command(label="New Game", command=self.reload_game)
        settings_menu.add_command(label="Settings", command=self.create_settings_win)
        settings_menu.add_command(label="Exit", command=config.WINDOW.destroy)
        menu_bar.add_cascade(label="Menu", menu=settings_menu)

    def reload_game(self):
        self.reloader.reload()
