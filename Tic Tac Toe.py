import tkinter as tk
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.buttons = [[None] * 3 for _ in range(3)]
        self.current_player = 'X'

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(root, text="", font=('normal', 20), width=10, height=3,
                                               command=lambda i=i, j=j: self.on_click(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def on_click(self, row, col):
        if self.buttons[row][col]['text'] == "" and not self.check_winner():
            self.buttons[row][col]['text'] = self.current_player
            if self.check_winner():
                self.show_winner()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                if self.current_player == 'O':
                    self.computer_move()

    def computer_move(self):
        available_moves = [(i, j) for i in range(3) for j in range(3) if self.buttons[i][j]['text'] == ""]
        if available_moves:
            row, col = random.choice(available_moves)
            self.on_click(row, col)

    def check_winner(self):
        for i in range(3):
            if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] != "":
                return True
            if self.buttons[0][i]['text'] == self.buttons[1][i]['text'] == self.buttons[2][i]['text'] != "":
                return True
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            return True
        return False

    def show_winner(self):
        winner = self.current_player if self.current_player == 'O' else 'Computer'
        result_label = tk.Label(self.root, text=f"{winner} wins!", font=('normal', 20))
        result_label.grid(row=3, columnspan=3)
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
