"""
The click_handling module is used to handle the button click event.
"""

import tkinter as tk
import config
from gui import MineSweeperGui, MyButton


class ClickHandling:
    """
    The class ClickHandling is used for the button click event handling.
    Methods:
        - get_click: Implement the click button commands.
        - breadth_first_search: This method is used for
        algorithmically searching all non-mined adjacent cells.
        - get_click: Implement the clicked button commands
    """

    def btn_click_bind(self):
        for i in range(1, config.ROW + 1):
            for j in range(1, config.COLUMN + 1):
                btn = config.BUTTONS[i][j]
                btn.config(command=lambda click_btn=btn: self.get_click(click_btn))

    def __breadth_first_search(self, click_btn: MyButton):
        btn_queue = [click_btn]

        while btn_queue:
            current_btn = btn_queue.pop()

            if current_btn.adjacent_mines_count != 0:
                current_btn.config(
                    text=current_btn.adjacent_mines_count, disabledforeground="black"
                )

                # Freeze the clicked button (only one click is possible).
                current_btn.config(state="disabled")
                # Make the clicked button is sunken.
                click_btn.config(relief=tk.SUNKEN)
                current_btn.is_open = True
            else:
                current_btn.config(text="", disabledforeground="black")
            current_btn.is_open = True
            # Freeze the clicked button (only one click is possible).
            current_btn.config(state="disabled")
            # Make the clicked button is sunken.
            current_btn.config(relief=tk.SUNKEN)
            if current_btn.adjacent_mines_count == 0:
                # It is used to obtain the coordinates of adjacent cells.
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if not abs(dx - dy) == 1:
                            continue

                        next_btn = config.BUTTONS[dx + current_btn.x][
                            dy + current_btn.y
                        ]

                        if (
                            not next_btn.is_open
                            and next_btn.number != 0
                            and next_btn not in btn_queue
                        ):
                            btn_queue.append(next_btn)

    def get_click(self, click_btn: MyButton):
        """
        Implement the clicked button commands.

        :param click_btn: The bound method of MyButton.
        :return: None
        """

        if click_btn.is_mine:
            # print(click_btn.__dict__)
            # If the cell has a mine "*" is printed on the cell.

            click_btn.config(text="*", disabledforeground="black")
            click_btn.is_open = True
        elif not click_btn.is_mine and click_btn.adjacent_mines_count != 0:
            # print(click_btn.__dict__)
            # Displaying the number of mines in the adjacent cells.
            click_btn.config(
                text=f"{click_btn.adjacent_mines_count}", disabledforeground="black"
            )
            click_btn.is_open = True

        else:
            # print(click_btn.__dict__)
            self.__breadth_first_search(click_btn)
            # Click.search_res_prnt()
        # Freeze the clicked button (only one click is possible).
        click_btn.config(state="disabled")
        # Make the clicked button is sunken.
        click_btn.config(relief=tk.SUNKEN)
