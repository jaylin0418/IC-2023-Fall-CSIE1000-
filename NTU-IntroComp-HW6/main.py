import os
from args import get_args

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self, file=None):
        for row in self.board:
            row_str = " | ".join(row)
            print(row_str, file=file)
            print("-" * 9, file=file)

    # TODO: Implement the check_winner() and is_board_full() methods below
    
    # check_winner() should return True if there is a winner, and False otherwise
    def check_winner(self):
        #*************add your code here*************
        # check 
        for i in range(3):
            if(self.board[i][0] == self.board[i][1] == self.board[i][2] != " "):
                return True
        for i in range(3):
            if(self.board[0][i] == self.board[1][i] == self.board[2][i] != " "):
                return True
        #check diagonal
        if(self.board[0][0] == self.board[1][1] == self.board[2][2] != " "):
            return True
        if(self.board[0][2] == self.board[1][1] == self.board[2][0] != " "):
            return True
        return False
        #*************end your code here*************

    # is_board_full() should return True if the board is full, and False otherwise
    def is_board_full(self):
        #*************add your code here*************
        for i in range(3):
            for j in range(3):
                if(self.board[i][j] == " "):
                    return False
        return True
        #*************end your code here*************
    
    #TODO: Implement the play_games() method below
    def play_game(self, input_file, output_file):
        #*************add your code here*************
        with open(input_file) as f:
            for line in f:
                row, col = line.split()
                row = int(row)
                col = int(col)
                #handle invalid input
                if(row > 3 or col > 3):
                    continue
                self.board[row-1][col-1] = self.current_player
                if(self.check_winner() == True):
                    with open(output_file, 'w') as f1:
                        self.print_board(f1)
                        print("Player", self.current_player, "wins!", file=f1)
                        return
                if(self.is_board_full() == True):
                    with open(output_file, 'w') as f1:
                        self.print_board(f1)
                        print("It's a draw!", file=f1)
                        return
                if(self.current_player == "X"):
                    self.current_player = "0"
                else:
                    self.current_player = "X"
        #*************end your code here*************

if __name__ == "__main__":
    args = get_args()
    input_folder = args.input_dir  # 輸入資料夾的名稱
    output_folder = args.output_dir  # 輸出資料夾的名稱
    for filename in os.listdir(input_folder):
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, filename)
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        game = TicTacToe()
        game.play_game(input_file, output_file)
        if not os.path.exists("check_functions"):
            os.makedirs("check_functions")
        with open("check_functions/" + filename, 'w') as f:
            print(game.check_winner(), file=f)
            print(game.is_board_full(), file=f)
