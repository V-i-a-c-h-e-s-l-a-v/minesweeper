from gui import MyButton
import tkinter as tk
import config


class AllCellShow:
    @staticmethod
    def show_all_cell(buttons: list[list[MyButton]]):
        for i in range(1, config.ROW + 1):
            for j in range(1, config.COLUMN + 1):
                btn = buttons[i][j]
                if btn.is_mine and not btn.is_open:
                    btn.config(
                        text="*",
                        disabledforeground="black",
                        state="disabled",
                    )
                elif not btn.is_mine and not btn.is_open:
                    btn.config(
                        text=f"{btn.adjacent_mines_count}",
                        state="disabled",
                        relief=tk.SUNKEN,
                    )
