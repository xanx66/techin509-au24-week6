import numpy as np

class TicTacToe:
    def __init__(self):
        self.board = np.array([
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ])
        self.turn = 'X'
        self.status = None
        
    def print_board(self):
        print('-------------')
        for row in self.board:
            print('| ', end='')
            for i in row:
                print(i, end=' | ')
            print()
            print('-------------')

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.turn
            self.check_winner()
            self.turn = 'X' if self.turn == 'O' else 'O'
        else:
            print('This spot is already taken. Try again.')
    
    def check_winner(self):
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            self.status = f'{self.board[0][0]} wins'
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            self.status = f'{self.board[0][2]} wins'
        if self.board[0][0] == self.board[0][1] == self.board[0][2] != ' ':
            self.status = f'{self.board[0][0]} wins'
        if self.board[1][0] == self.board[1][1] == self.board[1][2] != ' ':
            self.status = f'{self.board[1][0]} wins'
        if self.board[2][0] == self.board[2][1] == self.board[2][2] != ' ':
            self.status = f'{self.board[2][0]} wins'
        if self.board[0][0] == self.board[1][0] == self.board[2][0] != ' ':
            self.status = f'{self.board[0][0]} wins'
        if self.board[0][1] == self.board[1][1] == self.board[2][1] != ' ':
            self.status = f'{self.board[0][1]} wins'
        if self.board[0][2] == self.board[1][2] == self.board[2][2] != ' ':
            self.status = f'{self.board[0][2]} wins'
        if ' ' not in self.board:
            self.status = 'tie'
            
        
    def play(self):
        while not self.status:
            self.print_board()
            print(f'{self.turn}\'s turn')
            your_move = input('Enter row (0-2), column (0-2): ')
            row, col = your_move.split(',')
            print(f"You entered: {row}, {col}")
            self.make_move(int(row), int(col))
        self.print_board()
        if self.status == 'tie':
            print('Tie game!')
        else:
            print(f'{self.status} wins!')
            
game = TicTacToe()
game.play()