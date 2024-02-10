from random import shuffle
from config import Config


class Click:
    @staticmethod
    def get_click(button):
        if button.is_mine:
            button.config(text="*")
        else:
            button.config(text=f"{button.number}")
        print(button)


class Utilities:
    def setting_mines(self, buttons):
        btn_li = buttons
        num_li = [num for num in range(1, (Config.ROW * Config.COLUMN) + 1)]
        shuffle(num_li)
        num_li = num_li[: Config.MINES]

        for i in range(Config.ROW):
            for j in range(Config.COLUMN):
                btn = btn_li[i][j]

                if btn.number in num_li:
                    btn.is_mine = True

        self.print_btns(buttons)

    def print_btns(self, buttons):
        for row in buttons:
            print(row)

        print()

        for row in buttons:
            for btn in row:
                if btn.is_mine:
                    print(btn)
