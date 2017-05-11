from random import randint

board = []

# Created the board
for x in range(5):
    board.append(["O"] * 5)
#Separates the rows / cols with a ' '
def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

#Gives random location value to ship
def random_row(board):
    return randint(1, len(board) - 1)
def random_col(board):
    return randint(1, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

#prints ship's location (while testing)
print ship_row +1
print ship_col +1

#Defines all variable (ship's location and user's choice)
for turn in range(4):
    print "Turn", turn + 1
    
    #Get user's guesses
    guess_row = int(raw_input("Guess Row:")) -1
    guess_col = int(raw_input("Guess Col:")) -1
        
    #Congratulatory  or commiseration messages
    if guess_row == ship_row and guess_col == ship_col:
        board[guess_row][guess_col] = "B"
        print "Congratulations! You sunk my battleship!"
        break
    #Invalid choices from user
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
    if turn == 3:
        print "Game Over"
        
    print_board(board)