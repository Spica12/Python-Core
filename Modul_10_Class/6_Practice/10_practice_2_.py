import tkinter as tk
from tkinter import messagebox


class TicTacToo:

    def __init__(self, window):
        self.window = window
        self.window.title('Tic Tac Toe')
        self.create_board()
        self.initialize_variable()

    def create_board(self):
        
        for i in range(3):
            for j in range(3):

                button = tk.Button(self.window, text='', font=('Arial', 50), height=2, width=6, bg='lightblue',
                                   command=lambda row=1, col=j: self.handle_click(row, col))
                button.grid(row=i, column=j, stick='nsew')


    def initialize_variable(self):
        self.board = [[0, 0, 0], [0, 0,0], [0, 0, 0]]
        self.current_player = 1

    def handle_click(self, row, col):
        if self.board[row][col] == 0:
            if self.current_player == 1:
                self.board[row][col] = 'X'
                self.current_player = 2
            else:
                self.board[row][col] = '0'
                self.current_player = 1

            button = self.window.grid_slaves(row=row, column=col)[0]
            button.config(text=self.board[row][col])

            self.check_for_winner()

    def check_for_winner(self):
        winner = None

        for row in self.board:
            if row.count(row[0]) == len(row) and row[0] != 0:
                winner = row[0]
                break

        for col in range(len(self.board)):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != 0:
                winner = self.board[0][col]
                break

        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != 0:
                winner = self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != 0:
                winner = self.board[0][2]
        
        if all([all(row) for row in self.board]) and winner is None:
            winner = 'tie'
        
        if winner:
            self.declare_winner(winner)


    def declare_winner(self, winner):
        if winner == 'tie':
            message = 'It\'s a tie'
        else:
            message = f'Player {winner} win!'

        answer = messagebox.askyesno(f'Game over', message + 'Do you want to play again?')

        if answer:
            self.initialize_variable()
            for i in range(3):
                for j in range(3):
                    button = self.window.grid_slaves(row=i, column=j)[0]
                    button.config(text='')

        else:
            self.window.quit()


if __name__ == '__main__':
    window = tk.Tk()
    game = TicTacToo(window)
    window.mainloop()