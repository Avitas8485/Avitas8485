
#   Prolog
#   Authors: Avity Ngonyani
#   Email:  avity4585@gmail.com    
#   Project: Player vs Player Tic Tac Toe 
#   





def main():
    introductions = introduction()
    game_board = create_grid()
    design = better_design(game_board)
    choice_1, choice_2 = player_symbols()
    isfull = fullboard(game_board, choice_1, choice_2)

 
# The introduction to the game
def introduction():
    print('Players! I am an A.I and I will be the host for your tic tac toe game today!')
    print()
    print('Rules: \nThe game will be played by two players, using player 1 and player2 represented by X and O respectively '
    '\nThe game will take place in a 3*3 grid space.'
    '\nWinning conditions are similar to your usual tic tac toe game')
    print()

# This function creates a blank game board
def create_grid():
    print()
    game_board = [[' ', ' ', ' '],
                  [' ', ' ', ' '],
                  [' ', ' ', ' ']]
    return game_board

# This function decides the symbols for the players
def player_symbols():
    choice_1 = input('Player 1: Choose between X and O: ')
    if choice_1 == 'X':
        choice_2 = 'O'
        print('Player 2 is O.')
    else:
        choice_2 = 'X'
        print('Player 2 is X. ')
    input('Press enter to continue.')
    print('\n')
    return (choice_1, choice_2)


 # this function denotes the beginning of the game   
def begin_Game(game_board, choice_1, choice_2, count):
    if count % 2 == 0:
        player = choice_1
    elif count % 2 == 1:
        player = choice_2
    print('Player '+ player + ', It is your turn. ')
    row = int(input('Choose a row:'
                    '[upper row: enter 0, middle row: enter 1, bottom row: enter 2]: '))
    column  = int(input('Pick a column:'
                        '[left column: enter 0, middle column: enter 1, right column: enter 2]: '))
    

    # in case player selection is out of range
    while (row < 0 or row > 2) or (column < 0 or column > 2):
        Notinboard(row,column)
        row = int(input("Pick a row[upper row:"
                        "[enter 0, middle row: enter 1, bottom row: enter 2]: "))
        column = int(input("Pick a column:"
                           "[left column: enter 0, middle column: enter 1, right column enter 2]: "))
    

    # in case the square is already filled
    while (game_board[row][column] == choice_1) or (game_board[row][column] == choice_2):
        filled = illegal(game_board, choice_1, choice_2, row, column)
        row = int(input("Pick a row[upper row:"
                        "[enter 0, middle row: enter 1, bottom row: enter 2]: "))
        column = int(input("Pick a column:"
                           "[left column: enter 0, middle column: enter 1, right column enter 2]: "))
    

    # Locating the symbols in the board
    if player == choice_1:
        game_board[row][column] = choice_1
    else:
        game_board[row][column] = choice_2
    return (game_board)


# checking if the board is full
def fullboard(game_board, choice_1, choice_2):
    count = 1
    winner = True

    while count < 10 and winner == True:
        gaming=begin_Game(game_board, choice_1, choice_2, count)
        design=better_design(game_board)

        if count == 9:
            print('The board is full. Game over.')
            if winner == True:
                print('Its a tie!')

        
        winner = thewinner(game_board, choice_1, choice_2, count)
        count += 1
    if winner == False:
        print('Game over.')
    
    report(count, winner, choice_1, choice_2)

# in case the selection is out of range
def Notinboard(row, column):
    print('Not in range. Pick another one. ')



# this function is to create a better design for the board
def better_design(game_board):
    rows = len(game_board)
    cols = len(game_board)
    print('---+---+---')
    for i in range(rows):
        print(game_board[i][0], ' |', game_board[i][1], '|', game_board[i][2])
        print('---+---+---')
    return game_board


# this function checks for any winner
def thewinner(game_board, choice_1, choice_2, count):
    winner = True
    # in rows
    for row in range (0, 3):
        if (game_board[row][0] == game_board[row][1] == game_board[row][2] == choice_1):
            winner = False
            print("Player " + choice_1 + ", you won!")
   
        elif (game_board[row][0] == game_board[row][1] == game_board[row][2] == choice_2):
            winner = False
            print("Player " + choice_2 + ", you won!")
    
    # in columns
    for col in range (0, 3):
        if (game_board[0][col] == game_board[1][col] == game_board[2][col] == choice_1):
            winner = False
            print("Player " + choice_1 + ", you won!")
        elif (game_board[0][col] == game_board[1][col] == game_board[2][col] == choice_2):
            winner = False
            print("Player " + choice_2 + ", you won!")
    
    # in diagonals
    if game_board[0][0] == game_board[1][1] == game_board[2][2] == choice_1:
        winner = False 
        print("Player " + choice_1 + ", you won!")

    elif game_board[0][0] == game_board[1][1] == game_board[2][2] == choice_2:
        winner = False
        print("Player " + choice_2 + ", you won!")

    elif game_board[0][2] == game_board[1][1] == game_board[2][0] == choice_1:
        winner = False
        print("Player " + choice_1 + ", you won!")

    elif game_board[0][2] == game_board[1][1] == game_board[2][0] == choice_2:
        winner = False
        print("Player " + choice_2 + ", you won!")

    return winner

def illegal(game_board, choice_1, choice_2, row, column):
    print("The square you picked is already filled. Pick another one.")

    
def report(count, winner, choice_1, choice_2):
    print("\n")
    input("Press enter to see the game summary. ")
    if (winner == False) and (count % 2 == 1 ):
        print("Winner : Player " + choice_1 + ".")
    elif (winner == False) and (count % 2 == 0 ):
        print("Winner : Player " + choice_2 + ".")
    else:
        print("Its a tie!")

main()