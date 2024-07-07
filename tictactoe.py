class TicTacToe:
    
    # constructor
    def __init__(self):
        self.tictactoe = {
            'top-l': ' ', 'top-c': ' ', 'top-r': ' ',
            'mid-l': ' ', 'mid-c': ' ', 'mid-r': ' ',
            'bot-l': ' ', 'bot-c': ' ', 'bot-r': ' ',
        }


        
    # this method is to print the tic tac toe board
    def print_tile(self): 
        print()
        print(self.tictactoe['top-l'], '|', self.tictactoe['top-c'], '|', self.tictactoe['top-r'])
        print('--+---+--')
        print(self.tictactoe['mid-l'], '|', self.tictactoe['mid-c'], '|', self.tictactoe['mid-r'])
        print('--+---+--')
        print(self.tictactoe['bot-l'], '|', self.tictactoe['bot-c'], '|', self.tictactoe['bot-r'])
        print()

    

    # this method is to handle turns
    def recursive_call(self, turns):
        gameInput = input("Now is '" + turns + "' turn, enter a position: ")
        while gameInput == '':
            gameInput = input("Input cannot be empty. Now is '" + turns + "' turn, enter a position: ")

        # if the position is empty, add X/O. 
        # if input is empty/invalid position/position is not empty, prompt error message
        while gameInput != ' ':
            if gameInput in self.tictactoe.keys():
                if self.tictactoe[gameInput] == ' ':
                    self.tictactoe[gameInput] = turns
                    self.print_tile()
                    if self.check_result(turns):
                        return
                    else:
                        if turns == 'X':
                            return self.recursive_call('O')
                        else:
                            return self.recursive_call('X')
                else:
                    while self.tictactoe[gameInput] != ' ':
                        gameInput = input("It has been chosen. Enter another position: ")
                        self.check_input(gameInput, turns)
            else:
                gameInput = input("Invalid input. Enter a valid position: ")

                
                
    # this method is to check user input
    def check_input(self, gameInput, turns):
        while gameInput == '' or gameInput not in self.tictactoe.keys():
            if gameInput == '':
                gameInput = input("Input cannot be empty. Now is '" + turns + "' turn, enter a position: ")
            else:
                gameInput = input("Invalid input. Enter a valid position: ")

                
                
    # this method is to check result
    def check_result(self, turns):
        if (self.tictactoe['top-l'] == self.tictactoe['top-c'] == self.tictactoe['top-r'] == turns or
            self.tictactoe['mid-l'] == self.tictactoe['mid-c'] == self.tictactoe['mid-r'] == turns or
            self.tictactoe['bot-l'] == self.tictactoe['bot-c'] == self.tictactoe['bot-r'] == turns or
            self.tictactoe['top-l'] == self.tictactoe['mid-c'] == self.tictactoe['bot-r'] == turns or
            self.tictactoe['bot-l'] == self.tictactoe['mid-c'] == self.tictactoe['top-r'] == turns or
            self.tictactoe['top-l'] == self.tictactoe['mid-l'] == self.tictactoe['bot-l'] == turns or
            self.tictactoe['top-c'] == self.tictactoe['mid-c'] == self.tictactoe['bot-c'] == turns or
            self.tictactoe['top-r'] == self.tictactoe['mid-r'] == self.tictactoe['bot-r'] == turns):
            print("'" + turns + "' Wins!")
            return True
        elif all(value != ' ' for value in self.tictactoe.values()):
            print("It's a draw!")
            return True
        return False
