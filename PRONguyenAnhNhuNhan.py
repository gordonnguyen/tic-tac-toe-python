'''
Programmer Name: Anh Nhu Nhan Nguyen
Date: 12/05/2020
Filename: PRONguyenAnhNhuNhan.py
'''
# MAIN ORIGINAL PROGRAM

#Program Description:
'''
A tic-tac-toe game for 2 players in a 3x3 grid.
The grid is a 2d list composed of '[ ]' symbol,
[ ] is defined as empty spaces for player to mark.

Each player will take turn and enter a desired number
for row and column to mark their symbol [O] or [X].
That number must be within range of the grid and the
space chosen must not be already occupied by another player.

The player that placed 3 marks(symbols) in a horizontally,
vertically or diagonally row is the winner. If there is
no more space available for any player to mark and
no winner is declared, the match will be a draw.

Players can choose to restart the game or close it.
'''

#Basic Algorithm:
'''
while user choose to start/replay the game:
    declare a 2d list with '[ ]' to grid
    display initial grid
    
    while inner loop is True:
        get player one input(row/col) and mark symbol on the grid
        display the grid
        if the marks result in a win:
            assign 'Player One' to winner    #value define winner in display_result function
            break the loop

        if no winner is decided       
            assign False to winner
            break the loop

        get player two input and mark symbol on the grid
        display the grid
        if the marks result in a win:
            assign 'Player Two' to winner
            break the loop

    display_result and declare winner(or draw)
    get input from user to restart the game or not

'''

EMPTY_SPACE = '[ ]'     # Empty space for player to mark (on the grid)
LINE1 = "<>"*18
LINE2 = "-"*12
RESULT_ICON = '==>'

ROWS = COLS = 3
PLAYER_1_SYMBOL = '[X]'
PLAYER_2_SYMBOL = '[O]'


def main():
    print("Welcome to Tic-Tac-Toe!")
    print(LINE1)
    
    start_game = 'y'            # Value to start/replay the game
    while start_game == 'y' or start_game == 'Y':
        # Tic Tac Toe Grid #
        grid = [[EMPTY_SPACE]*COLS,       
                [EMPTY_SPACE]*COLS,
                [EMPTY_SPACE]*COLS]
        display_grid(grid)
        
        while True:
            ### Get player input, mark on the grid and check for winning condition ###
            symbol = PLAYER_1_SYMBOL
            print("It's Player One",symbol,"turn!")
            grid = mark_player_move(grid,symbol)    # Get input (row and col) from player 1 and mark on the grid
            display_grid(grid)
            if winning_condition(grid, symbol):     # Check if player 1 win, break if True
                winner = 'Player One'               # Variable to declare winner or none at result screen
                break
            
            # Check if no winner and no space left to play(DRAW)
            if not any(EMPTY_SPACE in x for x in grid):     #Because the maximum move is 9 (once player one make the last move)
                winner = False                              #This if condition is placed between 2 player
                break

            ### Get player 2 input (row/col) and check for winning condition ###
            symbol = PLAYER_2_SYMBOL
            print("It's Player Two",symbol,"turn!")
            grid = mark_player_move(grid,symbol)    # Get input (row and col) from player 2 and mark on the grid
            display_grid(grid)
            if winning_condition(grid, symbol):     # Check if player 2 win, break if True
                winner = 'Player Two'
                break

        display_result(winner)
        print(LINE1)
        start_game = input("Do you you want to play again? y/n: ")
        
    print(LINE1) 
    print("Game closed.")


### Display grid /and current moves(if any) ###
def display_grid(grid):
    print()
    print()
    print(LINE2)
    for r in range(ROWS):               
        for c in range(COLS):
            print(grid[r][c], end=' ')
        print()
    print(LINE2)
    

##############################################################

### Get row and column input from player and mark it on grid ###
def mark_player_move(grid,symbol):
    
    # Check which player is making the move
    if symbol == PLAYER_1_SYMBOL:            
        player_no = 'One'
    else:
        player_no = 'Two'

    # Get and validate player input
    player_row, player_col = get_and_validate_player_input(grid,player_no)

    # Mark player symbol
    grid[player_row][player_col] = symbol
    return grid


### Get input from player and make sure it's valid ###
def get_and_validate_player_input(grid,player_no):

    #Get input that is within range of the grid
    player_row = get_player_input_within_range(player_no,'row')     
    player_col = get_player_input_within_range(player_no,'column')

    #Check if the space is not occupied by another player
    while grid[player_row][player_col] != EMPTY_SPACE:    
        print("ERROR! It's occupied by another Player!!!")
        player_row = get_player_input_within_range(player_no,'row') 
        player_col = get_player_input_within_range(player_no,'column')
        
    return player_row, player_col


### Get input(row or col) from player and make sure it is within range ###
def get_player_input_within_range(player_no, input_type):
    player_input = int(input("Player "+player_no+" | Enter "+input_type+": "))-1
    while player_input < 0 or player_input > 2:
        print("ERROR! The "+input_type+" is out of range!")
        player_input = int(input("Player "+player_no+" | Enter "+input_type+": "))-1
    return player_input

###############################################################


