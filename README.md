# minesweeper
This project is set up for study purposes only. 
The current project is based on the ideas of the video tutorial. The link on the tutorial below:
https://www.youtube.com/watch?v=I4yl0VbXpA8&list=PLQAt0m1f9OHsd6U5okp1XLoYyQR0oBjMM&index=13

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