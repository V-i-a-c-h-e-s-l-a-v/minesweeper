"""
Settings module allows the gamer to change the application settings with class MenuBar.
"""


import tkinter as tk
from config import Config, WINDOW
from game_reloader import GameReloader


class MenuBar:
    config = Config()

    reloader = GameReloader()
    """
    Class MenuBar is a base class to use widget Menu of Tkinter module.

    Attributes:
        - menubar: creates a menu bar in Tkinter application.


    Methods:
        - __init__: Construct the class MenuBar to crate menu 'Menu' of the
        application,
        -  settings_apply: Implement the button 'Apply' functionality,
        - create_settings_win: Create the cascade window with a settings menu,
        - reload: Starting a new game by reloading the application GUI,
        - create_menu_bar: Creating a menu bar 'Menu'.

    """

    def __init__(self):
        """
        Construct the class MenuBar to crate menu 'Menu' of the
        application

        Attributes:
        - menubar: creates a menu bar in Tkinter application.
        """
        self.menubar = tk.Menu(WINDOW)
        self.buttons = MenuBar.config.BUTTONS
        self.reload = MenuBar.reloader

    def settings_apply(self, row, column, mines):
        """"""
        Config.ROW = int(row.get())
        Config.COLUMN = int(column.get())
        Config.MINES = int(mines.get())
        self.reload.reload()

    def create_settings_win(self):
        """
        Create the cascade window with following settings menus:
        - Rows number,
        - Columns number,
        - Mines number,
        - Cansel.
        :return: None
        """
        win_settings = tk.Toplevel(WINDOW)
        win_settings.title("Settings")

        tk.Label(win_settings, text="Rows number:").grid(row=0, column=0)
        rows_entry = tk.Entry(win_settings)
        rows_entry.grid(row=0, column=1, padx=3, pady=3)
        rows_entry.insert(0, str(Config.ROW))

        tk.Label(win_settings, text="Columns number:").grid(row=1, column=0)
        columns_entry = tk.Entry(win_settings)
        columns_entry.grid(row=1, column=1, padx=3, pady=3)
        columns_entry.insert(0, str(Config.COLUMN))

        tk.Label(win_settings, text="Mines number:").grid(row=2, column=0)
        mines_entry = tk.Entry(win_settings)
        mines_entry.grid(row=2, column=1, padx=3, pady=3)
        mines_entry.insert(0, str(Config.MINES))

        tk.Button(win_settings, text="Cansel", command=win_settings.destroy).grid(
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
        WINDOW.config(
            menu=self.menubar
        )  # Configuring the menu of WINDOW to be self.menubar.
        settings_menu = tk.Menu(self.menubar)
        settings_menu.add_command(label="New Game", command=self.reload_game)
        settings_menu.add_command(label="Settings", command=self.create_settings_win)
        settings_menu.add_command(label="Exit", command=WINDOW.destroy)
        self.menubar.add_cascade(label="Menu", menu=settings_menu)

    def reload_game(self):
        self.reload.reload()