### Condition to win the match ###
def winning_condition(grid, symbol):
    if grid[0][0] == symbol and grid[0][1] == symbol and grid[0][2] == symbol:
        return True
    elif grid[0][0] == symbol and grid[1][0] == symbol and grid[2][0] == symbol:
        return True
    elif grid[0][0] == symbol and grid[1][1] == symbol and grid[2][2] == symbol:
        return True
    elif grid[0][1] == symbol and grid[1][1] == symbol and grid[2][1] == symbol:
        return True
    elif grid[0][2] == symbol and grid[1][1] == symbol and grid[2][0] == symbol:
        return True
    elif grid[0][2] == symbol and grid[1][2] == symbol and grid[2][2] == symbol:
        return True
    elif grid[1][0] == symbol and grid[1][1] == symbol and grid[1][2] == symbol:
        return True
    elif grid[2][0] == symbol and grid[2][1] == symbol and grid[2][2] == symbol:
        return True
    else:
        return False

### Show match result/and winner(if any) ###
def display_result(winner):
    if winner == False:
        print(RESULT_ICON,"Match is draw!")
    else:
        print(LINE2)
        print(RESULT_ICON,"Congratulation!")
        print(RESULT_ICON,winner,"WIN!!!")
        

main()



##################
#OUTPUT
'''
RUN1:
Welcome to Tic-Tac-Toe!
<><><><><><><><><><><><><><><><><><>


------------
[ ] [ ] [ ] 
[ ] [ ] [ ] 
[ ] [ ] [ ] 
------------
It's Player One [X] turn!
Player One | Enter row: 1
Player One | Enter column: 3


------------
[ ] [ ] [X] 
[ ] [ ] [ ] 
[ ] [ ] [ ] 
------------
It's Player Two [O] turn!
Player Two | Enter row: 3
Player Two | Enter column: 3


------------
[ ] [ ] [X] 
[ ] [ ] [ ] 
[ ] [ ] [O] 
------------
It's Player One [X] turn!
Player One | Enter row: 4
ERROR! The row is out of range!
Player One | Enter row: 0
ERROR! The row is out of range!
Player One | Enter row: 3
Player One | Enter column: 3
ERROR! It's occupied by another Player!!!
Player One | Enter row: 1
Player One | Enter column: 2


------------
[ ] [X] [X] 
[ ] [ ] [ ] 
[ ] [ ] [O] 
------------
It's Player Two [O] turn!
Player Two | Enter row: 1
Player Two | Enter column: 1


------------
[O] [X] [X] 
[ ] [ ] [ ] 
[ ] [ ] [O] 
------------
It's Player One [X] turn!
Player One | Enter row: 2
Player One | Enter column: 3


------------
[O] [X] [X] 
[ ] [ ] [X] 
[ ] [ ] [O] 
------------
It's Player Two [O] turn!
Player Two | Enter row: 3
Player Two | Enter column: 2


------------
[O] [X] [X] 
[ ] [ ] [X] 
[ ] [O] [O] 
------------
It's Player One [X] turn!
Player One | Enter row: 3
Player One | Enter column: 1


------------
[O] [X] [X] 
[ ] [ ] [X] 
[X] [O] [O] 
------------
It's Player Two [O] turn!
Player Two | Enter row: 2
Player Two | Enter column: 2


------------
[O] [X] [X] 
[ ] [O] [X] 
[X] [O] [O] 
------------
------------
==> Congratulation!
==> Player Two WIN!!!
<><><><><><><><><><><><><><><><><><>
Do you you want to play again? y/n: y


------------
[ ] [ ] [ ] 
[ ] [ ] [ ] 
[ ] [ ] [ ] 
------------
It's Player One [X] turn!
Player One | Enter row: 1
Player One | Enter column: 1


------------
[X] [ ] [ ] 
[ ] [ ] [ ] 
[ ] [ ] [ ] 
------------
It's Player Two [O] turn!
Player Two | Enter row: 2
Player Two | Enter column: 2


------------
[X] [ ] [ ] 
[ ] [O] [ ] 
[ ] [ ] [ ] 
------------
It's Player One [X] turn!
Player One | Enter row: 3
Player One | Enter column: 3


------------
[X] [ ] [ ] 
[ ] [O] [ ] 
[ ] [ ] [X] 
------------
It's Player Two [O] turn!
Player Two | Enter row: 1
Player Two | Enter column: 2


------------
[X] [O] [ ] 
[ ] [O] [ ] 
[ ] [ ] [X] 
------------
It's Player One [X] turn!
Player One | Enter row: 3
Player One | Enter column: 2


------------
[X] [O] [ ] 
[ ] [O] [ ] 
[ ] [X] [X] 
------------
It's Player Two [O] turn!
Player Two | Enter row: 3
Player Two | Enter column: 1


------------
[X] [O] [ ] 
[ ] [O] [ ] 
[O] [X] [X] 
------------
It's Player One [X] turn!
Player One | Enter row: 1
Player One | Enter column: 3


------------
[X] [O] [X] 
[ ] [O] [ ] 
[O] [X] [X] 
------------
It's Player Two [O] turn!
Player Two | Enter row: 2
Player Two | Enter column: 3


------------
[X] [O] [X] 
[ ] [O] [O] 
[O] [X] [X] 
------------
It's Player One [X] turn!
Player One | Enter row: 2
Player One | Enter column: 1


------------
[X] [O] [X] 
[X] [O] [O] 
[O] [X] [X] 
------------
==> Match is draw!
<><><><><><><><><><><><><><><><><><>
Do you you want to play again? y/n: n
<><><><><><><><><><><><><><><><><><>
Game closed.
'''
