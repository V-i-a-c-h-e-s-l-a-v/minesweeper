from config import Config
import tkinter as tk
from gui import MineSweeperGui, MyButton

gui_btn = MineSweeperGui()


class ClickHandling:
    buttons = Config.BUTTONS
    """
    Class Click is to implement the handling of the button click.
    Methods:
        - get_click: Implement the click button commands.
    """

    def btn_click_bind(self):
        for i in range(1, Config.ROW + 1):
            for j in range(1, Config.COLUMN + 1):
                btn = ClickHandling.buttons[i][j]
                btn.config(command=lambda click_btn=btn: self.get_click(click_btn))

    @staticmethod
    def breadth_first_search(click_btn: MyButton):
        btn_queue = [click_btn]

        while btn_queue:
            print(btn_queue)
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

                        next_btn = ClickHandling.buttons[dx + current_btn.x][
                            dy + current_btn.y
                        ]
                        # print(next_btn.__dict__)
                        if (
                            not next_btn.is_open
                            and next_btn.number != 0
                            and next_btn not in btn_queue
                        ):
                            btn_queue.append(next_btn)

    def get_click(self, click_btn: MyButton):
        """
        Implement the click button commands.

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
            self.breadth_first_search(click_btn)
            # Click.search_res_prnt()
        # Freeze the clicked button (only one click is possible).
        click_btn.config(state="disabled")
        # Make the clicked button is sunken.
        click_btn.config(relief=tk.SUNKEN)
