import random

free_cells = 9

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+-------+-------+-------+")
    for i in range(3):
        print("|       |       |       |")
        print("|   " + str(board[i][0]) + "   |   " + str(board[i][1]) + "   |   " + str(board[i][2]) + "   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    already_signed = True
    while already_signed:
        try:
            my_choice = int(input("Enter your move: ")) - 1
            if my_choice >= 0:
                my_cell = board[my_choice // 3][my_choice % 3]
                if my_cell != 'O' and my_cell != 'X':
                    already_signed = False
                    board[my_choice // 3][my_choice % 3] = 'O'
                    global free_cells
                    free_cells -= 1
            else:
                raise ValueError
        except:
            print("Wrong value.")

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    for i in range(3):
        row = []
        row.append(3 * i + 1)
        row.append(3 * i + 2)
        row.append(3 * i + 3)
        board.append(row)
    return board

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == sign:
            return True
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == sign:
            return True
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    return False

def draw_move(board):
    # The function draws the computer's move and updates the board.
    already_signed = True
    while already_signed:
        choice = random.randint(0, 8)
        my_cell = board[choice // 3][choice % 3]
        if my_cell != 'O' and my_cell != 'X':
            already_signed = False
            board[choice // 3][choice % 3] = 'X'
            global free_cells
            free_cells -= 1


board = []
board = make_list_of_free_fields(board)

while True:
    draw_move(board)
    display_board(board)
    if victory_for(board, 'X'):
        print("Computer won!")
        break;
    if free_cells == 0:
        print("Tie!")
        break;
    enter_move(board)
    display_board(board)
    if victory_for(board, 'O'):
        print("You won!")
        break;    
    if free_cells == 0:
        print("Tie!")
        break;
